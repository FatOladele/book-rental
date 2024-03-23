FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

COPY django.sh ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]

