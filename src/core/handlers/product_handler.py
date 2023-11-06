import shortuuid

from src.config import MONGO
from src.constants.constants import Collections, FinalJson
from src.logging import logger
from src.utilities.mongo_utility import MongoConnect, MongoCollectionBaseClass


class productHandler:
    def __init__(self):
        try:
            mongo_client = MongoConnect(uri=MONGO.MONGO_URI)()
            self.product_object = MongoCollectionBaseClass(mongo_client=mongo_client,
                                                           database=MONGO.MONGO_DATABASE,
                                                           collection=Collections.products)
        except Exception as e:
            logger.exception(f"Error while initializing variables: {e}")

    def list_products(self, request_data):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while fetching the products",
                      FinalJson.data: {}}
        try:
            get_products = self.product_object.find({})
            if get_products:
                get_products = list(get_products)
                final_json[FinalJson.data] = get_products
                final_json[FinalJson.status] = True
                final_json[FinalJson.message] = "Successfully fetched the products"
        except Exception as e:
            logger.exception(f"Error while fetching the products: {e}")
        return final_json

    def add_products(self, request_data):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while adding the product", FinalJson.data: {}}
        try:
            if request_data.productId is None:
                request_data = dict(request_data)
                new_product_id = shortuuid.uuid()
                print(new_product_id)
                request_data["productId"] = new_product_id
                add_product_response = self.product_object.insert_one(request_data)
                if add_product_response:
                    final_json[FinalJson.status] = True
                    final_json[FinalJson.message] = "Successfully added the product"
            else:
                request_data = dict(request_data)
                update_product_response = self.product_object.update_one({"productId": request_data["productId"]},
                                                                         request_data)
                if update_product_response:
                    final_json[FinalJson.status] = True
                    final_json[FinalJson.message] = "Successfully Updated the product"
        except Exception as e:
            logger.exception(f"Error while editing the product: {e}")
        return final_json

    def delete_product(self, productId):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while deleting the product",
                      FinalJson.data: {}}
        try:
            delete_product_response = self.product_object.delete_one({"productId": productId})
            if delete_product_response:
                final_json[FinalJson.status] = True
                final_json[FinalJson.message] = "Deleted the product successfully"
        except Exception as e:
            logger.exception(f"Exception while deleting the product: {e}")
        return final_json
