# Flask Application with Docker Deployment
This repository contains a simple Flask application that calculates 
the temperature based on the user's location and greets the user with their name. 
It is deployed using Docker for easy setup and deployment.

## Prerequisites
Before you begin, ensure you have the following installed:

- Docker: Install Docker
- Python 3.9 or higher

## Getting Started
Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Wikki2000/HNG-internship_python/
cd 0-location_weather_api
```

### 2. Build the Docker Image
Build the Docker image using the provided Dockerfile.

```bash
docker build -t flask-app .
```

### 3. Run the Docker Container
Run the Docker container, exposing port 5000 from the container to your local machine.

## Project Structure
```bash
.
├── app.py                # Main Flask application file
├── Dockerfile            # Dockerfile for building the Docker image
├── requirements.txt      # List of Python dependencies
└── README.md             # Project README file
```

## Additional Notes
Replace Mark in the URL with any name to customize the greeting message.
Ensure you have necessary environment variables set if required by your Flask application.
For production deployment, consider using a cloud platform like Adaptable or AWS.

## Troubleshooting
If you encounter any issues, check Docker logs using docker logs <container_id_or_name> for more information.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
