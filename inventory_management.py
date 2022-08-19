"""Functions to keep track and alter inventory."""


def create_inventory(items: list):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    index = 0
    while index < len(items):
        if items[index] in inventory:
            inventory[items[index]] += 1
            index += 1
        else:
            inventory[items[index]] = 1
            index += 1
    return inventory

def add_items(inventory: dict, items: list):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    index = 0
    while index < len(items):
        if items[index] in inventory:
            inventory[items[index]] += 1
            index += 1
        else:
            inventory[items[index]] = 1
            index += 1
    return inventory

def decrement_items(inventory: dict, items: dict):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    index = 0
    while index < len(items):
        if items[index] in inventory:
            if inventory[items[index]] == 0:
                inventory[items[index]] = 0
            else:
                inventory[items[index]] -= 1
            index += 1
    return inventory

def remove_item(inventory: dict, item: str):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory: dict):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    tuple_list = []
    for key in inventory:
        if inventory[key] != 0:
            tuple_list.append((key, inventory[key]))
    return tuple_list
