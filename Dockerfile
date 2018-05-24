FROM python:3.6-alpine

MAINTAINER trivago Studio Platform <arnulfo.solis@trivago.com>

ENV APP_DIR "/app"

ENV PYTHONPATH "/app/src"

ENV PATH "/app/bin:${PATH}"

RUN apk add --no-cache build-base git

COPY ./requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY . ${APP_DIR}/

VOLUME ["/app/repos"]

WORKDIR ${APP_DIR}/bin

ENTRYPOINT ["/usr/local/bin/python3"]

CMD ["/app/bin/repos"]
