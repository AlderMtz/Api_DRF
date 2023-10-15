from .models import Project #importamos el "modelo" llamado "Project" del archivo "models.py"
from rest_framework import viewsets, permissions 
from .serializers import ProjectSerializer #los datos que se retornaran en JSON

class ProjectViewSet(viewsets.ModelViewSet):  #clasee para poder obtener una visulizacion de resultados
    queryset = Project.objects.all() #lo que va a retornar un query
    permission_classes = [permissions.AllowAny] #quines podran hacer consultas
    serializer_class = ProjectSerializer #especifica la clase de serializador que se utilizará para convertir los objetos del modelo en datos serializados