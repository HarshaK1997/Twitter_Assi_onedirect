#Database Implementation done here
#======== ============== ==== ====

import FetchData
from sqlalchemy import create_engine

print('\nStoring data to "sqlalchemy" database ...\n')

#establishing connection to database
db_url = "sqlite:///db.sqlite"
engine = create_engine(db_url)

#executing SQL commands
engine.execute('drop Table "URL";')
engine.execute('Create Table "URL" (url varchar);')

#first and last Strings are defined to pass the URL into insert command
first = 'Insert Into "URL" (url) values ("'
last = '");'

for url in FetchData.URL:
    insert = first+url+last
    engine.execute(insert)

#SQL command to retrieve data from database
result = engine.execute('Select * from "URL";')

#storing the result set inside the databaseResult variable of list type
databaseResult = []
for res in result:
    databaseResult.append(res)

#displaying fetched data from database
print("Fetched data from database -\n", databaseResult)
