import glob
import json
import os
import re
import shutil

import imagehash
import pandas as pd
from PIL import Image

images_dir_path = os.getcwd() + "\\all_flames\\"
save_dir_path = os.getcwd() + "\\flames\\"

#https://teshi-learn.com/2021-04/python-glob-glob-sorted/
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r"(\d+)", text) ]

images = sorted(glob.glob(images_dir_path + "*"), key=natural_keys)

hashes = {}
flames = []
for i in images:
	hash = imagehash.phash(Image.open(i))
	hashes_distance = sorted(map(lambda x: [(hash - x), x], hashes), key=lambda x: x[0])
	if hashes_distance == []:
		hashes[hash] = os.path.basename(save_dir_path + i)
		flames.append(os.path.basename(save_dir_path + i))
		continue
	most_near_hash = hashes_distance[0]
	if 5 < most_near_hash[0]:
		hashes[hash] = os.path.basename(save_dir_path + i)
		flames.append(os.path.basename(save_dir_path + i))
		continue
	else:
		flames.append(hashes[most_near_hash[1]])

os.makedirs(save_dir_path, exist_ok=True)
for i in hashes.values():
	shutil.copy(images_dir_path + i, save_dir_path)

with open("./output.json", "w") as f:
    json.dump(flames, f, indent=4)
