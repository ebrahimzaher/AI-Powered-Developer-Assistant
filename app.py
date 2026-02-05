import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Python Dev Assistant", page_icon="💻")
st.title("👨‍💻 Senior Python Developer Assistant")
st.markdown("Powered by **Groq** & **Llama-3**")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ Error: GROQ_API_KEY not found in .env file!")
    st.stop()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Senior Software Engineer named 'PyBot'. Explain concepts clearly and simply. You can talk Arabic if I wrote Arabic"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

user_question = st.text_area("Ask your coding question here:", height=150, placeholder="E.g., How do I use decorators in Python?")

if st.button("Get Answer 🚀"):
    if user_question:
        with st.spinner("Thinking..."):
            try:
                response = chain.invoke({"question": user_question})
                st.markdown("### 💡 Answer:")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a question first!")