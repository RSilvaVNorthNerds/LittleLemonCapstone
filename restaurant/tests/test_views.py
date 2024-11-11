from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):
    def test_get_menu_item(self):
        Menu.objects.create(title="Pizza", price=8, inventory=10)
        Menu.objects.create(title="Soda", price=4, inventory=10)
        Menu.objects.create(title="Fries", price=3, inventory=0)

        menu = Menu.objects.get(title="Pizza")
        self.assertEqual(menu.title, "Pizza")
        self.assertEqual(menu.price, 8)
        self.assertEqual(menu.inventory, 10)

    def test_get_all_menu_items(self):
        Menu.objects.create(title="Pizza", price=8, inventory=10)
        Menu.objects.create(title="Soda", price=4, inventory=10)
        Menu.objects.create(title="Fries", price=3, inventory=0)

        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)
        expected_data = [
            {'id': menus[0].id, 'title': 'Pizza', 'price': '8.00', 'inventory': 10},
            {'id': menus[1].id, 'title': 'Soda', 'price': '4.00', 'inventory': 10},
            {'id': menus[2].id, 'title': 'Fries', 'price': '3.00', 'inventory': 0},
        ]
        
        self.assertEqual(serialized_menus.data, expected_data)