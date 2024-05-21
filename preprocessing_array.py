from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import numpy as np

def preprocessing_array(df, avoid_norm, target, return_df=True, save_path=None):
    """
    Preprocesses a DataFrame by normalizing numerical columns, 
    encoding categorical columns, and returning the result as either a 
    DataFrame or a NumPy array.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to preprocess. Specified in
    main.py as df_trans as output from the step 2 of the pipeline.
    - avoid_norm (list): List of columns to exclude from normalization.
    Specified in definitions.py as AVOID_NORM.
    - return_df (bool, optional): Whether to return a DataFrame instead 
    of a NumPy array. Defaults to False. 
    - save_path (str, optional): Path to save the preprocessed DataFrame 
    as a CSV file. If None, the DataFrame is not saved. Defaults to None.

    Returns:
    - pd.DataFrame or np.ndarray: The preprocessed DataFrame or NumPy array.
    """

    # empty lissts to clasify the features of the dataframe
    categorical_columns = []
    numerical_columns = []
    # Separate columns into categorical and numerical
    for column in df.columns:
        if df[column].dtype == 'object':
            categorical_columns.append(column)
        else:
            numerical_columns.append(column)
    # Select numerical columns that are not in the avoid_norm list creating
    # a subset from df dataframe.
    numerical_subset = df[[column for column in numerical_columns if column not in avoid_norm]].copy()
    categorical_subset = df[categorical_columns].copy()
    transformed_subset = df[avoid_norm].copy()
    # Normalize numerical columns
    if not numerical_subset.empty:
        scaler = StandardScaler()
        numerical_subset = pd.DataFrame(scaler.fit_transform(numerical_subset), columns=numerical_subset.columns, index=numerical_subset.index)
    # Encode categorical columns
    if not categorical_subset.empty:
        le = LabelEncoder()
        for column in categorical_subset.columns:
            categorical_subset[column] = le.fit_transform(categorical_subset[column])
    # Concatenate all subsets
    df_transformed = pd.concat([transformed_subset, categorical_subset, numerical_subset], axis=1)
    # Ensure all data is float type
    df_transformed = df_transformed.astype(float) 
    # Save the preprocessed DataFrame if save_path is provided
    if save_path:
        df_transformed.to_csv(save_path, index=False)
    # Return the transformed DataFrame or NumPy array based on return_df flag
    if return_df:
        return df_transformed
    else:
        # empty list to store the numpy arrays
        ml_arrays_list = []
        # Creation of target variable numpy array
        X = df_transformed[target].to_numpy()
        # Append X to l_arrays_list
        ml_arrays_list.append(X)
        # Get the features without the target var
        del df_transformed[target]
        # Creattion of features arrays
        y = df_transformed.to_numpy()
        # Append y to l_arrays_list
        ml_arrays_list.append(y)
        return ml_arrays_list

