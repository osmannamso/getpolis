FROM python:3.8.0

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
# Copy project
COPY . /code/
