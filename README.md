
## Dependencies:

PyTorch 1.3 and other packages listed in `requirements.txt`.

## Dataset
[NYU Depth v2] Dataset

[SUN RGB-D Benchmark suit](http://rgbd.cs.princeton.edu/paper.pdf). Please download the data on the [official webpage](http://rgbd.cs.princeton.edu), unzip it, and place it with a folder tree like this,

```bash
SOMEPATH # Some arbitrary path
├── SUNRGBD # The unzip folder of SUNRGBD.zip
└── SUNRGBDtoolbox # The unzip folder of SUNRGBDtoolbox.zip
```

The root path `SOMEPATH` should be passed to the program using the `--data-dir SOMEPATH` argument.

## Usage:

For training, you can pass the following argument,

```
python main_train.py --cuda
```

If you do not have enough GPU memory, you can pass the `--checkpoint` option to enable the checkpoint container in PyTorch >= 0.4. For other configuration, such as batch size and learning rate, please check the ArgumentParser in [RedNet_train.py](RedNet_train.py).

For inference, you should run the [RedNet_inference.py](RedNet_inference.py) like this,

```
python inference.py --cuda
```

The pre-trained weight is released [here] for result reproduction.

## License

This software is released under a creative commons license which allows for personal and research use only.
For a commercial license please contact the authors.
You can view a license summary here: http://creativecommons.org/licenses/by-nc/4.0/
