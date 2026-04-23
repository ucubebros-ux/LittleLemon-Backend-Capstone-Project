from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from datetime import datetime


class MenuViewTest(TestCase):
    """Test cases for Menu API views"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.menu_items = [
            Menu.objects.create(title="Burger", price=9.99, inventory=50),
            Menu.objects.create(title="Pizza", price=12.99, inventory=30),
            Menu.objects.create(title="Salad", price=7.99, inventory=40),
        ]
        self.url = reverse('menu-list')
    
    def test_get_menu_items(self):
        """Test retrieving all menu items"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Response is paginated, so check the results key
        self.assertEqual(response.data['count'], 3)
    
    def test_menu_items_content(self):
        """Test menu items content"""
        response = self.client.get(self.url)
        serializer = MenuSerializer(self.menu_items, many=True)
        # Response is paginated, compare results key
        self.assertEqual(response.data['results'], serializer.data)
    
    def test_create_menu_item(self):
        """Test creating a new menu item"""
        data = {
            'title': 'Pasta',
            'price': 11.99,
            'inventory': 25
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 4)
    
    def test_get_single_menu_item(self):
        """Test retrieving a single menu item"""
        menu_item = self.menu_items[0]
        url = reverse('menu-detail', kwargs={'pk': menu_item.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], menu_item.title)
    
    def test_update_menu_item(self):
        """Test updating a menu item"""
        menu_item = self.menu_items[0]
        url = reverse('menu-detail', kwargs={'pk': menu_item.id})
        data = {
            'title': 'Deluxe Burger',
            'price': 14.99,
            'inventory': 60
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        menu_item.refresh_from_db()
        self.assertEqual(menu_item.title, 'Deluxe Burger')
    
    def test_delete_menu_item(self):
        """Test deleting a menu item"""
        menu_item = self.menu_items[0]
        url = reverse('menu-detail', kwargs={'pk': menu_item.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Menu.objects.count(), 2)


class BookingViewTest(TestCase):
    """Test cases for Booking API viewset"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.booking1 = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime.now()
        )
        self.booking2 = Booking.objects.create(
            name="Jane Smith",
            no_of_guests=6,
            booking_date=datetime.now()
        )
    
    def test_get_bookings_requires_auth(self):
        """Test that booking list requires authentication"""
        client_no_auth = APIClient()
        url = reverse('booking-list')
        response = client_no_auth.get(url)
        self.assertEqual(response.status_code, 401)
    
    def test_get_bookings_with_auth(self):
        """Test retrieving bookings with authentication"""
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Response is paginated, check results
        self.assertEqual(response.data['count'], 2)
    
    def test_create_booking(self):
        """Test creating a booking"""
        url = reverse('booking-list')
        data = {
            'name': 'Alice Brown',
            'no_of_guests': 5,
            'booking_date': datetime.now().isoformat()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 3)
    
    def test_get_single_booking(self):
        """Test retrieving a single booking"""
        url = reverse('booking-detail', kwargs={'pk': self.booking1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'John Doe')
    
    def test_update_booking(self):
        """Test updating a booking"""
        url = reverse('booking-detail', kwargs={'pk': self.booking1.id})
        data = {
            'name': 'John Updated',
            'no_of_guests': 8,
            'booking_date': datetime.now().isoformat()
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.booking1.refresh_from_db()
        self.assertEqual(self.booking1.name, 'John Updated')
    
    def test_delete_booking(self):
        """Test deleting a booking"""
        url = reverse('booking-detail', kwargs={'pk': self.booking1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Booking.objects.count(), 1)
