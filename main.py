from src.utils.selection import select
from src.utils.loading import loading_bar
from src.controllers.users import user_controller
from src.controllers.cart import cart_controller
from src.controllers.checkout import checkout_controller

import os
import pyfiglet
from colorama import Fore, Back, Style, init
from rich.console import Console
from time import sleep
from tabulate import tabulate
from pandas import DataFrame,read_json

if __name__ == '__main__':
    Console().clear()
    init(autoreset=True)
    user_config = user_controller()
    cart_config = cart_controller()
    checkout = checkout_controller()
    
    email = None
    
    print(pyfiglet.figlet_format("Freshify", font="slant"))

    answers:str = select(type='list',name='home-menu',choices=[f'\U0001F510  Login','\U0001F4DD  Register','\U0001F6D1  Exit'], message="select an option")
    
    if not answers['home-menu'].split(' ')[-1] == 'Exit':
        if answers['home-menu'].split(' ')[-1] == 'Login':
            while True :
                
                email = select(
                                    type='input',
                                    name='email', 
                                    message="\U00002709 Please enter your email",
                                    validate=lambda val: '\U0000274C Please enter a valid email!' if '@' not in val or '.' not in val else True)
                
                password = select(
                                    type='password',
                                    name='password', 
                                    message="\U0001F511 Please enter your password")
                                    
                new_data_user = {
                                'email': email['email'],
                                'password': str(password['password'])
                }
                
                # dummy = {'email':'ersa@gmail.com','password':'ridho'}
                status_user = user_config.user_login(data_user=new_data_user)
                if status_user == True :
                    break
                else :
                    continue
                
        if answers['home-menu'].split(' ')[-1] == 'Register':
                while True :
                        
                        email = select(
                                type='input',
                                name='email', 
                                message="\U00002709 Please enter your email",
                                validate=lambda val: '\U0000274C Please enter a valid email!' if '@' not in val or '.' not in val else True)
                        password = select(
                                type='password',
                                name='password', 
                                message="\U0001F511 Please enter your password")
                                
                        new_data_user = {
                            'email': email['email'],
                            'password': str(password['password'])
                        }
                        
                        
                        status_user = user_config.user_register(data_user=new_data_user)
                        if status_user == True :
                            break
                        else :
                            continue

        sleep(2)

        while True :
            Console().clear()
            print(pyfiglet.figlet_format("Freshify", font="slant"))
            answers:str = select(
                type='list',
                name='pelanggan-menu',
                choices=[
                    '\U0001F4CB  Menu',
                    '\U0001F6D2  Cart',
                    '\U0001F4B3  Checkout',
                    '\U0001F6D1  Logout'], 
                message="select an option")

            match answers['pelanggan-menu'].split(' ')[-1]:
                case 'Menu':
                    Console().clear()
                    
                    print(pyfiglet.figlet_format("Freshify", font="slant"))

                    path_file_menu = os.path.join(os.getcwd(), 'src', 'data', 'products.json')
                    menu = read_json(path_file_menu)
                    tabel_menu = tabulate(DataFrame(menu), headers='keys',tablefmt='grid',showindex=False)
                    print(f"{tabel_menu}".center(100))
                    while True :
                        answers:str = select(type='confirm',name='pelanggan-menu-menu', message="Quit")
                        if answers['pelanggan-menu-menu']:
                            break
                        else:
                            continue
                case 'Cart':
                    Console().clear()  
                    print(pyfiglet.figlet_format("Freshify", font="slant"))

                    cart_new = cart_config.create_cart_validation(email['email'])
                    
                case 'Checkout':
                    Console().clear()  
                    cart = cart_config.read_cart(where=email).reset_index(drop=True)
                    if cart.empty:
                        print('\U000026A0 You cannot checkout because the cart has not been created.')
                        sleep(2)
                        continue
                  
                    print(f'''
{print(pyfiglet.figlet_format("Freshify", font="slant"))}
ID Orderer {cart.loc[0, 'id']}
Email Orderer {cart.loc[0, 'email']}
your Order :
{tabulate(DataFrame(cart.loc[0, 'items']), headers='keys',tablefmt='grid',showindex=False)}
Total price Rp. {cart.loc[0, 'total_price']:,.0f}
                          ''')
                    
                    confirm = select(
                        type='confirm',
                        name='continue',
                        message='Do you want to checkout now ?',
                    )
                    
                    if not confirm['continue']:
                        continue
                    
                    address = select(
                        type='input',
                        name='location',
                        validate=lambda val: len(val) >= 10 or 'Must be a minimum of 10 characters in detail!' ,
                        message='Enter your address with details ?',
                    )
                    
                    payment = select(
                        type='list',
                        name='method',
                        choices=[
                            '\U0001F4B5  Cash',
                            '\U0001F4E6  Cash-on-Delivery',
                            '\U0001F4B3  Credit-Cart'
                            ], 
                        message="Select payment method!"
                    )
                    
                    loading_bar()
                    
                    print('\U00002705  Order was successfully placed')

                    cart['address'] = address['location']
                    cart['payment'] = payment['method'].split(' ')[-1]

                    checkout.validation_checkout(pyment=payment['method'],data=cart)

                    cart_config.delete_cart(cart.loc[0,'id'])
                
                    sleep(3)
                    
                case 'Logout':
                    Console().clear()
                    exit()
    else:
        exit()