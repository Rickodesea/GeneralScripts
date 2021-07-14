import Common
import argparse

def gen(cmdl, out, text):
	if cmdl.group: Common.Print(out, '(')
	for c in text.strip():
		if c.isalpha():
			Common.Print(out, f'[{c.upper()}{c.lower()}]')
		else:
			Common.Print(out, f'[{c}]')
	if cmdl.group: Common.Print(out, ')')
	Common.PrintLn(out, '')

def gen_lines(cmdl, out, text):
	lines = text.splitlines()
	for line in lines:
		gen(cmdl, out, line)

def main():
	parser = argparse.ArgumentParser(description='Generate Regular Expression rule for parsing a string of any letter case. Data is separated by lines.')
	Common.argparse_addArgument_IO(parser)
	parser.add_argument('-g', '--group', action='store_true', help='Group the generated regex.  Default is ungroup.')
	cmdl = parser.parse_args()
	if cmdl.input and cmdl.output:
		itext = Common.Read(cmdl.input)
		out = Common.Open(cmd.output)
		gen_lines(cmdl, out, itext)
	elif cmdl.input:
		itext = Common.Read(cmdl.input)
		gen_lines(cmdl, None, itext)
	else:
		while True:
			itext = input('> ')
			if itext:
				gen_lines(cmdl, None, itext)
			else:
				break

if __name__ == '__main__':
	main()







