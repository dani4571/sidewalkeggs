# Install python stuff

FROM python:3.7-alpine as py_builder
WORKDIR /opt/sidewalkeggs
COPY . .
RUN apk --update add npm mariadb-dev alpine-sdk  jpeg-dev \
	&& pip install --upgrade pip \
	&& pip install -r requirements2.txt \
	&& npm install -g bower \
	&& npm isntall \
	&& bower install \
	&& apk del alpine-sdk 

