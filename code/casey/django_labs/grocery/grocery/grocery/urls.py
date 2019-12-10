from django.contrib import admin
from django.urls import path
from groceryapp.views import groceryappView, addGrocery, deleteGrocery, completeGrocery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groceryapp/', groceryappView),
    path('addGrocery/', addGrocery),
    path('deleteGrocery/<int:grocery_id>/', deleteGrocery),
    path('completeGrocery/<int:grocery_id>/', completeGrocery),
]
