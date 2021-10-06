FROM python:3.8

RUN apt-get update
RUN pip install --upgrade pip

COPY build.py /build.py
COPY requirements.txt /requirements.txt

RUN chmod +x /build.py

WORKDIR /

RUN pip install -r requirements.txt

ENTRYPOINT ["/build.py"]