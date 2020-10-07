import os.path as osp

from shapenet_utils.functions import load_json
from shapenet_utils.calc_filling_rate import make_category_filling_rate

data_dir = osp.abspath(osp.dirname(__file__))


def filling_rate(method='convex_hull'):
    if method == 'convex_hull':
        return load_json(
            osp.join(data_dir, 'shapenet_filling_rate_convex_hull.json'))
    elif method == 'bounding_box':
        return load_json(
            osp.join(data_dir, 'shapenet_filling_rate_bounding_box.json'))


def category_filling_rate(method='convex_hull', to_label=False):
    data = filling_rate(method)
    return make_category_filling_rate(data, to_label)
