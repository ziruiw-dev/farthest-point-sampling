import numpy as np

class FPS:
    def __init__(self, pcd_xyz, n_samples):
        self.n_samples = n_samples
        self.pcd = pcd_xyz
        self.num_pts = pcd_xyz.shape[0]
        self.dim = pcd_xyz.shape[1]
        self.samples = None
        self.metric = None
        self.selected_points = np.zeros(shape=(n_samples, self.dim))
        self.remaining_points = np.copy(pcd_xyz)

        # random pick a start
        start_idx = np.random.randint(low=0, high=self.num_pts-1)
        self.selected_points[0] = self.remaining_points[start_idx]
        self.remaining_points = np.delete(self.remaining_points, start_idx, axis=0)  # delete the row of the sampled point
        self.n_selected_pts = 1


    def step(self):
        if self.n_selected_pts < self.n_samples:
            dist_list_entire = np.zeros((self.remaining_points.shape[0], 1))
            for pt_idx in range(self.remaining_points.shape[0]):
                dist = self.__distance__(self.remaining_points[pt_idx], self.selected_points[:self.n_selected_pts])
                dist_list_entire[pt_idx] = np.min(dist)

            selected_idx = np.argmax(dist_list_entire)
            self.selected_points[self.n_selected_pts] = self.remaining_points[selected_idx]
            np.delete(self.remaining_points, selected_idx, axis=0)
            self.n_selected_pts += 1
        else:
            print("Got enough number samples")


    def fit(self):
        for _ in range(1, self.n_samples):
            self.step()


    @staticmethod
    def __distance__(a, b):
        return np.linalg.norm(a - b, ord=2, axis=1)
