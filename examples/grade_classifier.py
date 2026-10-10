"""Fictional grading exercise; not UET's official grading policy."""


def classify(marks):
    if type(marks) is not int or not 0 <= marks <= 100:
        raise ValueError('Marks must be an integer from 0 to 100')
    for cutoff, grade in [(90, 'A+'), (80, 'A'), (70, 'B'), (60, 'C'), (50, 'D')]:
        if marks >= cutoff:
            return grade
    return 'F'


if __name__ == '__main__':
    try:
        print('Demo grade:', classify(int(input('Marks (0–100): '))))
    except ValueError as error:
        print(f'Error: {error}')
