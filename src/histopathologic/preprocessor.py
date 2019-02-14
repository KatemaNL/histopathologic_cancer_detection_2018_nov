from histopathologic.dataset import Dataset
from keras.preprocessing.image import ImageDataGenerator


class Preprocessor:
    def __init__(self, datapath_base: str):
        self.datapath_base = datapath_base

    def preprocess(self):
        self.preprocess_train_dataset()

    def preprocess_train_dataset(self):
        pass

    @staticmethod
    def augment_dataset(dataset: Dataset, featurewise_center: bool, featurewise_std_normalization: bool,
                        rotation_range: int, width_shift_range: float, height_shift_range: float,
                        horizontal_flip: bool, batch_size: int) -> Dataset:
        assert isinstance(dataset, Dataset)
        print('Augmenting dataset of shape: ' + str(dataset.x.shape))
        datagenerator = ImageDataGenerator(
            featurewise_center=featurewise_center,
            featurewise_std_normalization=featurewise_std_normalization,
            rotation_range=rotation_range,
            width_shift_range=width_shift_range,
            height_shift_range=height_shift_range,
            horizontal_flip=horizontal_flip)

        print('Fitting data')
        datagenerator.fit(dataset.x)

        print('Augmenting')
        data_iterator = datagenerator.flow(x=dataset.x, y=dataset.y, batch_size=batch_size)
        batches = 0
        x_augmented = []
        y_augmented = []
        for x in data_iterator:
            #x_batch, y_batch
            # TODO: ...
            batches += 1
            if batches >= len(dataset.x) / batch_size:
                break

        return dataset
