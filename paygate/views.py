# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import checksum

MERCHANT_KEY = "qrkQRVau@33pu@QV"

def paymentMode(request):
    param_dict = {
        "MID": "xlsLVE30301290882657",
        "ORDER_ID": "1029",
        "CUST_ID": "125",
        "TXN_AMOUNT": "199",
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        #"CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
        "CALLBACK_URL": "https://merchant.com/callback/"

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

    return render(request, 'paytm.html', {'params': param_dict})

@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
    return redirect('/Thanks')
