import argparse
from pisanoLib import *
from sympy import pprint

parser = argparse.ArgumentParser(description="Process modulus and height for Pisano Array.")
parser.add_argument("modulus", type=int, help="The modulus value (must be an integer)")
parser.add_argument("height", type=int, help="The height value (must be an integer)")

args = parser.parse_args()
modulus = args.modulus
height = args.height

try:
  pprint(pisanoArray(modulus, height), use_unicode=True)
except InvalidHeightError as e:
  print(f"error: {e}")
  exit()
