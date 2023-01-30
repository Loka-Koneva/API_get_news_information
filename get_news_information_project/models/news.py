from datetime import datetime
from typing import List

from pydantic import BaseModel

from .comments import CommentOutput


class NewsBase(BaseModel):
    id: int
    title: str
    date: datetime
    body: str
    deleted: bool


class NewsInput(NewsBase):
    pass


class NewsOutput(NewsBase):
    comments_count: int


class NewsOutputById(NewsOutput):
    comments: List[CommentOutput]



