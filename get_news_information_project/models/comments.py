from datetime import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    id: int
    news_id: int
    title: str
    date: datetime
    comment: str


class CommentInput(CommentBase):
    pass


class CommentOutput(CommentBase):
    pass
