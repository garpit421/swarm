FROM python:3.11-slim

WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies with specific versions
RUN pip install --no-cache-dir \
    pandas==2.1.4 \
    numpy==1.26.2 \
    python-dateutil==2.8.2 \
    pytz==2023.3.post1 \
    jsonschema==4.19.1 \
    PyPDF2==3.0.1 \
    pdfminer.six==20221105 \
    beautifulsoup4==4.12.2 \
    lxml==4.9.3 \
    requests==2.31.0 \
    tqdm==4.66.1 \
    matplotlib==3.8.2 \
    seaborn==0.13.0

# Create directory structure
RUN mkdir -p /input_artifacts /logs/agent /logs/verifier /logs/agent/intermediate

# Set Python path
ENV PYTHONPATH=/workspace:$PYTHONPATH
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
