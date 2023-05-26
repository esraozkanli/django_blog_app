#Url adreslerini verdiğimiz zaman çalıştırılacak fonksiyonları,dosyaları gösteren python dosyasıdır. Proje dosyası oluşturulduğunda otomatik olarak oluşur. Url adresler bu dosyaya girilir.
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


#Dahil edilmek istenen tüm fonksiyonlar bu şekilde eklenmelidir.
from article import views #article klasörünün içinde ki views dosyasını dahil ettik. Bundan sonra wiews dosyasının içinde ki tüm sayfaları views.sayfadı şeklinde path içinde belirterek kullanabiliriz.

#admin paneline ulaşmak için gerekli olan site otomatik olarak oluşturulur.Diğer url adresleri de bunun altına eklenecek.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"), #Burada url kısmını boş bırakırsak yanında belirtiğimiz viwes dosyasının içindeki index sayfasına gider. O yüzden boş bırakıyoruz. Daha sonra gidilen url sayfasında çalışmasını istediğimiz fonksiyonu yazıyoruz.
    path('about/',views.about,name = "about"), #about linkinin çalışmasını istediğimiz için 'about/' şeklinde linkimizi belirttik. Daha sonra bu linkte çalışacak fonksiyonu belirttik. Son olarakta bu linke bir isim verdik.
    path('articles/',include("article.urls")), #article uygulamamızı ana uygulamamıza dahil ettik.
    path('user/',include("user.urls")), #user uygulamamızı ana uygulamamıza dahil ettik.

]
###Flaskta yaptığımız redirect(url_for()) işlemini yapabilmek için url lerimize name = "url_ismi" şeklinde isim vererek yapabiliriz.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #medialarımıza python dosyaları üzerinden erişebilmek için ekledik.
