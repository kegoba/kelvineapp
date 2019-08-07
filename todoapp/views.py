from django.shortcuts import ( render, redirect)
from .models import Record2

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
    return render(request, "html/create.html" , {} )
   

#to view all the records
def Show(request):
    record = Record2.objects.all()
    return render(request, "html/show_record.html" , { "record" : record })

#To edith and updae the record
def Edith(request, id ):
    qry = Record2.objects.get(id=id)
    print(qry.id)
    print(qry.name)

    return render(request, "html/edith.html",
             {
            "name":qry.name, "description":qry.description,
            "product":qry.product, "amount":qry.amount,
            #"my_id":id.qry
             }) 

def Update(request, id):
    if request.method == "POST" and Record2.objects.get(id=id):
        data = Record2()
        data.name = request.POST.get("name")
        data.product = request.POST.get("product")
        data.amount = request.POST.get("amount" )
        data.description = request.POST.get("d")
        data.save()
    return render(request, "html/show_record.html")



#delete the record
def Delete(request, id):
    qry = Record2.objects.filter(id=id)
    qry.delete()

    return render(request, "html/show_record.html")