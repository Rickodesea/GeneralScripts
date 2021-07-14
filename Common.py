import argparse

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

def argparse_addArgument_IO(parser):
	parser.add_argument('-i', '--input', help='File to read the input data from.  Otherwise, input from stdin.')
	parser.add_argument('-o', '--output', help='File to write the output to.  Otherwise, output to stdout.')

def Print(f, text):
	if f:
		f.write(text)
	else:
		print(text, end='')

def PrintLn(f, text):
	if f:
		f.write(f'{text}\n')
	else:
		print(text)

def Open(filename):
	with open(filename) as f:
		return f
	return None

def Read(filename):
	with open(filename) as f:
		return f.read()
	return ''
