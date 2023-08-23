from dataclasses import dataclass


@dataclass
class Workspace:
    id: str
    owner: str
    instances: list[str]


@dataclass
class Instance:
    id: str
    owner: str
    workspace: str


@dataclass
class User:
    id: str
