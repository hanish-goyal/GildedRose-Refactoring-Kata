from item_constants import ItemNameMappings

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
                    item.quality = min(item.quality + 1 , 50)
                item.quality = min(item.quality + 1, 50)

            elif item.name == ItemNameMappings.SULFURAS:
                pass

            elif item.name == ItemNameMappings.BACKSTAGE:
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 5:
                    item.quality = min(item.quality + 3,  50)
                elif item.sell_in < 10:
                    item.quality = min(item.quality + 2,  50)
                else:
                    item.quality = min(item.quality + 1, 50)

            elif item.name == ItemNameMappings.CONJURED:
                item.sell_in = item.sell_in - 1
                item.quality = max(item.quality -2 , 0)
                if item.sell_in < 0:
                    item.quality = max(item.quality -2 , 0)

            else:
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = max(item.quality - 1, 0)
                item.quality = max(item.quality - 1, 0)