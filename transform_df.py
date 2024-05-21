import numpy as np
import pandas as pd

def transform_df(df, drows, dcolumns, todt, fcols, threshold=2, del_drows_col=True, save_df=None):
    """
    Transforms a DataFrame by performing various operations such 
    as feature engineering, outlier removal, and type conversion.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to transform. 
    Output for the first step of the pipeline in main.py,
    df_parsed object.
    - drows (list): List of columns to check for NaN values and 
    drop rows containing them. Specified in definitions.py, DROP_ROWS.
    - dcolumns (list): List of columns to delete.
    Specified in definitions.py, DROP_COLUMNS.
    - todt (list): List of columns to convert to datetime and 
    extract date parts. Specified in definitions.py, DATE_COLUMNS.
    - fcols (list): List of columns to adjust values and filter 
    outliers based on z-scores. Specified in definitions.py,
    PRICE_COLUMNS
    - threshold (int, optional): The z-score threshold for outlier removal. 
    Defaults to 2.
    - del_drows_col (bool, optional): Whether to delete the columns 
    in drows after processing. Defaults to True.
    - save_df (str, optional): Path to save the transformed 
    DataFrame as a CSV file. If None, the DataFrame is not 
    saved. Defaults to None. Defined in the parameter as comment in
    main.py.

    Returns:
    - pd.DataFrame: The transformed DataFrame.
    """
    # Add binary columns 'winner' and 'second_place' based on price comparison
    df['winner'] = np.where(df['participants_price'] == df['winner_price'], 0, 1)
    df['second_place'] = np.where(df['participants_price'] == df['second_place_price'], 0, 1)
    # Drop rows with NaN values in specified columns
    df = df.dropna(subset=drows)
    # Adjust values and remove outliers in specified columns
    for column in fcols:
        # Scale values
        df[column] = np.where(df[column] < 1, df[column] * 1000, df[column])  
        # Calculate mean
        mean = df[column].mean()
        # Calculate standard deviation.
        std = df[column].std()
        # Calculate z-scores
        df['z_score'] = (df[column] - mean) / std 
        # Filter out outliers based on threshold
        df = df[np.abs(df['z_score']) <= threshold]  
    # Remove the temporary z-score column
    del df['z_score']  
    # Convert specified columns to datetime and extract date parts
    for to_dt_col in todt:
        df[to_dt_col] = pd.to_datetime(df[to_dt_col])
        df[to_dt_col + '_year'] = df[to_dt_col].dt.year
        df[to_dt_col + '_month'] = df[to_dt_col].dt.month
        df[to_dt_col + '_day'] = df[to_dt_col].dt.day
        df[to_dt_col + '_dayofweek'] = df[to_dt_col].dt.dayofweek
    # Determine columns to remove
    remove_columns = set()
    if del_drows_col:
        for lst in [drows, dcolumns, todt]:
            remove_columns.update(lst)
    else:
        for lst in [dcolumns, todt]:
            remove_columns.update(lst)
    # Drop specified columns
    for column_to_drop in remove_columns:
        del df[column_to_drop]
    # Save the transformed DataFrame to a CSV file if a save path is provided
    if save_df:
        df.to_csv(save_df, index=False)
    # Return the transformed DataFrame
    return df  
