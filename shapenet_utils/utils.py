from shapenet_utils.filling_rate import filter_filling_rate


def all_synset():
    synset, _ = filter_filling_rate(0, 1)
    return synset


def all_label():
    label, _ = filter_filling_rate(0, 1, to_label=True)
    return label
