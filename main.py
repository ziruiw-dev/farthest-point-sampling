import open3d as o3d
import numpy as np
import argparse

from load_pcd import load_pcd
from fps import FPS


def vis_final_result(pcd_xyz, selected_xyz):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pcd_xyz)
    pcd.paint_uniform_color([0, 1, 0])  # original points: green

    pcd_selected = o3d.geometry.PointCloud()
    pcd_selected.points = o3d.utility.Vector3dVector(selected_xyz)
    pcd_selected.paint_uniform_color([1, 0, 0])  # selected points: red

    o3d.visualization.draw_geometries([pcd, pcd_selected])

    return


def vis_step():
    return


if __name__ == '__main__':

    example_data = "bunny"
    n_samples = 50
    manully_step = False

    pcd_xyz = load_pcd(example_data)

    fps = FPS(pcd_xyz, n_samples)

    if manully_step is False:
        fps.fit()
        vis_final_result(fps.pcd, fps.selected_points)
    else:
        pass