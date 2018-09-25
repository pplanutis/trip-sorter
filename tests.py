import unittest
import time
from collections import namedtuple
from trip_sorter import TripSorter
from trip_sorter2 import TripSorter2


class TestTripSorters(unittest.TestCase):
    def setUp(self):
        self.bcardsin = {
          0: {"from": "berlin", "to": "rome", "type": "flight", "no": "33A", "seatno": "seat no 69",
              "addinfo": "(Gate no 44)"},
          1: {"from": "krakow", "to": "bydgoszcz", "type": "bus", "no": "123B", "seatno": "", "addinfo": ""},
          2: {"from": "warsaw", "to": "poznan", "type": "train", "no": "777", "seatno": "", "addinfo": "(Track no 1)"},
          3: {"from": "barcelona", "to": "warsaw", "type": "flight", "no": "66", "seatno": "seat no 69",
              "addinfo": "(Gate no 55)"},
          4: {"from": "poznan", "to": "berlin", "type": "train", "no": "9", "seatno": "seat no 69",
              "addinfo": "(Track no 13)"},
          5: {"from": "rome", "to": "krakow", "type": "flight", "no": "111", "seatno": "seat no 69",
              "addinfo": "(Gate no 66)"},
        }

        BoardingCard = namedtuple("BoardingCard", "cfrom cto ctype no seatno addinfo")

        bc1 = BoardingCard(cfrom="berlin", cto="rome", ctype="flight", no="137", seatno="seat no A37",
                           addinfo="(Gate no 66)")
        bc2 = BoardingCard(cfrom="krakow", cto="bydgoszcz", ctype="bus", no="223", seatno="", addinfo="")
        bc3 = BoardingCard(cfrom="warsaw", cto="poznan", ctype="train", no="55", seatno="seat no C69",
                           addinfo="(Track no 1)")
        bc4 = BoardingCard(cfrom="barcelona", cto="warsaw", ctype="flight", no="69", seatno="seat no Z123",
                           addinfo="(Gate no 1)")
        bc5 = BoardingCard(cfrom="poznan", cto="berlin", ctype="bus", no="321", seatno="", addinfo="")
        bc6 = BoardingCard(cfrom="rome", cto="krakow", ctype="flight", no="Z123", seatno="seat no G321",
                           addinfo="(Gate no 55)")

        self.bcardsin2 = dict()
        self.bcardsin2[bc1.cfrom] = bc1
        self.bcardsin2[bc2.cfrom] = bc2
        self.bcardsin2[bc3.cfrom] = bc3
        self.bcardsin2[bc4.cfrom] = bc4
        self.bcardsin2[bc5.cfrom] = bc5
        self.bcardsin2[bc6.cfrom] = bc6

        self.start_point = 'barcelona'
        self.end_point = 'bydgoszcz'

        self.ts = TripSorter()
        self.ts2 = TripSorter2()

    def test_ts_dict(self):
        ttype = type(self.bcardsin)
        tstype = type(self.ts.bubbleit(self.bcardsin))
        self.assertEqual(ttype, tstype)

    def test_ts2_dict(self):
        ttype = type(self.bcardsin2)
        tstype = type(self.ts2.sortit(self.bcardsin2))
        self.assertEqual(ttype, tstype)

    def test_ts_dict_length(self):
        len_test = len(self.bcardsin)
        len_ts = len(self.ts.bubbleit(self.bcardsin))
        self.assertEqual(len_test, len_ts)

    def test_ts2_dict_length(self):
        len_test = len(self.bcardsin2)
        len_ts = len(self.ts2.sortit(self.bcardsin2))
        self.assertEqual(len_test, len_ts)

    def test_ts_start_point(self):
        ts_sp = self.ts.bubbleit(self.bcardsin)[0]["from"]
        self.assertEqual(self.start_point, ts_sp)

    def test_ts2_start_point(self):
        ts2_sp = self.ts2.sortit(self.bcardsin2)[0].cfrom
        self.assertEqual(self.start_point, ts2_sp)

    def test_ts_end_point(self):
        ts_ep = self.ts.bubbleit(self.bcardsin)[len(self.bcardsin) - 1]["to"]
        self.assertEqual(self.end_point, ts_ep)

    def test_ts2_end_point(self):
        ts2_ep = self.ts2.sortit(self.bcardsin2)[len(self.bcardsin2)].cto
        self.assertEqual(self.end_point, ts2_ep)

    def test_speed(self):
        s1 = time.clock()
        self.ts.bubbleit(self.bcardsin)
        e1 = time.clock()
        t1 = e1 - s1

        s2 = time.clock()
        self.ts2.sortit(self.bcardsin2)
        e2 = time.clock()
        t2 = e2 - s2

        self.assertGreater(t1, t2)


if __name__ == '__main__':
    unittest.main()
