# Rollbar Challenge

***NOTE: the notes are shown by -> in the text

This exercise must be done individually. Please use your personal email to sign up for the required services (GitHub, Rollbar, Datadog, etc).

The application consists in an integration of a 3rd party API Rollbar (error tracking platform). Sign up for a personal account in case that you don't have any, there's a free tier that is enough for this exercise.

We should be able to manage errors (get/create/update) and also be notified in a Slack channel based on some specific rules.

The backend should have 2 different interfaces (API Rest and CLI), both interfaces should run the same use cases.

It is recommended to follow the table of contents step by step.

# Step 1: Prepare the environment.
All the infrastructure services must be managed by Docker / Docker compose (databases, etc.).

We're going to use Python 3.10.6 version, use pyenv to manage this requirement.

## NOTE:  -> The python version is implemented in the .python-version file.

# Step 2 

Using Flask we will prepare 2 routes:

- (/)which will return a text message, for example "API under construction".
 
- (/check) should be the health check of the application and should return a JSON response like this:

## NOTE : -> We also implemented in the /check the testing for the connection with the database. If it returns OK, the connection is OK, if don't, it will return KO

# Step 3: CRUD API / CLI.

We want to manage errors using the Rollbar service. Rollbar is a SaaS to track the errors that you collect in your applications and get some reports from them.

Using Flask we will create an integration with the Rollbar API. Use the plain HTTP REST API, not the Python client provided by Rollbar. Follow these steps:

- Create a new project in Rollbar, then select "other" in the "select SDK" step. You'll get the credentials needed to access to the API.

- You can view the documentation (endpoints, payloads, etc) in the documentation page. Hint: Please check carefully the documentation and use the online API tester in order to see the exact format that you need to provide as input because sometimes could be tricky.

- Before start coding, check if you can access to the Rollbar API using curl as the documentation explains.

Write the minimum code to create, update, delete, show and list items in Rollbar using your application API. You could create the following endpoints in your application to meet the requirements (apply all or only the necessary):

## NOTE : -> We implement the endpoints in our flask app in the routes.py. All of them access to a method that we explain in the next lines. In this point of the app we only can use the command curl, or by the navigator we can acces to the get method of the /items that will return all the items.

- GET all (/items): curl --request get http://localhost:5000/items

- GET one (/items/<id>): curl --request get http://localhost:5000/items/id

- POST (/items): curl --request post http://localhost:5000/items

- PATCH (/items/<id>): curl --request patch http://localhost:5000/items

- DELETE (/items): WE CAN'T DO IT BECAUSE ROLLBAR API DOESN'T ALLOW US TO DELETE AN ITEM. IT RETURNS NONE IN OUR API. 



