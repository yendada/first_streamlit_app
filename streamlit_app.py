#Created the main Python file.

import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')


streamlit.text('🥣 Omega 3 & Blueberry Oat meal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avacado Toast')


streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [ 'Pineapple', 'Cherries'] )
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)


# Get the Fruityvice Data Looking a Little Nicer:

# New section to display Fruityvice api response

streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


  
# Get the JSON version of the Fruityvice response and normalize it.
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Diplaying the normalized data in a data frame.
streamlit.dataframe(fruityvice_normalized)







