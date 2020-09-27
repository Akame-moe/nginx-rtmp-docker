FROM ubuntu:latest

ARG NGINX_VERSION=1.9.2
ARG NGINX_SOURCE_URL=http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz
ARG RTMP_MODULE_SOURCE_URL=https://github.com/arut/nginx-rtmp-module/archive/master.tar.gz


RUN set -ex \
    && apt update \
    && apt install -y build-essential libpcre3 libpcre3-dev libssl-dev wget \
    && mkdir -p /tmp/source \
    && cd /tmp/source \
    && wget ${NGINX_SOURCE_URL} -O nginx-src.tar.gz \
    && wget $RTMP_MODULE_SOURCE_URL -O rtmp-module-src.tar.gz \
    && tar -zvxf rtmp-module-src.tar.gz \
    && tar -zvxf nginx-src.tar.gz  \
    && cd nginx-${NGINX_VERSION} \
    && ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master \
    && make \
    && make install \
    && rm -rf /tmp/source

#bin:/usr/local/nginx/sbin/nginx
#config:/usr/local/nginx/conf/nginx.conf
COPY nginx.conf /usr/local/nginx/conf/nginx.conf

EXPOSE 8080 1935
ENTRYPOINT [ "/usr/local/nginx/sbin/nginx" ]
CMD [ "-c", "/usr/local/nginx/conf/nginx.conf" ]