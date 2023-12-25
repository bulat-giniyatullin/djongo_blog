FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /blog_djongo
COPY requirements.txt /blog_djongo
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /blog_djongo