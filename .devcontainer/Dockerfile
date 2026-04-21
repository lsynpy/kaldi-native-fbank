FROM ubuntu:22.04

# Configure USTC Ubuntu mirror for faster apt downloads
RUN sed -i 's/ports.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# Install system dependencies
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    wget \
    ca-certificates \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    g++ \
    gcc \
    make \
    pkg-config \
    fish \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python
RUN ln -sf /usr/bin/python3 /usr/local/bin/python && \
    ln -sf /usr/bin/pip3 /usr/local/bin/pip

# Configure pip to use USTC mirror
RUN pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/

# Install uv
RUN pip install uv

# Configure uv to use USTC mirror and default venv
ENV UV_INDEX_URL=https://pypi.mirrors.ustc.edu.cn/simple/
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# Create venv outside workspace (persists through workspace mount)
RUN uv venv --seed /opt/venv && \
    uv pip install --python /opt/venv/bin/python numpy pytest cmake && \
    uv pip install --python /opt/venv/bin/python torch==2.4.0+cpu -f https://download.pytorch.org/whl/torch/ && \
    uv pip install --python /opt/venv/bin/python kaldifeat==1.25.4.dev20240725+cpu.torch2.4.0 -f https://csukuangfj.github.io/kaldifeat/cpu.html && \
    uv pip install --python /opt/venv/bin/python pyyaml

# Verify installation
RUN /opt/venv/bin/python -c "import torch; print('torch ok:', torch.__version__)"

# Set fish as default shell
RUN chsh -s /usr/bin/fish root
SHELL ["/usr/bin/fish", "-c"]

# Configure fish: set uv environment variables and paths
RUN mkdir -p /root/.config/fish && \
    echo 'set -x UV_INDEX_URL https://pypi.mirrors.ustc.edu.cn/simple/' >> /root/.config/fish/config.fish && \
    echo 'set -x PYTHONDONTWRITEBYTECODE 1' >> /root/.config/fish/config.fish

# Set working directory
WORKDIR /workspaces/kaldi-native-fbank

# Keep container running
CMD ["sleep", "infinity"]
