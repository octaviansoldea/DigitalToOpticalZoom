import cv2
import numpy as np

def align_images(img, ref_img, return_matrix=False):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    warp_mode = cv2.MOTION_EUCLIDEAN
    warp_matrix = np.eye(2, 3, dtype=np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5000, 1e-10)

    cc, warp_matrix = cv2.findTransformECC(ref_img, img_gray, warp_matrix, warp_mode, criteria)

    aligned = cv2.warpAffine(img, warp_matrix, (ref_img.shape[1], ref_img.shape[0]),
                             flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)

    if return_matrix:
        return aligned, warp_matrix
    return aligned