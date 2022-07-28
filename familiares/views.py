from django.shortcuts import render
from familiares.models import Relative


# Create your views here.
def listafamiliares(request):
    relative_1 = Relative.objects.create(name ='Tomás', age = 20 , ocupation = 'Profesor de fútbol infantil', relationship = 'hermano', born='2001-10-19')
    relative_2 = Relative.objects.create(name ='Javier', age = 47 , ocupation = 'Peluquero', relationship = 'papá', born='1975-01-08')
    relative_3 = Relative.objects.create(name ='Candela', age = 21 , ocupation = 'Estudiante de Kinesiología y Físiatria', relationship = 'novia', born='2000-12-28')
    relative_4 = Relative.objects.create(name ='Helena', age = 11 , ocupation = 'Estudiante de Primaria', relationship = 'hermana', born='2010-11-03')
    relative_5 = Relative.objects.create(name ='Catalina', age = 10 , ocupation = 'Estudiante de Primaria', relationship = 'hermana', born='2012-02-24')
    relative_6 = Relative.objects.create(name ='Carolina', age = 46 , ocupation = 'Ama de casa', relationship = 'mamá', born= "1975-07-09")
    context = {'relative_1': relative_1, 'relative_2':relative_2, 'relative_3':relative_3, 'relative_4':relative_4, 'relative_5':relative_5, 'relative_6':relative_6}
    return render (request, 'familiares.html', context = context)

