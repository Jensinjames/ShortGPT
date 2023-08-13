```python
import json

class JsonDataStore:

    def __init__(self):
        self.reddit_data_schema = []

    def store_data(self, data):
        self.reddit_data_schema.append(data)

    def save_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.reddit_data_schema, file)

    def load_from_json(self, file_path):
        with open(file_path, 'r') as file:
            self.reddit_data_schema = json.load(file)
```