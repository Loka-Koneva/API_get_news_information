import aiofiles
from datetime import datetime
from typing import List, Union

from fastapi import status, HTTPException

from ..models.input_data import InputNewsData, InputCommentsData
from ..models.news import NewsOutput, NewsInput, OutputNewsData, NewsOutputById
from ..models.comments import CommentOutput
from ..settings import settings


async def get_news_from_files() -> InputNewsData:
    async with aiofiles.open(settings.path_to_news) as f:
        content_news = await f.read()

    return InputNewsData.parse_raw(content_news)


async def get_comments_from_files() -> InputCommentsData:
    async with aiofiles.open(settings.path_to_comments) as f:
        content_comments = await f.read()

    return InputCommentsData.parse_raw(content_comments)


def _get_comments_by_news_id(
        news_id: int,
        comments: InputCommentsData
) -> Union[List[CommentOutput], list]:
    comments = filter(lambda x: x.news_id == news_id,
                      comments.comments)

    return list(comments)


def _get_output_news_by_id(
        news_id: int,
        input_news: InputNewsData
) -> Union[List[NewsInput], list]:
    output_news = filter(lambda x: x.id == news_id, input_news.news)
    return list(output_news)


def _get_output_news(
        input_news: InputNewsData,
        input_comments: InputCommentsData
) -> Union[List[NewsOutput], list]:
    output_news = []
    for news in input_news.news:
        if not news.deleted and datetime.now() > news.date:
            comments = _get_comments_by_news_id(news.id, input_comments)
            result = NewsOutput(**news.dict(), comments_count=len(comments))
            output_news.append(result)
    return output_news


def check_exception(output_news_list: Union[List[NewsInput], list]):
    if len(output_news_list) == 0 \
            or output_news_list[0].deleted \
            or output_news_list[0].date > datetime.now():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_output_news() -> OutputNewsData:
    input_news = await get_news_from_files()
    input_comments = await get_comments_from_files()
    output_news = _get_output_news(input_news, input_comments)
    output_news.sort(key=lambda x: x.date)

    return OutputNewsData(news=output_news, news_count=len(output_news))


async def get_output_news_by_id(news_id) -> NewsOutputById:
    input_news = await get_news_from_files()
    input_comments = await get_comments_from_files()
    output_news_list = _get_output_news_by_id(news_id, input_news)
    check_exception(output_news_list)
    output_comments = _get_comments_by_news_id(news_id,  input_comments)
    output_comments.sort(key=lambda x: x.date)

    return NewsOutputById(**output_news_list[0].dict(),
                          comments=output_comments,
                          comments_count=len(output_comments))
