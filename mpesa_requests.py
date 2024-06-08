from .mpesa import MpesaExpress

json_data = { 
    "party_b": 8864136,  
    "callback_url": "https://api.<url>.com/api/transactions/mpesa/", #Use your endpoint
    "account_reference": "CompanyXLTD",  
    "transaction_desc": "Payment of X",  
    "transaction_type": "CustomerBuyGoodsOnline",
    "short_code": "8864136",
    "pass_key": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
}


# if using the code in the mpesa express sandbox
def stk_iniitiate(*, client_phone, amount):
    consumer_key = '' #Place your consumer key here
    consumer_secret = '' #Place your secret key here
    mpesaobj = MpesaExpress(consumer_key=consumer_key, consumer_secret=consumer_secret)
    json_data["phone_number"] = client_phone
    json_data["amount"] = amount
    response = mpesaobj.initiate_transaction(json_data=json_data)
    return response

""" Feel freee to coment out any of the two stk initiate functions. use the above for sandbox testing and the below one for going live[production] """

# if using the code for production ( we must change the mpesa endpoints)
def stk_iniitiate(*, client_phone, amount):
    consumer_key = '' #Place your consumer key here
    consumer_secret = '' #Place your secret key here
    MpesaExpress.production_urls(authorization_url='https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
                             stk_initiate_url='https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest')
    mpesaobj = MpesaExpress(consumer_key=consumer_key, consumer_secret=consumer_secret)
    json_data["phone_number"] = client_phone
    json_data["amount"] = amount
    response = mpesaobj.initiate_transaction(json_data=json_data)
    return response 
