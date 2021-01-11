"""
    Database Layer of the project.
"""
import pymongo
import os
from datetime import datetime

class DBInsertUpdate:
    """
    Class that contains method to load data to mongodb server.
    """
    @staticmethod
    def insert_into_db(data):
        """Function to insert data to mongodb server.

        Args:
            data (dictionary): {'url': 'https://www.amazon.in/product_link', 
                                'product': {
                                    'name': 'abc', 
                                    'imageURL': 'https://images-na.ssl-images-amazon.com/images/xyz.jpg', 
                                    'description': 'This is a geniune product.', 
                                    'price': '₹100.00', 
                                    'totalReviews': 10
                                    }
                                }

        Raises:
            Exception: Any exception that could occur on database or python side.

        Returns:
            [dictionary]: returns a string acknowledging data is successfully inserted.
        """
        try:
            #connecting to local client of mongobd.
            myclient = pymongo.MongoClient('mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/')

            #use database "amazon_web_scrap".
            mydb = myclient[os.environ['MONGODB_DATABASE']]

            # set collection for inserting data.
            mycol = mydb['PageData']

            # Appending timestamp to dictionary.
            data["timestamp"] = datetime.now()
            print(data)

            #Using insert_one method to create and insert a document.
            mycol.insert_one(data)

            return {"result": "Data Inserted Successfully."}
        except Exception as e:
            raise Exception
