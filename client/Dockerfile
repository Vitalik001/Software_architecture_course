FROM python:3.8-slim

WORKDIR /client

COPY . /client

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5701

CMD ["python", "writer.py"]
