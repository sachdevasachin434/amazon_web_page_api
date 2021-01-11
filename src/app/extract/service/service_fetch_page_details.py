"""
    Service Layer of the Project
"""

import requests
from bs4 import BeautifulSoup
import json
import re


class AmazonPageScrape:
    """Class that contains function to scrape data from amazon product page.
    """
    @staticmethod
    def scrape_page(page_url):
        """Function to scrape title, price, image, description, review.

        Args:
            page_url ([string]): Url of Amazon's product for which information is required.

        Returns:
            [dictionary]: {'url': 'https://www.amazon.in/product_link', 
                            'product': {
                                'name': 'abc', 
                                'imageURL': 'https://images-na.ssl-images-amazon.com/images/xyz.jpg', 
                                'description': 'This is a geniune product.', 
                                'price': '₹100.00', 
                                'totalReviews': 10
                                }
                            }
        """
        # Setting user-agent to avoid any blocking.
        headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

        # fetching htmp content of the product page to apply beautiful soup on html.
        html_content = requests.get(page_url, headers=headers, params={'waits': 2}).text
        
        # Creating BeautifulSoup Object.
        soup = BeautifulSoup(html_content, 'html.parser')

        # Applying exception handling to avoid any code crash.
        try:
            # Fething details as per required logic.
            title = soup.find('span', {"id": "productTitle", "class": "a-size-large product-title-word-break"}).string.strip()
            price = soup.find('span', {"id": "priceblock_ourprice"}).string.strip().replace(" ", "")
            image = list(json.loads(soup.find('img', {"id": "landingImage"})['data-a-dynamic-image']).keys())[0]
            review = soup.find('span', {"id": "acrCustomerReviewText"}).string.strip()
            description_span_tag_list = soup.find('div', {"id": "featurebullets_feature_div"}).findAll('span', {"class": "a-list-item"})
            review = int(re.search(r'\d+', review.replace(',', '')).group())
            for i in range(len(description_span_tag_list)):
                description_span_tag_list[i] = description_span_tag_list[i].string.strip()

            description = "\n".join(description_span_tag_list)

            result = {
                "url": page_url,
                "product": {
                "name": title,
                "imageURL": image,
                "description": description,
                "price": str(price),
                "totalReviews": review
                }
            }
            return result
        except Exception as e:
            raise "HTML Page of the product has been modified from Amazon's side. Please debug the endpoint."
