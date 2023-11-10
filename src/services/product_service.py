from fastapi import APIRouter, Header

from src.api import app_base_url, Products
from src.constants.constants import ResponseMessage, ResponseStatus
from src.core.handlers.product_handler import productHandler
from src.logging import logger
from src.schemas.product_schema import *
from src.utilities.AESEnc import AESCipher

product_router = APIRouter(prefix=app_base_url)


@product_router.post(Products.list_products)
def list_product_fun(request_data: list_product_schema):
    try:
        product_object = productHandler()
        response = product_object.list_products(request_data=request_data)
        return response
    except Exception as e:
        logger.exception(f"Failed to list products- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to list products", data=None)


@product_router.post(Products.add_product)
def add_product_fun(request_data: add_product_schema):
    try:
        product_object = productHandler()
        response = product_object.add_products(request_data=request_data)
        return response
    except Exception as e:
        logger.exception(f"Failed to add the product: {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to add the product", data=None)


@product_router.put(Products.edit_product)
def edit_product_fun(request_data: add_product_schema):
    try:
        product_object = productHandler()
        response = product_object.add_products(request_data=request_data)
        return response
    except Exception as e:
        logger.exception(f"Failed to edit the product: {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to edit the product", data=None)


@product_router.delete(Products.delete_product)
def delete_product_fun(productId: str):
    try:
        print(productId)
        product_object = productHandler()
        response = product_object.delete_product(productId)
        return response
    except Exception as e:
        logger.exception(f"Failed to delete the product: {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to delete the product", data=None)


@product_router.post(Products.update_rating)
def add_rating_fun(request_data: update_rating_schema, token: str = Header(...)):
    try:
        token_data = AESCipher.token_validation(token)
        product_object = productHandler()
        response = product_object.give_rating(request_data=request_data, email=token_data["email"])
        return response
    except Exception as e:
        logger.exception(f"Failed to add rating: {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to add rating", data=None)
