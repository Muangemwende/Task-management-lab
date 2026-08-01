Workout Tracker API
Description
A Flask + SQLAlchemy backend API for a workout tracking application used by personal trainers. Trainers can create workouts, create reusable exercises, and attach exercises to workouts with reps/sets/duration data.

Entities: Exercise, Workout, WorkoutExercise (join table, many-to-many between Workout and Exercise).

Installation
pipenv install
pipenv shell
cd server
flask db init
flask db migrate -m "initial migration"
flask db upgrade head
python seed.py
Running the App
cd server
flask run -p 5555
Endpoints
Method	Route	Description
GET	/workouts	List all workouts
GET	/workouts/<id>	Get a single workout, including its exercises (reps/sets/duration)
POST	/workouts	Create a workout (date, duration_minutes, notes)
DELETE	/workouts/<id>	Delete a workout and its associated WorkoutExercises
GET	/exercises	List all exercises
GET	/exercises/<id>	Get a single exercise, including associated workouts
POST	/exercises	Create an exercise (name, category, equipment_needed)
DELETE	/exercises/<id>	Delete an exercise and its associated WorkoutExercises
POST	/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises	Add an exercise to a workout (reps, sets, duration_seconds)
Validations
Table constraints: exercise name not blank, workout duration_minutes > 0, reps/sets non-negative.
Model validations: exercise name required, category must be one of strength/cardio/flexibility/balance, workout duration must be positive, reps/sets can't be negative.
Schema validations: required fields on create, category restricted via OneOf, numeric fields restricted via Range.