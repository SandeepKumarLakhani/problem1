import streamlit as st
import openai
import os

# Setup
st.set_page_config(page_title="Auto Email Reply Generator", layout="wide")
st.title("📧 Auto Email Reply Generator (Gemini-powered)")

# Input form simulation
st.subheader("✍️ Paste User's Form Input Below:")
user_query = st.text_area("Customer message or query", height=200)

# Gemini API Key (enter your API key securely)
api_key = st.text_input("🔐 Gemini API Key", type="password")
os.environ["GOOGLE_API_KEY"] = api_key

# Reply generation logic
# Reply generation logic
if st.button("Generate Reply"):
    if not api_key or not user_query:
        st.warning("Please enter both API key and customer input.")
    else:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        # ✅ Fixed multiline f-string
        prompt = f"""Write a professional, friendly email reply to this customer message:

{user_query}"""
        
        try:
            response = model.generate_content(prompt)
            reply = response.text
            st.success("Generated Email Reply:")
            st.text_area("Reply", value=reply, height=200)
        except Exception as e:
            st.error(f"Error: {e}")

