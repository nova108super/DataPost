import pandas as pd

df = pd.read_sql(
    sql='SELECT * FROM users',  
    con=,  
)

print(df)