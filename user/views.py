from django.shortcuts import render,redirect
from user import forms #Oluşturduğumuz dosyasını dahil ettik.
from django.contrib import messages #Flasktaki flash gibi mesajları gönderebilmek için dahil ettik.
from django.contrib.auth.models import User #Djangonun içinde kendiliğinden var olan User modelini dahil ettik. Bunun sebebi kullanıcı kaydınız User modeline kayıt etmek için.

from django.contrib.auth import login,authenticate,logout #Kullanıcı kayıt yaptığında aynı zamanda giriş yapmasını sağlamak için login fonksiyonunu dahil ettik.authenticate fonksiyonu, verilen bilgilere göre bir kullanıcının olup olmadığını veri tabanından sorgulayıp eğer öyle bir kullanıcı varsa bize kullanıcının bilgilerini döner.Kullanıcı yoksa none değeri döner.
from django.contrib.auth.decorators import login_required #Sadece giriş yapıldıysa çıkış yapmamızı sağlayan login_required decoratronu ekledik.

def register(request): #Kayıt fonksiyonunu oluşturduk.
    form = forms.RegisterForm(request.POST or None) #RegisterFormumuzu post requestten gelen bilgilerle doldurup form objesine eşitledik. Eğer post request değilse boş olarak oluştur dedik.
    if form.is_valid(): #Bu fonksiyon çağırıldığında python forms dosyasına gider ve clean fonksiyonuna bakar. Eğer password ve confirm değerleri birbiriyle aynıysa values sözlüğünü döndürür. Bu değerler döndürülürse form.is_valid koşulu true gibi davranır. Eğer koşul sağlanmıyorsa ve values sözlüğünde ki değerler dönmüyorsa false gibi davranır ve raise ileValidationError fırlatılır.
        username = form.cleaned_data.get("username") #Post requestten gelen username bilgisini aldık.
        password = form.cleaned_data.get("password") #Post requestten gelen password bilgisini aldık.

        newUser = User(username = username) #Post requestten gelen username bilgisini newUser objesine ekledik.
        newUser.set_password(password) #Post requestten gelen password bilgimizi şifreleyerek newYser objesine ekledik.
        newUser.save()
        login(request,newUser) #newUser kullanıcımız sisteme giriş yaptı.
        messages.success(request,"Başarıyla Kayıt Oldunuz...") #Mesajımızı oluşturduk.
            
        return redirect("index") #işlem tamamlandıktan sonra ana sayfaya dönüş yaptık. redirect fonksiyonun içine url adresi yerine urls.py de tanımladığımız name i yazdık.
    #Eğer request post request değilse yukarıda ki şart sağlanmayacağı için if bloğuna girmez ve bu işlemler yapılır.
    context = {#Bir sonra ki ekranda gösterebilmek için sözlük halinde yazmamız grektiği için sözlük halinde yazdık.

        "form" : form
    }
    return render(request,"register.html",context) #Koşulumuz sağlanmadığı için sözlüğü register.html sayfasına gönderdik.

def loginUser(request): #Giriş fonksiyonunu oluşturduk.
    form = forms.LoginForm(request.POST or None) #Formumuzu post ya da boş dönme durumuna göre doldurduk.
    context = {
        "form" : form
    }

    if form.is_valid(): #forms.is_valid() fonksiyonu class içinde özellikle yazılmadığı sürece otomatik olarak kendisi eğer formlarda bir sıkıntı yoksa True değerini alır ve formdaki bilgileri döner.
        username = form.cleaned_data.get("username") #Formumuzdan username bilgisini aldık.
        password = form.cleaned_data.get("password") #Formumuzdan password bilgimizi aldık.
        
        user = authenticate(username = username,password = password) #Formumuzdan aldığımız bilgileri veri tabanında arattık. https://docs.djangoproject.com/en/4.2/topics/auth/default/
        
        if user is None: 
            messages.info(request,"Kullanıcı Adı Veya Parola Hatalı...") #Döndüğrdüğümüz ekrana mesajımızı yazdırdık.
            return render(request,"login.html",context) #Form bilgimizi login ekranına gönderdik.
        
        else:
            messages.success(request,"Başarıyla Giriş Yaptınız...") #Mesajımızı yayınladık.
            login(request,user) #Kullanıcıya giriş yaptırdık.
            return redirect("index") #Ana ekranı döndürdük.

        
    return render (request,"login.html",context) #Formumuz is_valid() durumuna girmediyse form bilgimizi giriş sayfasına gönderdik.

@login_required(login_url='user:login')
def logoutUser(request): #Çıkış fonksiyonunu oluşturduk.
    logout(request) #Çıkış yaptık.
    messages.info(request,"Başarıyla Çıkış Yapıldı...")
    return render(request,"index.html")
