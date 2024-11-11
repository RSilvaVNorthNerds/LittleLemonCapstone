from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pizza", price=8, inventory=10)
        self.assertEqual(item.title, "Pizza")
        self.assertEqual(item.price, 8)
        self.assertEqual(item.inventory, 10)

        item = Menu.objects.create(title="Soda", price=2, inventory=10)
        self.assertEqual(item.title, "Soda")
        self.assertEqual(item.price, 2)
        self.assertEqual(item.inventory, 10)

        item = Menu.objects.create(title="Fries", price=4, inventory=0)
        self.assertEqual(item.title, "Fries")
        self.assertEqual(item.price, 4)
        self.assertEqual(item.inventory, 0)