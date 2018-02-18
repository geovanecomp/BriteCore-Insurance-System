FROM node:8

MAINTAINER Geovane Pacheco <geovane.pacheco99@gmail.com>

WORKDIR /usr/src/app

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

RUN npm install
