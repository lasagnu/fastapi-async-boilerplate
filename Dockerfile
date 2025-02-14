FROM python:3.12-slim

WORKDIR /app
EXPOSE 443

COPY ./backend/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./backend /app/

CMD uvicorn app:app --host 0.0.0.0 --port 8080