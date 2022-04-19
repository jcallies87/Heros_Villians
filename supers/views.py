from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from .serializers import SupersSerializer
from .models import Supers
# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        supers_param = request.query_params.get('Type')
        if supers_param:
            supers = supers.filter(type__type = supers_param)

        serializer = SupersSerializer(supers, many= True)
        return Response(serializer.data)


        
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    product = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def super_types_list(request):
    super_types = SuperType.objects.all()
    custom_response_dictionary = {}
    for super_type in super_types:
        supers = Supers.objects.filter(super_type_id=super_type.id)
        supers_serializer = SupersSerializer(supers, many=True)
        
    return Response(custom_response_dictionary)

