import os
from save_output_dir import save_output_dir
from expand_df import expand_df
from transform_df import transform_df
from preprocessing_array import preprocessing_array
from definitions import SAVE_PATH_ROOT, SEP, PATH, DATE_COLUMNS, DROP_COLUMNS, DROP_ROWS, AVOID_NORM

save = False
if save:
    save_path = save_output_dir(root=SAVE_PATH_ROOT)
else:
    save_path=None

def main():
    df_parsed = expand_df(
        df_path=PATH,
        sept=SEP
        s=SEP,
        #save_df=os.path.join(save_path, 'df_parsed.csv')
        ) 
    df_trans = transform_df(
        df=df_parsed,
        drows=DROP_ROWS,
        dcolumns=DROP_COLUMNS,
        fcols=PRICE_COLUMNS,
        todt=DATE_COLUMNS,
        #save_df=os.path.join(save_path, 'df_trans.csv')
        )
    alg_array = preprocessing_array(
        df=step_2_prep_df,
        avoid_norm=AVOID_NORM),
        #return_df=os.path.join(save_path, 'alg_array.csv')
        )

if __name__ == '__main_':
    main()
