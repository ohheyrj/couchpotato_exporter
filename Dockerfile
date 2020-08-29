FROM python:3.7.9-slim-buster

COPY couchpotato_exporter/couchpotato_exporter.py couchpotato_exporter.py

RUN pip install prometheus_client urllib3

EXPOSE 9316

ENTRYPOINT [ "python3", "couchpotato_exporter.py" ]