FROM python:3.10


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "app.main:app", \
     "--host", "0.0.0.0", \
     "--port", "80", \
     "--no-server-header"]
