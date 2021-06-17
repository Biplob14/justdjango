from rest_framework import serializers
from django.db.models import fields
from django.db import models

from .models import Post
from django import forms

# for rest
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner',
        )

# # for django
'''
# class PostForm(forms.ModelForm):
#     class Meta:
#         models = Post
#         fields = (
#             'title', 'description'
#         )
'''