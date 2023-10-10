FROM python:3.10-alpine

WORKDIR /otus

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["--headless"]
ENTRYPOINT ["pytest"]