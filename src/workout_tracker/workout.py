from typing import List
from workout_tracker.exercises import Exercise

class Workout:
    """Different exercises put together to make a workout"""

    # creating an empty workout to store all the exercises
    def __init__(self):
        self._exercises: List[Exercise] = []

    # adds an exercise to the empty workout set
    def add_exercise(self, exercise: Exercise) -> None:
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to workout")
        self._exercises.append(exercise)

    # returns a copy of the exercise list 
    def get_exercises(self) -> List[Exercise]:
        return self._exercises.copy()

    # returns your total calories burned 
    def total_calories(self) -> float:
        return sum(ex.calculate_calories() for ex in self._exercises)

    # returns the total duration of your exercise in minutes 
    def total_duration(self) -> float:
        return sum(ex.get_duration() for ex in self._exercises)

    # returns the total number of exercises in your workout to you 
    def exercise_count(self) -> int:
        return len(self._exercises)

    # returns a fully formatted, detailed workout summary to you 
    def get_summary(self) -> str:
        if not self._exercises:
            return "Empty workout - no exercises added"
        
        lines = ["--- Workout Summary ---"]

        for i, exercise in enumerate(self._exercises, start=1):
            lines.append(f"{i}. {exercise}")

        lines.append(
            f"Total: {self.total_calories():.0f} calories, "
            f"{self.total_duration():.0f} minutes"
        )

        return "\n".join(lines)
    
    # returns just a one line workout summary to you 
    def __str__(self) -> str:
        return (
            f"Workout with {self.exercise_count()} exercises, "
            f"{self.total_calories():.0f} calories"
        )

    # returns the number of exercises 
    def __len__(self) -> int:
        return len(self._exercises)
    