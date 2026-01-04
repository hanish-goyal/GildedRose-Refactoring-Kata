# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_update_quality(self):
        items = [Item("foo", 10, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_update_quality_when_zero(self):
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_update_quality_when_sell_date_passed(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_update_quality_when_sell_date_passed_and_quality_zero(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_aged_brie_item_when_sell_in_more_than_zero(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_for_aged_brie_item_when_sell_in_zero(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_aged_brie_item_when_sell_in_zero_quality_50(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_sulfuras_item(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_more_than_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(11, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_between_five_and_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(7, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_less_than_five(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
