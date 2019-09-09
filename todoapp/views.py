from django.shortcuts import ( render, redirect)
from django.http import JsonResponse

from .models import Record2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializer import RecordSerializer

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

#delete the record
def Delete(request, id):
    qry = Record2.objects.filter(id=id)
    qry.delete()

    return render(request, "html/show_record.html")

@api_view(['POST', 'GET'])
def Createapi(request):
    if request.method == "POST":
        serializer = RecordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'key': request.data}, status=status.HTTP_200_OK)


        
        
@api_view(['GET', 'POST'])
def Showapi(request):
    if request.method == "GET":
        qry = Record2.objects.all()
        serializer = RecordSerializer(qry, many = True) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET", "PUT", "POST"])
def Edithapi(request, id):

    try:
        qry = Record2.objects.get(id=id)
        #return JsonResponse(qry={"qry" :qry}, data= request.data, status=status.HTTP_201_CREATED)
       # print(request.data)
    except Record2.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = RecordSerializer(qry)
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = RecordSerializer(qry, data=request.data) #data={"request": request.data})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE", "GET"])
def Deleteapi(request, id):
    try:
        qry = Record2.objects.get(id=id)
    except Record2.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = RecordSerializer(qry)
        return Response(serializer.data)

    elif request.method == "DELETE":
        qry.delete()
    return Response(request.data, status=status.HTTP_201_CREATED)
    return Response(request.errors, status=status.HTTP_400_BAD_REQ)  

