FROM python:3-alpine
COPY _version.py main.py /src/
CMD [ "python3", "/src/main.py" ]