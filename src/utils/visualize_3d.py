import os
import numpy as np
import plotly.graph_objects as go
import cv2

def visualize_3d(frames_dir, transforms, output_path):
    camera_centers = [(0, 0, 0)]  # Start with the reference image at the origin
    image_planes = []

    for i, warp_matrix in enumerate(transforms):
        # Compute the camera center in 3D (translation components)
        tx, ty = warp_matrix[0, 2], warp_matrix[1, 2]
        camera_centers.append((tx, ty, 0))

        # Add the image plane (projected in 3D)
        img_path = os.path.join(frames_dir, sorted(os.listdir(frames_dir))[i + 1])
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        h, w = img.shape[:2]
        x, y = np.meshgrid(np.linspace(tx, tx + w, w), np.linspace(ty, ty + h, h))
        z = np.zeros_like(x)
        image_planes.append((x, y, z, img))

    # Create a 3D plot
    fig = go.Figure()

    # Add camera centers
    xs, ys, zs = zip(*camera_centers)
    fig.add_trace(go.Scatter3d(x=xs, y=ys, z=zs, mode='markers', marker=dict(size=5, color='red'), name='Camera Centers'))

    # Add image planes
    for i, (x, y, z, img) in enumerate(image_planes):
        fig.add_trace(go.Surface(z=z, x=x, y=y, surfacecolor=img, colorscale='gray', showscale=False, name=f'Image {i+1}'))

    # Set plot layout
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ), title="3D Visualization of Images and Camera Centers")

    # Save the plot as an HTML file
    fig.write_html(output_path)
    print(f"3D visualization saved to: {output_path}")

    # Show the plot
    fig.show()