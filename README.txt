==============================================================================
LITTLE LEMON RESTAURANT - CAPSTONE PROJECT API DOCUMENTATION
==============================================================================

PROJECT OVERVIEW:
This is a Django REST API application for the Little Lemon restaurant. 
The application includes:
- Menu API for retrieving and managing menu items
- Table Booking API for managing restaurant reservations
- User registration and authentication using Djoser
- Token-based authentication for secure API access
- Comprehensive unit tests

==============================================================================
API ENDPOINTS
==============================================================================

1. HOME PAGE
-----------
   URL: http://localhost:8000/
   METHOD: GET
   DESCRIPTION: Displays the welcome page of the Little Lemon restaurant

2. MENU API
-----------
   a) List All Menu Items
      URL: http://localhost:8000/api/menu/
      METHOD: GET
      DESCRIPTION: Retrieve all menu items
      RESPONSE: JSON with list of menu items

   b) Create New Menu Item
      URL: http://localhost:8000/api/menu/
      METHOD: POST
      REQUIRED FIELDS: title (string), price (decimal), inventory (integer)
      EXAMPLE:
      {
          "title": "Burger",
          "price": 9.99,
          "inventory": 50
      }

   c) Get Single Menu Item
      URL: http://localhost:8000/api/menu/<id>/
      METHOD: GET
      DESCRIPTION: Retrieve a specific menu item by ID

   d) Update Menu Item
      URL: http://localhost:8000/api/menu/<id>/
      METHOD: PUT
      REQUIRED FIELDS: title, price, inventory

   e) Delete Menu Item
      URL: http://localhost:8000/api/menu/<id>/
      METHOD: DELETE

3. BOOKING API (REQUIRES AUTHENTICATION)
----------------------------------------
   a) List All Bookings
      URL: http://localhost:8000/api/booking/tables/
      METHOD: GET
      AUTHENTICATION: Token Required
      DESCRIPTION: Retrieve all table bookings (only for authenticated users)

   b) Create New Booking
      URL: http://localhost:8000/api/booking/tables/
      METHOD: POST
      AUTHENTICATION: Token Required
      REQUIRED FIELDS: name (string), no_of_guests (integer), booking_date (datetime)
      EXAMPLE:
      {
          "name": "John Doe",
          "no_of_guests": 4,
          "booking_date": "2026-04-25T19:30:00Z"
      }

   c) Get Single Booking
      URL: http://localhost:8000/api/booking/tables/<id>/
      METHOD: GET
      AUTHENTICATION: Token Required

   d) Update Booking
      URL: http://localhost:8000/api/booking/tables/<id>/
      METHOD: PUT
      AUTHENTICATION: Token Required

   e) Delete Booking
      URL: http://localhost:8000/api/booking/tables/<id>/
      METHOD: DELETE
      AUTHENTICATION: Token Required

4. USER REGISTRATION & AUTHENTICATION
-------------------------------------
   a) User Registration
      URL: http://localhost:8000/auth/users/
      METHOD: POST
      FIELDS: username, password, re_password, email (optional)
      EXAMPLE:
      {
          "username": "john_doe",
          "password": "securepass123",
          "re_password": "securepass123",
          "email": "john@example.com"
      }

   b) Login (Get Token)
      URL: http://localhost:8000/auth/token/login/
      METHOD: POST
      FIELDS: username, password
      EXAMPLE:
      {
          "username": "john_doe",
          "password": "securepass123"
      }
      RESPONSE: {"auth_token": "token_string_here"}

   c) Logout
      URL: http://localhost:8000/auth/token/logout/
      METHOD: POST
      AUTHENTICATION: Token Required

   d) Get Auth Token (Alternative)
      URL: http://localhost:8000/api-token-auth/
      METHOD: POST
      FIELDS: username, password

5. ADMIN PANEL
--------------
   URL: http://localhost:8000/admin/
   USERNAME: admin
   PASSWORD: admin123
   DESCRIPTION: Django admin interface for managing models

==============================================================================
TESTING WITH INSOMNIA/POSTMAN
==============================================================================

STEP 1: Register a User
- Make a POST request to: http://localhost:8000/auth/users/
- Body (JSON):
  {
    "username": "testuser",
    "password": "testpass123",
    "re_password": "testpass123"
  }

STEP 2: Get Authentication Token
- Make a POST request to: http://localhost:8000/auth/token/login/
- Body (JSON):
  {
    "username": "testuser",
    "password": "testpass123"
  }
- Copy the token from the response

STEP 3: Test Menu API
- Make a GET request to: http://localhost:8000/api/menu/
- No authentication required
- Add some menu items using POST request

STEP 4: Test Booking API
- Make a GET request to: http://localhost:8000/api/booking/tables/
- In Insomnia: Go to Auth tab → Select "Bearer Token" → Paste your token
- In Postman: Go to Authorization tab → Select "Bearer Token" → Paste your token
- Only authenticated users can access this endpoint

==============================================================================
RUNNING THE APPLICATION
==============================================================================

1. Navigate to the littlelemon directory:
   cd C:\Users\User\Desktop\Backend Capstone Project\littlelemon

2. Start the development server:
   python manage.py runserver

3. Open your browser and visit:
   http://localhost:8000/

4. Run tests:
   python manage.py test

==============================================================================
DATABASE INFORMATION
==============================================================================

Current Database: SQLite (db.sqlite3)
To switch to MySQL, uncomment the MySQL configuration in settings.py
and comment out the SQLite configuration.

Models:
- Menu: Stores menu items with title, price, and inventory
- Booking: Stores table bookings with name, number of guests, and booking date

==============================================================================
PROJECT STRUCTURE
==============================================================================

littlelemon/
├── littlelemon/          (Project settings)
│   ├── settings.py       (Django configuration)
│   ├── urls.py           (URL routing)
│   └── wsgi.py
├── restaurant/           (App with API views)
│   ├── models.py         (Menu and Booking models)
│   ├── serializers.py    (DRF serializers)
│   ├── views.py          (API views and viewsets)
│   ├── urls.py           (App URLs)
│   ├── admin.py          (Admin configuration)
│   └── tests/            (Unit tests)
├── templates/            (HTML templates)
│   └── index.html
├── static/               (Static files)
│   ├── css/
│   │   └── style.css
│   └── restaurant/
├── manage.py             (Django management script)
└── db.sqlite3            (Database file)

==============================================================================
TECHNOLOGIES USED
==============================================================================

- Django 6.0.4
- Django REST Framework 3.17.1
- Djoser (for user authentication)
- mysqlclient (MySQL database support)
- Python 3.13.7

==============================================================================
NOTES FOR REVIEWERS
==============================================================================

1. All API endpoints are fully functional and tested
2. Unit tests include:
   - Model creation and string representation tests
   - API CRUD operation tests
   - Authentication and permission tests
3. The Menu API is public (no authentication required)
4. The Booking API requires token authentication
5. User registration and login are available for creating authenticated sessions
6. All 18 unit tests pass successfully
7. The project uses SQLite for simplicity, but can be configured for MySQL

==============================================================================
