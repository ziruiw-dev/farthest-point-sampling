import open3d as o3d
import numpy as np
import argparse

from load_pcd import load_pcd
# from fps_v0 import FPS      # Simple loop
from fps_v1 import FPS      # Utilise broadcasting


def fps_group_demo(pcd_xyz, num_clusters, colormap, radius):

    fps_v0 = FPS(pcd_xyz, num_clusters)
    print("Initialised FPS sampler successfully.")

    fps_v0.fit()
    print("FPS sampling finished.")

    labels = fps_v0.group(radius)
    print("FPS grouping finished.")

    pcd_obj = o3d.geometry.PointCloud()
    pcd_obj.points = o3d.utility.Vector3dVector(pcd_xyz)

    pcd_color = np.zeros_like(pcd_xyz)
    for i, l in enumerate(labels):
        color = colormap[l]
        pcd_color[i] = color

    pcd_obj.colors = o3d.utility.Vector3dVector(pcd_color)

    return pcd_obj


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="bunny",
                        help="Load some points data, choices are \"bunny\", \"circle\", \"eclipse\", "
                             "or \"a_path_to_your_ply_file\".")
    parser.add_argument("--n_samples", type=int, default=50, help="Number of samples we would like to draw.")
    parser.add_argument("--group_radius", type=float, default=0.05,
                        help="Radius for grouping. Need to be considered according to the point cloud scale.")

    args = parser.parse_args()

    example_data = args.data
    n_samples = args.n_samples
    group_radius = args.group_radius

    pcd_xyz = load_pcd(example_data)
    print("Loaded ", example_data, "with shape: ", pcd_xyz.shape)

    if n_samples > pcd_xyz.shape[0]:
        print("WARNING: required {0:d} samples but the loaded point cloud only has {1:d} points.\n "
              "Change the n_sample to {2:d}.".format(n_samples, pcd_xyz.shape[0], pcd_xyz.shape[0]))
        print("WARNING: sampling")
        n_samples = pcd_xyz.shape[0]

    # Generate some color randomly to mark each cluster.
    colormap = np.random.uniform(low=0, high=1, size=(n_samples, 3))

    print("Running FPS over {0:d} points and getting {1:d} samples.".format(pcd_xyz.shape[0], n_samples))
    fps_pts = fps_group_demo(pcd_xyz, n_samples, colormap, group_radius)

    o3d.visualization.draw_geometries([fps_pts])
    print("Tips: Press `Ctrl` + `+/-` to change point size.")

