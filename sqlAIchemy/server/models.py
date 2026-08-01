from datetime import date

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

ALLOWED_CATEGORIES = ["strength", "cardio", "flexibility", "balance"]


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False, nullable=False)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="exercise", cascade="all, delete-orphan"
    )
    workouts = association_proxy("workout_exercises", "workout")

    __table_args__ = (
        CheckConstraint("length(trim(name)) > 0", name="check_exercise_name_not_blank"),
    )

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name cannot be empty")
        return value.strip()

    @validates("category")
    def validate_category(self, key, value):
        if value not in ALLOWED_CATEGORIES:
            raise ValueError(f"category must be one of {ALLOWED_CATEGORIES}")
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "equipment_needed": self.equipment_needed,
        }


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="workout", cascade="all, delete-orphan"
    )
    exercises = association_proxy("workout_exercises", "exercise")

    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="check_workout_duration_positive"),
    )

    @validates("duration_minutes")
    def validate_duration_minutes(self, key, value):
        if value is None or value <= 0:
            raise ValueError("duration_minutes must be a positive integer")
        return value

    def to_dict(self, include_exercises=False):
        data = {
            "id": self.id,
            "date": self.date.isoformat() if self.date else None,
            "duration_minutes": self.duration_minutes,
            "notes": self.notes,
        }
        if include_exercises:
            data["workout_exercises"] = [we.to_dict() for we in self.workout_exercises]
        return data


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    __table_args__ = (
        CheckConstraint("reps IS NULL OR reps >= 0", name="check_reps_nonnegative"),
        CheckConstraint("sets IS NULL OR sets >= 0", name="check_sets_nonnegative"),
    )

    @validates("reps")
    def validate_reps(self, key, value):
        if value is not None and value < 0:
            raise ValueError("reps cannot be negative")
        return value

    @validates("sets")
    def validate_sets(self, key, value):
        if value is not None and value < 0:
            raise ValueError("sets cannot be negative")
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "workout_id": self.workout_id,
            "exercise_id": self.exercise_id,
            "reps": self.reps,
            "sets": self.sets,
            "duration_seconds": self.duration_seconds,
            "exercise": self.exercise.to_dict() if self.exercise else None,
        }