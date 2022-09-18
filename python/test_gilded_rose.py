# -*- coding: utf-8 -*-
import unittest

from gilded_rose import LoggingItem, LoggingGildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [LoggingItem("foo", 0, 0)]
        gilded_rose = LoggingGildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)


if __name__ == '__main__':
    unittest.main()
