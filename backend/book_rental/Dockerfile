FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

COPY django.sh ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]

