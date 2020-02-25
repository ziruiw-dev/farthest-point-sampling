# Farthest Point Sampling (FPS)
This repo is a vanilla implementation of 3D farthest-point-sampling (FPS) algorithm in paper:
>"Eldar, Yuval, Michael Lindenbaum, Moshe Porat, and Yehoshua Y. Zeevi. "The farthest point strategy for progressive image sampling." IEEE Transactions on Image Processing 6, no. 9 (1997): 1305-1315."

The most important equation is _eq. 2.6_.

Two demos are avaible in this repo:
1. `main_sample.py`: demonstrates how the points are sampled in FPS and provides a function to visulise sampling process step by step.
2. `main_group.py`: A simple point grouping method which groups points using a fix radius sphere over the FPS sampled points. 


## Install Dependencies:
```
conda install numpy
conda install -c open3d-admin open3d=0.7
```

## Usage
To simply run the fps **sampling** demo:
```
python main_sample.py
```

To simply run the fps **grouping** demo:
```
python main_group.py
```


Other parameters can be set:

- `--n_samples`: num of samples.
- `--data`: choose an example data to load, available options are "bunny", "circle", "eclipse", or you can set it to a path points to your `ply` file.
- `--manually_step`: **(only in `main_sample`)** step the sampling process manully by pressing "N/n" key.
- `--group_radius`: **(only in `main_group`)** set the grouping radius.

Example:
```
python main_sample.py --data="circle" --n_samples=50 --manually_step=True
python main_group.py --data="circle" --n_samples=50 --group_radius=0.06
```
