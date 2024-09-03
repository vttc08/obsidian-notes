import argparse

# Create the parser
parser = argparse.ArgumentParser(description='My command-line program')

# Parser Arguments
## positional arguments
parser.add_argument('input', help='Input file')
parser.add_argument('add', help='add the number by 10.20', type=int)
# these are required unless with nargs='?', can use type for integer, float
parser.add_argument('default', nargs='+', default='foobar', help='default value')
# nargs of ? means 0 or 1 argument, in this case, if no argument is given, default value is used
# nargs of + means 1 or more arguments, in this case, if no argument is given, error is raised
# nargs of * means 0 or more arguments, in this case, if no argument is given, default value is used, args are stored in a list

# optional arguments
parser.add_argument('-o', '--output', metavar='output_file', help='Output file', default='output.txt') 
# metavar is the name of the argument in the help message, eg -o output_file instead of -o
# -o and --output are both allowed
# the name of this argument would be output, and the value would be stored in args.output
parser.add_argument('-v', '--verbosity', action='store_true', help='increase output verbosity')
# action='store_true' means if -v is used, the value is set to True, else False
parser.add_argument('-m','--mode', choices=['read','write'], help='read or write mode')
# choices is used to limit the choices of the argument
parser.add_argument('-c', '--count', action='count', help='count the action', default=0)
# action='count' means if -c is used, the value is incremented by 1, else 0 (default)
# eg. -cccc will increment the value by 4 from the default value of 0

# mutually exclusive arguments
transfer = parser.add_mutually_exclusive_group()
transfer.add_argument('-f', '--sftp', action='store_true')
transfer.add_argument('-s', '--scp', action='store_true')
# only one of the arguments can be used, if -fs or -sf is used, error is raised

# Parse the arguments
args = parser.parse_args()

# Access the values
input_file = args.input
output_file = args.output
add = args.add

# Access a boolean argument
if args.scp:
    print('scp')

