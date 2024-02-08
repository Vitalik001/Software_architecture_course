FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/logging-service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/logging-service/requirements.txt

COPY . /code/logging-service

CMD ["uvicorn", "logging-service.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--reload-dir", "/code/logging-service"]