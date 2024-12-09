from django.urls import path,include
from . import views

urlpatterns = [
    path("index/", views.index,name="index"),
    path("map/", views.map,name="map"),
    path("carContrl/", views.carContrl,name="carContrl"),
    path("message/", views.message,name="message"),
    path("static1/", views.static1,name="static1"),

    path('table/', views.table, name='table'),
    path("table1", views.table1,name="table1"),
    path("table2/", views.table2,name="table2"),

    path("tail_more.html/", views.tail_more,name="tail_more"),
    path("tail_sm.html/",views.tail_sm,name="tail_sm"),

    path('table/tail_more.html/', views.tail_more, name='tail_more.html'),
    path('table/tail_sm.html/', views.tail_sm, name='tail_sm'),
    path("table1/tail_more.html/", views.tail_more, name="tail_more"),
    path("table1/tail_sm.html/", views.tail_sm, name="tail_sm"),

    path('', views.upload,name="upload"),
    path('doupload/',views.doupload,name="doupload"),
    path('run_test/', views.run_test, name='run_test'),

    path('save_case_data/', views.save_case_data, name='save_case_data'),
    path('delete_item/', views.delete_item, name='delete_item'),
]