FROM python:3.10.5-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app .

# Set the command to run your application using chainlit
CMD ["chainlit", "run", "osada.py"]
