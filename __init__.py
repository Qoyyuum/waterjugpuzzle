import streamlit as st
from app import Jug, JugsProblem

st.title("Welcome to Water Jug Problem!")
st.write("You will be presented with problems where you can fill, empty and transfer water volumes of each jug to reach the target goal.")
st.write("Problem: 1.\nThere are 2 jugs. Jug A has a maximum capacity of 3 litres and Jug B has 5 litres. Your target goal: How to get a jug with only 4 litres?")

jug_a = Jug("A", 0, 3)
jug_b = Jug("B", 0, 5)
jugs = [jug_a, jug_b]
problem_1 = JugsProblem(jugs=jugs, goal=4)
if "problem" not in st.session_state:
    st.session_state["problem"] = problem_1

def check():
    st.session_state["problem"].status()
    return [jug for jug in st.session_state.problem.jugs]

status = check()

col1, col2 = st.columns(2)
with col1:
    if st.button("Check if its solved"):
        if st.session_state["problem"].goalcheck():
            st.success("PROBLEM SOLVED!")
        else:
            st.error("PROBLEM NOT SOLVED!")
        check()

    fill_which_jug = st.selectbox("Which jug to fill?", [jug.name for jug in st.session_state["problem"].jugs])
    if st.button(f'Fill {fill_which_jug}'):
        result = st.session_state["problem"].fill(fill_which_jug)
        if result:
            st.success(f"Successfully filled {fill_which_jug}")
        else:
            st.error(f"Unable to fill {fill_which_jug}")
        check()

    empty_which_jug = st.selectbox("Which jug to empty?", [jug.name for jug in st.session_state["problem"].jugs])
    if st.button(f'Empty {empty_which_jug}'):
        result = st.session_state["problem"].empty(empty_which_jug)
        if result:
            st.success(f"Successfully emptied {empty_which_jug}")
        else:
            st.error(f"Unable to empty {empty_which_jug}")
        check()

    from_which_jug = st.selectbox("Transfer from which jug?", [jug.name for jug in st.session_state["problem"].jugs])
    to_which_jug = st.selectbox("Transfer to which jug?", [jug.name for jug in st.session_state["problem"].jugs])
    if st.button(f'Transfer {from_which_jug} to {to_which_jug}'):
        result = st.session_state["problem"].transfer(from_which_jug, to_which_jug)
        if result:
            st.success(f"Successfully transfered from {from_which_jug} to {to_which_jug}")
        else:
            st.error(f"Unable to transfer from {from_which_jug} to {to_which_jug}")
        check()

with col2:
    st.write(status)

