import pandas as pd

file = '../../00 docs/data/vgsalesGlobale.csv'
games = pd.read_csv(file, index_col='Name')

# print(games.head())
# print(games.tail(10))
# print(len(games))
# print(games.shape)
# print(games.dtypes)
# print(games.iloc[299])
print(games.loc['Super Mario Bros.'])