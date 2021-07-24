from budget.storage.common.storage import Storage


class CsvStorage(Storage):
    def __init__(self, file_path: str):
        super().__init__()

    def save(self, transaction):
        print(f'save csv tansaction')