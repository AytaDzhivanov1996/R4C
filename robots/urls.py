from django.urls import path
from robots.views import create_robot, download_production_report

urlpatterns = [
    path('api/create-robot/', create_robot, name='create_robot'),
    path('api/download-production-report/', download_production_report, name='download_production_report')
]