# -*- coding: utf-8 -*-
from item import Item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        Item.update_quality(self.items)