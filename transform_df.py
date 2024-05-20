def transform_df(df, drows, dcolumns, todt, fcols, threshold=2, del_drows_col=True, save_df=None):
    df['winner'] = np.where(df['participants_price'] == df['winner_price'], 0, 1)
    df['second_place'] = np.where(df['participants_price'] == df['second_place_price'], 0, 1)
    df = df.dropna(subset=drows)
    for column in fcols:
        df[column] = np.where(df[column] < 1, df[column] * 1000, df[column])
        mean = df[column].mean()
        std = df[column].std()
        df['z_score'] = (df[column] - mean) / std
        df = df[np.abs(df['z_score']) <= threshold]
    del df['z_score']
    remove_columns = set()
    for to_dt_col in todt:
        df[to_dt_col] = pd.to_datetime(df[to_dt_col])
        df[to_dt_col + '_year'] = df[to_dt_col].dt.year
        df[to_dt_col + '_month'] = df[to_dt_col].dt.month
        df[to_dt_col + '_day'] = df[to_dt_col].dt.day
        df[to_dt_col + '_dayofweek'] = df[to_dt_col].dt.dayofweek
    if del_drows_col:
        for l in [drows, dcolumns, todt]:
            remove_columns.update(l)
    else:
        for l in [dcolumns, todt]:
            remove_columns.update(l)
    for column_to_drop in remove_columns:
        del df[column_to_drop]
    if save_df:
        df.to_csv(save_df, index=False)
    return df
