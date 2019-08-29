import open3d as o3d
import numpy as np
import math


def __points_on_circle__(radius, num_pts):
    pi = math.pi

    # a circle in 2D
    result_xy = np.asarray([(math.cos(2 * pi / num_pts * x) * radius,
                             math.sin(2 * pi / num_pts * x) * radius) for x in range(0, num_pts)])

    # put it in 3D by adding z = 0
    result_xyz = np.append(result_xy, np.zeros((num_pts, 1)), axis=1)
    return result_xyz


def __points_on_eclipse__(radius, num_pts):
    pi = math.pi
    eclipse_factor = 2

    # a circle in 2D
    result_xy = np.asarray([(math.cos(2 * pi / num_pts * x) * radius,
                             eclipse_factor * math.sin(2 * pi / num_pts * x) * radius) for x in range(0, num_pts)])

    # put it in 3D by adding z = 0
    result_xyz = np.append(result_xy, np.zeros((num_pts, 1)), axis=1)
    return result_xyz



def load_pcd(data="bunny"):
    """
    :param data:
        Choice: bunny, circle, eclipse, "a_ply_file_path"
    :return:
        A (N, 3) numpy array contains loaded 3D points
    """

    pcd_xyz = None
    if data == "bunny":
        pcd = o3d.io.read_point_cloud("./example_data/mesh/bunny/reconstruction/bun_zipper_res2.ply")
        pcd_xyz = np.asarray(pcd.points)
    elif data == "circle":
        pcd_xyz = __points_on_circle__(radius=1, num_pts=1000)
    elif data == "eclipse":
        pcd_xyz = __points_on_eclipse__(radius=1, num_pts=1000)
    else:
        # Try to load from specified folder
        pcd = o3d.io.read_point_cloud(data)
        pcd_xyz = np.asarray(pcd.points)

    return pcd_xyz


if __name__ == '__main__':
    bunny_xyz = load_pcd("bunny")
    print("Bunny data shape: ", bunny_xyz.shape)

    circle_xyz = load_pcd("circle")
    print("Cirlce data shape: ", circle_xyz.shape)

    eclipse_xyz = load_pcd("eclipse")
    print("Eclipse data shape: ", eclipse_xyz.shape)