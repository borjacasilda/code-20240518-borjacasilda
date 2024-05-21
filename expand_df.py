import pandas as pd

def expand_df(df_path, s, sept=None, save_df=None):
    """
    Expands a DataFrame by splitting string entries 
    in specified columns.

    Parameters:
    - df_path (str): Path to the input CSV file 
    (TSV in example case). Not specified in definitions.py
    
    - s (str): Delimiter used to split string values 
    within the cells. Specified for the Pipeline in
    definitions.py, SEP_CSV
    - sept (str, optional): Delimiter for reading the CSV file. 
    Defaults to None, which implies auto-detection by pandas.
    Specified for the Pipeline in definitions.py,
    - save_df (str, optional): Path to save the expanded DataFrame 
    as a CSV file. If None, the DataFrame is not saved. 
    Defaults to None. Specified in main.py as 

    Returns:
    - pd.DataFrame: The expanded DataFrame with split values 
    exploded into separate rows.
    """
    
    # List to track columns that will be exploded
    xplode_columns = []
    # Read the CSV file into a DataFrame
    df = pd.read_csv(df_path, sep=sept)
    # Iterate through each column and row to find and 
    # split values containing the delimiter
    for column in df.columns:
        for row, value in enumerate(df[column]):
            # Check if the cell contains the delimiter
            if isinstance(value, str) and s in value:
                # Add column to list of columns to be exploded
                xplode_columns.append(column)
                # Split the cell value
                df.at[row, column] = list(value.split(s))  
    # Remove duplicates from the list of columns to be exploded
    xplode_columns = list(set(xplode_columns))
    # Explode the DataFrame
    xplode_df = df.explode(xplode_columns)  
    # Reset index after explosion
    xplode_df.reset_index(drop=True, inplace=True)  
    # Convert split values to float where applicable
    for column in xplode_df.columns:
        if column in xplode_columns:
            try:
                xplode_df[column] = xplode_df[column].apply(lambda x: float(x))
            except ValueError:
                # Skip conversion if value cannot be converted to float
                continue  
    # Save the expanded DataFrame to a CSV file if a save path is provided
    if save_df:
        xplode_df.to_csv(save_df, index=False)
    # Return the expanded DataFrame
    return xplode_df  
