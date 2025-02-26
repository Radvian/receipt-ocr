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

GOOGLE_VISION_API_KEY = st.secrets["GOOGLE_VISION_API_KEY"]

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
    vision_client = vision.ImageAnnotatorClient(client_options={'api_key':GOOGLE_VISION_API_KEY})

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

def extract_ktp(ocr_text, system_prompt, model_name):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    openai.api_key = OPENAI_API_KEY
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
  
    # Initialize OpenAI and Google Vision clients
    openai_client = OpenAI()
    instructor_client = instructor.from_openai(openai_client) 
    class KTP(BaseModel):
        provinsi: str
        kota_kabupaten: str
        nik: str
        nama: str
        tempat_tgl_lahir: str
        jenis_kelamin: str
        alamat: str
        rt_rw: str
        kelurahan_desa: str
        kecamatan: str
        agama: str
        status_perkawinan: str
        pekerjaan: str
        kewarganegaraan: str
        berlaku_hingga: str
        golongan_darah: str
        tanggal_pembuatan_ktp: str

    ktp_info = instructor_client.chat.completions.create(
        model='gpt-4o-mini',
        response_model=KTP,
        messages=[
            {"role":"system", "content": system_prompt},
            {"role":"user", "content":ocr_text}
        ]
    )
    
    # Create a dictionary to hold the extracted KTP information
    ktp_dict = {
        "Provinsi": [ktp_info.provinsi],
        "Kota/Kabupaten": [ktp_info.kota_kabupaten],
        "NIK": [ktp_info.nik],
        "Nama": [ktp_info.nama],
        "Tempat/Tgl Lahir": [ktp_info.tempat_tgl_lahir],
        "Jenis Kelamin": [ktp_info.jenis_kelamin],
        "Alamat": [ktp_info.alamat],
        "RT/RW": [ktp_info.rt_rw],
        "Kelurahan/Desa": [ktp_info.kelurahan_desa],
        "Kecamatan": [ktp_info.kecamatan],
        "Agama": [ktp_info.agama],
        "Status Perkawinan": [ktp_info.status_perkawinan],
        "Pekerjaan": [ktp_info.pekerjaan],
        "Kewarganegaraan": [ktp_info.kewarganegaraan],
        "Berlaku Hingga": [ktp_info.berlaku_hingga],
        "Golongan Darah": [ktp_info.golongan_darah],
        "Tanggal Pembuatan KTP": [ktp_info.tanggal_pembuatan_ktp]
    }

    
    return ktp_dict

def extract_sim(ocr_text, system_prompt, model_name):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    openai.api_key = OPENAI_API_KEY
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
  
    # Initialize OpenAI and Google Vision clients
    openai_client = OpenAI()
    instructor_client = instructor.from_openai(openai_client) 
    class SIM(BaseModel):
        nama: str
        tipe_sim: str
        nomor_sim: str
        tempat_lahir: str
        tanggal_lahir: str
        golongan_darah: str
        jenis_kelamin: str
        alamat: str
        pekerjaan: str
        domisili: str
        tanggal_pembuatan_sim: str

    sim_info = instructor_client.chat.completions.create(
        model='gpt-4o-mini',
        response_model=SIM,
        messages=[
            {"role":"system", "content": system_prompt},
            {"role":"user", "content":ocr_text}
        ]
    )
    
    # Create a dictionary to hold the extracted KTP information
    sim_dict = {
        "Nama":[sim_info.nama],
        "Tipe SIM":[sim_info.tipe_sim],
        "Nomor SIM":[sim_info.nomor_sim],
        "Tempat Lahir":[sim_info.tempat_lahir],
        "Tanggal Lahir":[sim_info.tanggal_lahir],
        "Golongan Darah":[sim_info.golongan_darah],
        "Jenis Kelamin":[sim_info.jenis_kelamin],
        "Alamat":[sim_info.alamat],
        "Pekerjaan":[sim_info.pekerjaan],
        "Domisili":[sim_info.domisili],
        "Tanggal Pembuatan SIM":[sim_info.tanggal_pembuatan_sim]
    }

    
    return sim_dict