"""Bounded star patterns, repaired from the supplied pattern.py exercise."""


def patterns(size):
    if type(size) is not int or not 1 <= size <= 50:
        raise ValueError('Size must be an integer from 1 to 50')
    pyramid = [' ' * (size-i) + '*' * (2*i-1) for i in range(1, size+1)]
    square = ['*' * size if row in (0, size-1) else '*' + ' ' * (size-2) + '*'
              for row in range(size)]
    return '\n'.join(pyramid), '\n'.join(square)


if __name__ == '__main__':
    try:
        for pattern in patterns(int(input('Size (1–50): '))):
            print(pattern, '\n')
    except ValueError as error:
        print(f'Error: {error}')
