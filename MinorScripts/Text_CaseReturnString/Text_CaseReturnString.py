import argparse
import re

def readtext():
	with open("text.txt", "r") as f:
		return f.read();
	return ""

def readremove():
	with open("remove.txt", "r") as f:
		return f.read();
	return ""

def readignore():
	with open("ignore.txt", "r") as f:
		return f.read();
	return ""

def write(name, slist):
	with open(name, "w") as f:
		for s in slist:
			f.write(s + "\n")

def main():
	arg = argparse.ArgumentParser(description='Generate "case w: return s;" from text and format.\nText has w and Format converts w to s.')
	arg.add_argument('-o', '--output', help='File to write the output to.  Otherwise, output to stdout.')
	cmd = arg.parse_args()
	
	text = readtext()
	remove = readremove();
	ignore = readignore();
	
	wlist = re.sub("[^\w]", " ",  text).split()
	ilist = re.sub("[^\w]", " ",  ignore).split()
	rlist = re.sub("[^\w]", " ",  remove).split()
	wlist.append('12345') #bug where the last item is not printed
	
	result = []
	
	for w in wlist:
		if not w.isidentifier():
			continue
		if w in ilist:
			continue
		
		string = w		
		for r in rlist:
			pos = string.find(r)
			if pos == 0:
				string = string.replace(r, "")
		
		string = string.lower()
		string = string.replace("_", "-")
		
		text = f'case {w}: return "{string}";'
		text = "\t\t" + text
		
		result.append(text)
	if cmd.output:
		write(cmd.output, result)
	else:
		for r in result:
			print(r)
	
if __name__ == "__main__":
	main()
