# code-20240518-borjacasilda

The proyect tries to meet the following task:

"Please cleanse and provide validated "winner_price" data. This will be
used in machine learning pipeline and winner_price is target variable,
it cannot contain any anomalies, invalid prices."

## 1. What automated approaches can you use?

### a. Identification and handling of missing values. 
I chose the column 'second_place_outcome' because if the value 
of this column is nan  means that there is only one price linked 
to the contract_id (participants_price = winner price).
I think this info is not very useful to the alg. to discern the right
price in a situation with multiple prices.

### b. Outlier Detection and Removal
To ensure that prices do not contain outliers that could distort 
the analysis, statistical methods such as z-score calculation can be used. 
This allows us to identify and remove prices that deviate significantly 
from the mean, thus filtering out anomalous data.
I chose threshold = 2, although the most general setting is 3, because
when I set this value there were still some anomalous values that did not agree 
with the rest of the prices, so I decided to reduce it further to make 
sure that the algorithm only receives prices within a logical range 
(for example maximum price allowed >= participants_price 
or maximum price allowed >= winner_price).

### c. Normalizing and Scaling Data
To facilitate the use of data in machine learning algorithms, 
it is crucial to normalize prices and other numerical values. 
This involves transforming the data to have a uniform scale, 
enhancing the accuracy of predictive models. The preprocessing_array (mainly) 
function aids in this task by applying standard normalization and 
scaling techniques. 
Over the numerical features to achive this I performed first a sclaing 
multiplyng by 1000, because I saw that most of the values showed were 
correct, and for the ones that it isn't
I chose threshold = 2 when I did a z-score validation, although 
the most general setting is 3, because when I set this value there 
were still some anomalous values that did not agree with the rest 
of the prices, so I decided to reduce it further to make 
sure that the algorithm only receives prices within a logical range 
(for example maximum price allowed >= participants_price 
or maximum price allowed >= winner_price).

### d. Encoding Categorical Data
Categorical data needs to be converted to a numerical format 
before being used in machine learning models. This can be achieved 
through techniques such as label encoding, allowing the inclusion 
of categorical information without losing its meaning. 
I performed for the categorical values a label enconder extracted 
from sklearn, and and one-hot-encoder in transform.py 
when I saw that the information about winner - loser (0 - 1) 
allowing me to remove some columns that express the same.

### e. Verifying and Converting Data Types
Ensuring that all data is in the correct format is essential. 
Converting columns to appropriate data types, 
such as converting strings to dates or numerical values, 
ensures data integrity and consistency. I transform at the end 
of preprocessing_array all the values to float, because most 
all the algorythims prefers float as data input.

### f. Pipeline Process
Combining these techniques in an automated workflow allows for efficient 
processing of large volumes of data. By using the expand_df, 
transform_df, and preprocessing_array functions, we can implement a pipeline 
that performs these tasks sequentially and automatically, ensuring that 
the final data is clean and ready for use in machine learning models.
The modules expand_df.py,preprocessing_array.py and save_output_dir 
(Complementary, out of the scope of this task) I tried to make them 
as scalable as possible.
Transform_df, is where I make more direct declarations to the dataset, 
when targeting specific columns outside definitions and therefore not 
scalable to other processes. 

## 2. What manual tasks would you perform?

The first thing to do is to make an eda to understand the peculiarities 
of the dataset. Below I detail the tasks that were significant in determining 
the actions to be taken:
- View the dimension of the dataset, columns and get general information 
(df.info, df.shape,  



## 3. How would you improve this process long term and how would you build your roadmap?


## 4. Would you change anything if you would need to scale this process from a few SKU's to hundreds and thousands.


