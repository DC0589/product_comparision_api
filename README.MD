# Price Comparison Service

This project is a price comparison service that aggregates product prices from various online stores.

## Backend

The backend is built using FastAPI, SQLAlchemy, and Alembic for database migrations.

## Database

We chose PostgreSQL for the following reasons:
- Strong support for relational data.
- High performance and scalability.
- ACID compliance ensuring reliable transactions.

## Endpoints

- `/products/` [GET]: Retrieve a list of products, optionally filtered by name.
- `/products/` [POST]: Add a new product to the database.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Configure your database in `app/database.py`.

3. Initialize and apply database migrations:
    ```sh
    alembic revision --autogenerate -m "001"
    alembic upgrade head
    ```

4. Run the application:
    ```sh
    uvicorn app.main:app --reload
    ```
