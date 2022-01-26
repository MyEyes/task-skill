from .v_0_0_1 import Schema_v_0_0_1
class Schema:
    def __init__(self) -> None:
        self.versions = {
            '0.0.1': Schema_v_0_0_1()
        }
        self.first_schema = self.versions['0.0.1']

    def create_schema(self, db):
        self.first_schema.create_schema(db)

    def set_data(self, db):
        self.first_schema.set_data(db)

    def migrate(self, old_schema, db):
        pass