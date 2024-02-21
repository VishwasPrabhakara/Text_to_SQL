from langchain_help import get_few_shot_db_chain

import Streamlit as st

st.title("Atliq Tshirts: Database Chatbot")

question = st.text_input("Ask a question")
if question:
    chain = get_few_shot_db_chain()
    answer = chain.run(question)
    st.header("Answer")
    st.write(answer)