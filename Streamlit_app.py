import matplotlib.pyplot as plt
import requests
import streamlit as st
from io import BytesIO
from PIL import Image
from predict import predict_flower

def main():
    st.set_page_config(page_title="FlowerResNet",
                   page_icon="🔮",
                   )
    
    st.title('Flower Image Prediction')

    # Create sidebar
    st.sidebar.title('Choose Image Source')
    image_source = st.sidebar.radio('Select Image Source:', ('Upload', 'URL'))

    # Create theme selection in the sidebar
    st.sidebar.title('Choose Theme')
    theme = st.sidebar.selectbox('Select Theme:', ('Light', 'Dark'))

    # Set the theme based on the user's selection
    if theme == 'Dark':
        st.markdown(
            """
            <style>
            body {
                color: white;
                background-color: #262730;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    if image_source == 'Upload':
        uploaded_file = st.sidebar.file_uploader('Choose an image file', type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)

            st.image(image, caption='Uploaded Image', use_column_width=True, width=300)

            # Predict button in the sidebar
            if st.sidebar.button('Predict'):
                flower_name = predict_flower(image)
                st.success(f'Predicted Flower: {flower_name}')

    elif image_source == 'URL':
        image_url = st.sidebar.text_input('Enter Image URL:')
        if st.sidebar.button('Predict'):
            try:
                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))

                st.image(image, caption='Image from URL', use_column_width=True, width=300)

                flower_name = predict_flower(image)
                st.success(f'Predicted Flower: {flower_name}')

            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == '__main__':
    main()