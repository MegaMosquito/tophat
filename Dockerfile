FROM python:3-buster

RUN apt update && apt install -y python3-dev

# Get the support software for the Pimoroni Unicorn Hat HD
RUN pip3 install numpy
RUN pip3 install spidev
RUN pip3 install unicornhathd

# Copy in the source file
COPY ./tophat.py /

WORKDIR /
CMD python3 tophat.py


