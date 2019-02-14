import os
import numpy as np
from histopathologic.path_helper import PathHelper


class DatasetLoader:
    @staticmethod
    def load_dataset_from_path(filepath: str):
        print('Loading dataset from: ' + str(filepath))
        dataset = np.load(filepath)
        print('Loaded dataset shape: ' + str(dataset.shape))
        return dataset

    @classmethod
    def load_dataset(cls, dataset_name: str, **kwargs):
        load_dir = PathHelper.get_dir_for_dataset(dataset_name, **kwargs)
        filename = 'dataset.npy'
        filepath = os.path.join(load_dir, filename)
        dataset = cls.load_dataset_from_path(filepath)
        return dataset
