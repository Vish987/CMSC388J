# Final Project Writeup 

## Website
https://cmsc-388-j-final-project.vercel.app/

## Description of your final project idea:
Our final project idea is a personal budget tracker. This will be a web application designed to help users manage and track their personal finances. Users will be able to set up budgets for different categories (e.g., food, entertainment, groceries), log their daily expenses, and visualize their spending habits. The goal is to provide users with a clear overview of their financial health and help them make informed decisions about their spending.

## Describe what functionality will only be available to logged-in users:
Some of the functionalities that will only be available to logged-in users include:

Expense tracking:Users can add expenses to their personal budget. This allows for secure tracking of user-specific data.

Budget creation and management: Users will be able to set timely budgets for different categories and adjust them as needed.

View spending summary: Users will have access to a personalized dashboard that displays their spending by category and compares it with the set budget.

Save and retrieve data: Expense logs and budget data will be saved to a user-specific profile in the database, which can only be accessed by the authenticated user.

## List and describe at least 4 forms:

Registration Form:\
Purpose: To create a new user account.\
Fields: Email address, password, confirm password.\
Validation: Ensures that the passwords match and that the email is unique.

Login Form:\
Purpose: To authenticate users and allow them to access their budget data.\
Fields: Email, password.\
Validation: Ensures that the email and password match an existing user in the system.

Expense Entry Form:\
Purpose: To log a new expense and categorize it for tracking.\
Fields: Category, amount, description, date.\
Validation: Ensures the amount is a valid number and that the correct category is selected.

Budget Creation Form:\
Purpose: To create or modify a user’s budget for various categories.\
Fields: Category, amount, start date, end date.\
Validation: Ensures that the budget amount is a positive number and that the dates are valid.

## List and describe your routes/blueprints (don’t need to list all routes/blueprints you may have–just enough for the requirement):

Users Blueprint:\
/register (GET, POST): Displays and handles the registration form. If the user is already logged in, they will be redirected to the budget dashboard.\
/login (GET, POST): Displays and handles the login form. If the user is already logged in, they will be redirected to the budget dashboard.

Budget Blueprint:\
/budget/create (GET, POST): Allows logged-in users to create a new budget by filling out the budget creation form.\
/budget/view (GET): Displays the user's current budgets and their information.

Expenses Blueprint:\
/expenses/create (GET, POST): Displays and handles the expense entry form. Users can log new expenses, which are associated with specific categories.\
/expenses/view (GET): Displays the user's current expenses and their information.

## Describe what will be stored/retrieved from MongoDB:

User Data:\
Stored: User’s email and hashed password.\
Retrieved: Used for authentication and session management when users log in or register.

Expense Data:\
Stored: Each expense entry will have a category, amount, description, date, and the user ID that created it.\
Retrieved: When users view their expenses, this data will be queried to display their spending history.

Budget Data:\
Stored: Each user’s budget settings, including the budgeted amount per category, and the time period.\
Retrieved: This data will be queried to show users their budget status.

## Describe what Python package or API you will use and how it will affect the user experience:

Plotly:\
Purpose: To generate visual graphs showing users their spending patterns over time, by category, and in relation to their budgets.\
Impact on User Experience: Interactive charts will allow users to quickly assess where their money is going and whether they are staying within their financial limits. This helps users make informed decisions about their spending.