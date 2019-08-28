import open3d as o3d
import numpy as np
import argparse

from load_pcd import load_pcd
from fps import FPS


if __name__ == '__main__':

    example_data = "bunny"
    n_samples = 50
    manully_step = True

    pcd_xyz = load_pcd(example_data)

    fps = FPS(pcd_xyz, n_samples)


    pcd_all = o3d.geometry.PointCloud()
    pcd_all.points = o3d.utility.Vector3dVector(fps.pcd_xyz)
    pcd_all.paint_uniform_color([0, 1, 0])  # original: green

    pcd_selected = o3d.geometry.PointCloud()


    if manully_step is False:
        fps.fit()

        pcd_selected.points = o3d.utility.Vector3dVector(fps.selected_points)
        pcd_selected.paint_uniform_color([1, 0, 0])  # selected: red

        o3d.visualization.draw_geometries([pcd_all, pcd_selected])
    else:

        def fit_step_callback(vis):
            fps.step()

            pcd_selected.points = o3d.utility.Vector3dVector(fps.selected_points)
            pcd_selected.paint_uniform_color([1, 0, 0])  # selected:  red
            vis.update_geometry()


        key_to_callback = {ord("N"): fit_step_callback}

        # Draw the first sampled points.
        pcd_selected.points = o3d.utility.Vector3dVector(fps.selected_points)
        pcd_selected.paint_uniform_color([1, 0, 0])  # selected: red

        # Draw a new sample points every time press "N/n" key.
        o3d.visualization.draw_geometries_with_key_callbacks([pcd_all, pcd_selected], key_to_callback)
