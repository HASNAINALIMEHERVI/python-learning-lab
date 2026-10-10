"""Enumerate returns an index and value without a separate counter."""
def indexed_values(values, start=0):
    if type(start) is not int:
        raise ValueError('Start must be an integer.')
    return list(enumerate(values, start=start))


if __name__ == '__main__':
    for index, fruit in indexed_values(['apple', 'banana', 'mango'], start=1):
        print(index, fruit)
