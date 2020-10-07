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
 '02747177': 'trash bin ',
 '02773838': 'bag ',
 '02801938': 'basket',
 '02808440': 'bathtub',
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
