example_1_input = """
"matahari\nLippo MAL Cikarang\nJl. M.H Thamrin\nLippo City\nBEKASI\nNPWP/NPPKP: 01.317.956.9-054.000\nTgl. PKP 14 Juli 1999\nINVOICE\nINVOICE NO. 216592 23/05/2024 21.55.30\nCOUNTER: 01001 CASHIER:\nCUSTOMER ID: 08967*****\nNAME\nNova Tampubolon\n194347\nTEM\n2626806\nPRICE\n239,900\nAMOUNT\n239.900\nBALLERINAS WOMEN WMH\nDISCOUNT @ 60%\nTEM TOTAL:\n24783\nOL FEM DAKAIF02151\nDISCOUNT @ 30%\nITEM TOTAL\n1429,000\nGANGAN LUPA POINT 10 NYYA KAK,\nBIEA MENDAPAT SURVEI DARINAHARI.\nTERIMA KASIH\nGROSS TOTAL:\nNET TOTAL:\nDPP:\nPPN:11.00%\nCREDIT CARD 437450\nTOTAL RECEIVED AMOUN\nNO. OF ITEMS:\n-143,940\n95,960\n429,000\n-128,700\n300,300\n396.260\n396,260\n356.991\n39,269\nRP\n396,260\nRP\n396,260\nTOTAL ITEMS:\n2\nBALANCE POINTS: 3,700\nYOU\'RE SAVING:\nRP\n272,640\nUntuk Barang Kena Pajak,\nHarga termasuk PPN\nKeluhan Atas Pelayanan & Saran\nHubungi HALO MATAHARI: 021-50813024\nEKSTRA\nA BARU\nPEMBELIAN\nAT DAN KETENTUAN BERLAKU\nwww MATAHARI COM SEKARANG"
"""

example_1_output = """
{{
    'BALLERINAS WOMEN WMH':{
            'sku': '2626806',
            'original_price': 239900,
            'quantity': 1,
            'discount':143940,
            'final_price': 95960
        },
    'L FEM DAKAIF02151':{
            'sku': '24783',
            'original_price': 429000,
            'quantity': 1,
            'discount':128700,
            'final_price':300300
        },
}}
"""

example_2_input = """
"OTN\nPT. Global Teknologi Niaga\nNPWP:41.028.838.5-506.000\nno-reply@globalteknoniaga.com\nServed by User BLIBLI STORE BLUE-SUN PLAZA\nMEDAN\nSalesman: DAMAYANTI KARINA BR TARIGAN\nCustomer: Ira novayanti\niPhone 13 128GB Midnight\nSN 358293807063945\nPROMO CASHBACK APPLE\n(PWP) 20W USB-C Power\n10,999.000\n-1,000,000\nAdapter\n1PCs x Rp 449,000\nSpecial Promotion\n449,000\nther\n-50,000\nSN SFNT3325149PLX2AW\nAccessories T1\nTOTEBAG BLIBLI STORE\n1PCs x Rp O\nSubtotal\n0\nRp 10,398,000\nTOTAL\n(Harga Sudah Termasuk PPN) Rp 10,398,000\nDebit Mandiri\n10,398,000\nCHANGE\nRp O\nPotential Rewards:\n27,978 points\nOrder 123686-004-0033-1616\n09/06/2024 16:45:05"
"""

example_2_output = """
{{
    'iPhone 13 128GB Midnight':{
            'sku': 'SN 35829380706395',
            'original_price': 10999000,
            'quantity': 1,
            'discount':1000000,
            'final_price':''
        },
    'PWP 20W USB-C Power Adapter':{
            'sku': 'SN SFNT3325TCA9PLX2AW',
            'original_price': 449000,
            'quantity': 1,
            'discount':50000,
            'final_price':''
        },
    'TOTEBAG BLIBLI STORE':{
        'sku':'',
        'original_price':0,
        'quantity':1,
        'discount':0,
        'final_price':0
    }
}}
"""

