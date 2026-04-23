from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime


class MenuTest(TestCase):
    """Test cases for Menu model"""
    
    def setUp(self):
        """Set up test data"""
        self.menu_item = Menu.objects.create(
            title="Burger",
            price=9.99,
            inventory=50
        )
    
    def test_menu_str(self):
        """Test menu string representation"""
        self.assertEqual(str(self.menu_item), "Burger : 9.99")
    
    def test_menu_creation(self):
        """Test menu item creation"""
        self.assertEqual(self.menu_item.title, "Burger")
        self.assertEqual(self.menu_item.price, 9.99)
        self.assertEqual(self.menu_item.inventory, 50)
    
    def test_multiple_items(self):
        """Test creating multiple menu items"""
        item2 = Menu.objects.create(
            title="Pizza",
            price=12.99,
            inventory=30
        )
        self.assertEqual(Menu.objects.count(), 2)
        self.assertIn(self.menu_item, Menu.objects.all())
        self.assertIn(item2, Menu.objects.all())


class BookingTest(TestCase):
    """Test cases for Booking model"""
    
    def setUp(self):
        """Set up test data"""
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime.now()
        )
    
    def test_booking_creation(self):
        """Test booking creation"""
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.no_of_guests, 4)
    
    def test_booking_str(self):
        """Test booking string representation"""
        booking_str = str(self.booking)
        self.assertIn("John Doe", booking_str)
    
    def test_multiple_bookings(self):
        """Test creating multiple bookings"""
        booking2 = Booking.objects.create(
            name="Jane Smith",
            no_of_guests=6,
            booking_date=datetime.now()
        )
        self.assertEqual(Booking.objects.count(), 2)
