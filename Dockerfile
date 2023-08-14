FROM python:3.11-slim

WORKDIR /usr/app/

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

ARG OPENAI_API_KEY
ARG WEAVIATE_API_KEY
ARG WEAVIATE_URL

ENV PORT=7000

COPY .env ./
COPY src/ ./src/

ENTRYPOINT ["python", "src/app.py"]