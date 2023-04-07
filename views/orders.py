ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "settingId": 3
    },
    {
        "id": 2,
        "metalId": 1,
        "sizeId": 3,
        "styleId": 2,
        "settingId": 2
    },
    {
        "id": 3,
        "metalId": 1,
        "sizeId": 1,
        "styleId": 1,
        "settingId": 1
    }
]


def get_all_orders():
    '''return all orders'''
    return ORDERS


def get_single_order(id):
    '''function to identify order by id'''
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order


def create_order(order):
    '''function to post new item'''

    max_id = ORDERS[-1]["id"]

    new_id = max_id + 1

    order["id"] = new_id

    ORDERS.append(order)

    return order


def delete_order(id):
    '''delete function for order'''

    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    '''PUT function for order'''

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
