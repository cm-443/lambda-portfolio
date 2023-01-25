import pandas as pd

def lambda_handler(event, context):
    data = {'name': ['John', 'Jane', 'Mike'],
            'age': [30, 25, 35]}
    df = pd.DataFrame(data)
    df.to_csv('example.csv', index=False)
    print(df)