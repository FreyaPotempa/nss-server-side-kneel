STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 600
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 950
    }

]


def get_all_styles():
    '''function to return all styles'''
    return STYLES


def get_single_style(id):
    '''function to identify size by id'''
    requested_style = None

    for style in STYLES:
        if style["id"] == id:
            requested_style = style

    return requested_style
