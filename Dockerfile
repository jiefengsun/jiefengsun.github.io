

# # Use the official Python base image
# FROM python:3.10-slim

# # # Install locales and set the locale
# # RUN apt-get update && \
# #     apt-get install -y locales && \
# #     echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
# #     locale-gen
# # Install locales and set the locale
# RUN apt-get update && \
#     apt-get install -y locales && \
#     echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
#     locale-gen && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Set environment variables for locale
# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US:en
# ENV LC_ALL en_US.UTF-8

# # Set the working directory
# WORKDIR /app

# # Copy the project's dependency file (assuming you have requirements.txt)
# COPY requirements.txt ./

# # Install the project dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy all project files to the working directory
# COPY . .

# # Expose the port (assuming you will use Pelican's development server, port 8000)
# EXPOSE 8000

# # Set the container startup command with the correct configuration file
# CMD ["pelican", "--listen", "--autoreload", "-s", "pelicanconf2.py", "-b", "0.0.0.0"]

# Use the official Python base image
FROM python:3.10-slim

# Install locales and set the locale
RUN apt-get update && \
    apt-get install -y locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set the working directory
WORKDIR /app

# Copy the project's dependency file
COPY requirements.txt ./

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the working directory
# COPY . .

# Expose the port
EXPOSE 8000

# Set the container startup command with the correct configuration file
# CMD ["pelican", "--listen", "--autoreload", "-s", "/app/pelicanconf2.py", "-b", "0.0.0.0"]
