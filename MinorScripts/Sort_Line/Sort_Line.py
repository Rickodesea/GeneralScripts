import argparse
import re

def readtext_lines():
	with open("text.txt", "r") as f:
		return f.readlines();
	return ""

def write(name, slist):
	with open(name, "w") as f:
		for s in slist:
			f.write(s + "\n")

def main():
	arg = argparse.ArgumentParser(description='Sort Lines Alphabetically')
	arg.add_argument('-o', '--output', help='File to write the output to.  Otherwise, output to stdout.')
	cmd = arg.parse_args()
	
	textlines = readtext_lines()
	sortedlines = sorted(textlines)
	for i in range(len(sortedlines)):
		print(f'{sortedlines[i].strip()}')
	
if __name__ == "__main__":
	main()
