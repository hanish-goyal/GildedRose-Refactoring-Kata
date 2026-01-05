from item import AgedBrieItem, SulfurasItem, BackstageItem, ConjuredItem, GeneralItem

item_name_to_class_map = {
    "Aged Brie": AgedBrieItem,
    "Sulfuras, Hand of Ragnaros": SulfurasItem,
    "Backstage passes to a TAFKAL80ETC concert": BackstageItem,
    "Conjured Mana Cake": ConjuredItem
}

class ItemFactory:

    @staticmethod
    def create_item_object(item_name, sell_in, quality):
        return item_name_to_class_map.get(item_name, GeneralItem)(item_name, sell_in, quality)