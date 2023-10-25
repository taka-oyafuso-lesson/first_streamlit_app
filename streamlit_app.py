import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.title('Breakfast Faborites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# pandas 
import pandas
# S3 バケットから CSV ファイルを読み取り
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# ここに選択リストを置き、含めたい果物を選択できるようにしましょう。
# Let's put a pick list here so they can pick the fruit they want to include 
# 顧客が選択する果物に基づいてテーブル データをフィルタリングしたいので、顧客に例を示すためにリストを事前に設定します。 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# テーブルデータをフィルタリングする
fruits_to_show = my_fruit_list.loc[fruits_selected]

# ページにテーブルを表示します。
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
#テキスト入力ボックスを追加し、API 呼び出しの一部として入力を Fruityvice に送信します
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# Python パッケージ ライブラリを導入 リクエスト
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# json成形
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# 成形したjsonを表示
streamlit.dataframe(fruityvice_normalized)


