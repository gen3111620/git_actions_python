import pandas as pd 
import lightgbm as lgb
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder

from preprocessing import preprocessing


df = pd.read_csv("train.csv")

print(df.tail(10))


lb = LabelEncoder()

y_col = 'Survied'


df = preprocessing(df)

cols = ['Pclass', 'Age', 'SibSp', 'Fare', 'Sex']
train_df = df.sample(frac=0.8, random_state=2022)
valid_df = df.drop(index=train_df.index).reset_index(drop=True)
train_df = train_df.reset_index(drop=True)


clf = lgb.LGBMClassifier()
clf.fit(train_df[cols], train_df['Survived'])
valid_preds = clf.predict(valid_df[cols])

print(roc_auc_score(valid_df['Survived'], valid_preds))
