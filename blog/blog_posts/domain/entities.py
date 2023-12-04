import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class BaseEntity:
    pass


@dataclass
class AuthorEntity(BaseEntity):
    pk: int
    email: str
    username: str
    profile_pic: str
    following: List[int]
    followers: List[int]
    bio: str
