from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import numpy as np

def preprocessing_array(df, avoid_norm, return_df=False, save_path=None):
    categorical_columns = []
    numerical_columns = []
    for column in df.columns:
        if df[column].dtype == 'object':
            categorical_columns.append(column)
        else:
            numerical_columns.append(column)
    numerical_subset = df[[column for column in numerical_columns if column not in avoid_norm]].copy()
    categorical_subset = df[categorical_columns].copy()
    transformed_subset = df[avoid_norm].copy()
    if not numerical_subset.empty:
        scaler = StandardScaler()
        numerical_subset = pd.DataFrame(scaler.fit_transform(numerical_subset), columns=numerical_subset.columns, index=numerical_subset.index)
    if not categorical_subset.empty:
        le = LabelEncoder()
        for column in categorical_subset.columns:
            categorical_subset[column] = le.fit_transform(categorical_subset[column])
    df_transformed = pd.concat([transformed_subset, categorical_subset, numerical_subset], axis=1)
    df_transformed = df_transformed.astype(float)
    ml_array = df_transformed.to_numpy()
    if save_path:
        df_transformed.to_csv(save_path, index=False)   
    if return_df:    
        return df_transformed
    else:
        return ml_array
