FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/facade-service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/facade-service/requirements.txt

COPY . /code/facade-service

CMD ["uvicorn", "facade-service.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--reload-dir", "/code/facade-service"]