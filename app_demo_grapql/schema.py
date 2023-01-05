import graphene
from graphene import relay,ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from app_demo_grapql.models import *

class PageType(DjangoObjectType):
    class Meta:
        model = Page
        fields='__all__'
        #fields = ("id", "title", "show", "active", "styte")
        filter_fields = ["id", "title", "show", "active",]
        interfaces = (relay.Node, )

class Layout_catergoryType(DjangoObjectType):
    class Meta:
        model = Layout_catergory
        fields='__all__'
        #fields = ("id", "title",  "styte","groud")
        filter_fields = ["id", "styte","groud", ]
        interfaces = (relay.Node, )

class LayoutType(DjangoObjectType):
    class Meta:
        model = Layout
        #fields = ("id", "title", "show", "active", "styte","priority","name","dest","parent","catergory","page")
        filter_fields = ["id", "title","parent","parent","page", "show", "active",]
        interfaces = (relay.Node, )

class Layout_imgType(DjangoObjectType):
    class Meta:
        model = Layout_img
        fields='__all__'
        #fields = ("id", "title", "show", "active", "avatar","layout","name","dest")
        filter_fields = ["id", "title","layout","name", "show", "active",]
        interfaces = (relay.Node, )

class CategoryType(DjangoObjectType):
    class Meta:
        model = Catergory
        #fields = ("id", "title",  "avatar","parent")
        fields='__all__'
        filter_fields = ["id", "title","parent"]
        interfaces = (relay.Node, )

class MenuType(DjangoObjectType):
    class Meta:
        model = Menu
        fields='__all__'
        #fields = ("id", "title", "show", "active", "avatar","parent","priority","url")
        filter_fields = ["id", "title","parent", "show", "active",]
        interfaces = (relay.Node, )

class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        #fields = ("id", "title", "show", "active", "prite","prite_promotion","dest","user","created_date","updated_date")
        fields='__all__'
        filter_fields = {
            "id":['exact'], 
            "title":['exact', 'icontains', 'istartswith'],
            "prite":['exact'],
            "prite_promotion":['exact'],
            "user":['exact'],
        }
        interfaces = (relay.Node, )

class ItemConnection(relay.Connection):
    class Meta:
        node = ItemType

class Tag_catergoryType(DjangoObjectType):
    class Meta:
        model = tag_catergory
        fields='__all__'
        filter_fields = ["id", "catergory"]
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    all_menu = graphene.List(MenuType)
    page_by_name = graphene.Field(PageType, name=graphene.String(required=True))

    def resolve_all_menu(root, info):
        # We can easily optimize query count in the resolve method
        #return Menu.objects.select_related("category").all()
        return Menu.objects.all()

    def resolve_page_by_name(root, info, name):
        try:
            return Page.objects.get(name=name)
        except Page.DoesNotExist:
            return None
    
    items = relay.ConnectionField(ItemConnection)

    def resolve_questions(root, info, **kwargs):
        return Item.objects.all()

    page = relay.Node.Field(PageType)
    all_Pages = DjangoFilterConnectionField(PageType)
    layout_catergory = relay.Node.Field(Layout_catergoryType)
    all_Layout_catergory = DjangoFilterConnectionField(Layout_catergoryType)
    layout = relay.Node.Field(LayoutType)
    all_Layout = DjangoFilterConnectionField(LayoutType)
    layout_img = relay.Node.Field(Layout_imgType)
    all_Layout_img = DjangoFilterConnectionField(Layout_imgType)
    category = relay.Node.Field(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)
    menu = relay.Node.Field(MenuType)
    all_Menu = DjangoFilterConnectionField(MenuType)
    item = relay.Node.Field(ItemType)
    all_Item = DjangoFilterConnectionField(ItemType)
    tag_catergory = relay.Node.Field(Tag_catergoryType)
    all_Tag_catergory = DjangoFilterConnectionField(Tag_catergoryType)

schema = graphene.Schema(query=Query)