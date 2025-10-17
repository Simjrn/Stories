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
    book = st.file_uploader("upload story", type='txt', accept_multiple_files=False)
    if book:
        for line in book:
            if line[0:13] == b'<writeAnswer>':
                words = line[13:].decode('utf-8').split()
                answer = st.text_input(f"What is: {words[0]}")
                if answer == words[1]:
                    st.success("Well done!")                
                else:
                    if answer:
                        st.error(f"No, try {words[1]}")
                        break
                    else:
                        break
            elif line[0:11] == b'<writeTran>':
                words = line[11:].decode('utf-8').split()
                answer = st.text_input(f"What does '{words[0]}' mean?")
                if answer == words[1]:
                    st.success("Well done!")                
                else:
                    if answer:
                        st.error(f"No, try {words[1]}")
                        break
                    else:
                        break
            elif line[0:10] == b'<tranSent>':
                line = line.decode('utf-8')
                pos = line.find("|")
                term = line[11:pos]
                tran = line[pos:]
                answer = st.text_area(f"What is: {term}")
                if answer == tran:
                    st.success("Well done!")                
                else:
                    if answer:
                        st.error(f"No, try {tran}")
                        break
                    else:
                        break
            else:
                st.markdown(line.decode('utf-8'))
