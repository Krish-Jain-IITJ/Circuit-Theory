from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('theory-pdf/', views.theory_pdf_view, name='theory_pdf'),
       path('solve-circuit/', views.solve_circuit, name='solve_circuit')
]