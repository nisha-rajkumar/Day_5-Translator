import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ✅ Set page config as the first Streamlit command
st.set_page_config(page_title="English to French Translator", page_icon="🌍")

# 🌐 App title and description
st.title("🌍 English to French Translator")
st.write("Translate any English sentence into French using **Google Gemini + LangChain**.")

# 🔐 Hardcoded Gemini API Key (keep this secret!)
API_KEY = "AIzaSyC_iRD_Ss1ayBXadgIIrHAoMKu2xoXkTFY"

# 📝 Input for English sentence
english_sentence = st.text_input("Enter an English sentence:")

# 📤 Translate button
if st.button("Translate"):
    if not english_sentence:
        st.warning("Please enter a sentence to translate.")
    else:
        try:
            # 🔗 Connect to Gemini model
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)

            # 🧠 Prompt template
            prompt = PromptTemplate(
                input_variables=["sentence"],
                template="Translate the following English sentence to French:\n\n{sentence}"
            )

            # 🔄 Create LLMChain
            chain = LLMChain(llm=llm, prompt=prompt)

            # 🚀 Run the translation
            result = chain.run(english_sentence)

            # ✅ Display result
            st.success("✅ Translated Successfully!")
            st.write("**French Translation:**")
            st.code(result.strip(), language="markdown")

        except Exception as e:
            st.error(f"Error: {e}")
