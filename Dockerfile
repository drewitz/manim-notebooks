FROM docker.io/manimcommunity/manim:v0.15.1

COPY --chown=manimuser:manimuser . /manim

RUN sudo apt-get update
RUN sudo apt-get install -y git