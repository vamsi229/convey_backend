import base64
import datetime

import jwt

from src.logging import logger as log


class AESCipher(object):
    """
    A classical AES Cipher. Can use any size of data and any size of password thanks to padding.
    Also ensure the coherence and the type of the data with a unicode to byte converter.
    """

    def __init__(self, key):
        self.bs = 16
        self.key = AESCipher.str_to_bytes(key)

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AESCipher.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


    @staticmethod
    def token_validation(token):
        try:
            SECRET_KEY = '12222dgr23g3534423+-232244'
            ALGORITHM = 'HS256'
            # response = {"status": False, "message": "Verification Failed"}
            response = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
            # if result['expire'] > str(datetime.datetime.today()):
            #     response['data'] = result
            #     response['status'] = True
            #     response["message"] = "Verification Successful"
            #     return response
            # elif result['expire'] < str(datetime.datetime.today()):
            #     return {"status": False, "message": "Token Expired", "data": {'userRole': ""}}
            # else:
            #     return {"status": False, "message": "Invalid token", "data": {'userRole': ""}}
        except Exception as e:
            log.error("Error : {}".format(str(e)))
            response = {"status": False, "message": "Signature verification failed", "data": {'userRole': ""}}
        return response
