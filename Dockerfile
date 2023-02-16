FROM python:3.8-slim 
ENV PYTHONUNBUFFERED 1
COPY . /app/
WORKDIR /app 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD python crawler.py

