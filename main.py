import pandas as pd 
import lightgbm as lgb
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("train.csv")

print(df.tail(10))


lb = LabelEncoder()

y_col = 'Survied'

df['Sex'] = df['Sex'].fillna('')

sex_dict = {
    'male' : 0,
    'female' : 1
}
df['Sex'] = df['Sex'].apply(lambda x: sex_dict[x])


cols = ['Pclass', 'Age', 'SibSp', 'Fare', 'Sex']
train_df = df.sample(frac=0.8)
valid_df = df.drop(index=train_df.index).reset_index(drop=True)
train_df = train_df.reset_index(drop=True)


clf = lgb.LGBMClassifier()
clf.fit(train_df[cols], train_df['Survived'])
valid_preds = clf.predict(valid_df[cols])

from sklearn.metrics import roc_auc_score
print(roc_auc_score(valid_df['Survived'], valid_preds))