from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # director = DirectorSerializer()
    director = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title duration director reviews  rating'.split()

    def get_director(self, movie):
        try:
            return movie.director.name
        except:
            return 'No Director'

    def get_reviews(self, movie):
        serializer = ReviewSerializer(movie.reviews.all(), many=True)
        return serializer.data


class Director2Serializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()


class MovieCreateUptadeSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=10)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.CharField(max_length=30)


class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2, max_length=20)
    movie = serializers.CharField(min_length=2, max_length=10)
    author = serializers.CharField(min_length=2, max_length=20)
    stars = serializers.IntegerField()


class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=30)
