# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item

from item_factory import ItemFactory


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [ItemFactory.create_item_object(item_name="foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_update_quality(self):
        items = [ItemFactory.create_item_object(item_name="foo", sell_in=10, quality=22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_update_quality_when_zero(self):
        items = [ItemFactory.create_item_object(item_name="foo", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_update_quality_when_sell_date_passed(self):
        items = [ItemFactory.create_item_object(item_name="foo", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_update_quality_when_sell_date_passed_and_quality_zero(self):
        items = [ItemFactory.create_item_object(item_name="foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_aged_brie_item_when_sell_in_more_than_zero(self):
        items = [ItemFactory.create_item_object(item_name="Aged Brie", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_for_aged_brie_item_when_sell_in_zero(self):
        items = [ItemFactory.create_item_object(item_name="Aged Brie", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_aged_brie_item_when_sell_in_zero_quality_50(self):
        items = [ItemFactory.create_item_object(item_name="Aged Brie", sell_in=0, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_sulfuras_item(self):
        items = [ItemFactory.create_item_object(item_name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_more_than_ten(self):
        items = [ItemFactory.create_item_object(item_name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(11, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_between_five_and_ten(self):
        items = [ItemFactory.create_item_object(item_name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(7, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_less_than_five(self):
        items = [ItemFactory.create_item_object(item_name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

    def test_for_backstage_passes_item_when_sell_in_zero(self):
        items = [ItemFactory.create_item_object(item_name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_conjured_item_when_sell_in_more_than_zero(self):
        items = [ItemFactory.create_item_object(item_name="Conjured Mana Cake", sell_in=12, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(11, items[0].sell_in)

    def test_for_conjured_item_when_sell_in_zero(self):
        items = [ItemFactory.create_item_object(item_name="Conjured Mana Cake", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_for_conjured_item_when_sell_in_less_than_zero_and_quality_low(self):
        items = [ItemFactory.create_item_object(item_name="Conjured Mana Cake", sell_in=-2, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-3, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
