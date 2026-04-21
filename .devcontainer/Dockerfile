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

# Configure uv to use USTC mirror
ENV UV_INDEX_URL=https://pypi.mirrors.ustc.edu.cn/simple/

# Set fish as default shell
RUN chsh -s /usr/bin/fish root
SHELL ["/usr/bin/fish", "-c"]

# Configure fish: set uv environment variables and paths
RUN mkdir -p /root/.config/fish && \
    echo 'set -x UV_INDEX_URL https://pypi.mirrors.ustc.edu.cn/simple/' >> /root/.config/fish/config.fish && \
    echo 'set -x PYTHONDONTWRITEBYTECODE 1' >> /root/.config/fish/config.fish

# Verify uv is available
RUN uv --version

# Set working directory
WORKDIR /workspace

# Keep container running
CMD ["sleep", "infinity"]
