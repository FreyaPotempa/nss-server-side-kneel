import sqlite3
from models import Metal

METALS = [
    {
        "id": 1,
        "metal": "14K Gold",
        "price": 700
    },
    {
        "id": 2,
        "metal": "24K Gold",
        "price": 1000
    },
    {
        "id": 3,
        "metal": "Platinum",
        "price": 800
    },
    {
        "id": 4,
        "metal": "Palladium",
        "price": 1200
    }
]


def get_all_metals():
    '''function to return all metals'''
    return METALS

# Function with a single parameter


def get_single_metal(id):
    '''Variable to hold the found metal, if it exists'''
    requested_metal = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for metal in METALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal


def update_metal(id, new_metal):
    '''updating metal price'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
            SET
                metal = ?,
                price = ?
            WHERE id = ?
    """, (new_metal['metal'], new_metal['price'], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True
