from abc import ABC, abstractmethod
from item_helper import increase_quality, decrease_quality


class Item(ABC):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def update_quality(self):
        pass


class AgedBrieItem(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = increase_quality(self.quality)
        self.quality = increase_quality(self.quality)


class SulfurasItem(Item):
    def update_quality(self):
        pass


class BackstageItem(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality = increase_quality(self.quality, 3)
        elif self.sell_in < 10:
            self.quality = increase_quality(self.quality, 2)
        else:
            self.quality = increase_quality(self.quality)


class ConjuredItem(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        self.quality = decrease_quality(self.quality, 2)
        if self.sell_in < 0:
            self.quality = decrease_quality(self.quality, 2)


class GeneralItem(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = decrease_quality(self.quality)
        self.quality = decrease_quality(self.quality)
