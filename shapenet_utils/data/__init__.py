import os.path as osp

from shapenet_utils.functions import load_json

data_dir = osp.abspath(osp.dirname(__file__))


def filling_rate(method='convex_hull'):
    if method == 'convex_hull':
        return load_json(
            osp.join(data_dir, 'shapenet_filling_rate_convex_hull.json'))
    elif method == 'bounding_box':
        return load_json(
            osp.join(data_dir, 'shapenet_filling_rate_bounding_box.json'))
