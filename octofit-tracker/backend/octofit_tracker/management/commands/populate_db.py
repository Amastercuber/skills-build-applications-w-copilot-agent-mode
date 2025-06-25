from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **kwargs):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Populate users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password123"},
        ]
        for user in users:
            db.users.update_one({"email": user["email"]}, {"$set": user}, upsert=True)

        # Populate teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
            {"name": "Team Beta", "members": []},
        ]
        for team in teams:
            db.teams.update_one({"name": team["name"]}, {"$set": team}, upsert=True)

        # Populate activities
        activities = [
            {"activity_id": 1, "user": "john.doe@example.com", "type": "Running", "duration": 30, "date": "2025-06-01"},
            {"activity_id": 2, "user": "jane.smith@example.com", "type": "Cycling", "duration": 45, "date": "2025-06-02"},
        ]
        for activity in activities:
            db.activity.update_one({"activity_id": activity["activity_id"]}, {"$set": activity}, upsert=True)

        # Populate leaderboard
        leaderboard = [
            {"leaderboard_id": 1, "user": "john.doe@example.com", "score": 100},
            {"leaderboard_id": 2, "user": "jane.smith@example.com", "score": 150},
        ]
        for entry in leaderboard:
            db.leaderboard.update_one({"leaderboard_id": entry["leaderboard_id"]}, {"$set": entry}, upsert=True)

        # Populate workouts
        workouts = [
            {"workout_id": 1, "name": "Push-ups", "description": "Do 20 push-ups", "duration": 10},
            {"workout_id": 2, "name": "Sit-ups", "description": "Do 30 sit-ups", "duration": 15},
        ]
        for workout in workouts:
            db.workouts.update_one({"workout_id": workout["workout_id"]}, {"$set": workout}, upsert=True)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with test data."))
