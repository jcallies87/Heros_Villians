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
    super_types = SuperType.objects.all()
    custom_response_dictionary = {}
    for super_type in super_types:
        supers = Supers.objects.filter(super_type_id=super_type.id)
        supers_serializer = SupersSerializer(supers, many=True)
        
    return Response(custom_response_dictionary)
