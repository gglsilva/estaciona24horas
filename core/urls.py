from django.conf.urls import url, include
from .views import (
    Home,
    lista_pessoa,
    add_pessoa,
    update_pessoa,
    del_pessoa,
)

urlpatterns = [
    url(r'^$', Home, name='core_home'),
    url(r'^pessoa/$', lista_pessoa, name='core_lista_pessoa'),
    url(r'^add-pessoa/$', add_pessoa, name='core_add_pessoa'),
    url(r'^update-pessoa/(?P<id>\d+)/$', update_pessoa,
        name='core_update-pessoa'),
    url(r'^del-pessoa/(?P<id>\d+)/$', del_pessoa, name='core_del_pessoa'),

]