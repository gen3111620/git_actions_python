def preprocessing(df):
    sex_dict = {
        'male' : 0,
        'female' : 1
    }

    df['Sex'] = df['Sex'].fillna('')
    df['Sex'] = df['Sex'].apply(lambda x: sex_dict[x])
    return df
    