example_2_explanation = """
Explanation: In the Example 2 Receipt, the item's original price is mentioned, the discount is mentioned, but the final price after discount is not mentioned. Therefore, it's okay to just leave the field 'final_price' empty.
"""

example_3_input = """
"PT TOYS GAMES INDONESIA\nNPWP\nTGI Lippo Kemang\nPhone 0811-1050-8333\n02.751.004.9-086.000\nGED. KAWAN LAMA LT. 7, JL. PURI KENCANA\nNO. 1 RT. 005 RW. 002 KEMBANGAN SELATAN,\nKEMBANGAN, JAKARTA BARAT, DKI JAKARTA.\n121829 ANTO 01 Jun 2024 14:07\nReceipt No: 42.1.20240601.3\nWA Store: 081410201540\n10550593 SPMA-FIG BATMAN AS 95030099 61\n1 x\n69,900 :\nSaving:\n10537836 SPMA-FIG 12INC NO SUPERGIRL AS\n1 x\n249,900 :\nDisc 60 %:\n11,000 :\n69,900\n-10,000\n249,900\n-149,940\n11,000\n8997207320227 SOMETHING SWEET-WRAPPINGPA\n10444250 KIDD-SHOPPING BAG TIGGI GREEN\n1 x\n1 x\n10,000\n10,000\nTotal\n340, 800\nTotal saving\n-159,940\nTotal sales\n180,860\nMANDIRI Debit (RP)\n180,860\nCardID\n: ****\nHolder\n: 0\nApproval No\n: 164967\nTotal payment\n180, 860\nItem : 4\nQty : 4\nBKP - harga sudah termasuk PPN\nKode Voucher = MKN13FA-6L7HECG99723\n01/06/2024 - 14:07 121829 - ANTO\n*** REBATE ***\nTotal\n: 50,000\nSELAMAT! ANDA MENDAPATKAN VOUCHER 50.000\nUTK DIGUNAKAN PD TRANSAKSI BERIKUTNYA\nDI TOYS KINGDOM DGN MINIMAL\nPEMBELANJAAN RP 350.000 SD 30 JUNI 24\nDGN MEMBAWA RECEIPT INI. S&K BERLAKU"
"""

example_3_output = """
{{
    'SPMA-FIG BATMAN AS 95030099 61':{
            'sku': '10550593',
            'original_price': 69900,
            'quantity': 1,
            'discount':10000,
            'final_price':''
        },
    'SPMA-FIG 12INC NO SUPERGIRL AS':{
            'sku': '10537836',
            'original_price': 249900,
            'quantity': 1,
            'discount':149940,
            'final_price':''
        },
    'SOMETHING SWEET-WRAPPINGPA':{
        'sku':'8997207320227',
        'original_price':11000,
        'quantity':1,
        'discount':0,
        'final_price':''
    },
    'KIDD-SHOPPING BAG TINGGI GREEN':{
        'sku':'10444250',
        'original_price':10000,
        'quantity':1,
        'discount':0,
        'final_price':''
    }
}}
"""

example_3_explanation = """In Example 3, there are 4 products that has original price discount, but no final price. Therefore it makes sense to empty the 'final_price' field."""

