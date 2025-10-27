from utils.extract_frames import extract_frames
from utils.stack_frames import stack_frames
from utils.visualize_3d import visualize_3d

video_path = "data/MAH00319.MP4"
frames_dir = "data/frames"
stacked_path = "data/stacked.png"
sr_path = "data/super_res.png"
transforms_dir = "data/transforms"
visualization_path = "data/3d_visualization.html"

# Extract frames (uncomment if needed)
# n = extract_frames(video_path, frames_dir)
# print(f"Extracted {n} frames")

# Stack frames and save transformation matrices
stacked, transforms = stack_frames(frames_dir, stacked_path, max_frames=10, save_transforms_dir=transforms_dir)

# Visualize in 3D
visualize_3d(frames_dir, transforms, visualization_path)

#output = super_resolve(stacked, sr_path)
#print(f"Super-resolved image saved to {output}")
