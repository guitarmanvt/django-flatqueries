from django.urls import path

from flatqueries import views

urlpatterns = [
    path("flatquery/<int:id>/", views.run, name="run_flatquery"),
]