example_4_input = """
"HokBen\nCALL US AT\n1-500-505\nwww.hcaba.c\ntria Haka B\nJAPANI SE RESTAURANT\n1.\nICON PALEMBANG\nBILL. NO\nTelp: 1-500-505\n:A0202.1696.94\nDINDA, 30-05-24 20:19 GUEST: 0\nTAKE AWAY\n1 NEW BENTO SPECIAL 4\n58,182\n1 S. SET TERIYAKI 1\n37,728\n2 S. SET TERIYAKI 2\n75,456\n1 TAKE AWAY BAG REGU\n2,728\n1 FREE TAKE AWAY BAG\n2 COLD OCHA\n0\n18,182\n8 item\nSUB TOTAL.\nTA CHARGE\nPJK RESTO 10%.\n192,276\nSERVICE CHARGE\n0\nPEMBULATAN\nTOTAL\nNON TUNAI\nEDC BCA\nKEMBALI\nStyles\n2,728\n19,500\n-4\n214,500\n0\n214,500\nSALAD UDON - PERPADUAN UDON & SAYURAN\nSEGAAARRR BANGET PASTINYA !\nWHATSAPP: 081111500505\nEMAIL: CS@HOKBEN.CO.ID\nARIGATO GOZAIM MASU - TERIMA KASIH\nDiterima dlm keadaan baik & lengkap\nOleh:\nNama Lengkap"
"""

example_4_output = """
{{
    'New Bento Special 4':{
            'sku': '',
            'original_price': 58182,
            'quantity': 1,
            'discount':0,
            'final_price':58182
        },
    'S. SET TERIYAKI 1':{
            'sku': '',
            'original_price': 37728,
            'quantity': 1,
            'discount':0,
            'final_price':37728
        },
    'S. SET TERIYAKI 2':{
        'sku':'',
        'original_price':75456,
        'quantity':2,
        'discount':0,
        'final_price':75456
    },
    'TAKE AWAY BAG REGU':{
        'sku':'',
        'original_price':2728,
        'quantity':1,
        'discount':0,
        'final_price':2728
    },
    'COLD OCHA':{
        'sku':'',
        'original_price':18182,
        'quantity':2,
        'discount':0,
        'final_price':18182
    }
}}
"""

example_4_explanation = """
In Example 4, there are no discount, and there's only one price point per item.
If the item appears as such, then consider it the original and the final price. 
If there is no SKU, that's okay, leave the SKU column blank. 
"""

example_5_input = """
"SUMBER MAKMUR\nSUMBER MAKMUR\n16-05-2024 16:46 KAS\nFUDO BANANA 416 GR\n1,00x 40.000\nZESS SUGAR CRAC.192 GR\nMR.OAT ROLLED OATS 800 GR\n2,00% 23.000.\n1,00x 43.000\nAPOLLO SUSU 1011\n3,00% 15.000\n10,00% = 36.000\n10,00% = 41.400\n10,00% =\n38.700\n10,00% = 40.500\n10,00% = 55.800\n10,00% =\n32.400\n10,00%\n=\n54.000\n-800\nTotal = 298.000\nBIHUN LAKSA RICE VERM.125 GR\nMELI LUNC.MEAT 397 GR\n2,00x 31.000\n1,00x 36.000\n1,00x 60.000\nDISCOUNT\nMALING CANNED EGGROLLS W/PORK\nCash : 300.000\nKembali = 2.000\nTotal Qty. = 11,00"
"""

example_5_output = """
{{
    'FUDO BANANA 416 GR':{
            'sku': '',
            'original_price': 40000,
            'quantity': 1,
            'discount':'10%',
            'final_price':36000
        },
    'ZESS SUGAR CRAC':{
            'sku': '',
            'original_price': 23000,
            'quantity': 2,
            'discount':'10%',
            'final_price':41400
        },
    'MR.OAT ROLLED OATS 800 GR':{
        'sku':'',
        'original_price':43000,
        'quantity':1,
        'discount':'10%',
        'final_price':38700
    },
    'APOLLO SUSU 1011':{
        'sku':'',
        'original_price':15000,
        'quantity':3,
        'discount':'10%',
        'final_price':40500
    },
    'BIHUN LAKSA RICE VERM.125 GR':{
        'sku':'',
        'original_price':31000,
        'quantity':2,
        'discount':'10%',
        'final_price':40500
    },
    'MELI LUNC.MEAT 397 GR':{
        'sku':'',
        'original_price':36000,
        'quantity':1,
        'discount':'10%',
        'final_price':32400
    },
    'MALING CANNED EGGROLLS W/PORK':{
        'sku':'',
        'original_price':60000,
        'quantity':1,
        'discount':'10%',
        'final_price':54000
    }
}}
"""

