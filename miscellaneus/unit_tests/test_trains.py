import unittest
from assertpy import assert_that
from miscellaneus.trains import get_max_trains


class TestTrains(unittest.TestCase):
    def setUp(self):
        self.schedule_1 = [[1, 10], [2, 9], [3, 5], [6, 10],
                           [7, 9], [7, 10], [8, 9], [9.5, 10]]

        self.schedule_2 = [[1, 5], [5, 10], [2, 6]]

    def test_max_trains(self):
        max_trains = get_max_trains(self.schedule_1)
        assert_that(max_trains).is_equal_to(6)

    def test_max_trains_with_start_end_date(self):
        max_trains = get_max_trains(self.schedule_2)
        assert_that(max_trains).is_equal_to(3)
