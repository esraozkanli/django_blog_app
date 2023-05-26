from django import forms
from .models import Article #article klasörünün içinde ki models dosyasına daha önce oluşturduğumuz Article classını dahil ettik.

class ArticleForm(forms.ModelForm): #Makale oluşturma classımızı oluşturduk.
    class Meta: #djangonun bize önerdiği classı açtık.
        model = Article #Article classını model objesine eşitledik.
        fields = ["title","content","article_image"] #models.py dosyasında ki Article classında yer alan title, content ve article_image ten input alanı oluştur dedik.

