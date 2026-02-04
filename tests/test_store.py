import unittest
from datetime import date

from fake_data_app.store import StoreSensor

class TestStoreSensor(unittest.TestCase):

    def test_get_all_traffic(self):
        revel_store = StoreSensor('Revel', 1200, 300)
        visits = revel_store.get_all_traffic(date(2026,2,4))
        self.assertEqual(visits, 1648)

    def test_get_sensor_traffic(self):
        revel_store = StoreSensor('Revel', 1200, 300)
        visits = revel_store.get_sensor_traffic(2,date(2026,2,4))
        self.assertEqual(visits, 82)

    def test_sunday_closed(self):
        revel_store = StoreSensor('Revel', 1200, 300)
        visits = revel_store.get_sensor_traffic(2,date(2026,2,1))
        self.assertEqual(visits, -1)