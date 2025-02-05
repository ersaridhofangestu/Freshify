import os
from ..libs.pandas import PandasHandler

class cart_model(PandasHandler) :
    def __init__(self) -> None:
        self.PATH = os.path.join(os.getcwd(), 'src', 'data', 'cart.json')
        super().__init__(path=self.PATH)
        pass
    
    def create_cart(self, data):
        return self.create(data)
    
    def read_cart(self,where):
        return self.read_uniq(where)
    def delete_cart(self,id):
        return self.delete(id)