FROM alpine:latest as prepare_env
WORKDIR /app

RUN apk --no-cache -q add \
    python3 python3-dev py3-pip libffi libffi-dev musl-dev gcc
RUN pip3 install -q --ignore-installed distlib pipenv
RUN python3 -m venv /app/venv

ENV PATH="/app/venv/bin:$PATH" VIRTUAL_ENV="/app/venv"

COPY requirements.txt .
RUN pip3 install -q -r requirements.txt


COPY app.py .
RUN python3 app.py

CMD ["python3", "-m", "app"]
