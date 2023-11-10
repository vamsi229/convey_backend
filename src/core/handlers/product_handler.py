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
            self.rating_object = MongoCollectionBaseClass(mongo_client=mongo_client,
                                                          database=MONGO.MONGO_DATABASE,
                                                          collection=Collections.rating)
        except Exception as e:
            logger.exception(f"Error while initializing variables: {e}")

    def list_products(self, request_data):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while fetching the products",
                      FinalJson.data: {}}
        try:
            body_content = list()
            get_products = self.product_object.find({})
            get_ratings = self.rating_object.aggregate([{
                "$unwind": "$userRatings"
            }, {"$group": {"_id": "$productId", "val": {"$avg": "$userRatings.value"}}}])
            if get_products and get_ratings:
                get_products = list(get_products)
                get_ratings = list(get_ratings)
                for each_product in get_products:
                    temp_json = each_product
                    temp_json["aggregatedRating"] = 0
                    for each_rate in get_ratings:
                        # print(each_rate, each_product)
                        if each_rate["_id"] == each_product["productId"]:
                            temp_json["aggregatedRating"] = each_rate["val"]
                            break

                    body_content.append(temp_json)
                    # print(get_ratings)
            final_json[FinalJson.data] = body_content
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

    def give_rating(self, request_data, email):
        final_json = {FinalJson.status: False, FinalJson.message: "Error while updating rating", FinalJson.data: {}}
        try:
            request_data = dict(request_data)
            email = email
            get_rating = self.rating_object.find_one({"productId": request_data["productId"]})
            if not get_rating:
                insert_rating_response = self.rating_object.insert_one({"productId": request_data["productId"],
                                                                        "userRatings": [{"email": email,
                                                                                         "value": request_data[
                                                                                             "rate"],
                                                                                         "comment": request_data[
                                                                                             "comments"]}]})
                if insert_rating_response:
                    final_json[FinalJson.status] = True
                    final_json[FinalJson.message] = f"Successfully inserted the rating for product"
            else:
                userFound = False
                for each in range(len(get_rating["userRatings"])):
                    if get_rating["userRatings"][each]["email"] == email:
                        userFound = True
                        get_rating["userRatings"][each]["value"] = request_data["rate"]
                        get_rating["userRatings"][each]["comment"] = request_data["comments"]
                    update_rating_response = self.rating_object.update_one(query=
                                                                           {"productId": request_data["productId"]},
                                                                           data={"userRatings": get_rating[
                                                                               "userRatings"]})
                    break
                if not userFound:
                    update_rating_response = self.rating_object.update_one(strategy="$push", query={
                        "productId": request_data["productId"],
                    },
                                                                           data={"userRatings": {"email": email,
                                                                                                 "value": request_data[
                                                                                                     "rate"],
                                                                                                 "comment":
                                                                                                     request_data[
                                                                                                         "comments"]}})
                if update_rating_response:
                    final_json[FinalJson.status] = True
                    final_json[FinalJson.message] = "Successfully updated the rating for product"

        except Exception as e:
            logger.exception(f"Error while updating the rating: {e}")
        return final_json
