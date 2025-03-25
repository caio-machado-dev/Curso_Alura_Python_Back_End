from django.urls import path
from galeria.views import index, imagem
'''
Uma forma de isolar urls específicas daquele APP, e ir incluido na rota principal
da aplicação
'''
urlpatterns = [
    path('', index, name='index'),
    path ('imagem/<int:foto_id>', imagem, name='image')
]