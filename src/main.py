from utils.extract_frames import extract_frames
from utils.stack_frames import stack_frames
from super_resolve import super_resolve

video_path = "data/MAH00319.MP4"
frames_dir = "data/frames"
stacked_path = "data/stacked.png"
sr_path = "data/super_res.png"

#n = extract_frames(video_path, frames_dir)#, max_frames=30)
#print(f"Extracted {n} frames")

stacked = stack_frames(frames_dir, stacked_path, max_frames=10)
print(f"Saved stacked image to {stacked}")

#output = super_resolve(stacked, sr_path)
#print(f"Super-resolved image saved to {output}")