example_5_explanation = """
Example 5 is very complicated. Here are the key takeaways: 
- If the discount is in percentage, please write it using the percentage sign
- But, remember this, if the discount is in percentage, write it as a string
- So, instead of 10%, write it '10%'
- If there is no SKU, that's okay, leave the SKU Empty
"""


example_6_input = """
"SONDA\nNO CUST: 28594267720308\nHypermart Gajah Mada\n36623137 KINDER JOY FOR GIR\ndisc toko (-)(1) -8.990\n13.990\n36624412 KINDER JOY FOR BOY 2\n35783636 SOKLIN LIO ROSE 720M\nPENJUALAN\n274 27404 9816 26/05/24\n274027 16:22:40\n5,000\n13.990\n17.210\n30,590\n10,010\n5,890\n23,890\ndisc toko\ndisc toko 18% ( 1) -3,780\n20.990\n35703972 YURI HS PRE ROSE 375\n2 @ 25,590\ndisc toko (-)( 1) -20,590\n36332871 MAESTRO MAYO SCT100G\n2 @\ndisc toko 15%( 2) -1,770\n36201191 HGL CRS WARNA 200 GR\n2 @ 22,890\n(-)( 1) -21,890\n36631011 BENGBENG SHAREIT 95G 20,790\n2 @ 15,790\ndisc toko (-)(1) -10,790\n36545249 SUPERSTAR TRIPLE CHO 14,990\n2 @ 9,990\ndisc toko (-) ( 1) -4,990\n36549521 ROMA MALKIST KEJU MA 15,000\ndisc toko\n3 @ 9,140\n(-) ( 3) -12,420\n36549530 ROMA MALKIST CAPPUCI 10,000\ndisc toko\n2 @ 9,140\n(-) ( 2)\n-8,280\n36456998 ROMA MLKST CKTKLP95G 5,000\n1 @ 9,140\ndisc toko (-)( 1) -4,140\n36529730 ROMA MALKIST COKLAT 30,000\n6 @ 9,140\ndisc toko (-)( 6) -24,840\n25 ITEMS\n282008800\nTOTAL:\nVoucher5Ribu\n444032XXXXXX0001 ORIS_CIMB\nDapat 3 stamp BLAUMANN\nTotal 3 stamp BLAUMANN\nAnda Hemat\n122,480\n196,470\n5,000\n191,470\nPT MATAHARI PUTRA PRIMA TBK\nNPWP : 01.394.013.5-092.000\nCALL CENTER 1500216\ncs@hypermart.co.id\nTERIMA KASIH ATAS KUNJUNGAN ANDA\nGEDUNG GATAH MADA PLAZA LI.SG\nJL GAJAH MADA NO. 19 26 PE TOTO LITARA\nGAMBIR JAKARTA PUSAT DKI JAKARTA 10130\nBARANG KENA PATAK DIAN/AINI JASA KENA\nPAJAK, HARGA SUDAH TERMASUK PPN\nRF:0274-2024026 27404-9816 15\nCIMB NIAGA\nSM HYPE\nCIMB NIAGA\nYOW T\nJAKARTA\nгрозит\nSATE 26 May 24"
"""

