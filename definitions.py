import os

SAVE_PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
SEP_CSV = '\t'
PATH = r'<path_to_tsv_file_to_process>'
SEP_DF = '|'
DATE_COLUMNS = ['published_date', 'start_date', 'end_date_extension']
DROP_COLUMNS = ['outcome', 'second_place_outcome', 'atc', 'sku', 'pack_strength', 'active_ingredient']
DROP_ROWS = ['second_place_outcome']
PRICE_COLUMNS = ['winner_price ', 'second_place_price', 'maximum_price_allowed', 'participants_price']
AVOID_NORM = ['contract_id', 'duration', 'duration_extension', 
            'published_date_year', 'published_date_month', 'published_date_day', 'published_date_dayofweek',
            'start_date_year', 'start_date_month', 'start_date_day', 'start_date_dayofweek',
            'end_date_extension_year', 'end_date_extension_month', 'end_date_extension_day', 'end_date_extension_dayofweek'
                ]
