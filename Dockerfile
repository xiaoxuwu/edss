FROM python:3-slim

# Enable production settings by default; for development, this can be set to
# `false` in `docker run --env`
ENV DJANGO_PRODUCTION=true
ENV PYTHONBUFFERED 1

# Set terminal to be noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    git \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim \
    curl \
    nginx \
    supervisor

# # Project Files and Settings
# ARG PROJECT=edss_backend
# ARG PROJECT_DIR=/${PROJECT}
# RUN mkdir -p $PROJECT_DIR
# WORKDIR $PROJECT_DIR
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt

# Expose ports
# 80 = Nginx
# 8000 = Gunicorn
# 3306 = MySQL
EXPOSE 80 8000

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

ADD . /code/
ADD ./src/student_showcase/api /code/src/student_showcase
RUN chmod ug+x ./initialize.sh