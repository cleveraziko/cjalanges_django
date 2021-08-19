from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse



monthly_challages = {
    "january": 'Hello',
    "february": "YOOO wasup"
}

def index(request):
    list_items = ""
    months = list(monthly_challages.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challange", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)



def monthly_challages_by_number(request,month):
    
    
    months = list(monthly_challages.keys())
    if month > len(months):
        return HttpResponseNotFound("this is invalid")    

    months_number = months[month -1]
    redirect_path = reverse("monthly_challange",args=[months_number])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect('/challanges/' + months_number)



def monthly_challage(request,month):
    try:
        text = monthly_challages[month]
        data = f"<h1>{text}</h1>"
        return HttpResponse(data)
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
