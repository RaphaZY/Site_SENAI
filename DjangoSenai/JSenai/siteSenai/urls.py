from django.urls import path
from siteSenai.views import *

urlpatterns = [
    path("", index, name="index"),
    path("cc/", cadcard, name="cadastro_cards"),
    path("cadastro/", caduser, name="cadastro_user"),
]