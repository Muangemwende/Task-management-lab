#!/usr/bin/env python3
from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing tables...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    push_up = Exercise(name="Push Up", category="strength", equipment_needed=False)
    squat = Exercise(name="Squat", category="strength", equipment_needed=False)
    running = Exercise(name="Running", category="cardio", equipment_needed=False)
    deadlift = Exercise(name="Deadlift", category="strength", equipment_needed=True)
    plank = Exercise(name="Plank", category="balance", equipment_needed=False)
    db.session.add_all([push_up, squat, running, deadlift, plank])
    db.session.commit()

    print("Seeding workouts...")
    leg_day = Workout(date=date(2026, 7, 1), duration_minutes=45, notes="Leg day")
    full_body = Workout(date=date(2026, 7, 3), duration_minutes=60, notes="Full body")
    cardio_day = Workout(date=date(2026, 7, 5), duration_minutes=30, notes="Cardio")
    db.session.add_all([leg_day, full_body, cardio_day])
    db.session.commit()

    print("Seeding workout_exercises...")
    db.session.add_all([
        WorkoutExercise(workout_id=leg_day.id, exercise_id=squat.id, reps=12, sets=4),
        WorkoutExercise(workout_id=leg_day.id, exercise_id=deadlift.id, reps=8, sets=3),
        WorkoutExercise(workout_id=full_body.id, exercise_id=push_up.id, reps=15, sets=3),
        WorkoutExercise(workout_id=full_body.id, exercise_id=squat.id, reps=10, sets=3),
        WorkoutExercise(workout_id=full_body.id, exercise_id=plank.id, duration_seconds=60, sets=3),
        WorkoutExercise(workout_id=cardio_day.id, exercise_id=running.id, duration_seconds=1200),
    ])
    db.session.commit()

    print("Done seeding!")