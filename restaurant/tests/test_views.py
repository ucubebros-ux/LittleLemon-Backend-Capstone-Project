from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer
from datetime import datetime


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Burger", price=9.99, inventory=50)
        self.menu2 = Menu.objects.create(title="Pizza", price=12.99, inventory=30)
    
    def test_get_menu(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 2)
    
    def test_create_menu(self):
        data = {'title': 'Pasta', 'price': 11.99, 'inventory': 25}
        response = self.client.post(reverse('menu-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 3)
    
    def test_get_single_menu(self):
        response = self.client.get(reverse('menu-detail', kwargs={'pk': self.menu1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Burger')
    
    def test_update_menu(self):
        data = {'title': 'Deluxe Burger', 'price': 14.99, 'inventory': 60}
        response = self.client.put(reverse('menu-detail', kwargs={'pk': self.menu1.id}), data)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_menu(self):
        response = self.client.delete(reverse('menu-detail', kwargs={'pk': self.menu1.id}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Menu.objects.count(), 1)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_booking_requires_auth(self):
        client_no_auth = APIClient()
        response = client_no_auth.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 401)
    
    def test_get_bookings(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)
