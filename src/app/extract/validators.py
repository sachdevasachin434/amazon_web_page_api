"""
    HTTP argument validation
"""
from marshmallow import (
    Schema,
    fields as api_fields,
    validates,
    ValidationError,
)
import requests

class FetchPageDetailsSchema(Schema):
    pageUrl = api_fields.String(required=True)
    @validates("pageUrl")
    def validate_quantity(self, value):
        headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        if requests.get(value, headers=headers).status_code != 200:
            raise ValidationError("Please enter valid product page url.")