example_6_output = """
{{
    'KINDER JOY FOR GIRL':{
            'sku': '36623137',
            'original_price': 13990,
            'quantity': 1,
            'discount': 8990,
            'final_price':5000
        },
    'KINDER JOY FOR BOY 2':{
            'sku': '36624412',
            'original_price': 13990,
            'quantity': 1,
            'discount':0,
            'final_price':13990
        },
    'SOKLIN LIO ROSE 720M':{
        'sku':'35783636',
        'original_price': 20990,
        'quantity':1,
        'discount':3780,
        'final_price':17210
    },
    'YURI HS PRE ROSE 375':{
        'sku':'35703972',
        'original_price':25590,
        'quantity':2,
        'discount':20590,
        'final_price':30590
    },
    'MAESTRO MAYO SCT100G':{
        'sku':'36332871',
        'original_price':5890,
        'quantity':2,
        'discount':1770,
        'final_price':10010
    },
    'HGL CRS WARNA 200 GR':{
        'sku':'36201191',
        'original_price':22890,
        'quantity':2,
        'discount':21890,
        'final_price':23890
    },
    'BENGBENG SHAREIT 95G':{
        'sku':'36631011',
        'original_price':15790,
        'quantity':2,
        'discount':10790,
        'final_price':20790
    },
    'SUPERSTAR TRIPLE CH0':{
        'sku':'36545249',
        'original_price':9990,
        'quantity':2,
        'discount':4990,
        'final_price':14990
    },
    'ROMA MALKIST KEJU MA':{
        'sku':'36549521',
        'original_price':9140,
        'quantity':3,
        'discount':12420,
        'final_price':15000
    },
    'ROMA MALKIST CAPPUCI':{
        'sku':'36549530',
        'original_price':9140,
        'quantity':2,
        'discount':8280,
        'final_price':10000
    },
    'ROMA MALKIST CKTKLP95G':{
        'sku':'36456998',
        'original_price':9140,
        'quantity':1,
        'discount':4140,
        'final_price':5000
    },
    'ROMA MALKIST COKLAT':{
        'sku':'36529730',
        'original_price':9140,
        'quantity':6,
        'discount':24840,
        'final_price':30000
    }
}}
"""

example_6_explanation = """
In Example 6, we see that: 
- the final price is mentioned first, then the details are elaborated later
- the quantity is mentioned before the original price (i.e 2 @ 9140) >> 2 is the quantity, 9140 is the original price
"""


example_7_input = """"GION\nGion Sushi Lippo Mall Puri\nLippo Mall Puri\nTable: 21\nDine In\nPax: 1\nServer : ALINA\nCashier:\n18 May 2024 19:14\n12-20240518-5189\n1 EDO SASHIMI SET\n205,000\n1 GOHAN\n18,000\n1 OCHA\n11,000\n2 OCHA\n1 TUNA SASHIMI SET\n1 SALMON BELLY ROLL\n22,000\n173,000\n1 FREE BIRTHDAY SUSHI CAKE\n205,000\n0\nTotal FOOD\nTotal BEVERAGE\n601,000\nSubtotal\n33,000\nSC\n634,000\nPB1\n47,550\n68,155\nTOTAL\n749,705\nTerima kasih telah berbelanja di\nGion Sushi Lippo Mall Puri."
"""

example_7_output = """
{'EDO SASHIMI SET': 
    {'sku': '', 
    'original_price': 205000, 
    'quantity': 1, 
    'discount': 0, 
    'final_price': 205000}, 
'GOHAN': 
    {'sku': '', 
    'original_price': 18000, 
    'quantity': 1, 'discount': 0, 
    'final_price': 18000}, 
'OCHA_1': 
    {'sku': '', 
    'original_price': 11000, 
    'quantity': 1, 
    'discount': 0, 
    'final_price': 11000}, 
'OCHA_2': 
    {'sku': '', 
    'original_price': 11000, 
    'quantity': 2, 
    'discount': 0, 
    'final_price': 22000}, 
'SALMON BELLY ROLL':
    {'sku':'',
    'original_price':173000,
    'quantity':1,'discount':0,
    'final_price':173000
    },
'TUNA SASHIMI SET': 
    {'sku': '', 'original_price': 205000, 'quantity': 1, 'discount': 0, 'final_price': 205000}, 
'FREE BIRTHDAY SUSHI CAKE': {'sku': '', 'original_price': 0, 'quantity': 1, 'discount': 0, 'final_price': 0}}
"""

