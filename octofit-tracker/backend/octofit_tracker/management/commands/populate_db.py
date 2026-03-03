from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captainamerica@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user_email='ironman@marvel.com', type='Running', duration=30, date=date.today())
        Activity.objects.create(user_email='captainamerica@marvel.com', type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user_email='batman@dc.com', type='Swimming', duration=60, date=date.today())

        # Create Workouts
        Workout.objects.create(name='Push Ups', description='Do 3 sets of 15 push ups', difficulty='Easy')
        Workout.objects.create(name='HIIT', description='20 min high intensity interval training', difficulty='Hard')

        # Create Leaderboard
        Leaderboard.objects.create(team_name='Marvel', points=150)
        Leaderboard.objects.create(team_name='DC', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
