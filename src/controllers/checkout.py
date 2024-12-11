from ..utils.selection import select
from ..models.checkout import checkout_modul
from ..libs.firebase import create_checkout_to_firebase

from time import sleep

class checkout_controller(checkout_modul) :
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def validation_checkout(self,pyment, data):
        if pyment.split(' ')[-1] == 'Cash':
            price = int(data.loc[0, 'total_price'])
            sleep(0.5)
            method = select(
                        type='input',
                        name='cash',
                        validate=lambda val: (val.isdigit() and int(val) >= price ) or 'Enter the nominal amount of money and make sure it is enough to pay!' ,
                        message='pay ? ',
                    )
            money = int(method['cash'])
            sleep(0.5)
            print(f'\U0001F4B5  You pay the amount Rp. {money:,.0f}')
                            
            if money > price :
                sleep(0.5)
                print(f'\U0001F4B5  Your refund amount is Rp. {(money - price):,.0f}')
            else:    
                sleep(0.5)
                print('\U0001F4B5  Your money is right')
                                
        else:
            sleep(0.5)
            print('\U0001F4B5  Your order will be sent immediately to your address.') 
            print('\U0001F4B5  Your order has been successfully placed.')
            sleep(0.5)
        print('\U0001F4B5  Thank you for ordering on Freshify')
        data['status'] = 'success'
        self.checkin(data=data)
        create_checkout_to_firebase(data)
        
        return