FROM python:3.8.3-slim

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc libc-dev
RUN pip install -r /requirements.txt

RUN mkdir /backend
COPY ./backend /backend
WORKDIR /backend
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 744 /vol/web
USER user

CMD ["entrypoint.sh"]