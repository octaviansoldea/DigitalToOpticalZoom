import cv2
import os

def extract_frames(video_path, output_dir, max_frames=None):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_dir}/frame_{count:04d}.png", frame)
        count += 1
        if max_frames and count >= max_frames:
            break
    cap.release()
    return count
