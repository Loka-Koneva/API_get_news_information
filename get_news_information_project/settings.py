from pydantic import BaseSettings


class Settings(BaseSettings):
    path_to_news: str = 'get_news_information_project/test_data/news.json'
    path_to_comments: str = 'get_news_information_project/test_data/comments.json'


settings = Settings(
    _env_file='get_news_information_project/.env',
    _env_file_encoding='utf-8',
)
