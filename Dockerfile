# Use a base image with Python and specify the version
FROM python:3.9-slim

# Install required system libraries
# Install required system libraries and wget


# Install required system libraries and wget
RUN apt-get update && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*

# Download libssl1.1 package
RUN wget "http://ports.ubuntu.com/ubuntu-ports/pool/main/o/openssl/libssl1.1_1.1.1-1ubuntu2.1~18.04.23_arm64.deb"

# Install libssl1.1 package using dpkg
RUN dpkg -i ./libssl1.1_1.1.1-1ubuntu2.1~18.04.23_arm64.deb

# Clean up downloaded package
RUN rm ./libssl1.1_1.1.1-1ubuntu2.1~18.04.23_arm64.deb

# Install other required system libraries
RUN apt-get update && \
    apt-get install -y \
    libc6 \
    libpthread-stubs0-dev \
    libasound2 \
    ca-certificates \
    alsa-utils \
    pulseaudio

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your Streamlit app is using
EXPOSE 8501

# Command to run your Streamlit application
CMD ["streamlit", "run", "myapp.py"]


