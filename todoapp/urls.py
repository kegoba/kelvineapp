from django.urls import path


from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('show/', views.Show, name="Show"),
    path('create/', views.Create, name="Create"),
    path('edith/<int:id>/', views.Edith, name="Edith"),
    path('edith/<int:id>/update/', views.Update, name="Update"),
    path('delete/<int:id>/', views.Delete, name="Delete"),
    
]