example_7_explanation = """
The problem in Example 7 is that it has TWO OCHAS. 
This should be a mistake on the receipt's end. There should be no two items named the same appearing in the same column
The customer orders 1 OCHA, priced at 11000, then orders 2 more OCHA product, and since each OCHA is priced at 11000, 2 OCHAS would make the price to 22000

If this happens, do the above:
the first ocha item could be named OCHA_1
the second ocha item could be named OCHA_2
"""

example_7_payment_output = """
'gross_total':0
'net_total':0
'sub_total':634000
'service':47550
'pb1_tax':68155
'discount':0
'rounding':0
'total_paid':749705
'payment_method':'Debit Mandiri'
"""

input_prompt_item_price_info = f"""
You will be given an OCR result of a picture of a receipt. 

You are tasked to extract the details of items ordered in the receipt. 

The discount should be served in a positive number format. 
For example, some tenants like to write discount as '-5000' (negative number), while some others write discount in positive number
We want to standardize this, so just write discount in a positive number format. 

Please format your output as dictionary as such: 
    {{    'item_1_name':{{
            'sku': 'the code or SKU of the item, leave it blank if there is none',
            'original_price': 'the starting price of the item, before any discount or price changes',
            'quantity': 'the quantity of the item (how many of this item is bought)',
            'discount': 'the discount price changes to the item (discounts). fill it with 0 if there are no discounts',
            'final_price': 'the final price of the item (it is totally possible that the final price of the item is the same as the original price as there are no changes, but if there are price changes, please take note of the final price here)'
        }},

        'item_2_name':{{...etc...}}
    }}

If you cannot find the information of one of the keys, it's okay, leave it blank.

If the discount is in percentage, for example, 5%, write it like this: '5%' instead of just 5%
Remember, if the discount is in percentage, write it as a string
Only extract information from the items that are ordered, no need to parse in the sub total, service charge, etc. 
Do not hallucinate. Here, I will give you 6 examples. Please understand them well.


IMPORTANT INFORMATION REGARDING DISCOUNT: 
```
For please just parse discount that is relevant to INDIVIDUAL ITEM BREAKDOWN.
Do NOT parse discount for the OVERALL SALES
Just extract discount IF IT IS MENTIONED IN THE INDIVIDUAL ITEM BREAKDOWN DETAILS.
Not overall transaction at-the-end discount/voucher.

SO, if the discount is NOT INCLUDED in the INDIVIDUAL ITEM BREAKDOWN, do NOT include it in your output.
your task is to take note of the individual item breakdown details, NOT THE OVERALL SALES

Furthermore, for discount in percentages, write it using quotation marks such as '4%', '3%', '10%'
```
### EXAMPLE 1 ###
### EXAMPLE 1 INPUT: {example_1_input} ###
### EXAMPLE 1 OUTPUT: {example_1_output} ###

### EXAMPLE 2 ###
### EXAMPLE 2 INPUT: {example_2_input} ###
### EXAMPLE 2 OUTPUT: {example_2_output} ###
### EXAMPLE 2 EXPLANATION: {example_2_explanation} ###

### EXAMPLE 3 ###
### EXAMPLE 3 INPUT: {example_3_input} ###
### EXAMPLE 3 OUTPUT: {example_3_output} ###
### EXAMPLE 3 EXPLANATION: {example_3_explanation} ###

### EXAMPLE 4 ###
### EXAMPLE 4 INPUT: {example_4_input} ###
### EXAMPLE 4 OUTPUT: {example_4_output} ###
### EXAMPLE 4 EXPLANATION: {example_4_explanation} ###

### EXAMPLE 5 ###
### EXAMPLE 5 INPUT: {example_5_input} ###
### EXAMPLE 5 OUTPUT: {example_5_output} ###
### EXAMPLE 5 EXPLANATION: {example_5_explanation} ###

### EXAMPLE 6 ###
### EXAMPLE 6 INPUT: {example_6_input} ###
### EXAMPLE 6 OUTPUT: {example_6_output} ###
### EXAMPLE 6 EXPLANATION: {example_6_explanation} ###

### EXAMPLE 7 ###
### EXAMPLE 7 INPUT: {example_6_input} ###
### EXAMPLE 7 OUTPUT: {example_6_output} ###
### EXAMPLE 7 EXPLANATION: {example_6_explanation} ###

IMPORTANT:

if the discount is in percentage, write it like this: 
'discount':'10%'

'discount': '5%'

'discount':'3%'

Use quotation marks!
Given these examples of input, output, and explanation, please process the following OCR input: 

Input OCR:
"""

