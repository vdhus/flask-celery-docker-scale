FROM ubuntu:artful

ENV PYTHONUNBUFFERED 1
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -q vim-nox git build-essential python3 \
    python3-dev python3-pip 

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

ENV HOST 0.0.0.0
ENV PORT 5000
ENV DEBUG true

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code
