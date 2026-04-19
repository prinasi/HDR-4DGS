import cv2
import numpy as np
import glob

files = sorted(glob.glob("test_hdr_20000_*.exr"))

first = cv2.imread(files[0], cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
h, w, _ = first.shape

video = cv2.VideoWriter("video.mp4",
                        cv2.VideoWriter_fourcc(*'mp4v'),
                        30,
                        (w, h))

for f in files:
    img = cv2.imread(f, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

    # simple HDR tone mapping
    img = img * 2.0  # increase exposure
    img = img / (1.0 + img)

    img = np.clip(img, 0, 1)
    img8 = (img * 255).astype(np.uint8)

    video.write(img8[:, :, ::-1])

video.release()