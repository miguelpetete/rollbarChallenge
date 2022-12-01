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

