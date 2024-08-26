items = []

def create_item(item):
    items.append(item)
    return item

def read_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return item
    raise ValueError("Item not found")

def update_item(item_id, updated_item):
    for index, item in enumerate(items):
        if item['id'] == item_id:
            items[index] = updated_item
            return updated_item
    raise ValueError("Item not found")

def delete_item(item_id):
    for index, item in enumerate(items):
        if item['id'] == item_id:
            return items.pop(index)
    raise ValueError("Item not found")