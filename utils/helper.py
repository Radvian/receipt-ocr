import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional, Union
import openai
from openai import OpenAI, AsyncOpenAI
import instructor
from google.cloud import vision
from .prompt import input_prompt_item_price_info, input_prompt_payment_info, input_prompt_tenant_info
import streamlit as st
# import asyncio
from google.oauth2 import service_account
import json

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Initialize OpenAI and Google Vision clients
openai_client = OpenAI()
instructor_client = instructor.from_openai(openai_client)

def numberstring_convert(numstring):
    if type(numstring) == str:
        if numstring == '':
            return 0
        else:
            numstring_new = numstring.replace(",","")
            numstring_new = int(float(numstring_new))
    else:
        numstring_new = numstring
    
    return numstring_new

def detect_text(path):
    credentials={
      "type": "service_account",
      "project_id": "boxwood-diagram-426306-s3",
      "private_key_id": "08d2ae3cca77c6c2e3d0ca4aaa0f48a59bd122c2",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQDUeMzPURzAh3jn\nUMVOlO/2JiWnlluYR0AUiMDBA6xHCSxXNt6rgHN7ADI++5zhkjdyEUgn0IUzEyXX\nGzNHNvWY0mPDqp75giQ6k0FeIsVpidnMWW9i1I6vIH/dhwjnZ2Eb+10SH/Diun58\nxc4DROS+mwbxWrhu0z2fGYJniCGf/ktflk9b9gn6ICHsq9WNF3V7tsTKageYKoVO\nlPkKustbd+HZ9QRhPdBzs8H6SZxUHt2q6XCJ6GOTN3JsaFWw79RbNHGCRfL1d424\nJBknYXmAFujO6RMZYAxP46MaH9qcM+2Q4eFOwvFMRttoh8+e9N7AJxVBCE5VtUCi\nhlGrfM7vAgMBAAECggEABAQJ0EahhdIJqvWP2nMI21zP4WGqIYVXOgwg+ITv600f\nwBY9ZyhqW6zJRlTNxkWpM/K3q75Ohi9FISerycYe0OCeb22jdjvLdiqfqv56lLVn\nnxZ2+yXhUdYKFKR0uqBC6ZslSy5nXcxV5QMoEvppCGE4ZF9pP6RRHyywQPIFu1cI\n6rt7vucRqjN7/CYL7/OBsMJq21oWAWhG91scn7HR7C4reXKwJEPL3L+JrGEkPBeg\npdykAxUax2ek0CIak/0LYiU8hmwL0PRHvEOyFTpJFPoTXGzqZ3Ed2JKW38l/sTYb\n/Z4gAidDrLvBMbJdILUHqcocM1Ltcm2K4MDQZOdyoQKBgQDzSeaIHknoVpznFCs/\nZjExP9sefxwDIH9NLl/kba90lVDFAwxFSujZnDpx3S8tTI7Ui+7iS6zp5rLdKMnO\nMjGc5vegdi9zm8SDJiWlwCZQIIf+C+/FEmJAhcWz4aUXbWaQzp7H73TDLePwlpla\nvCfbEvvzZdDxX72p4QHoiwC+DQKBgQDfkrXhM7iwq4rE+s26HRgUgY2+dCtKkNMZ\nVp2GHg4JM88Az5K3lnuEXp/xVh1WhlnfM+5RrQ3l3Z5w74UrBh+e9Vl5fPOW15za\ngmeB0T9ebyn9iMW9jqsiy2ef6vf6AuP8XhH87nlXdDR/4ForgId+0o3spsN3aRYu\nq0KWyop96wKBgHCR3S1WdnQev3LcjjZDnrdfCJBP2DJKMx0PPCeB6RFUlY7THjZh\ntuQZuaE96rpXFi+an+ntghCoQlK6sMXLy9EBvcptZP9lL8RPPlQ3WILyynnuI/9X\nxkZ8n0HgQndYk4ClWirAzZISBcoopMSrEvX3DsVMcyV8W1HjXvKufqVxAn8+4QRG\nUkWfap+cxu0VaxlaqxUye3mxfwngFnw3PDy2WdveXoLlH22dzP8u4QlfTGn6XKCq\nWAGQpMPq/3J0p0Q9cMO5Z2sbAYkb65Ew8ajg5mLo646xwW5gWtTKJUuZBTcZw1tL\nx8ZY0lXxoSe7FGsHQDCqXjybWPLkLUaNImnRAoGBAPC5jOkxyxgxmE6/7CTB4h0F\n3ozpmYqo2N5AkoKDSDSd2LPWaT/dNi8ns78rSVh6X2E+8tq71gCPjThn6ARpE6QH\nUq3setwncQdFOinMPty3PqI2tAC0aXe5VmHq4kH9hQLgjfSbAP8kBQo5TKnP4V/g\nuhTSywm3bMpOJRb7oyXF\n-----END PRIVATE KEY-----\n",
      "client_email": "ocrservice@boxwood-diagram-426306-s3.iam.gserviceaccount.com",
      "client_id": "108422349427166697157",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ocrservice%40boxwood-diagram-426306-s3.iam.gserviceaccount.com",
      "universe_domain": "googleapis.com"
    }
    
    # Set the environment variable for Google Application Credentials
    with open('google_application_credentials.json', 'w') as json_file:
        json.dump(credentials, json_file)
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "boxwood-diagram-426306-s3-08d2ae3cca77.json"
    vision_client = vision.ImageAnnotatorClient()

    """Detects text in the file."""
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = vision_client.text_detection(image=image)
    return response.text_annotations[0].description

