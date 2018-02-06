

class OpenFruitTaxonomyAPI:
    version = 1
    base_url = 'openfruit.io/api/v1/'

    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url


    def get_cultivars(self):
        pass

