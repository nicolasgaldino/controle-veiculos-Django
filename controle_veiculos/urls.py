from django.contrib import admin
from django.urls import path
from veiculos.views import (
    home,
    form,
    create,
    view,
    edit,
    update,
    delete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:id>', view, name='view'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
