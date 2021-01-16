FROM python:3.8.3-slim-buster AS release
WORKDIR /app

## install non-python dependencies
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get install -y --no-install-recommends dnsutils inetutils-ping bash curl jq=1.5* && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

# Install dependencies:
RUN pip install --upgrade pip && pip install wheel
COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . /app

ENTRYPOINT ["gunicorn", "-c", "./src/gunicorn.conf.py", "src.server:app"]
