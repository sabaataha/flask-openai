
FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install  -r requirements.txt
RUN apk update && apk add postgresql-client
COPY ./entrypoint.sh /app
RUN chmod +x entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]








