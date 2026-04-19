import cv2
import os

image_folder = "/data/Gopi/Aditi/HDR-4DGS/output/HDR-4D-Syn/tank/02260114/images/20000"   # folder containing images
video_name = "output_video.mp4"
fps = 30

images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")])

first_frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

for img in images:
    frame = cv2.imread(os.path.join(image_folder, img))
    video.write(frame)

video.release()