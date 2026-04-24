LITTLE LEMON RESTAURANT - DJANGO REST API

PROJECT SETUP:
- Django Project: littlelemon
- Django App: restaurant  
- Database: SQLite (db.sqlite3)

MODELS:
- Menu: id, title, price, inventory
- Booking: id, name, no_of_guests, booking_date

INSTALLED APPS:
- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes
- django.contrib.sessions
- django.contrib.messages
- django.contrib.staticfiles
- rest_framework
- rest_framework.authtoken
- djoser
- restaurant

TEMPLATES DIRECTORY CONFIGURED: templates/ with DIRS setting

VIEWS IMPLEMENTED:
- MenuItemsView (ListCreateAPIView)
- SingleMenuItemView (RetrieveUpdateAPIView, DestroyAPIView)
- BookingViewSet (ModelViewSet)

API ENDPOINTS:

HOME:
GET / - Welcome page

MENU API (Public):
GET /api/menu/ - List menu items
POST /api/menu/ - Create menu item
GET /api/menu/<id>/ - Get single item
PUT /api/menu/<id>/ - Update item
DELETE /api/menu/<id>/ - Delete item

BOOKING API (Token Authentication Required):
GET /api/booking/tables/ - List bookings
POST /api/booking/tables/ - Create booking
GET /api/booking/tables/<id>/ - Get booking
PUT /api/booking/tables/<id>/ - Update booking
DELETE /api/booking/tables/<id>/ - Delete booking

AUTHENTICATION:
POST /api/api-token-auth/ - Get token (username/password)
POST /auth/users/ - Register new user
POST /auth/token/login/ - Login
POST /auth/token/logout/ - Logout

ADMIN PANEL:
URL: http://localhost:8000/admin/
Username: admin
Password: admin123

HOW TO RUN:
1. cd littlelemon
2. python manage.py runserver
3. Open http://localhost:8000/

TESTING API WITH INSOMNIA:

Step 1 - Register:
POST http://localhost:8000/auth/users/
Body: {"username":"john","password":"test123","re_password":"test123"}

Step 2 - Login:
POST http://localhost:8000/auth/token/login/
Body: {"username":"john","password":"test123"}
(Copy the token from response)

Step 3 - Test Menu API:
GET http://localhost:8000/api/menu/

Step 4 - Test Booking API (with token):
GET http://localhost:8000/api/booking/tables/
Headers: Authorization: Token <your_token>

RUNNING TESTS:
python manage.py test

TEST FILES:
- restaurant/tests/test_models.py (Model tests)
- restaurant/tests/test_views.py (View tests)

STATIC FILES:
- static/css/style.css
- static/restaurant/

SETTINGS:
- TEMPLATES DIRS: ['templates']
- DATABASES: SQLite configuration
- REST_FRAMEWORK: TokenAuthentication and SessionAuthentication enabled
- DJOSER: USER_ID_FIELD set to "username"
