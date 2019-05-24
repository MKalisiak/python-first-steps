import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', type=int, nargs='+', help='an integer', metavar='N')
parser.add_argument('--sum', action='store_true', help='sum the integers')
parser.add_argument('--max', action='store_true', help='find max of the integers')
parser.add_argument('--min', action='store_true', help='find min of the integers')
parser.add_argument('-g', '--greeting', type=str, action='store', help='a greeting to display')

args = parser.parse_args()

if args.greeting:
    print(args.greeting)

print("Your provided integers:")
print(args.integers)
print()

if args.sum:
    print(f'Their sum: {sum(args.integers)}')

if args.max:
    print(f'Their max: {max(args.integers)}')

if args.min:
    print(f'Their min: {min(args.integers)}')