input_prompt_tenant_info = f"""
    You will be given an OCR result from a picture of receipt. 

    You are tasked to extract the following parameters/metadata: 
    - is_receipt: do you think the inputed ocr result is a receipt or not? 'yes' if it is a receipt, 'no' if it is not a receipt
    - tenant_name: the name of the tenant
    - tenant_location_mall: the mall that the tenant is in (leave it blank if you cannot infer)
    - tenant_address: the address of the tenant (leave it blank if you cannot infer)
    - receipt_number: the receipt number
    - cashier: the cashier ID or cashier name that is responsible for the receipt. pay attention, this is tricky: some receipts have ID for their cashier, or some receipts have name for their cashier. Identify them well. 
    - transaction_date: the date of the transaction
    - transaction_time: the time (time, clock, hour minute second) of the transaction
    - customer_name: the name of the customer (left blank if not detected)
    - customer_phone_number: the phone number of the customer, if available. If not, leave it blank.

    Please read all the input text carefully. Sometimes, the tenant name is located near the end of the receipt text, so not always at the top.
    Use your reasoning skill to discern everything well. 

    POS itle is not a cashier name.

    If you think the ocr result is not a receipt, please write 'no' in the 'is_receipt' part
    If what you parse is a movie ticket, it is not a receipt, so write 'no' in the 'is_receipt' part
    
    Now, with the above instructions, do the OCR of the below receipt: 
    Receipt OCR: 
    """

example_payment_input = """
"OTN\nPT. Global Teknologi Niaga\nNPWP:41.028.838.5-506.000\nno-reply@globalteknoniaga.com\nServed by User BLIBLI STORE BLUE-SUN PLAZA\nMEDAN\nSalesman: DAMAYANTI KARINA BR TARIGAN\nCustomer: Ira novayanti\niPhone 13 128GB Midnight\nSN 358293807063945\nPROMO CASHBACK APPLE\n(PWP) 20W USB-C Power\n10,999.000\n-1,000,000\nAdapter\n1PCs x Rp 449,000\nSpecial Promotion\n449,000\nther\n-50,000\nSN SFNT3325149PLX2AW\nAccessories T1\nTOTEBAG BLIBLI STORE\n1PCs x Rp O\nSubtotal\n0\nRp 10,398,000\nTOTAL\n(Harga Sudah Termasuk PPN) Rp 10,398,000\nDebit Mandiri\n10,398,000\nCHANGE\nRp O\nPotential Rewards:\n27,978 points\nOrder 123686-004-0033-1616\n09/06/2024 16:45:05"
"""