# Define your desired output structure
def extract_receipt_tenant_info(ocr_text, system_prompt, model_name):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    openai.api_key = OPENAI_API_KEY
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
  
    # Initialize OpenAI and Google Vision clients
    openai_client = OpenAI()
    instructor_client = instructor.from_openai(openai_client)  
    class ReceiptTenantInfo(BaseModel):
          is_receipt: str
          tenant_name: str
          tenant_location_mall: str
          tenant_address: str
          receipt_number: str
          cashier: str
          transaction_date: str
          transaction_time: str
          customer_name: Optional[str]
          customer_phone_number: Optional[str]

    if '3.5' in model_name.lower():
        try:
            receipt_tenant_info = instructor_client.chat.completions.create(
                model=model_name,
                response_model=ReceiptTenantInfo,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )
        except:
            receipt_tenant_info = instructor_client.chat.completions.create(
                model='gpt-4o',
                response_model=ReceiptTenantInfo,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )
    else:
        receipt_tenant_info = instructor_client.chat.completions.create(
                model=model_name,
                response_model=ReceiptTenantInfo,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )

    receipt_tenant_info_dict = {
        "Is Receipt": [receipt_tenant_info.is_receipt],
        "Tenant Name": [receipt_tenant_info.tenant_name],
        "Tenant Location Mall": [receipt_tenant_info.tenant_location_mall],
        "Tenant Address": [receipt_tenant_info.tenant_address],
        "Receipt Number": [receipt_tenant_info.receipt_number],
        "Cashier": [receipt_tenant_info.cashier],
        "Transaction Date": [receipt_tenant_info.transaction_date],
        "Transaction Time": [receipt_tenant_info.transaction_time],
        "Customer Name": [receipt_tenant_info.customer_name],
        "Customer Phone Number": [receipt_tenant_info.customer_phone_number],
    }
    return receipt_tenant_info_dict

