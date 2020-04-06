from django.conf.urls import url, include
from .views import (
    Home,
    lista_pessoa,
    add_pessoa,
    upd_pessoa,
    del_pessoa,
    lista_veiculo,
    add_veiculo,
    upd_veiculo,
    del_veiculo,
    lista_mov_rota,
    add_mov_rota,
    upd_mov_rota,
)

urlpatterns = [
    url(r'^$', Home, name='core_home'),

    # PESSOA
    url(r'^pessoa/$', lista_pessoa, name='core_lista_pessoa'),
    url(r'^add-pessoa/$', add_pessoa, name='core_add_pessoa'),
    url(r'^upd-pessoa/(?P<id>\d+)/$', upd_pessoa, name='core_upd_pessoa'),
    url(r'^del-pessoa/(?P<id>\d+)/$', del_pessoa, name='core_del_pessoa'),

    # VEÍCULO
    url(r'^veiculo/$', lista_veiculo, name='core_lista_veiculo'),
    url(r'^add-veiculo/$', add_veiculo, name='core_add_veiculo'),
    url(r'^upd-veiculo/(?P<id>\d+)/$', upd_veiculo, name='core_upd_veiculo'),
    url(r'^del-veiculo/(?P<id>\d+)/$', del_veiculo, name='core_del_veiculo'),

    # MOVIMENTO ROTATIVO
    url(r'^mov-rotativo/$', lista_mov_rota, name='core_lista_mov_rota'),
    url(r'^add-mov-rota/$', add_mov_rota, name='core_add_mov_rota'),
    url(r'^upd-mov-rota/(?P<id>\d+)/$', upd_mov_rota,
        name='core_upd_mov_rota'),

]