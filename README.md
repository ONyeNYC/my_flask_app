# Flask-PeeWee API Application

## Overview

This application is a simple REST API built using Flask and PeeWee ORM. It's designed to demonstrate basic CRUD (Create, Read, Update, Delete) operations on a SQLite database. The application allows the creation, retrieval, and deletion of 'items' in a database.

## Features

- Simple REST API to interact with a SQLite database.
- CRUD operations:
  - Create new items.
  - Read all items.
  - Delete an item.

## Getting Started

### Prerequisites

- Python 3
- pip (Python package manager)
- Virtual environment (recommended for Python package management)

### Installation

1. **Clone the Repository:**

   - Clone this repository to your local machine using:
     ```bash
     git clone [https://github.com/ONyeNYC/my_flask_app.git]
     ```
   - Navigate to the project directory:
     ```bash
     cd my_flask_app
     ```

2. **Set Up a Virtual Environment (Optional):**

   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   - Install the required packages using:
     ```bash
     pip install -r requirements.txt
     ```

### Running the Application

1. **Start the Flask Server:**
   - Run the application using:
     ```bash
     python run.py
     ```
   - The server will start on `http://127.0.0.1:5000/`.

## API Endpoints

1. **Create an Item (POST):**

   - Endpoint: `/items`
   - Method: POST
   - Body: JSON object with `name` key (e.g., `{"name": "Sample Item"}`)

2. **Read All Items (GET):**

   - Endpoint: `/items`
   - Method: GET

3. **Delete an Item (DELETE):**
   - Endpoint: `/items/<item_id>`
   - Method: DELETE
   - Replace `<item_id>` with the actual ID of the item.

## Testing the Application

You can test the API using tools like Postman or curl. Here are some example commands:

- **Create a New Item:**
  ```bash
  curl -X POST http://127.0.0.1:5000/items -H 'Content-Type: application/json' -d '{"name": "New Item"}'
  ```
- **Get All Item:**

  ```bash
  curl http://127.0.0.1:5000/items

  ```

  **Delete an Item:**

  ```bash
  curl -X DELETE http://127.0.0.1:5000/items/1

  ```
