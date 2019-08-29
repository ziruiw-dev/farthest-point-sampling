import numpy as np

class FPS:
    def __init__(self, pcd_xyz, n_samples):
        self.n_samples = n_samples
        self.pcd_xyz = pcd_xyz
        self.n_pts = pcd_xyz.shape[0]
        self.dim = pcd_xyz.shape[1]
        self.selected_pts = np.zeros(shape=(n_samples, self.dim))
        self.remaining_pts = np.copy(pcd_xyz)

        self.grouping_radius = None
        self.labels = None  # (n_pts, 1), States which point belong to which cluster.

        # Random pick a start
        self.start_idx = np.random.randint(low=0, high=self.n_pts - 1)
        self.selected_pts[0] = self.remaining_pts[self.start_idx]
        self.n_selected_pts = 1

    def get_selected_pts(self):
        return self.selected_pts

    def step(self):
        if self.n_selected_pts < self.n_samples:
            dist_list = np.zeros((self.remaining_pts.shape[0], 1))
            for pt_idx in range(self.remaining_pts.shape[0]):
                dist = self.__distance__(self.remaining_pts[pt_idx], self.selected_pts[:self.n_selected_pts])
                dist_list[pt_idx] = np.min(dist)

            selected_idx = np.argmax(dist_list)
            self.selected_pts[self.n_selected_pts] = self.remaining_pts[selected_idx]
            self.n_selected_pts += 1
        else:
            print("Got enough number samples")


    def fit(self):
        for _ in range(1, self.n_samples):
            self.step()
        return self.get_selected_pts()


    def group(self, radius):
        self.grouping_radius = radius
        self.labels = np.zeros((self.n_pts,), dtype=int)

        for i, selected_pt in enumerate(self.selected_pts):
            dist = self.__distance__(selected_pt, self.pcd_xyz)
            self.labels[dist < self.grouping_radius] = i

        return self.labels


    @staticmethod
    def __distance__(a, b):
        return np.linalg.norm(a - b, ord=2, axis=1)
