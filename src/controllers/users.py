from ..view.user import user_view
from ..models.user import user_model
from ..utils.loading import loading_bar

from typing import Dict
from time import sleep

class user_controller(user_view,user_model):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    
    def user_login(self,data_user:Dict):
        try:
            data_frame = self.read_uniq(where={'email' : str(data_user['email'])}).reset_index(drop=True)
            if data_frame.empty:
                print("\U0000274C Email not found.")
                return
            
            email , password = str(data_frame.loc[0,'email']), str(data_frame.loc[0,'password'])
            if email == str(data_user['email']):
                if password == str(data_user['password']):
                    loading_bar()
                    print('\U00002705  Login in successfully')
                    return True
                else:
                    print('\U0000274C  invalid password email.')
                    return False
            else:
                print('\U0000274C  invalid email.')
                return False
        except ValueError :
            print('\U0000274C  invalid email') 
            return False
    
    def user_register(self,data_user:Dict):
        user = self.read_uniq(where={'email' : data_user['email']})
        
        if len(user) > 0 :
            print('\U000026A0  email is already in use.')
            return False
        
        add_data = self.create_user(data=data_user)
        response = self.view_register_user(add_data)
        if response['status'] == 201:
            loading_bar()
            print('\U00002705  Signed in successfully')
            print
            return True
        else :
            return False