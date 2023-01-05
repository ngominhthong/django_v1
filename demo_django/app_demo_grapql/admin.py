from django.contrib import admin
from . models import *
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.
    

class layoutForm(forms.ModelForm):
    dest=forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        models=Layout
        fields='__all__'

class layout_imgInline(admin.StackedInline):
    model=Layout_img
    pk_name='layout'
    readonly_fields=['img_read']
    def img_read(self,obj):
        return mark_safe(u'<img src="/%s" />' % (obj.avatar))



class layoutAdmin(admin.ModelAdmin):
    inlines=(layout_imgInline, )
    form =layoutForm   
    #list_display=["id","title","show","active","priority","parent","page","catergory"]
    list_filter=["show","active","parent","page","catergory__styte"]
    search_fields=["id","title","parent","page","catergory__styte"]

class itemForm(forms.ModelForm):
    dest=forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        models=Item
        fields='__all__'

class tag_catergoryInline(admin.StackedInline):
    model=tag_catergory
    pk_name='item'

class itemAdmin(admin.ModelAdmin):
    inlines =(tag_catergoryInline, )
    form=itemForm
    #list_display=["id","title","show","active","prite","prite_promotion"]
    list_filter=["show","active"]
    search_fields=["id","title"]
    readonly_fields=['img_read']
    def img_read(self,obj):
        return mark_safe(u'<img src="/%s" />' % (obj.avatar))
       
class img_Admin(admin.ModelAdmin):
    readonly_fields=['img_read']
    def img_read(self,obj):
        return mark_safe(u'<img src="/%s" />' % (obj.avatar))

admin.site.register(User)
admin.site.register(Page)
admin.site.register(Layout,layoutAdmin)
admin.site.register(Catergory)
admin.site.register(Menu)
admin.site.register(Item,itemAdmin)
#admin.site.register(tag_catergory)
admin.site.register(Layout_catergory)
#admin.site.register(Layout_img)