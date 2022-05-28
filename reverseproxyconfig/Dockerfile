FROM python:3.8.5-alpine
COPY . /code
WORKDIR /code
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install -r requirements.txt

