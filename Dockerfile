FROM python:3.11-slim

WORKDIR /usr/app/

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

ENV PORT=7000

COPY .env ./
COPY src/ ./src/

ENTRYPOINT ["python", "src/app.py"]