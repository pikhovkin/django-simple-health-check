from django.urls import path

from .views import Liveness, Readiness


urlpatterns = [
    path('liveness/', Liveness.as_view()),
    path('readiness/', Readiness.as_view()),
]
