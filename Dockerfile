FROM python:3.7.2-jessie

MAINTAINER rochan87@gmail.com

ENV SRVHOME=/admin

WORKDIR $SRVHOME

COPY ./ $SRVHOME

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [". ./start.sh"]