FROM python:3-alpine3.10

WORKDIR /workdir/1
ADD . .

RUN pip install notion falcon waitress

ENTRYPOINT ["python", "main.py"]