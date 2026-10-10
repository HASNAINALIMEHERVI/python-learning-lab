"""Python 3.10 structural matching; fictional data only."""


def point_location(point):
    if not isinstance(point, (tuple, list)) or len(point) != 2 or any(type(v) is not int for v in point):
        raise ValueError('Use two integer coordinates')
    match point:
        case (0, 0):
            return 'Origin'
        case (0, y) if type(y) is int:
            return 'Y axis'
        case (x, 0) if type(x) is int:
            return 'X axis'
        case (x, y) if type(x) is int and type(y) is int:
            return 'Off axes'
        case _:
            raise ValueError('Use two integer coordinates')


def day_kind(day):
    match day.strip().casefold():
        case 'saturday' | 'sunday':
            return 'Weekend'
        case 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday':
            return 'Weekday'
        case _:
            raise ValueError('Use a full English weekday name')


if __name__ == '__main__':
    print(point_location((0, 0)))
    print(day_kind('Saturday'))
