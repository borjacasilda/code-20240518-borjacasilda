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
(df.info, df.shape, df.describe, df.column.unique, etc)
- With Matplotlib (Or directly with Pandasor with Seaborn) create histograms 
for the numerical columns (Basically all price dolumns) to get insigths about 
the distribution of the columns, specially if doesn't follow a Normal distribution
to apply Normalization techniques such Standard Scaler, min max, etc.
- Perform assert df['column_price'].min() >= 0 to detect if there are negative
values in the price coluns. I do this because there cannot be negative prices in 
the columns containing prices, if so you have to see if a transformation can be 
performed to correct it and if not eliminate them. This can be done with a 
pandas mask too.
- Apply over the columns a df['winner_price'].isnull().sum(), to determine the amount 
of null values that there are per column to determine if we can fill the nan values
with a value like the mean, or directly if there are a huge number of null´s, drop 
the column.
- Determine with the z-score (IQR can be applied too) the possible outliers to 
see what to do wit them. If they are representative we can leave them, but if they are 
not and they will mess up the distribution we should remove them. 
It could also be determined with graphical representations through a violinplot or 
a boxplot if we want to observe these outliers in a more graphical way.


## 3. How would you improve this process long term and how would you build your roadmap?
In the long term, I would begin by incorporating a correlation analysis for the columns, 
which is an important step I overlooked initially. This will help us better understand 
the relationships between variables. Additionally, I would work on standardizing the 
second module, transform.py, to enhance its scalability across different datasets managed 
by our team. This involves refining its architecture to ensure it can be easily adapted 
for various data scenarios.
Given the low number of observations in the current dataset, it would also be beneficial to 
develop a process for generating synthetic observations. This synthetic data can be particularly 
useful for training algorithms when dealing with sparse datasets, thereby improving the robustness 
and reliability of our models.


## 4. Would you change anything if you would need to scale this process from a few SKU's to hundreds and thousands.
Absolutely. Scaling the process from a few SKUs to hundreds or thousands requires several 
adjustments. Firstly, I would retain the columns (All the columns that I identify as 
contants, nvalues = 1, I dropped it) related to the product itself,  as we will be dealing 
with multiple SKUs, each potentially having its own distinct optimal price. Additionally, 
I would examine whether the SKU-related characteristics 
in the dataset, such as the quantity of the active ingredient, provide valuable 
information that can enhance our analysis.
If the number of SKUs increases significantly, it may be necessary to add more features 
to our dataset. In such cases, I would apply techniques like Principal Component Analysis 
(PCA) or other dimensionality reduction algorithms to manage the increased complexity 
efficiently. 
Moreover, I would review the methods used to handle missing values (NaNs) to ensure they 
remain appropriate as the dataset grows in size and complexity. By continuously evaluating 
and adapting these aspects, we can maintain the accuracy and effectiveness of our process 
as it scales.

