from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    path_to_news: str = 'get_news_information_project/test_data/news.json'
    path_to_comments: str = 'get_news_information_project/test_data/comments.json'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
