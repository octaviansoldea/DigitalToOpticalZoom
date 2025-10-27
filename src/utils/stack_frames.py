import cv2
import numpy as np
import os
from .align_frames import align_images

def stack_frames(frames_dir, output_path, max_frames=10, save_transforms_dir=None):
    files = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])
    if len(files) < 2:
        raise ValueError("Need at least 2 frames for stacking")

    ref_img = cv2.imread(os.path.join(frames_dir, files[0]), cv2.IMREAD_GRAYSCALE)
    aligned_stack = []
    transforms = []

    for f in files[1:max_frames]:
        print(f"stack_frames processing file: {f}")
        img = cv2.imread(os.path.join(frames_dir, f))
        aligned, warp_matrix = align_images(img, ref_img, return_matrix=True)
        aligned_stack.append(aligned)
        transforms.append(warp_matrix)

        # Save transformation matrices if a directory is provided
        if save_transforms_dir:
            os.makedirs(save_transforms_dir, exist_ok=True)
            np.save(os.path.join(save_transforms_dir, f"{os.path.splitext(f)[0]}_transform.npy"), warp_matrix)

    avg_img = np.mean(aligned_stack, axis=0).astype(np.uint8)
    cv2.imwrite(output_path, avg_img)
    return output_path, transforms