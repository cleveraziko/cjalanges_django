from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

monthly_challages = {
    "january": 'Hello',
    "february": "YOOO wasup"
}


def monthly_challages_by_number(request,month):
    
    
    months = list(monthly_challages.keys())
    if month > len(months):
        return HttpResponseNotFound("this is invalid")    

    months_number = months[month]
    return HttpResponseRedirect('/challanges/' + months_number)



def monthly_challage(request,month):
    try:
        text = monthly_challages[month]
        return HttpResponse(text)
    except :
        return HttpResponseNotFound("invalid")












# def monthly_challages_by_number(request,month):
#     months = list(monthly_challages.keys())
#     if month > len(months):
#         return HttpResponseNotFound("invalid mont")
#     months_list = months[month]
#     return HttpResponseRedirect("/challanges/" + months_list)

# def monthly_challage(request,month):
#     try:
#         challage_text = monthly_challages[month]
    
#         return HttpResponse(challage_text)
#     except: 
#         HttpResponseNotFound("this month is not supported")
