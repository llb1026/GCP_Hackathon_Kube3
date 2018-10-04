FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install image tensorflow keras

RUN apt-get update && apt-get install -y \
   python3 \
   python3-dev \
   build-essential \
   cmake \
   pkg-config \
   libx11-dev \
   libatlas-base-dev \
   libgtk-3-dev \
   libboost-python-dev \

RUN pip install flask

EXPOSE 5000

CMD ["python", "test.py"]