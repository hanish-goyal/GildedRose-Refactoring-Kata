# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0 and item.quality < 50:
                    item.quality = item.quality + 1
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 10 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 5 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = 0
            elif item.name == "Conjured Mana Cake":
                item.sell_in = item.sell_in - 1
                item.quality = max(item.quality -2 , 0)
                if item.sell_in < 0:
                    item.quality = max(item.quality -2 , 0)
            else:
                item.sell_in = item.sell_in - 1
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.sell_in < 0 < item.quality:
                    item.quality = item.quality - 1


