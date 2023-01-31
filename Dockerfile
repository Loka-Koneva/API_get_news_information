FROM python:3.8-slim

COPY ./requirements.txt /tmp/requirements.txt

RUN set -eux \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./get_news_information_project /get_news_information_project

CMD ["uvicorn", "get_news_information_project.app:app", "--host", "0.0.0.0", "--port", "8000"]
