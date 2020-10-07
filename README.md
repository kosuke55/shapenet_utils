# shapenet_utils

### Install
```
pip install -e .
```

```
In [1]: from shapenet_utils import synset_to_label, category_filling_rate

In [2]: synset_to_label
Out[2]:
{'02691156': 'airplane',
 '02747177': 'trash bin ',
 '02773838': 'bag ',
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
 '02958343': 'car ',
 '02992529': 'cellular telephone',
 '03001627': 'chair',
 '03046257': 'clock',
 '03085013': 'keyboard',
 '03207941': 'dishwasher',
 '03211117': 'display',
 '03261776': 'earphone',
 '03325088': 'faucet',
 '03337140': 'file cabinet',
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
 '04074963': 'remote',
 '04090263': 'rifle',
 '04099429': 'rocket',
 '04225987': 'skateboard',
 '04256520': 'sofa',
 '04330267': 'stove',
 '04379243': 'table ',
 '04401088': 'telephone',
 '04460130': 'tower',
 '04468005': 'train',
 '04530566': 'watercraft',
 '04554684': 'washer'}

In [3]: label, value = category_filling_rate(method='convex_hull', to_label=True)
Out[3]: value
[0.9274702724843501,
 0.5695847453986468,
 0.3831096826087529,
 0.6880423710990163,
 0.7539653216532688,
 0.9510796449519844,
 0.636804187208665,
 1.0171738537692023,
 0.5608166699984033,
 0.2898344341983889,
 0.30448144761597995,
 0.9716584869125827,
 0.8063006134185886,
 0.5391106380147636,
 0.2368718490564961,
 0.5389352466950139,
 0.36685061828840226,
 1.0042192739862916,
 0.6418562933325935,
 0.2857848051599215,
 0.20674748843344498,
 0.9633626555883376,
 0.8368855019131544,
 0.5506567259766126,
 0.4171439148007365,
 0.6316031701444631,
 0.8687623811720252,
 1.0154023680987743,
 0.6521205498031758,
 0.1692592569068655,
 0.8072992763544153,
 0.48886088829087376,
 0.23636623482049327,
 0.951116159758458,
 0.23348070921282857,
 0.5090312213922484,
 0.7357072047077154,
 0.7433282369549693,
 0.5421771757301681,
 0.7290206652514003,
 0.26813991702632956,
 0.46922672888486905,
 0.3516724088426876,
 0.5420597379212854,
 0.36788512028741643,
 0.5182860551378584,
 0.7235519477729031,
 0.17415447988717522,
 0.25597652044020086,
 0.320851439521325,
 0.8708492736464309,
 0.37213782760065384,
 0.709486121642566,
 0.20992030585085217,
 0.1868298955127837]
 ```

 <img src="https://user-images.githubusercontent.com/39142679/95360572-84f47880-0906-11eb-9455-b6abbbd580c1.png" height="600">
