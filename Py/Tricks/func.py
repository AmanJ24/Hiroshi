import pandas as pd

df = {
    'House': ['Chenab', 'Ganga', 'Jamuna', 'Jhelum', 'Ravi', 'Satluj'],
    'First': [5, 10, 8, 12, 5, 10],
    'Second': [7, 5, 13, 9, 11, 5],
    'Third': [6, 4, 15, 12, 10, 3]
    }

data = pd.DataFrame(df)
print(data)
print(data['House'][(data['Second'] >= 12) and (data['Second'] <= 20)])