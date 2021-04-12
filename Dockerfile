FROM python:3.8

RUN apt-get update
RUN pip install --upgrade pip

COPY src /src
COPY build_job.py /build_job.py
COPY requirements/base.txt /requirements.txt

RUN chmod +x /build_job.py

WORKDIR /

RUN pip install -r requirements.txt

ENTRYPOINT ["/build_job.py"]