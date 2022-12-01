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

Just to make it clear, your /items endpoint will request data to the /items endpoint of Rollbar.
 
In Rollbar you can create different kind of items, for the sake of simplicity we're going to support only message type items.
 
Organize your code in a way to reuse as much as possible your data structures and code, we're not going to allow a mere copy/paste from the documentation API tester.

The service must be able to be executed also via CLI. You could use the click library to do that.

## NOTE : -> Now, we should use the CLI to execute our app. We use click for that. To make it as simple as possible, we only have to execute the cli.py followed by --help to see the options that we have. We will see what do we have to do for execute the same commands than before. It also allows us to post  an item not randomly as before, we could create it with a message. 
 
- GET all (/items): python cli.py 

- GET one (/items/<id>): python cli.py --get 1 --id <id>

- POST (/items): python cli.py --post 1 --message <message> 

- PATCH (/items/<id>): python cli.py --patch 1 
 
## NOTE : -> In future implementations we will take all the neccesary info to do the create not only with the message and algo do the same with the patch of an item. 
 
 
# Step 4: Adapt the CRUD adding a database.
 
We're going to add a PostgreSQL database to store reports. You can use whatever ORM or library that you consider to operate the database.
 
- Create a Report model with the appropriate fields to store the meaningful data of the Rollbar report object.
 
- Make a CLI command to retrieve the reports from Rollbar (/reports endpoint) and store it in the database.

- Create a new /reports endpoint in your application that will return a JSON with the stored reports. If you don't have any report stored in your database, you'll query Rollbar to get the top active items, then subsequent calls to your endpoint will retrieve the data from the database, not Rollbar.
 
- Create a CLI command in your application to clear the reports.
 
## NOTE : -> We created the following implementations: 
 
- An endppoint called /reports in wich we get access to the top active items. It works as follows: first, look in the database if we have an old report. If don't go to the rollbar API and take the top active items from there. If it isn't empty, it takes it from the database. 
 
- GET top active items (/reports): curl --request get http://localhost:5000/reports
 
- DELETE top active items (/reports): curl --request delete http://localhost:5000/reports -> it deletes the info from the database, so it's the way that we have to update the database: delete all and then make a get request to the rollbar API. 
 
- GET top active items (/reports):  python cli.py --getreport 1
 
- DELETE top active items (/reports):  python cli.py --deletereports 1
 
 
 
# Step 5: Test your application with Pytest
 
## NOTE : -> I have created the test.py and in it we test the expected connections with the api and the database. It uses app.test_client().
 
# Step 6: Instrument your application with Datadog.
 
## NOTE : -> In this firts version of the app I couldn't implement the conection with Datadog, but it is in process. In the future versions it will work. 
 
# Step 7: Bonus
 
## NOTE : -> In this first version the pagination isn't implemented yet, but in future versions it will be done. I have implemented the test of the connection with the database in the /check endpoint, it's working fine. Also, I've implemented dotenv to make the environment variables and having more security in the app for don't publish the secret keys of the rollbar API. 
 
## LAST NOTE : -> In future versions I will make better the CLI and more intuitive for the user. Also, make better the way of creating (POST) and updating (PATCH) items, giving the opportunity to fullfil or change all the fields of an item. Also implementing Datadog and making better the testing of the app. Last, implementing a GUI to make easier to the user the interaction with the app. 
 
