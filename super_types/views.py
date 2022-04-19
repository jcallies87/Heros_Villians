from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType
from supers.models import Supers
from supers.serializers import SupersSerializer
# Create your views here.
@api_view(['GET'])
def super_types_list(request):
    custom_response_dictionary = {}    
    super_types = SuperType.objects.all()
    for super in super_types:
        super_types = super_types.filter(supers_type_id = super_types.id)
        serializer = SuperTypeSerializer(super_types, many= True)
        custom_response_dictionary[SuperType.type]
    
    return Response(custom_response_dictionary)


    

