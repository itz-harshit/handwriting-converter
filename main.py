import streamlit as st
import pywhatkit as kit
import os

# Function to convert text to handwritten text
def convert(text, font):
    try:
        kit.text_to_handwriting(text, save_to='hw.png', font=font)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app
def main():
    st.title("Text to Handwritten Text Converter")
    text = st.text_area("Enter the text")
    available_fonts = kit.get_available_fonts()
    font = st.selectbox("Select font style", available_fonts)
    if st.button("Convert"):
        if text:
            convert(text, font)
            st.success("Conversion complete!")
            st.image("hw.png")
            os.remove("hw.png")
        else:
            st.warning("Please enter some text.")

# Run the app
if __name__ == "__main__":
    main()
