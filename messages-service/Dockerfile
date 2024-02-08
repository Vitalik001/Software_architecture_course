FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/messages-service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/messages-service/requirements.txt

COPY . /code/messages-service

CMD ["uvicorn", "messages-service.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--reload-dir", "/code/messages-service"]