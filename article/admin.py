#Uygulama için django admin panelini özelleştirmeye yarayan dosyadır.
from django.contrib import admin
from .models import  Article,Comment #models dosyasının içinde ki Article classını import(içe aktarma) ettik.

# Register your models here.

admin.site.register(Comment) #Comment modelimizi admin panalinde gösterdik."""#Bu hali admin panelinde sadece bilginin gösterildiği ekleme yapılamayan halidir.

@admin.register(Article) #Article classından bir decorator oluşturduk.
class ArticleAdmin(admin.ModelAdmin): #Admin panelinde makalelerimizin görünmesini istediğimiz özelliklerini eklemk için bir class oluşturduk.

    list_display = ["title","author","created_date"] #Admin panelinde görünmesini istediğimiz özellikleri belirttik.

    list_display_links = ["title","created_date"] #Normalde makalemize sadece makalenin başlığına basıldığında erişebiliyoruz. Belirttiğimiz özelliklere de link özelliği eklendi.

    search_fields = ["title"] #Article(makaleleri) içinde belirtilen özelliğe(özelliklere) göre arama özelliği ekledik.

    list_filter = ["created_date"] #İçinde belirtilen özelliğe göre filterleme yaptık.

    class Meta: #ArticleAdmin classıyla Article classını birleştirdik.Bu classının ismi Meta olmalıdır başka bir isim olamaz.
        model = Article
