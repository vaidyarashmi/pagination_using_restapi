from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework import generics
from testapp.pagination import MyPagination,MyOffsetPagination,MyCursorPagination

# Create your views here.




class EmployeeListView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class    =EmployeeSerializer
    pagination_class    =MyPagination
    # pagination_class    =MyOffsetPagination
    # pagination_class    =MyCursorPagination
  
    #searching ,filtering,ordering
    # search_fields=('ename','eno') 
    # ordering_fields=('eno','esal')
    
    
    '''
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        print("name",name)
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs
    '''
