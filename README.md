# shapenet_utils

### Install
```
pip install -e .
```

```
In [1]: from shapenet_utils import synset_to_label, category_filling_rate, filter_filling_rate

In [2]: synset_to_label
Out[2]:
{'02691156': 'airplane',
 '02747177': 'trash_bin',
 '02773838': 'bag',
 '02801938': 'basket',
 '02808440': 'bathtub',
 '02818832': 'bed',
 '02828884': 'bench',
 '02834778': 'bicycle',
 '02843684': 'birdhouse',
 '02871439': 'bookshelf',
 '02876657': 'bottle',
 '02880940': 'bowl',
 '02924116': 'bus',
 '02933112': 'cabinet',
 '02942699': 'camera',
 '02946921': 'can',
 '02954340': 'cap',
 '02958343': 'car',
 '02992529': 'cellular_telephone',
 '03001627': 'chair',
 '03046257': 'clock',
 '03085013': 'keyboard',
 '03207941': 'dishwasher',
 '03211117': 'display',
 '03261776': 'earphone',
 '03325088': 'faucet',
 '03337140': 'file_cabinet',
 '03467517': 'guitar',
 '03513137': 'helmet',
 '03593526': 'jar',
 '03624134': 'knife',
 '03636649': 'lamp',
 '03642806': 'laptop',
 '03691459': 'loudspeaker',
 '03710193': 'mailbox',
 '03759954': 'microphone',
 '03761084': 'microwave',
 '03790512': 'motorbike',
 '03797390': 'mug',
 '03928116': 'piano',
 '03938244': 'pillow',
 '03948459': 'pistol',
 '03991062': 'pot',
 '04004475': 'printer',
 '04074963': 'remote_control',
 '04090263': 'rifle',
 '04099429': 'rocket',
 '04225987': 'skateboard',
 '04256520': 'sofa',
 '04330267': 'stove',
 '04379243': 'table',
 '04401088': 'telephone',
 '04460130': 'tower',
 '04468005': 'train',
 '04530566': 'watercraft',
 '04554684': 'washer'}
 ...

In [3]: label, value = category_filling_rate(method='convex_hull', sort=False, to_label=True)
Out[3]: value
[0.18682989551278367,
 0.5380902359048308,
 0.6874236684944967,
 0.2676654243221465,
 0.3664247096367181,
 ...

In [4]: filtered_label, filtered_value = filter_filling_rate(0, 0.5, sort=False, to_label=True)
In [5]: filtered_value
Out[5]:
[0.18682989551278367,
 0.2676654243221465,
 0.3664247096367181,
 0.36788512028741643,
 0.16914450910344583,
 ...
```

 <img src="https://user-images.githubusercontent.com/39142679/95375879-3a312b80-091b-11eb-9fe7-6cfb05428be4.png" height="600">
