# Weather Application

This is a simple weather application that provides weather information for a given city.

## Project Structure

```
weather-app
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── weather
│   │   ├── __init__.py
│   │   └── weather_service.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

You will be prompted to enter a city name. The application will then fetch and display the current weather information for that city.

## Dependencies

This project requires the following Python packages:
- requests

Make sure to install them using the provided `requirements.txt` file.