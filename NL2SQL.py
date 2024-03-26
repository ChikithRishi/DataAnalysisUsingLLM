import numpy as np
import pandas as pd
import sqlite3
import os

os.environ['OPENAI_API_KEY'] = 'sk-YOur open ai key'
df = pd.read_csv("C:/Users/chiki/Downloads/iris.csv")
print(df)

conn = sqlite3.connect('llm_db.sqlite')
c = conn.cursor()



c.execute('CREATE TABLE IF NOT EXISTS llm (sepal_length INT, sepal_width INT, petal_length INT, petal_width INT, variety varchar(20))')
conn.commit()

df.to_sql('llm', conn, if_exists='replace', index = False)

c.execute('''
SELECT  * from llm LIMIT 100
          ''')

for row in c.fetchall():
    print (row)

def read_sql_query(sql, db):
    import sqlite3
    read_sql_query('SELECT * FROM llm LIMIT 10;',
               "llm_db.sqlite")
    

from langchain import OpenAI, SQLDatabase
import langchain_experimental
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import OpenAI
input_db = SQLDatabase.from_uri('sqlite:///llm_db.sqlite')
llm_model = OpenAI(temperature=0)
db_agent = SQLDatabaseChain(llm = llm_model,
                            database = input_db,
                            verbose=True)
query=input("Enter your query?")
result=db_agent.invoke(query)
print(result)
db_agent.run("Average sepal length of setosa")
r=db_agent.run("Which species has highest sepal length ?")
print(r)
q4=db_agent.run("which species has lowest of sepal length, sepal width , petal length and width?")
print(q4)
    
