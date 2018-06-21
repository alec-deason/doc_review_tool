from pathlib import Path

import pandas as pd
import numpy as np

from .globals import DocReviewerError


class DataError(DocReviewerError):
    pass


class DataModel:
    def __init__(self, data_path: str):
        self._data = self._load(Path(data_path).resolve())

    @property
    def columns(self):
        return self._data.columns

    @staticmethod
    def _load(path: Path) -> pd.DataFrame:
        if not path.exists() or path.is_dir():
            raise DataError("Must provide a path to a csv or hdf file.")

        if path.suffix == '.csv':
            data = pd.read_csv(path)
        elif path.suffix == '.hdf':
            data = pd.read_hdf(path)
        else:
            raise DataError("Must provide a path to a csv or hdf file.")

        return data

    def add_column(self, column_name, data_type):
        self._data[column_name] = pd.Series(np.empty(len(self._data), dtype=data_type), index=self._data.index)

    def get_data(self, row, column):
        return self._data.at[row, column]

    def set_data(self, data, row, column):
        self._data.at[row, column] = data
