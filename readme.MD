# Earthbond Technical Assessment - Book Rental App

Welcome to the technical assessment for Book Rental Application! This README.md file will guide you through the setup process, including instructions on how to use and deploy the project both with Docker and without Docker.

## Objectives

Design a web application for student book rentals. 

Here's the core business requirement: Students can rent a book for one month without any charge. If they desire to keep the book beyond the initial month, they are charged a fee determined by the book's page count divided by 100. For instance, if a book has 300 pages, the fee would be $3.00 for every subsequent month.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose
- Python
- Node
- postgresql

## Installation

Follow these steps to get the project up and running on your local machine:

1. [Clone the repository](#) to your local machine.
2. [Navigate to the project directory](#).
3. on your terminal
    ```
    cd backend
    ```
    setup virtual enviroment
    Activate your virtual enviroment
    ```
    cd ./book_rental
    pip install -r requirements.txt
    python manage.py makemigrations book_rental_app
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
    ```
4. 
```
cd ../../frontend
npm install
npm run dev
```
## Usage

### With Docker

To run the project using Docker, follow these steps:

1. [Ensure Docker is installed](#) on your local machine.
2. Open a terminal and navigate to the project directory.
3. Build the Docker image:
  ```
  docker compose up
  ```
