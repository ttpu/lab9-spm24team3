<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        header {
            background: #007BFF;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        main {
            max-width: 800px;
            margin: 2rem auto;
            background: #fff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #007BFF;
        }
        pre {
            background: #f4f4f4;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 0.5rem;
            text-align: left;
        }
        th {
            background: #f4f4f4;
        }
        code {
            background: #f4f4f4;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: monospace;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        footer {
            text-align: center;
            margin-top: 2rem;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>Expense Tracker Documentation</h1>
    </header>
    <main>
        <section>
            <h2>Overview</h2>
            <p>The Expense Tracker is a web-based application that helps users manage their expenses. Users can add, update, delete, and view their expenses in a tabular format, categorized by date, title, category, and amount. A total expense amount is displayed below the table for quick reference.</p>
        </section>

        <section>
            <h2>Features</h2>
            <ul>
                <li>Add, edit, or delete expenses.</li>
                <li>Display expenses in a table format with columns: Date, Title, Category, Amount, and Action.</li>
                <li>Calculate and display the total expense dynamically.</li>
                <li>Responsive and user-friendly design.</li>
            </ul>
        </section>

        <section>
            <h2>Technology Stack</h2>
            <ul>
                <li><strong>Backend:</strong> FastAPI (Python)</li>
                <li><strong>Database:</strong> SQLAlchemy (SQLite/MySQL/PostgreSQL)</li>
                <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
                <li><strong>Deployment:</strong> (e.g., Heroku, AWS, or locally using Uvicorn)</li>
            </ul>
        </section>

        <section>
            <h2>Project Structure</h2>
            <pre>
Expense-Tracker/
├── config/                       # Configuration files for the project
│   ├── __init__.py               # Initializes the config package
│   ├── asgi.py                   # ASGI configuration for asynchronous support (used for ASGI servers like Daphne or Uvicorn)
│   ├── settings.py               # Project settings (e.g., database, middleware, installed apps)
│   ├── urls.py                   # URL routing for the project (maps URLs to views)
│   ├── wsgi.py                   # WSGI configuration for synchronous support (used for WSGI servers like Gunicorn)
│    
├── expenses/                     # Core app for handling expenses and related functionality
│   ├── __init__.py               # Initializes the expenses app package
│   ├── admin.py                  # Registers models for Django admin interface (if using Django)
│   ├── apps.py                   # Configuration for the expenses app
│   ├── forms.py                  # Forms for handling user input (e.g., for creating or editing expenses)
│   ├── models.py                 # Database models for expenses (e.g., Expense, Category)
│   ├── tests.py                  # Unit tests for the expenses app
│   ├── urls.py                   # URL routing for the expenses app (maps URLs to views related to expenses)
│   ├── views.py                  # Views that handle the logic for rendering pages or APIs related to expenses
│   ├── migrations/               # Database migration files for changes to models
│   │   ├── __init__.py           # Initializes the migrations package
│   │   ├── 0001_initial.py       # Initial migration file (generated automatically when models change)
│   ├── templates/                # HTML templates for rendering pages
│   │   ├── edit_expense.html     # Template for editing an expense
│   │   ├── index.html            # Template for displaying all expenses or main page
│   ├── static/                   # Static files (CSS, JS, images)
│   │   ├── css/                  # CSS styles
│   │   │   ├── styles.css        # Main CSS file for the frontend
│
├── manage.py                     # Command-line utility for administrative tasks (e.g., runserver, makemigrations, migrate)
├── Pipfile                       # Specifies the dependencies for the project (used by Pipenv)
├── db.sqlite3                    # SQLite database file containing all the data for the app
├── requirements.txt              # Project dependencies (for Pip package manager)
├── README.md                     # Project documentation

            </pre>
        </section>

        <section>
            <h2>Setup Instructions</h2>
            <h3>1. Clone the Repository</h3>
            <pre>
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
            </pre>

            <h3>2. Set Up the Backend</h3>
            <ol>
                <li><strong>Create a Virtual Environment:</strong>
                    <pre>python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate</pre>
                </li>
                <li><strong>Install Dependencies:</strong>
                    <pre>pip install -r requirements.txt</pre>
                </li>
                <li><strong>Run the Backend:</strong>
                    <pre>uvicorn app.main:app --reload</pre>
                </li>
            </ol>

            <h3>3. Set Up the Frontend</h3>
            <p>Place your HTML, CSS, and JavaScript files in the <code>frontend/static/</code> directory. Ensure the backend serves <code>index.html</code> from the <code>templates</code> directory.</p>

            <h3>4. Run the Application</h3>
            <p>Visit <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a> in your browser to view the app.</p>
        </section>

        <section>
            <h2>API Endpoints</h2>
            <table>
                <thead>
                    <tr>
                        <th>Method</th>
                        <th>Endpoint</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>GET</td>
                        <td>/</td>
                        <td>Serves the main HTML page.</td>
                    </tr>
                    <tr>
                        <td>GET</td>
                        <td>/expenses</td>
                        <td>Fetches all expenses.</td>
                    </tr>
                    <tr>
                        <td>POST</td>
                        <td>/expenses</td>
                        <td>Adds a new expense.</td>
                    </tr>
                    <tr>
                        <td>PUT</td>
                        <td>/expenses/{id}</td>
                        <td>Updates an expense.</td>
                    </tr>
                    <tr>
                        <td>DELETE</td>
                        <td>/expenses/{id}</td>
                        <td>Deletes an expense.</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section>
            <h2>Contributing</h2>
            <ol>
                <li>Fork the repository.</li>
                <li>Create a feature branch:
                    <pre>git checkout -b feature-name</pre>
                </li>
                <li>Commit your changes:
                    <pre>git commit -m "Feature description"</pre>
                </li>
                <li>Push to the branch:
                    <pre>git push origin feature-name</pre>
                </li>
                <li>Submit a pull request.</li>
            </ol>
        </section>

        <section>
            <h2>Future Improvements</h2>
            <ul>
                <li>Add user authentication for personalized expense tracking.</li>
                <li>Implement data visualization (charts and graphs).</li>
                <li>Support exporting expenses to CSV.</li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Expense Tracker Team</p>
    </footer>
</body>
</html>
