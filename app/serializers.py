from hello.models import Game, GamePerformance, Player, RatingList, LastMonthRatingList
from rest_framework import serializers

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('nickname', 'postion', 'skill' , 'mu', 'sigma', 'winnerPercentage', 'goalAverage')

class GamePerformanceSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    
    class Meta:
        model = GamePerformance
        fields = ('goals','owngoals','playerposition','winner','player','crawling') 
    
class GameSerializer(serializers.ModelSerializer):
    team1of = GamePerformanceSerializer()
    team1def = GamePerformanceSerializer()
    team2of = GamePerformanceSerializer()
    team2def = GamePerformanceSerializer()

    class Meta:
        model = Game
        fields = ('created','timestamp','team1of','team1def','team2of','team2def')

class RatingListSerializer(serializers.ModelSerializer):
    players = PlayerSerializer()

    class Meta:
        model = RatingList
        fields = ('timestamp')

class LastMonthRatingListSerializer(serializers.ModelSerializer):
    players = PlayerSerializer()

    class Meta:
        model = LastMonthRatingList
        fields = ('timestamp')