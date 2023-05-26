from django.contrib import admin
from django.urls import path,include
from user import views #user klasörünün içinde ki views dosyasını dahil ettik. Bundan sonra wiews dosyasının içinde ki tüm sayfaları views.sayfadı şeklinde path içinde belirterek kullanabiliriz.

app_name = "user" #Uygulamamızın adını belirlerdik.

urlpatterns = [
    path('register/',views.register,name = "register"), #Kayıt linkimizi oluşturduk.
    path('login/',views.loginUser,name = "login"),  #Giriş linkimizi oluşturduk.
    path('logout/',views.logoutUser,name = "logout"), #Çıkış linkimizi oluşturduk.

]
