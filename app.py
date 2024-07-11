import streamlit as st
from PIL import Image
from PIL import ImageOps
import pandas as pd
import time

# import asyncio

from utils.helper import detect_text, main_extract

def main():
    st.title("Receipt OCR and Information Extraction")
    uploaded_file = st.file_uploader("Upload a .jpg receipt", type=["jpg"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)

        col1.header("Uploaded Receipt")
        # Display the uploaded image
        image = Image.open(uploaded_file)
        image = ImageOps.exif_transpose(image)
        #image = image.rotate(270, expand=True)
        col1.image(image, caption='Receipt:', use_column_width=True)
        
        # Save the image to a temporary file
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Perform OCR on the image with loading spinner and timer
        with st.spinner('Performing OCR...'):
            start_time = time.time()
            ocr_result = detect_text("temp.jpg")
            end_time = time.time()
            st.success(f'OCR completed in {end_time - start_time:.2f} seconds')
        
        # st.write("OCR Result:", ocr_result)
        
        # Extract structured information from OCR result with loading spinner and timer
        with st.spinner('Extracting information...'):
            start_time = time.time()

            receipt_info_list = main_extract(ocr_result, selected_model_name='gpt-4o')
            # st.write(receipt_info_list)

            end_time = time.time()
            st.success(f'Information extraction completed in {end_time - start_time:.2f} seconds')
        
        item_info, payment_info, tenant_info = receipt_info_list[0], receipt_info_list[1], receipt_info_list[2]
            
        receipt_dictionary = {}
        receipt_dictionary.update(tenant_info)
        receipt_dictionary.update(item_info)
        receipt_dictionary.update(payment_info)

        df = pd.DataFrame(receipt_dictionary).transpose()
        col2.table(df)

        # # Validation
        # item_list_price_dictionary = receipt.item_list_price
        # for k in item_list_price_dictionary:
        #     try:
        #         item_list_price_dictionary[k] = int(item_list_price_dictionary[k].replace(',',''))
        #     except:
        #         item_list_price_dictionary[k] = int(item_list_price_dictionary[k])
        
        # receipt.item_list_price = item_list_price_dictionary
        # item_list_price_total = sum(item_list_price_dictionary.values())
        # col2.write(item_list_price_dictionary)
        # col2.write(f"Penjumlahan Harga Barang di Item List: {item_list_price_total}")

        # col2.write(""" 
        # ### Validasi penjumlahan masing-masing item dan sub-total
        # """)
        # if item_list_price_total > receipt.sub_total:
        #     col2.write("Sub Total lebih kecil dari penjumlahan harga barang yang di-ekstrak. Kemungkinan besar ini bukan fraud.")
        # elif item_list_price_total < receipt.sub_total:
        #     col2.write("Sub Total lebih besar dari penjumlahan harga barang yang ter-ekstrak. Bisa jadi fraud, silakan dicheck kembali.")
        # else:
        #     col2.write("Sub Total sama dengan penjumlahan harga barang yang ter-ekstrak.")

        # col2.write(""" 
        # ### Validasi sub-total dengan 'final' total
        # """)
        # if receipt.sub_total + receipt.service + receipt.pb1_tax - receipt.discount == receipt.total_paid:
        #     col2.write("Sub Total + Service + PB1 Tax = Total Paid")
        # else: 
        #     if receipt.sub_total == receipt.total_paid:
        #         col2.write("Sub Total samadengan Total Paid")
        #     else:
        #         difference_total = receipt.sub_total + receipt.service + receipt.pb1_tax - receipt.total_paid
        #         col2.write("Sub Total + Service + PB1 Tax =/= Total Paid")
        #         col2.write(f"Sub Total: {receipt.sub_total}\nService: {receipt.service}\nPB1 Tax: {receipt.pb1_tax}")
        #         col2.write(f"Total Paid: {receipt.total_paid}")
        #         col2.write(f"Selisih (Sub Total + Service + PB1 Tax - Total Paid): {difference_total}")


if __name__ == "__main__":
    main()
