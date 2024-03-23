#!/bin/bash
echo "Create migrations"
python3 manage.py makemigrations book_rental_app
echo "=================================="

echo "Migrate"
python3 manage.py migrate
echo "=================================="

echo "Start server"
python3 manage.py runserver 0.0.0.0:8000