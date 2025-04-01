# Flask Superheroes API

## Overview

This project is a Flask-based REST API for managing superheroes, their powers and the relationships between them. It allows users to retrieve heroes and their respective powers, update power descriptions and assign powers to heroes with specific strength levels.

## Features

- Retrieve a list of all heroes.
- Retrieve a specific hero by ID, including their assigned powers.
- Retrieve a list of all available powers.
- Retrieve and update a specific power's description.
- Assign a power to a hero with a defined strength level.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite

## Installation and Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python (3.7 or later)
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Setup Steps

1. **Clone the repository**

   ```sh
   git clone <repository_url>
   cd phase-4-code-challenge-superheroes
   ```

2. **Install dependencies and Create a virtual environment**

   ```sh
   pipenv install 
   pipenv shell
   ```

3. **Change directory in Server - In your terminal**

   ```sh
   cd server
   export FLASK_APP=app.py
   export FLASK_RUN_PORT=5555 or a port No. of your choice
   ```

4. **Set up the database**

   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Seed the database**

   ```sh
   python seed.py
   ```

6. **Run the application**

   ```sh
   python app.py
   Alternatively using flask run
   ```

## API Endpoints

### **1. Home Route**

**`GET /`**  
Returns a welcome message for the API.

### **2. Heroes**

- **`GET /heroes`**
  - Retrieves a list of all heroes.
  - **Response:**

    ```json
    [
      {"id": 1, "name": "Superman", "super_name": "Clark Kent", "powers": []}
    ]
    ```

- **`GET /heroes/<id>`**
  - Retrieves details of a specific hero including their powers.
  - **Response:**

    ```json
    {"id": 1, "name": "Superman", "super_name": "Clark Kent", "powers": [{"id": 2, "name": "Flying"}]}
    ```

### **3. Powers**

- **`GET /powers`**
  - Retrieves a list of all available powers.
  - **Response:**

    ```json
    [{"id": 1, "name": "Flying", "description": "Allows hero to fly."}]
    ```

- **`GET /powers/<id>`**
  - Retrieves a specific power by ID.
  - **Response:**

    ```json
    {"id": 1, "name": "Flying", "description": "Allows hero to fly."}
    ```

- **`PATCH /powers/<id>`**
  - Updates the description of a specific power.
  - **Request Body:**

    ```json
    {"description": "Updated power description."}
    ```

  - **Response:**

    ```json
    {"id": 1, "name": "Flying", "description": "Updated power description."}
    ```

### **4. Hero Powers**

- **`POST /hero_powers`**
  - Assigns a power to a hero with a strength level.
  - **Request Body:**

    ```json
    {"hero_id": 1, "power_id": 2, "strength": "Strong"}
    ```

  - **Response:**

    ```json
    {"id": 1, "hero_id": 1, "power_id": 2, "strength": "Strong"}
    ```

## Validations

- Power descriptions must be at least 20 characters long.
- Strength values must be either "Strong", "Weak", or "Average".

## Error Handling

- **404 Not Found**: Returned when a requested resource does not exist.
- **400 Bad Request**: Returned when validation fails (e.g., missing or invalid data).

## License

This project is licensed under the MIT License.

## Author

- Samuel 0.
