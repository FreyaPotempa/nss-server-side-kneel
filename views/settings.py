SETTINGS = [
    {
        "id": 1,
        "setting": "Ring"
    },
    {
        "id": 2,
        "setting": "Earrings"
    },
    {
        "id": 3,
        "setting": "Necklace"
    }
]


def get_all_settings():
    '''function to return all settings'''
    return SETTINGS


def get_single_setting(id):
    '''function to return setting by id'''
    requested_setting = None

    for setting in SETTINGS:
        if setting["id"] == id:
            requested_setting = setting

    return requested_setting
