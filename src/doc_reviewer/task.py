from .globals import DocReviewerError


class TaskError(DocReviewerError):
    """Error raised when an invalid task is specified."""
    pass


class TaskModel:
    """Encapsulates information about the task being performed."""

    MAX_REVIEW_COLS = 3
    MAX_TARGET_COLS = 2

    def __init__(self, task='reclassify'):
        self.task = task
        self._review_columns = []
        self._target_columns = []

    @property
    def review_columns(self):
        return self._review_columns

    @property
    def target_columns(self):
        return self._target_columns

    def add_review_column(self, review_column):
        if len(self.review_columns) < TaskModel.MAX_REVIEW_COLS:
            self.review_columns.append(review_column)
        else:
            raise TaskError("Too many review columns specified.")

    def add_target_column(self, target_column):
        if len(self.target_columns) < TaskModel.MAX_TARGET_COLS:
            self._target_columns.append(target_column)
        else:
            raise TaskError("Too many target columns specified.")
