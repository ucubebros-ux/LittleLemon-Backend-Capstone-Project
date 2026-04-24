from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime


class MenuTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Burger",
            price=9.99,
            inventory=50
        )
    
    def test_get_item(self):
        self.assertEqual(str(self.menu_item), "Burger : 9.99")
    
    def test_menu_creation(self):
        self.assertEqual(self.menu_item.title, "Burger")
        self.assertEqual(self.menu_item.price, 9.99)
        self.assertEqual(self.menu_item.inventory, 50)


class BookingTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime.now()
        )
    
    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.no_of_guests, 4)
