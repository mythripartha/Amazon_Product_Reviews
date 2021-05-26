# Amazon_Product_Reviews
Capstone Project 3
Amazon is widely used to purchase several types of products. Amazon has revolutionized techmology with its electronics, review system, and many more features and services. My goal is to create a model where we can predict the star rating/whether the review is positive or negative using natural language processing techniques.
## Data Acquisition
I found the datasets on dataworld and they were collected by datafiniti (a database with information about several products, businesses and property listings from all corners of the internet)
https://data.world/datafiniti/consumer-reviews-of-amazon-products
![image](https://user-images.githubusercontent.com/72578347/119586134-ba64ae00-bd91-11eb-9757-8b57a9b7db05.png)
## Data Cleaning
I primarily observed where missing values occurred, dropped rows with several missing values, dropped columns that were not necessary in predicting ratings, then renamed columns so they would be easier to code with. The categories were also mislabelled, so I tokenized the names of the products and wrote conditional statements to see if certain words were contained in the name, if they were, the category would be changed to something like tablet, fire TV, personal assistant, etc.
## Exploratory Data Analysis
For the EDA section, I mainly wanted to see the patterns of how different features were related. For example, I wanted to see how many of each star rating there was for each type of product and I wanted to see the distribution of ratings for each star rating. The data was very skewed at first because there were way more 5 star reviews than there were 1,2,3, and 4 (resampling was done in the pre-processing/modeling step)
![star_ratings_all_prods](https://user-images.githubusercontent.com/72578347/119587481-67d8c100-bd94-11eb-80b3-acff8733b16e.png)
## Preprocessing
I resampled the data to make the dataset more balanced, so that the models would not have an excess of five star reviews flooded in. Balanced data will increase the model's predictive power. I used an undersampling method and selected random indices from the 3, 4, and 5 ratings to make the dependent variable even.![ratings_even](https://user-images.githubusercontent.com/72578347/119590144-d2d8c680-bd99-11eb-8586-a5b57b3905c2.png)

My main factor in predicting the rating would be the text of the review, I then performed text preprocessing by making the reviews lower case, removing special characters, and extra spaces. I opted to leave the stopwords in as words like "not" are very important in deciding whether or not reviews are positive. I then created my independent and dependent variables, for X (independent), I ran the reviews into a TF-IDF vectorizer and y was just the star ratings, I created 2 more datasets, one wherein all the star ratings had the same amount of reviews and another in which the reviews were classified as either positive (contained 4 and 5 star reviews and was denoted with the number 1) or negative (contained 1 and 2 star ratings and was denoted with a 0). My test set was about 0.25 while training was 0.75
## Modeling
I created models for the 3 separate datasets to see their prediction power. I started out with the first dataframe and performed LinearSVC (other models could not be computed with Jupyter). Then I completed 
