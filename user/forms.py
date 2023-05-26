from typing import Dict,Any 
from django import forms #Djangonun kendi içinde var olan forms classını dahil ediyoruz. Djangonun içinde Form classı olduğu için ve ondan türeteceğimiz için bu classı dahil ettik.

class RegisterForm(forms.Form): #forms classında ki Form classından türeteceği için onu miras aldık.
    username = forms.CharField(max_length=50,label="Kullanıcı Adı") #username objesini forms classının içinde ki CharField dan oluşturduk.
    password = forms.CharField(max_length=20, label="Parola",widget = forms.PasswordInput) #password objemizin parola alanı gibi görünmesini istediğimiz için "PasswordInput" özelliğini belirttik.
    confirm = forms.CharField(max_length=20, label = "Parolayı Doğrula", widget= forms.PasswordInput)

    def clean(self): #Djangonun bize password ve confirm alanı aynıysa verileri submit(göndermek) eden değilse göndermeyen clean metodu için fonksiyonumuzu yazdık. Bu fonksiyon yalnızca formobjesiadı.is_valid() ile çağırılırsa çalışır diğer türlü python bu fonksiyonu çalıştırmaz.
        username = self.cleaned_data.get("username") #Hemen üstte oluşturduğumuz form bilgilerini aldık.
        password = self.cleaned_data.get("password") #Hemen üstte oluşturduğumuz form bilgilerini aldık.
        confirm = self.cleaned_data.get("confirm") #Hemen üstte oluşturduğumuz form bilgilerini aldık.
    
        if password and confirm and password != confirm: #Password ve confirm verilerimizi kıyasla ve ikisi birbirine eşit değilse if bloğunu çalıştır demek.
            raise forms.ValidationError("Parolalar Eşleşmiyor") #raise ile ekrana forms classında yer alan ValidationError ile hata mesajı fırlattık.
        
        values = {
            "username" : username,
            "password" : password    
        }
        return values #İf bloğuna girmediği zaman değerleri dönebilmesi için values isimli bir sözlük oluşturduk ve o sözlüğü döndük. Bu değerlerin bir sonraki sayfaya dönebilmesi için mutlaka sözlük olarak oluşturulması lazım.

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password =forms.CharField(label="Parola",widget=forms.PasswordInput)

