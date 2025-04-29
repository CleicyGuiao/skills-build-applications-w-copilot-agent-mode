from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activity, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Usuários
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='senha123')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='senha456')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='senha789')

        # Times
        team1 = Team.objects.create(name='Team Octo')
        team2 = Team.objects.create(name='Team Fit')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Atividades
        Activity.objects.create(user=user1, type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, type='strength', duration=20, date=timezone.now())

        # Workouts
        Workout.objects.create(user=user1, description='Pushups and situps', date=timezone.now())
        Workout.objects.create(user=user2, description='Running intervals', date=timezone.now())
        Workout.objects.create(user=user3, description='Yoga and stretching', date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=100)

        self.stdout.write(self.style.SUCCESS('Dados de teste populados com sucesso!'))
#teste