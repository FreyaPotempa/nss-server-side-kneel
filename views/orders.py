import sqlite3
from models import Order, Metal, Size, Setting, Style

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
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.style_id,
            o.setting_id,
            o.size_id,
            m.metal,
            m.price,
            st.style,
            st.price,
            sz.size,
            sz.price
        FROM Orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Styles st ON st.id = o.style_id
        JOIN Sizes sz ON sz.id = o.size_id
        """)

        # Initialize an empty list to hold all animal representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            order = Order(row['id'], row['metal_id'], row['style_id'],
                          row['setting_id'], row['size_id'])

            # Create a Location instance from the current row
            metal = Metal(row['id'], row['metal'], row['price'])
            style = Style(row['id'], row['style'], row['price'])
            size = Size(row['id'], row['size'], row['price'])
            # setting = Setting(row['id'], row['setting'], row['price'])

            # Add the dictionary representation of the location to the animal
            order.metal = metal.__dict__
            order.style = style.__dict__
            order.size = size.__dict__
            # order.jewelry = setting.__dict__

            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    '''function to identify order by id'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.style_id,
            o.setting_id,
            o.size_id
        FROM Orders o
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['metal_id'], data['style_id'],
                      data['setting_id'], data['size_id'])
        return order.__dict__


def create_order(new_order):
    '''create an order'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('''
        INSERT INTO Orders
            ( metal_id, style_id,
            setting_id,
            size_id )
        VALUES
            ( ?, ?, ?, ?);
            ''', (new_order['metal_id'], new_order['style_id'], new_order['setting_id'], new_order['size_id'], ))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order


def delete_order(id):
    '''delete function for order'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    '''PUT function for order'''

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
