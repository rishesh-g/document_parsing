# Use NVIDIA’s CUDA base image with Ubuntu
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# Install Python and pip
RUN apt update && apt install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy your backend code
COPY . .
# Upgrade pip, setuptools, and wheel
RUN pip3 install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip3 install --upgrade pip setuptools wheel && \
    pip3 install --no-cache-dir --upgrade --index-url https://pypi.org/simple/ -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Run the Flask app (update if you use a different entrypoint)
CMD ["python3", "app_be.py"]