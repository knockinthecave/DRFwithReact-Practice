from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import WorkerSerializer
from .models import Worker

# Create your views here.



class WorkerList(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        
        serializer = WorkerSerializer(workers, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkerSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class WorkerDetail(APIView):
    def get_object(self, wid):
        try:
            return Worker.objects.get(wid=wid)
        except Worker.DoesNotExist:
            raise Http404
    
    def get(self, request, wid, format=None):
        worker = self.get_object(wid)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)
    
    def put(self, request, wid, format=None):
        worker = self.get_object(wid)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, wid, format=None):
        worker = self.get_object(wid)
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    