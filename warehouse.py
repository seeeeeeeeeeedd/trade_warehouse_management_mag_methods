class Warehouse:
    def __init__(self):
        self.MISSING_ITEM_COUNT = 0
        self.__warehouse = {}

    def __setitem__(self, item, count):
        self.__warehouse[item] = count

    def __getitem__(self, item):
        return self.__warehouse.get(item, self.MISSING_ITEM_COUNT)

    def __len__(self):
        total_item = self.__warehouse.values()
        total_items_count = sum(total_item)

        return total_items_count

    def __iter__(self):
        items = self.__warehouse.items()
        sorted_items = sorted(items)

        return iter(sorted_items)
