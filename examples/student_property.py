"""A property with validation; underscores indicate convention, not access security."""
class Student:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be nonempty text.")
        self._name = value.strip()

if __name__ == "__main__":
    student = Student("Demo Student")
    print(student.name)
    student.name = "Updated Student"
    print(student.name)
