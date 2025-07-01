from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        w=Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer=WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_post=Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': WomenSerializer(new_post).data})


# class WomenAPIView(generics.ListAPIView):
#     queryset=Women.objects.all()
#     serializer_class = WomenSerializer