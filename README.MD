# GENERAL FUNCTIONS

## GETTING STARTED

#### Passwords

```genPass``` is the first security layer to prevent unwanted tampering.
```adminPass``` is the second security layer to prevent employees from reading sensitive data.

#### Limitations

Using incorrect data entries WILL crash the program, such as inputting strings into an integer input.
Leaving blank inputs will also crash the program.

## Inventory

#### Adding Items

Adding Items is a simple task. Simply follow the input boxes as follows.
If you wish to alter a pre-existing item, simply type in the same name and ID and it will update the values. 

#### Deletion of Items

There is no function to delete items, however blanking the values will work for regular employees who do not have access to the codebase.

## Point of Sales

#### Checking out Items

To check out items, simply input the name OR the ID into the text box. All transactions will not be saved unless you hit the ```LOG TRANSACTION``` button. If you made an error, simply press the ```CLEAR``` button to erase it. 

Prices will automatically be calculated assuming a tax rate of 13%.

#### Accessing Receipts

Item receipts can be accessed under the ```transactions``` folder with the corresponding date. Each receipt file will be named on the date the purchase was made, and the individual purchases will be indentified by the timestamp.

Logged transactions are as follows:
```
[pencil,1,20]
 ^      ^ ^
 |      | | 
 |      |  \_ Cost
 |       \___ Amount
  \__________ Name
  ```
  Total cost and tax will be added at the end of the list.

It should be noted that items with the same ID will not work.

# ADMINISTRATIVE FUNCTIONS
These are functions that are not accessed by regular users.
## Employee Info

#### Adding Employee Info

To add an employee, simply follow the instructions on the page. If you wish to edit an employee's info, simply type in the person you wish to change, and the info will be updated according to user input.

Much like the inventory page, there is no way to remove users, so you must blank out the information with zeroes or simply remove it from the codebase.

## Financial Log

#### Adding Financial Data

To add fnancial data, simply follow the input boxes. Much like the inventory and the employee logs, you can alter financial data by typing in the name, which is year-month (25-01) It should be noted that this is **NON-PERMANENT** and should not be relied upon for important financial data.

## Misc

#### Accessing Receipts

To access the receipts, simply find the location you installed this program in, and navigate to the
```transaction_logs```
folder. 

#### Accessing Written Data.

All stored data is stored in the
```config```
folder. 

# THANK YOU!

This project is completely open source and can be accessed via: 
https://github.com/AidenDeane/database_app/tree/main








