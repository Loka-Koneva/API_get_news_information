from typing import List

from fastapi import APIRouter

from ..models.news import NewsOutput, NewsOutputById

router = APIRouter()


@router.get('/', response_model=List[NewsOutput])
def get_news():
    pass


@router.get('/news/{id}', response_model=NewsOutputById)
def get_news_by_id():
    pass
