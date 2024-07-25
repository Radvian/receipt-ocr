import streamlit as st
from PIL import Image
from PIL import ImageOps
import pandas as pd
import time

# import asyncio

from utils.helper import detect_text, main_extract, extract_sim
from utils.prompt import sim_extract_prompt

def main():
    st.title("SIM OCR and Information Extraction")
    uploaded_file = st.file_uploader("Upload a .jpg photo of SIM", type=["jpg", "jpeg"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)

        col1.header("Uploaded SIM Image")
        # Display the uploaded image
        image = Image.open(uploaded_file)
        image = ImageOps.exif_transpose(image)
        #image = image.rotate(270, expand=True)
        col1.image(image, caption='SIM:', use_column_width=True)
        
        # Save the image to a temporary file
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Perform OCR on the image with loading spinner and timer
        with st.spinner('Performing OCR...'):
            start_time = time.time()
            ocr_result = detect_text("temp.jpg")
            end_time = time.time()
            st.success(f'OCR completed in {end_time - start_time:.2f} seconds')
        
        # Extract structured information from OCR result with loading spinner and timer
        with st.spinner('Extracting information...'):
            start_time = time.time()

            sim_dict = extract_sim(ocr_result, sim_extract_prompt, 'gpt-4o-mini')
            # st.write(receipt_info_list)

            end_time = time.time()
            st.success(f'Information extraction completed in {end_time - start_time:.2f} seconds')
        
        df = pd.DataFrame(sim_dict).transpose()
        col2.table(df)

if __name__ == "__main__":
    main()
