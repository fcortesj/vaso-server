FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip git && pip3 install gunicorn flask flask-restful pymongo dnspython flask-pymongo

RUN git clone https://github.com/fcortesj/vaso-server.git
RUN cd vaso-server && git pull && cd ..

WORKDIR /vaso-server/server

EXPOSE 8080

CMD ["gunicorn", "-w", "4", "-b", ":8080", "server:app"]