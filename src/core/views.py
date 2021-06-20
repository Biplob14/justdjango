from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, response

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, serializers
from rest_framework import mixins

from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        # send an email
        serializer.save()
    # add a form to add post
    def post(self, requst, *args, **kwargs):
        return self.create(requst, *args, **kwargs)

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# with rest api
# class TestView(APIView):  #TestView class inherits from APIView
#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         # serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# with django
# def test_view(request):
#     data = {
#         'name': 'testName',
#         'age': '33'
#     }
#     return JsonResponse(data)