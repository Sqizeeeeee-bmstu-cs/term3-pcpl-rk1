class Driver:
    def __init__(self, id: int, name: str, salary: int, autopark_id: int):
        self.id = id
        self.name = name
        self.salary = salary
        self.autopark_id = autopark_id


class Autopark:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class ConnectionDriverToAutopark:
    def __init__(self, autopark_id: int, driver_id: int):
        self.autopark_id = autopark_id
        self.driver_id = driver_id
