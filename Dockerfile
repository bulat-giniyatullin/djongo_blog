FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /blog_djongo
WORKDIR /blog_djongo
COPY . /blog_djongo/
RUN pip install --upgrade pip && pip install -r requirements.txt
