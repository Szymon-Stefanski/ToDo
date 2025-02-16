from operator import index

import streamlit
from streamlit import checkbox

import options


tasks = options.show()

def add_task():
    task = streamlit.session_state["new_task"]
    tasks.append(task)
    options.add(task)

streamlit.title("Todo:")
streamlit.subheader("This is my app.")
streamlit.write("This app is to increase your productivity.")


for task in tasks:
    checkbox = streamlit.checkbox(task, key=task)
    if checkbox:
        tasks.remove(task)
        options.delete(task)
        streamlit.session_state.pop(task, None)
        streamlit.rerun()

streamlit.text_input(label="New Task", placeholder="Enter your task:",
                     on_change=add_task, key='new_task', label_visibility="hidden")