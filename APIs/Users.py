from APIs.Base_API import BaseAPI
import os
from dotenv import load_dotenv

class UsersAPI(BaseAPI):

    def call_user_register_api(self, parameters):
        url = f"{self.host}{self.user_register_endpoint}"