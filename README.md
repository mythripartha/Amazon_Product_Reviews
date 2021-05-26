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
For the EDA section, I mainly wanted to see the patterns of how different features were related. For example, I wanted to see how many of each star rating there was for each type of product and I wanted to see the distribution of ratings for each star rating. The data was very skewed at first because there were way more 5 star reviews than there were 1,2,3, and 4.
!![star_ratings_all_prods](https://user-images.githubusercontent.com/72578347/119587481-67d8c100-bd94-11eb-80b3-acff8733b16e.png)
