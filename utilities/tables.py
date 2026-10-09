"""Generate multiplication tables without overwriting existing files."""
import argparse
from pathlib import Path


def generate(start, end, rows, directory):
    if not (1 <= start <= end <= 1000 and 1 <= rows <= 1000):
        raise ValueError('Use 1 <= start <= end <= 1000 and 1 <= rows <= 1000')
    directory = Path(directory)
    targets = [directory / f'table_{n}.txt' for n in range(start, end + 1)]
    if any(p.exists() for p in targets):
        raise FileExistsError('An output already exists; choose a new directory')
    directory.mkdir(parents=True, exist_ok=True)
    for number, target in zip(range(start, end + 1), targets):
        with target.open('x', encoding='utf-8') as stream:
            stream.write(''.join(f'{number} × {i} = {number*i}\n' for i in range(1, rows+1)))
    return targets


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=int, default=1)
    parser.add_argument('--end', type=int, default=20)
    parser.add_argument('--rows', type=int, default=10)
    parser.add_argument('--output', type=Path, default=Path('generated-tables'))
    args = parser.parse_args()
    try:
        print(f'Created {len(generate(args.start, args.end, args.rows, args.output))} tables')
    except (ValueError, OSError) as error:
        parser.exit(2, f'Error: {error}\n')
