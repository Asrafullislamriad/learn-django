from  rest_framework import serializers
from .models import Todo

class TodoSerilizer(serializers.ModelSerializer):
 
    model=Todo
    fields="__all__"