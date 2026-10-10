"""List, dictionary and set exercises using fictional data."""
def sorted_marks(values):
    values = list(values)
    if any(type(value) is not int or not 0 <= value <= 100 for value in values):
        raise ValueError('Marks must be integers from 0 to 100.')
    return sorted(values)


def language_directory(pairs):
    result = {}
    for name, language in pairs:
        name, language = name.strip(), language.strip()
        if not name or not language:
            raise ValueError('Name and language must be non-empty.')
        result[name] = language  # Repeated keys replace the earlier value.
    return result


if __name__ == '__main__':
    print('Sorted marks:', sorted_marks([85, 72, 91]))
    print('Directory:', language_directory([('Student A', 'Python'), ('Student A', 'C++')]))
    print('Equal numeric values collapse in a set:', len({70, '70', 70.0}))
