# Farthest Point Sampling (FPS)
This repo is a vanilla implementation of 3D farthest-point-sampling (FPS) algorithm in paper:
>"Eldar, Yuval, Michael Lindenbaum, Moshe Porat, and Yehoshua Y. Zeevi. "The farthest point strategy for progressive image sampling." IEEE Transactions on Image Processing 6, no. 9 (1997): 1305-1315."

The most important equation is _eq. 2.6_.


# Install Dependencies:
```
conda install numpy
conda install -c open3d-admin open3d 
```

# Usage
To simply run the demo:
```
python main.py
```

Other parameters can be set:

- `--n_samples`: num of samples.
- `--data`: choose an example data to load, available options are "bunny", "circle", "eclipse", or you can set it to a path points to your `ply` file.
- `--manually_step`: step the sampling process manully by pressing "N/n" key.

Example:
```
python main.py --data="circle" --n_samples=50 --manually_step=True
```
