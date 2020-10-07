import os.path as osp

from shapenet_utils.file_io import load_json
from shapenet_utils.filling_rate import make_category_filling_rate

data_dir = osp.abspath(osp.dirname(__file__))


def filling_rate(method='convex_hull'):
    if method == 'convex_hull':
        return load_json(
            osp.join(data_dir, 'shapenet_filling_rate_convex_hull.json'))
    elif method == 'bounding_box':
        return load_json(
            osp.join(data_dir, 'shapenet_filling_rate_bounding_box.json'))


def category_filling_rate(method='convex_hull', to_label=False, sort=False):
    data = filling_rate(method)
    return make_category_filling_rate(data, to_label, sort)


# def filter_filling_rate(
#         min_value=0., max_value=1., method='convex_hull', to_label=False):
#     """Filter categories by filling rate

#     Parameters
#     ----------
#     min_value : float, optional
#         min filling rate value, by default 0.
#     max_value : float, optional
#         max filling rate value, by default 1.
#     method : str, optional
#         'convex_hull' or 'bounding_box', by default 'convex_hull'
#     to_label : bool, optional
#         If True, convert synset to label, by default False

#     Returns
#     -------
#     filtered_synset : list[float]
#     filtered_value : list[float]
#     """
#     synset, value = category_filling_rate(method, to_label)
#     filtered_value = []
#     filtered_synset = []
#     for i, v in enumerate(value):
#         if min_value < v < max_value:
#             filtered_value.appned(v)
#             filtered_synset.appned(synset[i])
#     return filtered_synset, filtered_value
