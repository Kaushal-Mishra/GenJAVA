

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCGwtv94hX3XGsTzJ57h3zU_zLE-0M4Vgk"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_code(task_description):
    template = f"""
        {task_description}

        Write Java code to achieve the task described above.
    """
    response = model.generate_content(template)
    java_code = response.text
    java_code = java_code.replace("```java", "").rstrip("```")
    return java_code

def main():
    st.set_page_config(page_title="Java Program Generator", page_icon="🚀")
    st.markdown(
        """
            <div style="text-align:center;">
                <h1>Java Program Generator</h1>
                <h3>I can generate Java codes for you!</h3>
            </div>
        """,
        unsafe_allow_html=True,
    )

    task_description = st.text_area("Describe the Program:")

    submit = st.button("Generate Java Code")

    if submit:
        with st.spinner("Generating Java Program Code..."):
            java_code = generate_code(task_description)

            with st.container():
                st.success("Java Code Generated! Here is your code:")
                st.code(java_code, language="Java")

if __name__ == "__main__":
    main()