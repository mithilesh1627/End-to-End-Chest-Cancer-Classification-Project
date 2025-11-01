FROM python:3.10-slim

WORKDIR /app

COPY . /app

EXPOSE 8080:8080

RUN pip install -r requirements.txt

CMD [ "python",'app.py']
