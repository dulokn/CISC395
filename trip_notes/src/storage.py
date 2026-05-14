import os
import json
from dataclasses import asdict
from src.models import Destination, TripCollection

def get_data_path():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(BASE_DIR, "data", "trips.json")

def load_trips() -> TripCollection:
    DATA_PATH = get_data_path()
    collection = TripCollection()
    
    if not os.path.exists(DATA_PATH):
        return collection
        
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            for d in data:
                collection.add(Destination(**d))
    except (json.JSONDecodeError, FileNotFoundError):
        pass
        
    return collection

def save_trips(collection: TripCollection) -> None:
    DATA_PATH = get_data_path()
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    
    list_of_dicts = [asdict(dest) for dest in collection.get_all()]
    
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(list_of_dicts, f, indent=2)
