# Amazon Web Scraper

Amazon Web Scraper contains two post endpoints that work serially to scrape data from amazon's product page given its URL and load data to MongoDB. 

### endpoint('localhost/api/fetch_details')

It retrieves the following information from a product webpage given its URL:
- Product Name/Title
- Product image URL
- Product description
- Product price
- Product total number of reviews.

### endpoint('localhost/api/payload_to_document')
It stores the data (obtained in JSON format) into the MongoDB database with the timestamp appended to the JSON passed.

## Installation
-  **Git**: Refer following link for installation guide: [Click Here](https://github.com/git-guides/install-git "click here").
The git version used to push this project is 2.17.1.
- **Docker**: Refer following link for installation guide: [Click Here](https://docs.docker.com/engine/install/ "click here"). The Docker version which has been used for this project is 20.10.2. Please update your docker to the latest configuration to be able to run this application seamlessly.

- **Docker-Compose**: Refer following link for installation guide: [Click Here](https://docs.docker.com/compose/install/ "click here"). The docker-compose version which has been used for this project is 1.17.1. Please update your docker-compose to the latest configuration to be able to run this application seamlessly.

## Project Clone
Steps: 
- Move to the location at which git clone is required.
- Use the below command to clone Sachin's git repository.

```git clone https://github.com/sachdevasachin434/amazon_web_scraper.git```


## Images used and their versions



## Steps to setup the project
Run the following set of commands to run this project. *Make sure that you have successfully installed git, docker and docker-compose on the desired machine and have updated docker and docker-compose to the above mentioned versions.* Use sudo commands for docker and docker-compose to avoid any permission issue.

**Step-1** -

Go inside the following directory to run docker-compose up command - 

```cd /${root_directory}/amazon_web_page_api/docker-compose.yml```

**Step-2** - 

Since the services are defined in a single file(docker-compose.yml), you just need to issue a single command to start the containers, create the volumes, and set up the networks. This command also builds the image for your Flask application and the Nginx web server. Run the following command to build the containers. 

```sudo docker-compose up```

**Note** -

Use the following command to list the running containers once the build process is complete:

```sudo docker ps```

![docker-compose-ps-output](https://github.com/sachdevasachin434/amazon_web_page_api/blob/master/output/docker-compose-ps-output.png?raw==True)


## Steps to run flask application(amazon_web_scraper)
**Step-1**
Search the product on amazon for which scraping is required and copy its URL.

![product_page](https://github.com/sachdevasachin434/amazon_web_page_api/blob/master/output/product_page.jpeg?raw==True)

**Step-2**
After URL is copied to clipboard open postman or any such application to hit the flask endpoint.

If no such application is installed. Follow following steps:
1. Open Chrome Web Browser.
2. Open [Chrome Web Store](https://chrome.google.com/webstore/category/extensions "click here").
3. Search [Tabbed Postman](https://chrome.google.com/webstore/detail/tabbed-postman-rest-clien/coohjcphdfgbiolnekdpbcijmhambjff "tabbed postman").
4. Open the extension as shown below.
5. Click on Add Extension to Chrome.
6. Open the added extension in Chrome.

![tabbed_postman](https://github.com/sachdevasachin434/amazon_web_page_api/blob/master/output/tabbed_postman.jpeg?raw==True)

**Step-3**

**POST APIs required for the application**

**1. Fetch Details(/api/fetch_details)** - Accepts product's URL and scrapes required information from it.

After tabbed postman is installed and is running, hit the first endpoint(/api/fetch_details) using the following steps.
- Search *http://localhost/api/payload_to_document* in postman.
- Make sure you don't have any headers defined as it accepts form data as input.
- The required output will be in the json format.

![fetch_details_output](https://github.com/sachdevasachin434/amazon_web_page_api/blob/master/output/fetch_details_output.jpeg?raw==True)

**2. Insert Details to MongoDB(/api/payload)** - Accepts the JSON format as input inserts data into MongoDB.
- Input Format - Example of the JSON input format : (The result of the above API can be used as an input to this API)
```
{
	"url": "https://www.amazon.com/PlayStation-4-Pro-1TB-Console/dp/B01LOP8EZC/",
	"product": {
		"name": "PlayStation 4 Pro 1TB Console",
		"imageURL": "https://images-na.ssl-images-amazon.com/images/I/41GGPRqTZtL._AC_.jpg",
		"description": "Heighten your experiences.\n Enrich your adventures.",
		"price": "$348.00",
		"totalReviews": 4436
	}
}
```
![insert_details_input](https://github.com/sachdevasachin434/amazon_web_page_api/blob/master/output/insert_into_db_input.jpeg?raw==True)

- Returns the result as successfully inserted or gives an error if the input is not in the correct format or server goes down or any issue arises with the database.

![insert_details_output](https://github.com/sachdevasachin434/amazon_web_page_api/blob/master/output/insert_into_db_output.jpeg?raw==True)

**Step-4**

**MongoDB Data Validation**

- Use following command to enter into mongodb shell interface.
```sudo docker exec -it mongodb bash```

- Login with following credentials.
```
username - sellerapp
password - sellerapp
```
- The database name for the database used is ProductData. Use below command to enter into the database that is used in this app.
```
use ProductData
```

- Use below command to get the Document written inside the database.
```
db.PageData.find({})
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
