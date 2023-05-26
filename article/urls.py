from django.contrib import admin
from django.urls import path,include

#Dahil edilmek istenen tüm fonksiyonlar bu şekilde eklenmelidir.
from article import views #Şu anda bulunduğumuz klasörünün içinde ki views dosyasını dahil ettik. Bundan sonra wiews dosyasının içinde ki tüm sayfaları views.sayfadı şeklinde path içinde belirterek kullanabiliriz.
app_name = "article"
#admin paneline ulaşmak için gerekli olan site otomatik olarak oluşturulur.Diğer url adresleri de bunun altına eklenecek.
urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addarticle,name = "addarticle"),
    path('article/<int:id>/',views.detail,name="detail"),
    path('update/<int:id>/',views.updateArticle,name="update"),
    path('delete/<int:id>/',views.deleteArticle,name="delete"),
    path('',views.articles,name="articles"), #blog klasörünün altında ki urls.py dosyasında articles uzantısı geldiğinde article.url e git diye yönlendirdiğimiz için burada url kısmını boş bırakırsak direkt makaleler sayfasına gider.
    path('comment/<int:id>/',views.addComment,name="comment"),
]
###Flaskta yaptığımız redirect(url_for()) işlemini yapabilmek için url lerimize name = "url_ismi" şeklinde isim vererek yapabiliriz.