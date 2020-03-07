from rest_framework.serializers import ModelSerializer

from blog.models import Posts

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

