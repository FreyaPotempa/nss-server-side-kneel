SIZES = [
    {
        "id": 1,
        "carets": 0.5,
        "price": 400
    },
    {
        "id": 2,
        "carets": 0.75,
        "price": 700
    },
    {
        "id": 3,
        "carets": 1,
        "price": 1400
    },
    {
        "id": 4,
        "carets": 1.5,
        "price": 1950
    },
    {
        "id": 5,
        "carets": 2,
        "price": 3000
    }
]


def get_all_sizes():
    '''function to return all sizes'''
    return SIZES


def get_single_size(id):
    '''function to identify size by id'''
    requested_size = None

    for size in SIZES:
        if size["id"] == id:
            requested_size = size

    return requested_size
