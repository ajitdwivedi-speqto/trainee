from rest_framework.exceptions import APIException

class InvalidProductId(APIException):
    status_code = 400
    default_detail = "Invalid product ID. No product exists with this ID."
    default_code = "invalid_product_id"


