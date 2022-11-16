from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('prestamos',views.PrestamosView.as_view(),name='prestamos'),
    path('prestamo/<int:prestamo_id>',views.PrestamosDetailView.as_view())
]