from rest_framework import serializers
from .models import Music, Artist, Comment

# serializers.ModelSerializer
# forms.ModelForm과 비슷한 느낌으로

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        # model = Artist
        # fields = ('id', 'name',) 알아서 들어가 있음
        fields = ArtistSerializer.Meta.fields + ('music_set',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id',)

class MusicDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comment_set',)