from fastapi import APIRouter

from ..models.news import OutputNewsData, NewsOutputById
from ..services.news import get_output_news, get_output_news_by_id

router = APIRouter()


@router.get('/', response_model=OutputNewsData)
async def get_news():
    return await get_output_news()


@router.get('/news/{news_id}', response_model=NewsOutputById)
async def get_news_by_id(news_id: int):
    return await get_output_news_by_id(news_id)
