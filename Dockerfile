FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip git && pip3 install gunicorn flask flask-restful pymongo dnspython flask-pymongo

RUN git clone https://github.com/fcortesj/vaso-server.git

WORKDIR /vaso-server/server

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "server:app"]