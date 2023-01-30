from typing import List

from pydantic import BaseModel

from .news import NewsInput
from .comments import CommentInput


class InputNewsData(BaseModel):
    news: List[NewsInput]
    news_count: int


class InputCommentsData(BaseModel):
    comments: List[CommentInput]
    comments_count: int
