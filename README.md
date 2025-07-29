# Project Description
A simple RESTful API built with Django REST Framework to manage a collection of books. It supports full CRUD operations along with filtering and pagination.

🔗 [Medium Article: Building a Simple REST API with DRF](https://medium.com/@ankitpoudel_/build-a-simple-rest-api-with-django-rest-framework-a-step-by-step-guide-bc996201d248)

## Tech Stack
- Django REST Framework
- SQLite 
- django-filter (for filtering)
- Swagger (for documentation)

## API Endpoints
- books/
Handles GET (list books with filtering and pagination) and POST (create new book).

- books/<int:id>/
Handles GET (retrieve), PUT (update), PATCH (partial update), and DELETE (remove) a specific book by ID.

## Filtering & Pagination
- Case-insensitive filtering on `title` and `author`
- Example: 
`/books/?author=ankit&page=2`

- Pagination is enabled by DRF's `PageNumberPagination`:
```
{
  "count": 6,
  "next": "http://localhost:8000/books/?page=2",
  "previous": null,
  "results": [
    { "title": "Good Book", ... },
    ...
  ]
}
```

## Project Setup Guide
1. cd into project directory
2. Create a new .env file by copying the env.example file
3. Open the .env file and update it with your credentials as needed
4. Install dependencies `pip install -r requirements.txt`
5. Run migrations `python manage.py migrate`
6. Start the server `python manage.py runserver`
