from models.models import Sheep
from typing import Dict

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, sheep: Sheep) -> Sheep:
        if sheep.id in self.data:
            raise ValueError(f"Sheep with this ID already exists")
        self.data[sheep.id] = sheep
        return sheep

    def get_all_sheep(self):
        return list(self.data.values())

    def update_sheep(self, sheep_id: str, updated_data: dict):
        if sheep_id in self.data:
            existing = self.data[sheep_id]
            for key, value in updated_data.items():
                setattr(existing, key, value)
            return existing
        return None

    def delete_sheep(self, sheep_id: str):
        return self.data.pop(sheep_id, None) is not None

db = FakeDB()
db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Blondie", breed="Polypay", sex="ram"),
    3: Sheep(id=3, name="Deedee", breed="Jacobs Four Horns", sex="ram"),
    4: Sheep(id=4, name="Rommy", breed="Romney", sex="ewe"),
    5: Sheep(id=5, name="Vala", breed="Valais Blacknose", sex="ewe"),
    6: Sheep(id=6, name="Esther", breed="Border Leicester", sex="ewe")
}