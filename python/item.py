from item_constants import ItemNameMappings
from item_helper import increase_quality, decrease_quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @staticmethod
    def update_quality(items):
        for item in items:
            if item.name == ItemNameMappings.AGED_BRIE:
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality =  increase_quality(item.quality, 1)
                item.quality = increase_quality(item.quality, 1)

            elif item.name == ItemNameMappings.SULFURAS:
                pass

            elif item.name == ItemNameMappings.BACKSTAGE:
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 5:
                    item.quality = increase_quality(item.quality, 3)
                elif item.sell_in < 10:
                    item.quality = increase_quality(item.quality, 2)
                else:
                    item.quality = increase_quality(item.quality, 1)

            elif item.name == ItemNameMappings.CONJURED:
                item.sell_in = item.sell_in - 1
                item.quality = decrease_quality(item.quality, 2)
                if item.sell_in < 0:
                    item.quality = decrease_quality(item.quality, 2)

            else:
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = decrease_quality(item.quality, 1)
                item.quality = decrease_quality(item.quality, 1)