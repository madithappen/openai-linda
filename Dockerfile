FROM python:3.8-slim

LABEL name ="openai-linda" \
      maintainer="Stephen M Abbott <stephenabbott20@gmail.com>" \
      version="1.0"

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN apt-get update
RUN apt-get install gcc libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev libespeak1 -y
RUN pip install -r requirements.txt

# Copy the source code
COPY src /app/src

# Copy the main script
COPY main.py /app/main.py

# Set the entry point
ENTRYPOINT ["python", "main.py"]