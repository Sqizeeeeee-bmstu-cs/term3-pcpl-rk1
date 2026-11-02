from dataclasses import dataclass


@dataclass(frozen=True)
class Driver:
    id: int
    name: str
    salary: int
    autopark_id: int


@dataclass(frozen=True)
class Autopark:
    id: int
    name: str


@dataclass(frozen=True)
class ConnectionDriverToAutopark:
    autopark_id: int
    driver_id: int
