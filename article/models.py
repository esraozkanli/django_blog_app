#Oluşturduğumuz uygulamamıza özgü tabloları buraya class(model) halinde oluşturmamız gereklidir. Eğer bu modellerimizi admin panelinde göstermek istiyorsak admin.py dosyasına kayıt etmemiz gereklidir.
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model): #Oluşturacağımız classları models in içindeki Model classından türetmemiz gerekir.
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name="Yazar") #ForeignKey ile author objemizi Djangonun içindeki auth.User tablosundan oluşturduk. author objesiyle oluşturulan user silindiğinde ona ait tüm tabloların ve özelliklerinde silinmesini istediğimiz için sil anlamına gelecek bir on_delete anahtar kelimesi oluşturduk ve buna silme fonksiyonu olan CASCADE i atadık. 
    title = models.CharField(max_length = 50, verbose_name="Başlık") #Bu obje bizim başlığımızı oluşturacağı için CharFieldden max uzunluğu 50 olacak şekilde oluşturduk."verbose_name" ile de admin panelinde görünmesini istediğimiz ismini yazdık.
    content = RichTextField() #Bu obje bizim makalemizi yazacağımız alan olacağı için TextFieldden oluşturduk.
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi") #Bu objemiz zamanı ve tarihi gösterdiği için DateField ile oluşturduk. Bir makale eklendiğinde eklendiği tarihi ve saati created_date atamasını istediğimiz için auto_now_add=True yaptık. 
    article_image = models.FileField(blank= True, null= True, verbose_name="Makaleye Fotoğraf Ekleyin") #Makaleye eklenen dosyasını resim dışındaki dosyalarda olabilmesi için FileField ile oluşturduk. Bu dosyanın resim dışında bir dosya da olabileceğini boşta olabileceğini belirttik. Son olarakta objemizin ekranda görünecek ismini belirledik.

    def __str__(self): #Admin panelinde tüm articleların göründüğü alanda Article object (1,2,...vb) şeklinde görünmesi yerine hangi bilginin görünmesini istiyorsak onu döndürerek admin panelinde yazdırabiliriz.
        return self.title
    class Meta():
        ordering = ["-created_date"] #Başında ki eksi sayesinde en son eklenen makale ilk sırada gösterilecektir. Böylelikle en yeni eklenenden en eski eklenene doğru sıralama yapmış olduk. Eğer başına - konmazsa en eski eklenenden en yeni eklenen doğru sıralama yapar.


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete= models.CASCADE,verbose_name="Makale",related_name="comments") #Bu işlemle yukarıda ki Article classımızla Comment classımız arasında ki bağlantıyı gerçekleştirdik. İleride Articleların Commentlerini alabilmek için related_name="comments" şeklinde bir isim belirledik. Böylelikle ileride Article.comments yazdığımıza o article ın commentslerine de erişebilmiş olacağız.
    comment_author = models.CharField(max_length=50, verbose_name= "İsim")
    comment_content = models.CharField(max_length=200,verbose_name= "Yorum")
    comment_created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self): #Admin panelinde tüm commentlerın göründüğü alanda Comment object (1,2,...vb) şeklinde görünmesi yerine hangi bilginin görünmesini istiyorsak onu döndürerek admin panelinde yazdırabiliriz.
        return self.comment_content
    class Meta():
        ordering = ["-comment_created_date"] #Başında ki eksi sayesinde en son eklenen makale ilk sırada gösterilecektir. Böylelikle en yeni eklenenden en eski eklenene doğru sıralama yapmış olduk. Eğer başına - konmazsa en eski eklenenden en yeni eklenen doğru sıralama yapar.