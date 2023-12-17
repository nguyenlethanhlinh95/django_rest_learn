from restframework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['date']
        # fields = ('id', 'title', 'content', 'created_at', 'updated_at')