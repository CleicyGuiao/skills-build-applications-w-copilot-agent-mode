# Test data for Octofit (adaptado do exemplo MonaFit)
# Este arquivo serve apenas para referência dos dados de teste usados no populate_db.py

TEST_USERS = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

TEST_TEAMS = [
    {"name": "Blue Team"},
    {"name": "Gold Team"},
]

TEST_ACTIVITIES = [
    {"user": 0, "activity_type": "Cycling", "duration": 60},
    {"user": 1, "activity_type": "Crossfit", "duration": 120},
    {"user": 2, "activity_type": "Running", "duration": 90},
    {"user": 3, "activity_type": "Strength", "duration": 30},
    {"user": 4, "activity_type": "Swimming", "duration": 75},
]

TEST_LEADERBOARD = [
    {"user": 0, "score": 100},
    {"user": 1, "score": 90},
    {"user": 2, "score": 95},
    {"user": 3, "score": 85},
    {"user": 4, "score": 80},
]

TEST_WORKOUTS = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
