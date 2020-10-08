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


def filtering_result():
    return load_json(
        osp.join(data_dir, 'filtering_result.json'))


def hanging_points_dict(to_label=False, post_process=None):
    _hanging_points_dict = {}
    _filtering_result = filtering_result()
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


def hanging_synset(thresh=0, manipulation=True, post_process='median'):
    _hanging_synset = []
    _hanging_points_dict = hanging_points_dict(post_process=post_process)
    for synset in _hanging_points_dict:
        if _hanging_points_dict[synset] > thresh:
            _hanging_synset.append(synset)
    if manipulation:
        _hanging_synset = [
            s for s in _hanging_synset if s in manipulation_synset()]
    return _hanging_synset


def hanging_label(thresh=0, manipulation=True):
    return [synset_to_label[s] for s in hanging_synset(thresh, manipulation)]
