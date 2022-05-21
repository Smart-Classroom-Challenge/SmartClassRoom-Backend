import graphene
from graphene_django import DjangoObjectType
from .models import Classroom

class ClassroomType(DjangoObjectType):
    class Meta:
        model = Classroom
        fields = ('id','updated_on', 'room_number', 'name', 'description')

class Query(graphene.ObjectType):
    classrooms = graphene.List(ClassroomType)

    def resolve_classrooms(root, info, **kwargs):
        # Querying a list
        return Classroom.objects.all()
    
    
schema = graphene.Schema(query=Query)