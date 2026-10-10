"""Finally runs on both a successful return and an exception."""
def divide_with_cleanup(a, b, events):
    try:
        return a / b
    finally:
        events.append('cleanup')


if __name__ == '__main__':
    events = []
    print('Result:', divide_with_cleanup(10, 2, events))
    try:
        divide_with_cleanup(1, 0, events)
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    print('Cleanup events:', events)
