import collections
import os
import glob
from pathlib import Path

import numpy as np
from PIL import Image
from tqdm import tqdm

import pprint


def exif_size(img):
    # Returns exif-corrected PIL size
    s = img.size  # (width, height)
    try:
        rotation = dict(img._getexif().items())[orientation]
        if rotation == 6:  # rotation 270
            s = (s[1], s[0])
        elif rotation == 8:  # rotation 90
            s = (s[1], s[0])
    except:
        pass
    return s


def img2label_paths(img_paths):
    # Define label paths as a function of image paths
    sa, sb = os.sep + 'images' + os.sep, os.sep + 'labels' + os.sep  # /images/, /labels/ substrings
    return [x.replace(sa, sb, 1).replace('.' + x.split('.')[-1], '.txt') for x in img_paths]


def cache_labels(img_files, label_files):
    # Cache dataset labels, check images and read shapes
    x = {}  # dict
    pbar = tqdm(zip(img_files, label_files), desc='Scanning images', total=len(img_files))
    for (img, label) in pbar:
        l = []
        im = Image.open(img)
        im.verify()  # PIL verify
        shape = exif_size(im)  # image size
        # assert (shape[0] > 9) & (shape[1] > 9), 'image size <10 pixels'
        if os.path.isfile(label):
            with open(label, 'r') as f:
                l = np.array([x.split() for x in f.read().splitlines()], dtype=np.float32)  # labels
        if len(l) == 0:
            l = np.zeros((0, 5), dtype=np.float32)
        x[img] = [l, shape]
    # x['hash'] = get_hash(label_files + img_files)
    # torch.save(x, path)  # save for next time
    return x


img_dir = "coco128/images/train2017/"
path = [img_dir]

f = []  # image files
for p in path if isinstance(path, list) else [path]:
    p = Path(p)  # os-agnostic
    if p.is_dir():  # dir
        f += glob.glob(str(p / '**' / '*.*'), recursive=True)
img_files = sorted([x.replace('/', os.sep) for x in f])


# Check cache
label_files = img2label_paths(img_files)  # labels
# cache_path = str(Path(label_files[0]).parent) + '.cache'  # cached labels
# if os.path.isfile(cache_path):
#     cache = torch.load(cache_path)  # load
#     if cache['hash'] != get_hash(label_files + img_files):  # dataset changed
#         cache = cache_labels(cache_path)  # re-cache
# else:
cache = cache_labels(img_files, label_files)  # cache

# Read cache
# cache.pop('hash')  # remove hash
labels, shapes = zip(*cache.values())
# pprint.pprint(labels)
labels = list(labels)


# pprint.pprint(labels)

classes = []
for f in labels:
    cl = []
    for l in f:
        cl.append(int(l[0]))
    classes.append(cl)
# pprint.pprint(classes)

classes_smooth = sum(classes, [])
print("counter:", collections.Counter(classes_smooth))


# HOW TO USE
# docker-instant $(pwd)
# apt update && apt install -y python3-pip
# pip3 install numpy Pillow tqdm
# python3 coco_breakdown.py
