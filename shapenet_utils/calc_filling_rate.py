from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import trimesh
from tqdm import tqdm

from shapenet_utils.shapenet_synset_dict import synset_to_label
from shapenet_utils.functions import save_json


def make_category_filling_rate(data, to_label):
    synset = []
    value = []
    for d in [[k, v] for k, v in data.items()]:
        synset.append(d[0])
        value_list = []
        for _d in [[k, v] for k, v in d[1].items()]:
            value_list.append(_d[1])
        value.append(np.mean(value_list))
    if to_label:
        label = [synset_to_label[s] for s in synset]
        return label, value
    else:
        return synset, value


def make_graph(data, method):
    label, value = make_category_filling_rate(data, to_label=True)
    plt.bar(label, value, width=0.5)
    plt.title('filling rate %s' % method.replace('_', ' '))
    plt.xlabel('category')
    plt.xticks(rotation=90)
    plt.ylabel('filling rate')
    plt.tight_layout()
    # plt.show()
    plt.savefig('filling_rate_%s.png' % method, format='png', dpi=300)


if __name__ == '__main__':
    shapenet_dir = '/media/kosuke/SANDISK/meshdata/ShapeNetCore.v2'
    paths = sorted(list(Path(shapenet_dir).glob(
        '*/*/models/model_normalized.obj')))

    data = {}
    data_box = {}
    prev_category = None

    for path in tqdm(paths):
        category = str(path.parent.parent.parent.name)
        # if prev_category is not None and category == prev_category:
        #     if len(data[category]) == 3:
        #         continue
        if category not in data:
            data[category] = {}
            data_box[category] = {}

        prev_category = category
        mesh = trimesh.load(
            str(path), skip_materials=True,
            skip_texture=True, force='mesh')

        voxel_path = path.parent / 'model_normalized.solid.binvox'
        if voxel_path.exists():
            voxel = trimesh.load(str(voxel_path))
        else:
            voxel = mesh.voxelized(0.01)

        filling_rate_box = voxel.volume / mesh.bounding_box_oriented.volume
        filling_rate_convex_hull = voxel.volume / mesh.convex_hull.volume
        print(filling_rate_convex_hull)
        data_id = str(path.parent.parent.name)
        data_box[category][data_id] = filling_rate_box
        data[category][data_id] = filling_rate_convex_hull

    save_json('shapenet_filling_rate_convex_hull.json', data)
    save_json('shapenet_filling_rate_bounding_box.json', data_box)

    make_graph(data, 'convex_hull')
    make_graph(data_box, 'bounding_box')
