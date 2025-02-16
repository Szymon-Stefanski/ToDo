import streamlit
import options

tasks = options.show()

streamlit.title("Todo:")
streamlit.subheader("This is my app.")
streamlit.write("This app is to increase your productivity.")


for task in tasks:
    streamlit.checkbox(task)

streamlit.text_input(label="", placeholder="Enter your task:")