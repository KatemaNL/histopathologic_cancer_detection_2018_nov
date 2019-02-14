import os


class PathHelper:
    GREYSCALE_CENTER_FILENAME_POSTFIX = '_greyscale_center'
    DATA_DIR = 'data'
    TRAIN_DATA_SUBDIR = 'train'
    TEST_DATA_SUBDIR = 'test'
    PREPROCESSED_DATA_SUBDIR = 'preprocessed'
    SAMPLE_DATA_SUBDIR = 'samples'
    FULL_DATASET_DATA_SUBDIR = 'dataset'
    LABEL_SUBDIR = 'labels'

    @classmethod
    def get_dir_for_dataset(cls, dataset_name: str, preprocessed=False, full_dataset=False, labels=False):
        files_dir = ''
        if dataset_name == 'train':
            files_dir = os.path.join(cls.DATA_DIR, cls.TRAIN_DATA_SUBDIR)
        if dataset_name == 'test':
            files_dir = os.path.join(cls.DATA_DIR, cls.TEST_DATA_SUBDIR)
        if labels:
            files_dir = os.path.join(files_dir, cls.LABEL_SUBDIR)
        else:
            if preprocessed:
                files_dir = os.path.join(files_dir, cls.PREPROCESSED_DATA_SUBDIR)
            if not full_dataset:
                files_dir = os.path.join(files_dir, cls.SAMPLE_DATA_SUBDIR)
            else:
                files_dir = os.path.join(files_dir, cls.FULL_DATASET_DATA_SUBDIR)
        return files_dir
