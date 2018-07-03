from .iterators import SequentialIterator
from .prediction_kernels import NgramWeightKernel


class Predictor:
    def __init__(self, data, out_columns):
        self._data = data
        self._out_columns = out_columns
        self._iterator = SequentialIterator()
        self._kernel = NgramWeightKernel(3, data)
