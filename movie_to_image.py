import os

import cv2

movie_path = os.getcwd() + "\\☆ゲッダン☆.mp4"
save_dir_path = os.getcwd() + "\\all_flames\\"

capture = cv2.VideoCapture(movie_path)

os.makedirs(save_dir_path, exist_ok=True)
n = 0

while True:
	ret, frame = capture.read()
	if ret:
		cv2.imwrite(save_dir_path + str(n) + ".png", frame)
		n += 1
	else:
		break
