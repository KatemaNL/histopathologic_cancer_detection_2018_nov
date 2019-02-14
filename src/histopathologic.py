import os
import sys

sys.path.append('src')
from histopathologic.path_helper import PathHelper
from histopathologic.dataset_loader import DatasetLoader
from histopathologic.preprocessor import Preprocessor
from histopathologic.dataset import Dataset


print('Python executable: ' + str(sys.executable))
print('Python version: ' + str(sys.version))
print('Working dir: ' + str(os.getcwd()))


def main():
    # dataset_path = PathHelper.get_dir_for_dataset('train')
    dataset = DatasetLoader.load_dataset('train', preprocessed=True, full_dataset=True)

    dataset1 = dataset[0:3, :, :, :]
    dataset1 = Dataset(x=dataset1, y=None)

    dataset1_aug = Preprocessor.augment_dataset(
        dataset=dataset1,
        featurewise_center=True,
        featurewise_std_normalization=True,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        batch_size=32
    )


if __name__ == "__main__":
    main()
