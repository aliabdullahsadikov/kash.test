import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from news.models import Tag, News


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = ['name', 'news']
        interfaces = (relay.Node, )


class NewsNode(DjangoObjectType):
    class Meta:
        model = News
        # Allow for some more advanced filtering here
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'tags': ['exact'],
            'tags__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    tag = relay.Node.Field(TagNode)
    all_categories = DjangoFilterConnectionField(TagNode)

    news = relay.Node.Field(NewsNode)
    all_ingredients = DjangoFilterConnectionField(NewsNode)