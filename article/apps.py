from django.apps import AppConfig

#Uygulamamızın ismini gösteren dosyadır.

class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'