# Receipt Item List Info
def extract_receipt_item_info(ocr_text, system_prompt, model_name):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    openai.api_key = OPENAI_API_KEY
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
  
    # Initialize OpenAI and Google Vision clients
    openai_client = OpenAI()
    instructor_client = instructor.from_openai(openai_client) 
    if '3.5' in model_name.lower():
        try:
            response = openai_client.chat.completions.create(
                model=model_name,

                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )
        except:
            response = openai_client.chat.completions.create(
                model='gpt-4o',
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )
    else:
        response = openai_client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": ocr_text}
            ],
        )
            
    receipt_item_info = response.choices[0].message.content
    receipt_item_info = receipt_item_info.replace('```python', '').replace('json', '').replace('```','').replace('python','')

    # st.write(type(receipt_item_info))
    # st.write(receipt_item_info)
    receipt_item_info = eval(receipt_item_info)

    for k in receipt_item_info:
        relevant_dict = receipt_item_info[k]
        org_price = relevant_dict["original_price"]
        new_org_price = numberstring_convert(org_price)
        relevant_dict["original_price"] = new_org_price

    for k in receipt_item_info:
        relevant_dict = receipt_item_info[k]
        disc = relevant_dict["discount"]
        if type(disc) == str:
            if '%' in disc: 
                new_disc = (int( float(disc.replace('%','')) )/100) * relevant_dict["original_price"]
            else:
                new_disc = numberstring_convert(disc)
        else:
            if disc < 1:
                new_disc = (disc) * relevant_dict["original_price"]
            else:
                new_disc = disc

        relevant_dict["discount"] = new_disc

    for k in receipt_item_info:
        relevant_dict = receipt_item_info[k]
        final_price = relevant_dict["final_price"]
        if type(final_price) == str:
            if final_price == "":
                new_final_price = relevant_dict["original_price"] - relevant_dict["discount"]
            else:
                new_final_price = numberstring_convert(final_price)
        else:
            new_final_price = final_price
            
        relevant_dict["final_price"] = new_final_price

    # print(receipt_item_info)
    receipt_item_info_dictionary = {
        "Item Details":[receipt_item_info]
    }

    return receipt_item_info_dictionary

# Receipt Payment Info
def extract_receipt_payment_info(ocr_text, system_prompt, model_name):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    openai.api_key = OPENAI_API_KEY
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
  
    # Initialize OpenAI and Google Vision clients
    openai_client = OpenAI()
    instructor_client = instructor.from_openai(openai_client) 
    class ReceiptPaymentInfo(BaseModel):
        gross_total: Optional[Union[int, float]]
        net_total: Optional[Union[int, float]]
        sub_total: Optional[Union[int, float]]
        total_paid: Union[int,float]
        service: Union[int,float]
        pb1_tax: Union[int,float]
        discount: Union[int, float]
        rounding: Union[int, float]
        payment_method: Optional[str]

    if '3.5' in model_name.lower():
        try:
            receipt_payment_info = instructor_client.chat.completions.create(
                model=model_name,
                response_model=ReceiptPaymentInfo,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )
        except:
            receipt_payment_info = instructor_client.chat.completions.create(
                model='gpt-4o',
                response_model=ReceiptPaymentInfo,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": ocr_text}
                ],
            )
    else:
        receipt_payment_info = instructor_client.chat.completions.create(
            model=model_name,
            response_model=ReceiptPaymentInfo,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": ocr_text}
            ],
        )

    receipt_payment_info_dict = {
        "Gross Total": [receipt_payment_info.gross_total],
        "Net Total": [receipt_payment_info.net_total],
        "Sub Total": [receipt_payment_info.sub_total],
        "Total Paid": [receipt_payment_info.total_paid], 
        "Service": [receipt_payment_info.service],
        "PB1_Tax": [receipt_payment_info.pb1_tax],
        "Discount": [receipt_payment_info.discount],
        "Rounding": [receipt_payment_info.rounding],
        "Payment Method": [receipt_payment_info.payment_method]
    }
    return receipt_payment_info_dict

def main_extract(ocr_text, selected_model_name):
    item_info = extract_receipt_item_info(ocr_text, input_prompt_item_price_info, selected_model_name)
    payment_info = extract_receipt_payment_info(ocr_text, input_prompt_payment_info, selected_model_name)
    tenant_info = extract_receipt_tenant_info(ocr_text, input_prompt_tenant_info, selected_model_name)
    
    result_list = [item_info, payment_info, tenant_info]
    return result_list
