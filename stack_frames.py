import cv2
import numpy as np
import os
from align_frames import align_images

def stack_frames(frames_dir, output_path, max_frames=10):
    files = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])
    if len(files) < 2:
        raise ValueError("Need at least 2 frames for stacking")

    ref_img = cv2.imread(os.path.join(frames_dir, files[0]), cv2.IMREAD_GRAYSCALE)
    aligned_stack = []

    for f in files[1:max_frames]:
        print(f"stack_frames processing file: {f}")
        img = cv2.imread(os.path.join(frames_dir, f))
        aligned = align_images(img, ref_img)
        aligned_stack.append(aligned)
        

    avg_img = np.mean(aligned_stack, axis=0).astype(np.uint8)
    cv2.imwrite(output_path, avg_img)
    return output_path
