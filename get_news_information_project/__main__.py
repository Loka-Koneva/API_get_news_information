import uvicorn

from .settings import settings

uvicorn.run(
    'get_news_information_project.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
