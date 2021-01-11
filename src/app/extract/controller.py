"""
    Endpoint controller layer of the project
"""
from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
import app.extract.validators as validator
import requests
from app.extract.service.service_fetch_page_details import AmazonPageScrape
from app.extract.data_access.insert_into_db import DBInsertUpdate

API = Namespace("Extract", description="Extract API")


@API.route("/fetch_details")
class FetchPageDetails(Resource):
    """
        Class handling HTTP requests to endpoint /api/fetch_details
    """

    @classmethod
    def post(cls):
        # validating the page url for which scraping is required.
        if request.form['pageUrl']:
            page_url = request.form['pageUrl']
        else:
            return "Please pass page url for which information is required", 400
        headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        if requests.get(page_url, headers=headers).status_code != 200:
            raise ValidationError("Please enter valid product page url.")

        try:
            # Calling service layer function.
            return (
                AmazonPageScrape.scrape_page(
                    page_url=page_url,
                ),
                200,
            )
        except ValidationError as err:
            return err.messages, 400


@API.route("/payload_to_document")
class InsertIntoDB(Resource):
    """
        Class handling HTTP requests to endpoint /api/payload_to_document
    """

    @classmethod
    def post(cls):
        try:
            return (
                DBInsertUpdate.insert_into_db(
                    data=request.get_json(),
                ),
                200,
            )
        except ValidationError as err:
            return err.messages, 400
