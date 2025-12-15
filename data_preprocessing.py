from typing import List
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import argparse

parser= argparse.ArgumentParser()
parser.add_argument("--path", "-p")
parser.add_argument("--target", "-t")

parsed= parser.parse_args()

le= LabelEncoder()
scaler= StandardScaler()

target_name= parsed.target
path= parsed.path
 

def read_dataset(path):
    return pd.read_csv(path)
   

def inspect_column(df):

    columns= list(df.columns)
    columns.remove(target_name)

    columns_to_drop= []
    columns_to_encode= []

    for column in columns:
        if df[column].nunique()==1:
            columns_to_append(column)

        elif (df[column].nunique() <=5) and (df[column].nunique() >= 1):
            columns_to_encode.append(column)

        else:
            df[column] = le.fit_transform(df[column])

    print("Columns_to_encode: ", columns_to_encode)
    print("Columns_to_drop: ", columns_to_drop)  

    df.drop(labels= columns_to_drop, axis=1, inplace=True) 
    df= pd.get_dummies(df, columns=columns_to_encode, prefix_sep="__",drop_first=True)                   

    return df
def do_scale(df):
    columns= list(df.columns)
    columns.remove(target_name)

    for column in columns:
        df[column]= scaler.fit_transform(df[[column]])

    return df    

def save_df(df):
    df.to_csv("output.csv")
    print("Saved!")

def main():
    df= read_dataset(path)
    df=inspect_column(df)
    df=do_scale(df)
    save_df(df)

    #df= save_df(do_scale(inspect_column(read_dataset(path))))
if __name__ == "__main__":
    main()   