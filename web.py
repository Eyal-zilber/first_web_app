import streamlit as st
import functions

todos =functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)



st.title("my to do apps")
st.subheader ("this is my to do app")
st.write ("eyal")

for index, todo in  enumerate (todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label = "enter to do" ,on_change= add_todo , key = "new_todo")