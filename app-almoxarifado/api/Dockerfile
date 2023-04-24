FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -ms /bin/bash developer

USER developer

COPY . .

CMD ["python", "app.py"]
