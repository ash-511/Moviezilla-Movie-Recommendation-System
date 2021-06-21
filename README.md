# FreshMart - Online Grocery Mart
## *Problem Statement:* 
From Amazon Prime to Netflix, the need for a robust recommendation system is extremely necessary given the amount of personalised content consumed by the users of these platforms. Moviezilla is a movie recommendation system that aims to provide users personalised movie recommendations based on a range of various attributes, be it genres, cast or overview, making it a user-friendly and hassle-free experience for consumers.

## *Project Scope:*
The proposed system aims to provide users with personalized recommendations on receiving a movie input from the user. This is done using machine learning algorithms and the
Content Based Filtering approach. Users are presented with top movies on the platform, receive movie recommendations based on genre, cast, overview, etc. and are even provided with the option to wishlist a movie they like to watch later.

## *Key Features:*
* **Recommendation Basis:**
In the Recommendation feature, the recommendations can be done on the basis of Movie name and  User’s favourite Actors. The Recommendation Model works on the basis of Cosine Similarity.
* **Wishlist Movies:** 
We provide the user with a facility to wishlist the movies they want to save on their User profile page and these movies are recorded in the wishlist Database.
* **Trending Movies:**
In this feature, with the help of EDA done on the dataset, we determine top 3 movies according to the popularity attribute and display those in the Treding movies section on the Dashboard.
* **User’s Favourites Section:**
In this feature,  we ask the user to select their favorite genres during Signup and we use the stored data to display movies from the User’s favourite genres on their Dashboard.

## *Technologies Used:*
Python 3.6, Django, HTML/CSS, Bootstrap 4, TMDB API

## *Team members:*
* Aiswarya Suresh - 1814122
* Shreya Ughade - 1814116
* Rhutuja Thakur - 1814128 
* Sukhada Virkar - 1814119

## *To run this project:*
In command prompt, enter the command:
python manage.py runserver

The following URL would be shown : http://127.0.0.1:8000/   

which on clicking, would redirect you to the Moviezilla Home page.
