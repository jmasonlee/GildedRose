# -*- coding: utf-8 -*-
import unittest

from approvaltests import SimpleLogger, verify

from gilded_rose import LoggingItem, LoggingGildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        output = SimpleLogger.log_to_string()
        items = [LoggingItem("foo", 0, 0)]
        gilded_rose = LoggingGildedRose(items)
        gilded_rose.update_quality()
        verify(output)


if __name__ == '__main__':
    unittest.main()
