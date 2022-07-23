from sklearn.model_selection import StratifiedKFold
import pandas as pd

df = pd.read_excel('data_teeth.xlsx')
print(df.head())

kf = StratifiedKFold(4, shuffle=True, random_state=42)
fold = 0

#x = df.drop(' respondent')
y = df.loc[:, 'respondent']

i = 1
for train_index, test_index in kf.split(df, y):
    train = df.loc[train_index, :]
    test = df.loc[test_index, :]
    train_filename = 'train_split_' + str(i) + '.xlsx'
    test_filename = 'test_split_' + str(i) + '.xlsx'
    train.to_excel(train_filename, index=False)
    test.to_excel(test_filename, index=False)
    print("-------------------------")
    i += 1