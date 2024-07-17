FROM python:3.9.7-alpine

ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV DB_URI=${DB_URI}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

WORKDIR /app
COPY requirements.txt /app/
RUN pip install  --no-cache-dir -r requirements.txt
RUN apk add --no-cache postgresql-client
COPY . /app
RUN chmod +x entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]








