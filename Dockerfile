# Use a multi-stage build for a smaller final image
FROM python:3.11-alpine3.19 AS builder

# Set up a non-root user for security
RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY app .

# Final stage (to reduce image size)
FROM python:3.11-alpine3.19

# Create the same user and working directory
RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser/app
EXPOSE 8000

# Copy only the necessary files from the builder stage
COPY --from=builder /home/myuser/app .

# Set the command to run your application using chainlit
CMD ["chainlit", "run", "osada.py"]