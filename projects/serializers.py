from rest_framework import serializers #importamos libreria de "rest_framework"
from .models import Project            # importamos el modelo llamado "Project"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project #nombre del proyecto
        fields = ('id', 'title', 'description','technology', 'created_at') #campos que se van a rteronrar con GET, PUT, ETC.
        #fields = '__all__' #selecciona todos los campos
        read_only_fields = ('created_at',) #Campos que unicamene seran de "solo lectura".