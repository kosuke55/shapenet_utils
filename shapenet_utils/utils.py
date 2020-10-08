from shapenet_utils.filling_rate import filter_filling_rate
from shapenet_utils.shapenet_synset_dict import label_to_synset


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
        = [label_to_synset[l] for l in manipulation_label()]
    return manipulation_synset
