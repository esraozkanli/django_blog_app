#Herhangi bir url adresine göre çalışacak fonksiyonların yazıldığı dosyadır.
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment #article klasörünün içinde ki models dosyasında yer alan Article classını dahil ettik.
from django.contrib.auth.decorators import login_required #Kullanıcı girişi kontrolü yapabilmemizi sağlayan ogin required decoratorunu dahil ettik.

#HttpResponse, sayfada bir html içerik döndürmeye yarar. "return HttpResponse("Anasayfa")" şeklinde kullanılır.

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword") #Bizim articles.html sayfasındaki form yapımız bize bir GET request ile bize bir keyword anahtar kelimesi olarak belirlediğimiz kelimeyi bize gönderir.Bizde bu keyword bilgisini alıp keyword objesine eşitledik.
    if keyword: #Eğer keyword bilgisi geldiyse if bloğuna girecek.
        articles = Article.objects.filter(title__contains = keyword) #title__contains bize Articleların içinde keyword ün geçtiklerini döndürecek.
        return render(request,"articles.html",{"articles":articles})
    
    articles = Article.objects.all() #Eğer bir sorgu işlemi yapılmadıysa ve bize GET requestle bir keyword bilgisi gelmediyse bu işlem yapılarak döndürülür.
    return render (request,"articles.html",{"articles":articles})

def index(request): #views dosyasının içinde oluşturulacak tüm fonksiyonlarda fonksiyonun içine gönderilen ilk parametre her zaman "request" olmalıdır.Bu yüzden request parametresini gönderdik.
    return render(request,"index.html") #İlk parametre olarak yine mutlaka request yazılmalı. Daha sonra döndürülmek istenen templates ismini yazdık.

    #Eğer dödnürmek istediğimiz templates templates klasörünün içinde ki başka bir klasörde yer alıyorsa mutlaka bu belirtilerek yazılmalı. Örneğin(article/index.html) gibi.

def about(request): #Hakkımızda sayfası için about şeklinde bir fonksiyon oluşturduk.
    return render(request,"about.html") #Fonksiyona about sayfasını döndürttürdük.

@login_required(login_url='/user/login/') #url adresi bu şekilde yazılabildiği gibi user:login(dinamik url) şeklinde de yazılabilir.
def dashboard(request):
    articles = Article.objects.filter(author = request.user) #Article tablosundan şu anda giriş yapmış kullanıcının makale verilerini al demek.
    context = {
        "articles" :articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url='user:login')    
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None) #POST request gelirse onu döndür get request gelirse boş olarak alıp döndür ve FILES gelirse onu alıp döndür get request gelirse boş olarak alıp döndür.

    if form.is_valid(): #Formumuzda bir problem yoksa if bloğu çalışır.
        article = form.save(commit=False) #formdaki bilgileri al fakat kayıt etme işlemini yapma demiş olduk.
        article.author = request.user #Yazar bilgisini şu anda ki kullanıcının user bilgisi olarak belirledik.
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu...")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form}) #form objemizi form olarak gönderdik.

@login_required(login_url='/user/login/')
def detail(request,id): #Şu an ki makalenin id bilgisini gönderdi
    #article = Article.objects.filter(id = id).first() #makalenin id sine göre filtereleme yaparak makalemizi alıp article objesine eşitledik.
    article = get_object_or_404(Article,id = id) #İlk olarak hangi modelden veri çekmek istediğimizi girdik ve sonra sorgumuzu yazdık.
    comments = article.comments.all()
    return render (request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url='user:login')
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id) #Eğer içine girilen ilk değerdeki class yapısında verilen id de bir veri varsa olur alır eğer yoksa 404 hatası döndürür.
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article) #Form sayfasının ilk halinde o id deki makalenin veritabanındaki haliyle doldurulmuştur.(instance=article)
    if form.is_valid(): #Formumuzda bir problem yoksa if bloğu çalışır.
        article = form.save(commit=False) #formdaki bilgileri al fakat kayıt etme işlemini yapma demiş olduk.
        article.author = request.user #Yazar bilgisini şu anda ki kullanıcının user bilgisi olarak belirledik.
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi...")
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url='user:login')
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id) #Eğer içine girilen ilk değerdeki class yapısında verilen id de bir veri varsa olur alır eğer yoksa 404 hatası döndürür.
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi...")
    return redirect("article:dashboard") #article klasörünün altında ki urls.py dosyasına bakar ve içinde ki dashboardu döndürür. Burada dashboardun bulunduğu klasörü belirtmemiz gereklidir.

def addComment(request,id):
    article = get_object_or_404(Article,id = id) #İlk olarak id ye göre postumuzu alıyoruz. O postun üstüne ekleme yapacağımız için bu işlemi mutlaka yapmalıyız.
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content = comment_content )
        newComment.article = article
        newComment.save()
        messages.success(request,"Yorum Başarıyla Eklendi...")
        
    return redirect(reverse("article:detail",kwargs ={"id":id}))
