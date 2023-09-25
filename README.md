
# Automatización Reclutamiento

A Flask application that integrates with OpenAI for automating recruitment processes.

## Prerequisites

- Python 3.9.7
- OpenAI API key
- Docker

## Setup and Installation

### Installing Docker

#### For Windows:

1. Visit the Docker Desktop for Windows [download page](https://www.docker.com/products/docker-desktop).
2. Click "Download from Docker Hub".
3. On the Docker Hub page, click "Get Docker".
4. After downloading, double-click on the installer file to run it.
5. Follow the on-screen instructions to complete the installation.

#### For Mac:

1. Visit the Docker Desktop for Mac [download page](https://www.docker.com/products/docker-desktop).
2. Click "Download from Docker Hub".
3. On the Docker Hub page, click "Get Docker".
4. After downloading, drag and drop the Docker.app into the Applications folder.
5. Open the Applications folder and click on Docker.app to start it.

### Application Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lvillarroel457/Automatizacion-Reclutamiento.git
   cd Automatizacion-Reclutamiento
   ```

2. **Configuration**:
   Create a `.env` file in the root directory with the following format:

   ```
   OPENAI_API_KEY = YOUR_OPENAI_API_KEY
   ```

   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

3. **Build the Docker Image**:
   ```bash
   docker build -t automatizacion-reclutamiento .
   ```

## Running the Application

1. Run the Flask application inside a Docker container:
   ```bash
   docker run -p 5000:5000 automatizacion-reclutamiento
   ```

   By default, the app will be accessible at `http://127.0.0.1:5000/`.

## Running Tests

To run the unittests:

```bash
docker run -it automatizacion-reclutamiento python -m unittest test/test_runner.py
```

## Contribution

Please follow the standard pull request process if you have any updates or features to add.
