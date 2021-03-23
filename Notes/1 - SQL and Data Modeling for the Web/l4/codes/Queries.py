from HelloApp import db, User
from sqlalchemy import func

# Implement a query to filter all users by name 'Bob'. 
print(User.query.filter_by(name='Bob').all())

# Implement a LIKE query to filter the users for records with a name that includes the letter "b". 
search = "%{}%".format('B')
print(User.query.filter(User.name.like(search)).all())

# Return only the first 3 records of the query above.
print(User.query.filter(User.name.like(search)).limit(3).all())

# Re-implement the LIKE query using case-insensitive search. 
search = search.lower()
print(User.query.filter(func.lower(User.name).like(search)).all())

# Return the number of records of users with name 'Bob'.
print(User.query.filter_by(name='Bob').count())
