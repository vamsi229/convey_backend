app_base_url = "/convey"


class Login:
    login = "/login"
    sign_up = "/sign-up"
    get_user_details = "/get-user-details"
    update_user_details = "/update-user-details"
    change_password = "/change-password"


class Products:
    product_base = "/products"
    list_products = product_base + "/list-products"
    add_product = product_base + "/add-product"
    edit_product = product_base + "/edit-product"
    delete_product = product_base + "/delete-product"
    update_rating = product_base + "/update-rating"
