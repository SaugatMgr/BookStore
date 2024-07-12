# BookStore Project

## Description
This project is an online BookStore developed using Django. It allows users to browse, search for books. Users can manage their profiles, provide reviews for books. Admin users can perform CRUD operations on books, manage categories, tags, etc.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SaugatMgr/BookStore.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd BookStore
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Migrate changes**
   - Run the following command to migrate changes to database:
      ```bash
      python manage.py migrate
      ```
2. **Create a superuser:**
    - Run the following command and follow the prompts:
        ```bash
        python manage.py createsuperuser
        ```
    - Alternatively, you can sign up and log in from the home page with normal forms or social authentication.

3. **Run the server:**
    ```bash
    python manage.py runserver
    ```
