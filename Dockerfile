# Use an official Python runtime as a parent image
FROM python:3.12.6-slim

# Set the working directory in the container
WORKDIR /app

COPY . /app

CMD ["python", "book.py"]
