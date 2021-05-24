from alpine:latest

RUN apk add --no-cache python3-dev
RUN apk add --no-cache py3-pip


WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

ENTRYPOINT  ["python3"]

CMD ["start.py"]
