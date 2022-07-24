FROM docker.io/manimcommunity/manim:v0.15.1

COPY --chown=manimuser:manimuser . /manim

RUN apt-get update
RUN apt-get install -y git