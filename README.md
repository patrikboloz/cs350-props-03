Homework 10
====

### Tasks 1 through 6 constitute Homework 10. __Due date is Friday, April 27__ by 11:59pm. Submit by pushing to your github repository.

# Get Started
1. __fork__ this repository to your GitHub account (use the fork button at the top)
2. __clone__ your forked repo to your local working directory
3. cd to repository/project root
... you know the drill...
4. create a virtual environment for this project
5. Run: `pip install -r requirements.txt`
6. Setup the django app: `python manage.py migrate`
7. Load the database with sample data containing a set of real estate properties and transactions: 

    `python manage.py loaddata property-testdata`

    `python manage.py loaddata transaction-testdata`

8. Create a superuser for the app: `python manage.py createsuperuser`
9. Run the test server: `python manage.py runserver`
10. At the home page, click on the `see our properties` link to view the five property listings that were loaded in step 7.
11. Click on the `View Transactions` button for any property to show a list of transactions related to that property. 

E.g., `http://localhost:8000/transaction/list/1/`

The above page should show one transaction object for the property. Note the green add, blue view, and yellow edit buttons. Your task for this homework is to implement the views to handle those three buttons.

TODO: transactions App
----

The transactions app (`transactions/models.py`) contains a model for storing real estate related transactions (e.g., offers, etc.). Modify the views and urls of the transactions app to support operations for adding, viewing, and editing transaction objects.


### 1. Add a generic view to the transactions app to show the details of a single transaction. Remember to update `transactions/urls.py` to route your new view. Use the DetailView generic.

### 2. Add a generic view to the transactions app to create an existing transaction. Remember to update `transactions/urls.py` to route your new view. Use the CreateView generic.

### 3. Add a generic view to the transactions app to edit an existing transaction. Remember to update `transactions/urls.py` to route your new view. Use the UpdateView generic.

### 4. Create the three necessary template files for the above views. Be sure to place these in `transactions/templates/transactions/` directory.

### 5. To finally implement the buttons, you must specify the correct URL in the anchor tags in `transactions/templates/transactions/list.html`. These anchors should link to the appropriate route you added above for each button.








