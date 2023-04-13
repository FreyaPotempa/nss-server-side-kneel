DATABASE = {
    "metals": [
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
    ],
    "styles": [
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

    ],
    "settings": [
        {
            "id": 1,
            "setting": "Ring",
            "price": 100
        },
        {
            "id": 2,
            "setting": "Earrings",
            "price": 150
        },
        {
            "id": 3,
            "setting": "Necklace",
            "price": 200
        }
    ],
    "sizes": [
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
    ],
    "orders": [
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
}


def all(resource):
    '''get all of a collection'''
    if resource in DATABASE.keys():
        return DATABASE[resource]


def retrieve(resource, id):
    '''get a single item'''
    requested_resource = None

    if resource in DATABASE.keys():
        asset_list = DATABASE[resource]
        matching_metal = {}
        matching_size = {}
        matching_style = {}
        matching_setting = {}

        for asset in asset_list:
            if asset["id"] == id:
                requested_resource = asset
                for metal in DATABASE["metals"]:
                    if requested_resource["metalId"] == metal["id"]:
                        matching_metal = metal
                for size in DATABASE["sizes"]:
                    if requested_resource["sizeId"] == size["id"]:
                        matching_size = size
                for setting in DATABASE["settings"]:
                    if requested_resource["settingId"] == setting["id"]:
                        matching_setting = setting
                for style in DATABASE["styles"]:
                    if requested_resource["styleId"] == style["id"]:
                        matching_style = style

                requested_resource["metal"] = matching_metal
                requested_resource["size"] = matching_size
                requested_resource["setting"] = matching_setting
                requested_resource["style"] = matching_style
                total_price = requested_resource["style"]["price"] + requested_resource["metal"]["price"] + \
                    requested_resource["size"]["price"] + \
                    requested_resource["setting"]["price"]
                requested_resource["total price"] = total_price

                requested_resource.pop("settingId")
                requested_resource.pop("metalId")
                requested_resource.pop("sizeId")
                requested_resource.pop("styleId")

    return requested_resource


def create(post_body):
    '''post a new item'''
    max_id = DATABASE["orders"][-1]["id"]
    new_id = max_id + 1
    post_body["id"] = new_id
    print("post", post_body)

    DATABASE["orders"].append(post_body)

    return post_body


def update(id, post_body):
    '''update an item'''
    for index, order in enumerate(DATABASE["metals"]):
        if order["id"] == id:
            DATABASE["metals"][index] = post_body
            break
