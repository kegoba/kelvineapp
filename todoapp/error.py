good day family.
please i am having issue with django rest_framework.
on my post-man this is my error 
#############################################################################
{
    "detail": "JSON parse error - Expecting value: line 1 column 1 (char 0)"
}
#############################################################################

on my terminal this my error 
Bad Request: /create_api/
[24/Aug/2019 13:53:45] "POST /create_api/?name=qsqsq&amount=qssqsqs&description=sqsqsq&product=sqsqs
qsq HTTP/1.1" 400 73

#############################################################################


this my serialer.py
from rest_framework import serializers
from .models import Record2

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record2
        fields = ["id", "name","product", "amount", "description"]
        read_only_fields =["id"]


#############################################################################
ths is my view.py
@api_view(['POST', 'GET'])
def Create_api(request):
    if request.method == "POST":
        print(request.data)
        data = JSONParser().parse(request)
        serializer = RecordSerializer(data = request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)