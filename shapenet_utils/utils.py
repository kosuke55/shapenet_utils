import os.path as osp

import numpy as np

from shapenet_utils.data import data_dir
from shapenet_utils.file_io import load_json
from shapenet_utils.filling_rate import filter_filling_rate
from shapenet_utils.shapenet_synset_dict import label_to_synset
from shapenet_utils.shapenet_synset_dict import synset_to_label


def all_synset():
    synset, _ = filter_filling_rate(0, 1)
    return synset


def all_label():
    label, _ = filter_filling_rate(0, 1, to_label=True)
    return label


def manipulation_label():
    manipulation_list = \
        ['bag',
         'bottle',
         'bowl',
         'camera',
         'can',
         'cap',
         'cellular_telephone',
         'keyboard',
         'earphone',
         'faucet',
         'guitar',
         'helmet',
         'jar',
         'knife',
         'lamp',
         'laptop',
         'loudspeaker',
         'microphone',
         'mug',
         'pillow',
         'pistol',
         'pot',
         'remote_control',
         'rifle',
         'telephone']
    return manipulation_list


def manipulation_synset():
    manipulation_synset \
        = [label_to_synset[label] for label in manipulation_label()]
    return manipulation_synset


def filtering_result(task_type='hanging', file_path=None):
    if file_path is not None:
        return load_json(file_path)

    if task_type == 'hanging':
        filename = 'filtering_result.json'
    elif task_type == 'pouring':
        filename = 'filtering_result_pouring.json'
    else:
        raise ValueError('task_type should "be hanging" or "pouring"')
    return load_json(
        osp.join(data_dir, filename))


def points_dict(task_type='hanging_points', file_path=None,
                to_label=False, post_process=None):
    _hanging_points_dict = {}
    _filtering_result = filtering_result(
        task_type=task_type, file_path=file_path)
    for key in _filtering_result:
        category = key.split('_')[0]
        if to_label:
            category = synset_to_label[category]
        num_points = _filtering_result[key]['post_points_num']
        if category not in _hanging_points_dict:
            _hanging_points_dict[category] = []
        _hanging_points_dict[category].append(num_points)
    length = max(
        [len(item[1]) for item in _hanging_points_dict.items()])
    for key in _hanging_points_dict:
        if len(_hanging_points_dict[key]) < length:
            _hanging_points_dict[key].extend(
                [0] * (length - len(_hanging_points_dict[key])))
        if post_process == 'median':
            _hanging_points_dict[key] = np.median(_hanging_points_dict[key])
        elif post_process == 'mean':
            _hanging_points_dict[key] = np.mean(_hanging_points_dict[key])

    return _hanging_points_dict


def hanging_points_dict(to_label=False, post_process=None):
    return points_dict(task_type='hanging',
                       to_label=to_label, post_process=post_process)


def pouring_points_dict(to_label=False, post_process=None):
    return points_dict(task_type='pouring',
                       to_label=to_label, post_process=post_process)


def function_synset(task_type, thresh=0,
                    manipulation=True, post_process='median'):
    _function_synset = []
    if task_type == 'hanging':
        _function_points_dict = hanging_points_dict(post_process=post_process)
    elif task_type == 'pouring':
        _function_points_dict = pouring_points_dict(post_process=post_process)
    else:
        raise ValueError('task_type should be "hanging" or "pouring"')

    for synset in _function_points_dict:
        if _function_points_dict[synset] > thresh:
            _function_synset.append(synset)
    if manipulation:
        _function_synset = [
            s for s in _function_synset if s in manipulation_synset()]
    return _function_synset


def hanging_synset(thresh=0, manipulation=True,
                   post_process='median'):
    return function_synset(task_type='hanging', thresh=thresh,
                           manipulation=manipulation,
                           post_process=post_process)


def pouring_synset(thresh=0, manipulation=True,
                   post_process='median'):
    return function_synset(task_type='pouring', thresh=thresh,
                           manipulation=manipulation,
                           post_process=post_process)


def hanging_label(thresh=0, manipulation=True):
    return [synset_to_label[s] for s in hanging_synset(thresh, manipulation)]


def pouring_label(thresh=0, manipulation=True):
    return [synset_to_label[s] for s in pouring_synset(thresh, manipulation)]
