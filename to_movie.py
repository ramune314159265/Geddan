import json
import sys

import cv2

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('video.mp4',fourcc, 25.0, (480, 360))

with open('./☆ゲッダン☆.json') as f:
	images_list = json.load(f)

	for i in images_list:
		image = cv2.imread('./all_flames/' + i)
		if image is None:
			print("image is not found")
			break
		video.write(image)

video.release()
print('written')
