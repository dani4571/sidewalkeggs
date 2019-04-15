# Install python stuff

FROM python:3.7-alpine as py_builder
WORKDIR /opt/sidewalkeggs
COPY requirements.txt bower.json ./
RUN whoami
RUN apk --update add npm mariadb-dev alpine-sdk  jpeg-dev \
	&& pip install --upgrade pip \
	&& pip install -r requirements.txt \
	&& npm install -g bower \
	&& npm install \
	&& bower install --allow-root \	
	&& apk del alpine-sdk 



FROM py_builder as code_copy
WORKDIR /opt/sidewalkeggs
COPY . .
