from django.shortcuts import ( render, redirect)
from .models import Record2
from django.db.models import F

# Create your views here.

def Home(request):

    return render(request, "html/home.html", {})

#add new record
def Create(request):
    data = Record2()
    if request.method == "POST":
        data.name = request.POST.get("name")
        data.product = request.POST.get("product")
        data.amount = request.POST.get("amount" )
        data.description = request.POST.get("d")
        data.save()
        return render(request, "html/home.html" , {} )
    return render(request, "html/create.html" , {} )
   

#to view all the records
def Show(request):
    record = Record2.objects.all()
    return render(request, "html/show_record.html" , { "record" : record })

#To edith and updae the record
def Edith(request, id ):
    qry = Record2.objects.get(id=id)
    return render(request, "html/edith.html",
             {
            "name":qry.name, "description":qry.description,
            "product":qry.product, "amount":qry.amount,
             }) 

def Update(request, id):
    qry = Record2.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        product = request.POST.get("product")
        amount = request.POST.get("amount" )
        description = request.POST.get("d")
        qry.name = name
        qry.product = product
        qry.amount = amount
        qry.description = description
        qry.save()
        record = Record2.objects.all()
    #return render(request, "html/show_record.html")
    return render(request, "html/show_record.html",{ "record" : record} )





def Update1(request, id):
    data = Record2()
    if request.method == "POST":
        qry = Record2.objects.get(id=id)
        data.name = request.POST.get("name")
        data.product = request.POST.get("product")
        data.amount = request.POST.get("amount" )
        data.description = request.POST.get("d")
    if qry:
        data.save()
    record = Record2.objects.all()
    #return render(request, "html/show_record.html")
    return render(request, "html/show_record.html",{ "record" : record} )




#delete the record
def Delete(request, id):
    qry = Record2.objects.filter(id=id)
    qry.delete()

    return render(request, "html/show_record.html")