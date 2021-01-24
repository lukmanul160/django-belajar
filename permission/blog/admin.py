from django.contrib import admin
from .models import Artikel
# Register your models here.
class AdminArtikel(admin.ModelAdmin):
    

    def get_readonly_fields(self, request, obj=None):

        current_user = request.user
        # print(current_user.has_perm("blog.add_artikel"))
        # print(obj.is_published)

        if obj != None:
            if current_user.has_perm("blog.can_publish"):
                readonly_fields = [
                    'created',
                    'published',
                    'updated',
                    'slug',
                    ]
                return readonly_fields
            elif current_user.has_perm("blog.add_artikel"):

                if obj.is_published:
                    # semua readonly
                    return [data.name for data in self.model._meta.fields]
                else:
                    readonly_fields = [
                        'created',
                        'published',
                        'is_published',
                        'updated',
                        'slug',
                        ]
                    return readonly_fields
        
        else:
            readonly_fields = [
                    'created',
                    'published',
                    'is_published',
                    'updated',
                    'slug',
                    ]
            return readonly_fields
                
                

admin.site.register(Artikel,AdminArtikel)
