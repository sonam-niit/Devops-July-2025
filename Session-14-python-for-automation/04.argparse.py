#making complex things using CLI
import argparse

parser= argparse.ArgumentParser("Sample Example for CLI")
parser.add_argument("name",help="Your Name")
parser.add_argument("age",type=int, help="Your Age")
parser.add_argument("--city",default="unknown",help="City you live in (Optional)")

args=parser.parse_args()

print(f" Hello {args.name}, age: {args.age} from {args.city}")

## Run with below commands
# py 04.argparse.py (you can see validation error for argumemt)
# py 04.argparse.py -h (see the help details)
# py 04.argparse.py "sonam soni" 45 (you can see the city unknows)
# py 04.argparse.py "sonam soni" 45 --city Mumbai