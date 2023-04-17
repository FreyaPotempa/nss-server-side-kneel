class Order():
    '''class that defines metals properties'''

    def __init__(self, id, metal_id, style_id, setting_id, size_id):
        self.id = id
        self.metal_id = metal_id
        self.style_id = style_id
        self.setting_id = setting_id
        self.size_id = size_id
        self.style = None
        self.metal = None
        self.size = None