example_payment_output = """
'gross_total':0
'net_total':0
'sub_total':10398000
'service':0
'pb1_tax':0
'discount':0
'rounding':0
'total_paid':10398000
'payment_method':'Debit Mandiri'
"""
input_prompt_payment_info = f"""
    You will be given an OCR result from a picture of receipt. 

    You are tasked to extract the following parameters/metadata: 
    - gross_total: if there is mentioned 'gross total', 'GROSS TOTAL', or similar to that, put it here, otherwise leave it blank
    - net_total: if there is mentioned 'net total' 'NET TOTAL', 'NETT', 'NETT TOTAL', or similar to that, put it here, otherwise leave it blank
    - sub_total: if there is mentioned 'sub total', 'sub-total', 'SUB-TOTAL', 'SUBTOTAL', 'subtotal', 'Subtotal', or similar to that, put it here, otherwise leave it blank. SubTotal should be the 'total' before the 'final/grand total'.
    - service: SC, service fee, biaya servis, service charge, service, service fee. If you don't find any service tax or fee, please just write 0 (zero) as the 'service' key requires an integer value
    - pb1_tax: PB1 or TAX, or PAJAK, pajak, pjk amount. If you don't find any PB1 or Tax, please just write 0 (zero)
    - discount: if there are any discounts, or voucher, or any price cut from the subtotal/grosstotal/nettotal. If you don't find any discount, please just write 0 (zero)
    - rounding: if there are any rounding. If you don't find any rounding, just write 0 (zero)
    - total_paid: the amount of monetary value that is finally paid from the customer to the tenant. the final final total, the amount of money that is paid, after considering all adjustments (fees, taxes, rounding)
    - payment_method: the payment method. leave it blank if you cannot infer

    Please read all the input text carefully. 

    Regarding 'discount': this discount is referring to disounts that are located in the final payment section, not in the individual item price breakdown.
    For example, if the receipt is structured like this: 

    ### EXAMPLE RECEIPT: {example_6_input} ###
    
    Then, the `sub_total` is 196470, the `discount` is 5000, and the `total_paid` is 191470
    This is because the final total is 191470, the total before the final total is 196470 (this is parsed as 'sub_total' in our pipeline)
    And then from the total before the final total, there is a deduction because of a voucher for 5000, so this will go in the 'discount' section.

    We see that in the individual item breakdown, there are discounts - this should not be put in the 'discount' section.
    Remember, the 'discount' section is the 'discount' before the final total paid, and after the gross total, net total, and/or sub total.

    Regarding 'sub_total':
    - If you found these sections in the receipt: "TOTAL" and "GRAND TOTAL", then the first "TOTAL" is the "sub_total"
    - the "sub_total" is always the total before the final total, grand total, final final total

    I will give you another example.
    ### EXAMPLE 2: {example_payment_input}###
    ### EXAMPLE 2 OUTPUT: {example_payment_output}###
    Why? Because in the Example 2, the Subtotal is 10398000 and the Total/Debit mandiri payment is also 10398000

    I will give you another example.
    ### EXAMPLE 3: {example_7_input} ###
    ### EXAMPLE 3 OUTPUT: {example_7_payment_output}###
    Explanation: the subtotal is 634000, the SC or service charge is 47550, and the PB1 is 68155

    Now, with the above instructions, do the OCR of the below receipt: 
    Receipt OCR: 
    """


ktp_extract_prompt = """
    You will be given OCR from KTP (Kartu Tanda Penduduk Indonesia).
    Please extract the following data:
    - "provinsi"
    - "kota_kabupaten"
    - "NIK"
    - "nama"
    - "tempat_tgl_lahir"
    - "jenis_kelamin"
    - "alamat"
    - "rt_rw"
    - "kelurahan_desa"
    - "kecamatan"
    - "agama"
    - "status_perkawinan"
    - "pekerjaan"
    - "kewarganegaraan"
    - "berlaku_hingga"
    - "golongan_darah"
    - "tanggal_pembuatan_ktp"
"""

sim_extract_prompt = """
    You will be given OCR from SIM (Surat Izin Mengemudi Indonesia).
    Please extract the following data: 
    - "nama"
    - "tipe_sim": the type of SIM (Sim A, Sim B, Sim C, Sim D, Sim A Umum, Sim B Umum)
    - "nomor_sim"
    - "tempat_lahir"
    - "tanggal_lahir"
    - "golongan_darah"
    - "jenis_kelamin"
    - "alamat"
    - "pekerjaan"
    - "domisili"
    - "tanggal_pembuatan_sim"
"""