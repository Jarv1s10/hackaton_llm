FROM python:3.10

ADD ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

ADD .env /code/.env
ADD ./app/ /code
WORKDIR /code