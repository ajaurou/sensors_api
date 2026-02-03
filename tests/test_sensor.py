import unittest

from fake_data_app.sensor import VisitSensor
from datetime import date

class TestVisitSensor(unittest.TestCase):

    def test_monday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit(date(2026,2,2))

        self.assertFalse(visit_count == -1)

    def test_tuesday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit(date(2026,2,3))

        self.assertFalse(visit_count == -1)

    def test_sunday_closed(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.get_visit_count(date(2026,2,1))

        self.assertFalse(visit_count != -1)

    def test_with_break(self):
        visit_sensor = VisitSensor(1200, 300, perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(2023, 10, 22))

        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        visit_sensor = VisitSensor(1200, 300, perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(2023, 11, 28))

        self.assertEqual(visit_count, 238)

