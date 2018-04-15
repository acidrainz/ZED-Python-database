# This Project will be updated in the comming release you will be able to use Database Models and database releationships
# ZED-Python-database
a python database helper to make the CRUD very easy ... Enjoy!

# Code Examples

> ### you can get all data from a table using

```python 
#table method takes 1 param which is the name of the table
# the all() method doesn`t take any params
DB().table("table_name").all()
``` 

> ### you can get some data from a table using

```python 
#where method takes only 2 params which is the column name and the value of it
DB().table("table_name").where('id',1).get()
#another example with or where
DB().table("table_name").where('id',1).orWhere('username','zed').get()
#another example with whereNot this will get all records which not equal this value
DB().table("table_name").whereNOT('id',1).get()
``` 
#### you can change the id with any col name
> ### EXAMPLE WITH ORDER BY AND LIMIT
```python
DB().table("table_name").where('name','zed').orderBy('id','desc').limit(5).get()
```
> ### then you can use the result data from READ by for loop
##Example 
```python
users = DB().table("users").all()
for user in users:
  print(user)
```
> ### you can insert data to database using dictionary like this
```python
DB().table("table_name").create({"username":"zed","email":"zed@mail.com","password":"123456"})
```
> ### also you can update data with dictionary
```python
 DB().table("table_name").where('id',2).update({"username":"zed_magdy","password":"122222"})
 ```
> ### you can delete a record by using the following method
```python
  #find method takes 1 param wich is the "id"
  DB().table("table_name").find(1).delete()
  ```
  > # Open Source for life <3
