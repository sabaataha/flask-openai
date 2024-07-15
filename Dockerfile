FROM python:3.9-alpine


ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV DB_URI=${DB_URI}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

WORKDIR /app
COPY . /app
RUN pip install  -r requirements.txt
RUN apk update && apk add postgresql-client
COPY ./entrypoint.sh /app
RUN chmod +x entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]








