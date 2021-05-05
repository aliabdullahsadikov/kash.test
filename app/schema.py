
import graphene
from graphene_django import DjangoObjectType

from news.models import Tag, News

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ("name", "news")

class NewsType(DjangoObjectType):
    class Meta:
        model = News
        fields = ("id", "title", "description", "tags")

class Query(graphene.ObjectType):
    all_news = graphene.List(NewsType)
    news_by_tag = graphene.Field(TagType, name=graphene.String(required=True))

    def resolve_all_news(root, info):
        return News.objects.select_related("author").all()

    def resolve_news_by_tag(root, info, name):
        try:
            return Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
