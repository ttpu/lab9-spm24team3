# Expense Tracker

## Project Overview
Expense Tracker is a web application designed for tracking personal or organizational expenses. The application allows users to add, view, edit, and delete expense records in a table format. The project is built using Django for the backend and HTML, CSS, and JavaScript for the frontend, with SQLite as the database.

## Features
- **Add Expenses**: Form for adding new expenses (date, title, category, and amount).
- **View Expenses**: Displays expenses in a table with columns for date, title, category, amount, and actions.
- **Edit & Delete Expenses**: Options to modify or remove existing expense records.
- **Total Amount Calculation**: Displays the total expense amount at the bottom of the table.
- **No Authorization**: Open access without user authentication.

---

## Project Structure
```
Expense-Tracker/
├── config/                     # Configuration files for the project
│   ├── __init__.py             # Initializes the backend package
│   ├── asgi.py                 # ASGI configuration for asynchronous server
│   ├── settings.py             # Project settings (database, installed apps, etc.)
│   ├── urls.py                 # URL routing for the project
│   ├── wsgi.py                 # WSGI configuration for synchronous server
│    
├── expenses/                   # Main app for handling expenses
│   ├── __init__.py             # Initializes the expenses app
│   ├── admin.py                # Admin interface configurations for expenses model
│   ├── apps.py                 # App configuration for the expenses app
│   ├── forms.py                # Forms for handling user input (expenses data)
│   ├── models.py               # Database models for expenses
│   ├── tests.py                # Unit tests for the expenses app
│   ├── urls.py                 # URL routing specific to the expenses app
│   ├── views.py                # Views to handle user requests (rendering pages, etc.)
│   ├── migrations/             # Database migrations (tracking changes to models)
│   │   ├── __init__.py         # Initializes migrations directory
│   │   ├── 0001_initial.py     # Initial database migration file
│   ├── templates/              # HTML templates for rendering views
│   │   ├── edit_expense.html   # Template for editing expenses
│   │   ├── index.html          # Template for displaying the expense tracker
│   ├── static/                 # Static files (CSS, JavaScript, images)
│   │   ├── css/                # CSS files
│   │   │   ├── styles.css      # Styles for the frontend
├── manage.py                   # Command-line utility for managing the project
├── Pipfile                     # Dependency management file (Pipenv)
├── db.sqlite3                  # SQLite database file
├── requirements.txt            # List of dependencies (if not using Pipenv)
├── README.md                   # Project documentation and instructions
```

---

## Team Roles
1. **Team Lead**
   - Assigns tasks to team members and oversees project milestones.
   - Monitors progress and ensures timely delivery.

2. **Backend Developer**
   - Develops and manages the Django backend.
   - Creates models, views, and forms.
   - Configures database integration and business logic.

3. **Frontend Developer**
   - Implements the user interface using HTML, CSS, and JavaScript.
   - Integrates the frontend with backend APIs.

4. **Designer**
   - Designs UI/UX components.
   - Creates mockups and ensures design consistency.

---

## Milestones
1. **Project Setup**
   - Initialize the repository and set up the Django environment.
   - Create the required project structure.
   - Add dependencies and initial database configuration.

2. **Integration & Finishing**
   - Develop the backend functionalities (models, views, and forms).
   - Build the frontend interface (HTML, CSS, and JavaScript).
   - Integrate backend and frontend components.

3. **Testing & Deployment**
   - Test all functionalities (add, view, edit, delete expenses).
   - Debug and ensure cross-browser compatibility.
   - Deploy the application to a hosting platform.

---

## Getting Started
### Prerequisites
- Python 3.x
- Django
- SQLite

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/Expense-Tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd src
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage
1. Open the application in a web browser at `http://127.0.0.1:8000/`.
2. Add, view, edit, or delete expenses using the interface.
3. View the total expense amount at the bottom of the table.

---

## Contribution Guidelines
- Fork the repository and create a new branch for your feature or bugfix.
- Commit your changes with meaningful commit messages.
- Submit a pull request for review.

---

## License
This project is licensed under the [MIT License](LICENSE).
