# Dev container image for this repository — includes NASM and common build tools
FROM mcr.microsoft.com/devcontainers/base:ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    jupyter notebook \
    git \
    build-essential \
  && apt-get clean \