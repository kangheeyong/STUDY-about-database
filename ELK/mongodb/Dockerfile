FROM mongo:4.2.8

WORKDIR /usr/src
RUN mkdir configs
WORKDIR /usr/src/configs

COPY config/replicaSet.js .
COPY config/setup.sh .

RUN chmod +x ./setup.sh

CMD ["./setup.sh"]