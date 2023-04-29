import unittest
from roster_generator import gen_dates_times

class Test(unittest.TestCase):

    t = { "Monday" : ["", ""],
      "Tuesday" : ["", ""],
      "Wednesday" : ["", ""],
      "Thursday" : ["", ""],
      "Friday" : ["", ""],
      "Saturday" : ["", ""],
      "Sunday" : ["", ""],
    }
    
    # Test that valid usage is not None
    def test_gen_dates_times_not_none(self):
        t = { "Monday" : ["06:00", "14:30"],
            "Tuesday" : ["06:00", "14:30"],
            "Wednesday" : ["19:00", "00:00"],
            "Thursday" : ["", ""],
            "Friday" : ["", ""],
            "Saturday" : ["06:00", "16:00"],
            "Sunday" : ["", ""],
        }

        self.assertIsNotNone(gen_dates_times(1, t))

    def test_gen_dates_times_empty(self):
        # TODO
        return