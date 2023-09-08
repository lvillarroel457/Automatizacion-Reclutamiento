
# Automatización Reclutamiento

A Flask application that integrates with OpenAI for automating recruitment processes.

## Prerequisites

- Python 3.9.7
- OpenAI API key

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lvillarroel457/Automatizacion-Reclutamiento.git
   cd Automatizacion-Reclutamiento
   ```

2. **Set up a virtual environment** (optional, but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set the Python Path**:
   ```bash
   source set_python_path.sh
   ```

5. **Configuration**:
   Create a `config.ini` file in the root directory with the following format:

   ```
   [OPENAI]
   API_KEY = YOUR_OPENAI_API_KEY
   ```

   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

## Running the Application

1. Activate the virtual environment (if you set one up):
   ```bash
   source venv/bin/activate
   ```

2. Run the Flask application:
   ```bash
   flask run
   ```

   By default, the app will be accessible at `http://127.0.0.1:5000/`.

## Running Tests

To run the unittests:

```bash
python -m unittest test/test_runner.py
```

## Contribution

Please follow the standard pull request process if you have any updates or features to add.
