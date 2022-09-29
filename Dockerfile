FROM ubuntu:latest

RUN set -ex && \
    apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    mkdir /usr/local/project/

COPY . /usr/local/project/

RUN pip3 install --upgrade pip
RUN cd /usr/local/project && \
    pip3 install -r requirements.txt

# env variable
ENV LANG C.UTF-8
ENV PYTHONIOENCODING UTF-8

# when images run, will complie main.py
WORKDIR /usr/local/project
CMD ["python3", "main.py"]