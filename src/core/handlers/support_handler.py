import datetime

import shortuuid

from src.config import MONGO
from src.constants.constants import Collections, FinalJson
from src.logging import logger
from src.utilities.mongo_utility import MongoConnect, MongoCollectionBaseClass


class SupportHandler:
    def __init__(self):
        try:
            mongo_client = MongoConnect(uri=MONGO.MONGO_URI)()
            self.support_object = MongoCollectionBaseClass(mongo_client=mongo_client,
                                                           database=MONGO.MONGO_DATABASE,
                                                           collection=Collections.support_collection)
        except Exception as e:
            logger.exception(f"Error while initializing variables: {e}")

    def contact_support(self, request_data, user_email):
        final_json = {FinalJson.data: {}, FinalJson.message: "Error while raising the support ticket",
                      FinalJson.status: False}
        try:
            support_id = shortuuid.uuid()
            insert_json = {"supportId": support_id, "email": request_data.email, "message": request_data.message,
                           "insertedAt": datetime.datetime.now(), "updatedAt": "", "userEmail": user_email}
            support_insert_response = self.support_object.insert_one(insert_json)
            if support_insert_response:
                final_json[FinalJson.status] = True
                final_json[FinalJson.message] = "Successfully raised the support ticket"
        except Exception as e:
            logger.exception(f"Error while raising the support ticket: {e}")
        return final_json
