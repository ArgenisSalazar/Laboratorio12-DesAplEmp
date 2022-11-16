from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Prestamos
from .serializers import PrestamosSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class PrestamosView(APIView):
    
    def get(self,request):
        dataPrestamos = Prestamos.objects.all()
        serPrestamos = PrestamosSerializer(dataPrestamos,many=True)
        return Response(serPrestamos.data)
    
    def post(self,request):
        serPrestamos = PrestamosSerializer(data=request.data)
        serPrestamos.is_valid(raise_exception=True)
        serPrestamos.save()
        
        return Response(serPrestamos.data)
    
class PrestamosDetailView(APIView):
    
    def get(self,request,prestamo_id):
        dataPrestamos = Prestamos.objects.get(pk=prestamo_id)
        serPrestamos = PrestamosSerializer(dataPrestamos)
        return Response(serPrestamos.data)
    
    def put(self,request,prestamo_id):
        dataPrestamos = Prestamos.objects.get(pk=prestamo_id)
        serPrestamos = PrestamosSerializer(dataPrestamos,data=request.data)
        serPrestamos.is_valid(raise_exception=True)
        serPrestamos.save()
        return Response(serPrestamos.data)
    
    def delete(self,request,prestamo_id):
        dataPrestamos = Prestamos.objects.get(pk=prestamo_id)
        serPrestamos = PrestamosSerializer(dataPrestamos)
        dataPrestamos.delete()
        return Response(serPrestamos.data)