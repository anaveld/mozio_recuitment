from rest_framework.exceptions import APIException


class WrongGeoTypeException(APIException):
    status_code = 400
    default_detail = 'You need to pass Point instance to perform a search.'
