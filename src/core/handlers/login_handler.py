import jwt

from src.config import MONGO
from src.constants.constants import FinalJson, Collections
from src.logging import logger
from src.utilities.mongo_utility import MongoConnect, MongoCollectionBaseClass


class LoginHandler:
    def __init__(self):
        try:
            mongo_client = MongoConnect(uri=MONGO.MONGO_URI)()
            self.user_object = MongoCollectionBaseClass(mongo_client=mongo_client,
                                                        database=MONGO.MONGO_DATABASE,
                                                        collection=Collections.users)
        except Exception as e:
            logger.exception(f"Error while initializing: {e}")

    def login_function(self, request_data):
        final_json = {FinalJson.status: False, FinalJson.message: "Failed when login the user", FinalJson.data: {}}
        try:
            get_user_details = self.user_object.find_one({"email": request_data.email})
            if get_user_details:
                if get_user_details["password"] != request_data.password:
                    final_json[FinalJson.message] = "Please check your UserName/Password is Incorrect"
                else:
                    jwt_payload = {"user_name": get_user_details["userName"], "email": get_user_details["email"]}
                    encoded_jwt = jwt.encode(jwt_payload, '12222dgr23g3534423+-232244', algorithm='HS256')
                    final_json[FinalJson.message] = "User Logged in Successfully"
                    final_json[FinalJson.status] = True
                    final_json[FinalJson.data]["authToken"] = encoded_jwt
            else:
                final_json[FinalJson.message] = "User do not exist"
        except Exception as e:
            logger.exception(f"Error while logging in: {e}")
        return final_json

    def signup_function(self, request_data):
        final_json = {FinalJson.status: False, FinalJson.message: "Failed when signing the user", FinalJson.data: {}}
        try:
            request_data = dict(request_data)
            get_existing_user = self.user_object.find_one({"email": request_data["email"]})
            if get_existing_user:
                final_json[FinalJson.message] = "A user with this email already exists"
            else:
                if request_data["password"] != request_data["cPassword"]:
                    final_json[FinalJson.message] = "Password and Confirm Password do not match"
                else:
                    del request_data["cPassword"]
                    insert_user_response = self.user_object.insert_one(request_data)
                    if insert_user_response:
                        final_json[FinalJson.status] = True
                        final_json[FinalJson.message] = "User created Successfully"
        except Exception as e:
            logger.exception(f"Error while signing up the user: {e}")
        return final_json

    def get_user_details(self, request_data):
        final_json = {FinalJson.status: False, FinalJson.message: "Could not get the user details", FinalJson.data: {}}
        try:
            get_user_info = self.user_object.find_one({"email": request_data["email"]})
            if get_user_info:
                final_json[FinalJson.message] = "Successfully fetched the user information"
                final_json[FinalJson.status] = True
                final_json[FinalJson.data] = get_user_info
        except Exception as e:
            logger.exception(f"Error while getting the user details: {e}")
        return final_json

    def update_user_details(self, request_data, email):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while updating the user details",
                      FinalJson.data: {}}
        try:
            print(request_data, email)
            request_data = dict(request_data)
            update_user_response = self.user_object.update_one({"email": email}, request_data)
            if update_user_response:
                final_json[FinalJson.message] = "Successfully updated the password"
                final_json[FinalJson.status] = True
        except Exception as e:
            logger.exception(f"Error while updating the user details: {e}")
        return final_json

    def change_password(self, request_data, email):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while updating password", FinalJson.data: {}}
        try:
            get_user_details = self.user_object.find_one({"email": email})
            if get_user_details:
                if get_user_details["password"] != request_data.password:
                    final_json[FinalJson.message] = "Your  credentials do not match"
                else:
                    print(request_data.newPassword, request_data.confirmPassword)
                    if request_data.newPassword == request_data.confirmPassword:
                        update_password_response = self.user_object.update_one({"email": email},
                                                                               {"password": request_data.newPassword})
                        if update_password_response:
                            final_json[FinalJson.message] = "Successfully updated the new password"
                            final_json[FinalJson.status] = True
                    else:
                        final_json[FinalJson.message] = "New and Confirm Password do not match"
            else:
                final_json[FinalJson.message] = "Could not get the user details for updating password"
        except Exception as e:
            logger.exception(f"Error while updating password: {e}")
        return final_json
