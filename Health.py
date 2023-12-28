import streamlit as st
import google.generativeai as palm
import os


API_KEY = "AIzaSyBENpuEOg11XpaqRKGrL6hpY-bxGixnXEM"
palm.configure(api_key=API_KEY)

def main():
    st.header("Healthcare Guardians Bot👨‍⚕️🤖")
    st.write("")

    prompt = st.text_area("Ask your health-related query here...", height=150, max_chars=500)

    if st.button("SEND", use_container_width=True):
        model = "models/text-bison-001"    # This is the currently available model

        response = palm.generate_text(
            model=model,
            prompt=prompt,
            max_output_tokens=1024
        )

        st.write("")
        st.header(":blue[Response]")
        st.write("")

        filtered_response = filter_health_info(response.result)
        st.markdown(filtered_response, unsafe_allow_html=False, help=None)

def filter_health_info(response_text):

    general_health_keywords = [
        "health", "wellness", "disease", "nutrition", "exercise", 
        "mental health", "prevention", "medical advice", "symptoms", "treatments"
    ]

    if response_text and any(keyword in response_text.lower() for keyword in general_health_keywords):
        return response_text

    return "Sorry, the response is not directly related to general health information."

if __name__ == "__main__":
    main()