from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'https://organic-space-guide-wrv697j9j4529p9p-8000.app.github.dev/api/users/',
        'teams': 'https://organic-space-guide-wrv697j9j4529p9p-8000.app.github.dev/api/teams/',
        'activities': 'https://organic-space-guide-wrv697j9j4529p9p-8000.app.github.dev/api/activities/',
        'leaderboard': 'https://organic-space-guide-wrv697j9j4529p9p-8000.app.github.dev/api/leaderboard/',
        'workouts': 'https://organic-space-guide-wrv697j9j4529p9p-8000.app.github.dev/api/workouts/'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer