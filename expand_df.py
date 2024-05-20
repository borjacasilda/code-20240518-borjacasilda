import pandas as pd

def expand_df(df_path, s, save_df:os.path=None):
    xplode_columns = []
    df = pd.read_csv(df_path, sep=SEP)
    for column in df.columns:
        for row, value in enumerate(df[column]):
            if isinstance(value, str) and s in value:
                xplode_columns.append(column)
                df.at[row, column] = list(value.split(s))
    xplode_columns = list(set(xplode_columns))
    xplode_df = df.explode(xplode_columns)
    xplode_df.reset_index(drop=True, inplace=True)
    for column in xplode_df.columns:
        if column in xplode_columns:
            try:
                xplode_df[column] = xplode_df[column].apply(lambda x: float(x))
            except:
                continue
    if save_df:
        xplode_df.to_csv(save_df, index=False)
    return xplode_df
