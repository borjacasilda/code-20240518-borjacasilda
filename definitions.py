import os

# Directory to save processed files
SAVE_PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
# CSV file delimiter
SEP_CSV = '\t'
# Path to the TSV file to process
PATH = r'path/to_tsv_file/to_process'
# DataFrame column delimiter
SEP_DF = '|'
# Columns to convert to date-time format
DATE_COLUMNS = ['published_date', 'start_date', 'end_date_extension']
# Columns to drop from the DataFrame
DROP_COLUMNS = ['outcome', 'second_place_outcome', 'atc', 'sku', 'pack_strength', 'active_ingredient']
# Rows with NaN values in these columns will be dropped
DROP_ROWS = ['second_place_outcome']
# Columns related to prices for transformations
PRICE_COLUMNS = ['winner_price ', 'second_place_price', 'maximum_price_allowed', 'participants_price']
# Columns to exclude from normalization during preprocessing
AVOID_NORM = ['contract_id', 'duration', 'duration_extension', 
            'published_date_year', 'published_date_month', 'published_date_day', 'published_date_dayofweek',
            'start_date_year', 'start_date_month', 'start_date_day', 'start_date_dayofweek',
            'end_date_extension_year', 'end_date_extension_month', 'end_date_extension_day', 'end_date_extension_dayofweek'
                ]
# Targert variable to pass to the algorythm
TARGET = 'winner_price'
