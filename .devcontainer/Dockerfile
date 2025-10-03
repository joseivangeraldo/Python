# Use Ubuntu as base image
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh \
    && $CONDA_DIR/bin/conda clean -tipsy \
    && ln -s $CONDA_DIR/bin/conda /usr/local/bin/conda

ENV PATH=$CONDA_DIR/bin:$PATH

# Optionally, create a default environment
RUN conda create -n codespace python=3.10 -y

# Set bash to activate conda by default
RUN echo "source $CONDA_DIR/etc/profile.d/conda.sh && conda activate codespace" >> /root/.bashrc
