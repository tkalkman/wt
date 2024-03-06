print("hey allemaal! ik ga een csv file lezen, leuk he?")
import pandas as pd
df = pd.read_csv('pokemon.csv')
namen = df['Name']
