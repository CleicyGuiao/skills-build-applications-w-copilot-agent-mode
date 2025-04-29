from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId
from django.utils import timezone

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activity, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Conecta ao MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], int(settings.DATABASES['default']['CLIENT']['port']))
        db = client[settings.DATABASES['default']['NAME']]

        # Limpa as coleções
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Usuários
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Times
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        blue_team.save()
        gold_team.save()
        blue_team.members.add(*users)
        gold_team.members.add(*users)

        # Atividades
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=60, date=timezone.now()),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=120, date=timezone.now()),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=90, date=timezone.now()),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=30, date=timezone.now()),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=75, date=timezone.now()),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], description='Cycling Training', date=timezone.now()),
            Workout(_id=ObjectId(), user=users[1], description='Crossfit', date=timezone.now()),
            Workout(_id=ObjectId(), user=users[2], description='Running Training', date=timezone.now()),
            Workout(_id=ObjectId(), user=users[3], description='Strength Training', date=timezone.now()),
            Workout(_id=ObjectId(), user=users[4], description='Swimming Training', date=timezone.now()),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Dados de teste populados com sucesso!'))