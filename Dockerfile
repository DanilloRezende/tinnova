FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    SHELL=/bin/bash LANG=en_US.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    
WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY .build.sh ./
COPY manage.py ./

