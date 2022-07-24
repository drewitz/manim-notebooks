FROM docker.io/manimcommunity/manim:v0.15.1

COPY --chown=manimuser:manimuser . /manim

RUN apt-get -y update
RUN apt-get -y install git