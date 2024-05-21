import os
from save_output_dir import save_output_dir
from expand_df import expand_df
from transform_df import transform_df
from preprocessing_array import preprocessing_array
from definitions import SAVE_PATH_ROOT, SEP_CSV, SEP_DF, PATH, DATE_COLUMNS, DROP_COLUMNS, DROP_ROWS, AVOID_NORM, PRICE_COLUMNS

# Flag to determine whether to save the processed DataFrames and arrays
save = False
if save:
    save_path = save_output_dir(root=SAVE_PATH_ROOT)
else:
    save_path = None

def main():
    """
    Main function to execute the data pipeline workflow. 
    It expands, transforms, and preprocesses the DataFrame, 
    and optionally saves the results.
    """
    # Expand the DataFrame by splitting specified columns and 
    # exploding rows
    df_parsed = expand_df(
        df_path=PATH,
        sept=SEP_CSV,
        s=SEP_DF,
        # Uncomment to save the expanded DataFrame
        # save_df=os.path.join(save_path, 'df_parsed.csv')  
    )
    # Transform the DataFrame by cleaning, feature engineering, and 
    # removing outliers
    df_trans = transform_df(
        df=df_parsed,
        drows=DROP_ROWS,
        dcolumns=DROP_COLUMNS,
        fcols=PRICE_COLUMNS,
        todt=DATE_COLUMNS,
        # Uncomment to save the transformed DataFrame
        # save_df=os.path.join(save_path, 'df_trans.csv')  
    )
    # Preprocess the DataFrame by normalizing numerical columns, encoding 
    # categorical columns, and converting to a NumPy array
    alg_array = preprocessing_array(
        df=df_trans,
        avoid_norm=AVOID_NORM,
        return_df=False,
        # Uncomment to save the preprocessed array
        # save_path=os.path.join(save_path, 'alg_array.csv')  
    )

if __name__ == '__main__':
    main()

