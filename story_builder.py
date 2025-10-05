import streamlit as st
import time

with st.sidebar:
    page = st.radio("make or read", ["Make", 'Read'])

if page == "Make":
    with st.form("my_form"):
        lang = st.text_input("What language is this for?")
        name = '# ' + st.text_input("Enter the name of your story:")
        story = st.text_area("Enter story:")
        submitted = st.form_submit_button("Submit")

    if submitted:
        text = f"""{name}
{story}"""
        st.download_button(
        label="Download Story",
        data=text,
        file_name=f"{lang}_{name[2:].replace(' ', '_')}.txt",
        mime="text/plain"
    )
elif page == "Read":
    st.markdown("#### The error message goes away once you upload a file")
    book = st.file_uploader("upload story", type='txt', accept_multiple_files=False)
    container = st.container(border=True)
    for line in book:
        if line[0:13] == b'<writeAnswer>':
            words = line[13:].decode('utf-8').split()
            answer = st.text_input(f"What is: {words[0]}")
            if answer == words[1]:
                st.success("Well done!")
        else:
            st.markdown(line.decode('utf-8'))
