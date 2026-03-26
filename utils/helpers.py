import json
import os
from config.config import Config

def load_json_data(file_path):
    full_path = os.path.join(Config.BASE_DIR, file_path)
    with open(full_path, "r") as f:
        return json.load(f)