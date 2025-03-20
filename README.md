# Animal Encyclopedia

A comprehensive Django-based web application that provides educational content about animals for both kids and adults. The application features a dual-mode interface with simplified content for children and detailed scientific information for adults.

## Features

- **Dual Learning Sections**
  - Kids Section: Simple, engaging content for young learners
  - Adults Section: Detailed scientific information for advanced learning

- **Animal Categories**
  - Air Animals
  - Water Animals
  - Land Animals

- **Rich Media Content**
  - Multiple images per animal
  - Optional audio descriptions
  - Interactive image carousel

- **User Features**
  - User registration and authentication
  - Comment system for registered users
  - Search functionality
  - Dark/Light mode toggle

- **Responsive Design**
  - Mobile-friendly interface
  - Bootstrap 5 based layout
  - Modern and clean UI

## Setup Instructions

1. Create and activate virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Project Structure

```
animal_encyclopedia/
├── home/                   # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── admin.py         # Admin panel configuration
│   ├── models.py        # Database models
│   ├── urls.py          # URL routing
│   └── views.py         # View logic
├── static/               # Static files (CSS, JS, images)
├── media/               # User-uploaded files
├── templates/           # Base templates
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Technologies Used

- Django 5.0.2
- Bootstrap 5
- SQLite Database
- Pillow for image handling
- Crispy Forms with Bootstrap 5
- Font Awesome icons

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
