"""
Copyright (c) <'2020'> <'Alrick Grandison'>

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
"""

#CEnumToString.py
#This script converts c enum to string.

from __future__ import print_function
import os
import argparse as ap
import sys
import re
import pycparser


type_function = 'function'
type_array = 'array'
type_line = 'line'

TYPE_VALUES = [
	type_function,
	type_array,
	type_line
]

def Read(Path):
	if Path:
		with open(Path, 'r') as f:
			return f.read()
	else:
		return input('Enter String: ')

def Write(Text, Path):
	if Path:
		with open(Path, 'w') as f:
			f.write(Text)
	else:
		print(Text)

def CreateStringFromStringList(StringList, Separator=''):
	string = ''
	for i, item in enumerate(StringList):
		string += item
		if Separator and i < len(StringList) - 1:
			string += Separator
	return string

def getEnumValues(ast):
	values = []
	for astitem in ast.children():
		for decl in astitem:
			if type(decl) == pycparser.c_ast.Decl:
				for declitem in decl:
					if type(declitem) == pycparser.c_ast.Enum:
						enum = {}
						enum['name'] = declitem.name
						enum['values'] = []
						for enumerator in declitem.children():
							for eitem in enumerator:
								if type(eitem) == pycparser.c_ast.EnumeratorList:
									for item in eitem:
										enum['values'].append(item.name)
						values.append(enum)
	return values

def GenerateString(cmd, listvalues):
	for values in listvalues:
		values['result'] = values['values'].copy()
		
		if cmd.regex and len(cmd.regex) > 0:
			for regex in cmd.regex:
				regex = regex.strip('"').strip("'")
				print(f'applying re.sub("{regex}")')
				for i, name in enumerate(values['result']):
					values['result'][i] = re.sub(regex, '', name)
					
		
		if not cmd.eliminate.lower() == 'false':
			common = values['values'][0]
			for i, name in enumerate(values['values']):
				common = os.path.commonprefix([common, name])
			if common:
				for i, name in enumerate(values['result']):
					if common == name:
						continue
					if len(common) > len(name):
						continue
					else:
						values['result'][i] = name.replace(common, '')
						
		if not cmd.lowercase.lower() == 'false':
			for i, name in enumerate(values['result']):
				values['result'][i] = name.lower()
			
		if cmd.type == type_array:
			name = values['name']
			vlist = values['result']
			string = 'array'		
			if name: string = f'{name}_{string}'
			string = f'const char * {string} [] = '+'{' + '\n'
			for i, item in enumerate(vlist):
				text = '\"' + item + '\"'
				string += f'\t'+f'{text}'
				if i < len(vlist) - 1:
					string += ','
				string +='\n'
			string = f'{string}'+'}'
			Write(string, cmd.output)
		elif cmd.type == type_line:
			name = values['name']
			vlist = values['result']
			vkey = values['values']
			string = 'line'		
			if name: string = f'{name}_{string}'
			string = f'[{string}]' + '\n'
			for i, item in enumerate(vlist):
				text = '\"' + item + '\"'
				string += f'{text}' + '\n'
			Write(string, cmd.output)
		else:
			name = values['name']
			vlist = values['result']
			vkey = values['values']
			unnamed = '"--unnamed--"'
			string = 'getidstring'		
			if name: string = f'{name}_{string}'
			string = f'const char * {string} ( unsigned int id ) '+'{\n\tswitch(id){\n'
			for i, item in enumerate(vlist):
				text = '\"' + item + '\"'
				string += f'\t\tcase {vkey[i]}: return {text};\n'
			string = f'{string}'+'\t}\n\n\treturn '+f'{unnamed};'+'\n}'
			Write(string, cmd.output)

def CEnumFile(cmd):
	text = Read(cmd.input)
	listvalues = []
	try:
		parser = pycparser.CParser()
		ast = parser.parse(text, '')
		listvalues = getEnumValues(ast)
		print (f'parsed by pycparser: {listvalues}')
	except:
		wlist = list(set(re.findall(r"[_]*[A-Za-z][A-Za-z0-9_]*", text)))
		try:
			wlist.remove('enum')
		except:
			pass
		listvalues = [{'name':None, 'values':wlist}]
		print(f'parsed by regex: {listvalues}')
	
	GenerateString(cmd, listvalues)

def Interactive(cmd):
	text = 'dummy'
	while text and len(text) > 0:
		text = input('> ')
		listvalues = []
		try:
			parser = pycparser.CParser()
			ast = parser.parse(text, '')
			listvalues = getEnumValues(ast)
			print (f'parsed by pycparser: {listvalues}')
		except:
			wlist = list(set(re.findall(r"[_]*[A-Za-z][A-Za-z0-9_]*", text)))
			try:
				wlist.remove('enum')
			except:
				pass
			listvalues = [{'name':None, 'values':wlist}]
			print(f'parsed by regex: {listvalues}')
		
		GenerateString(cmd, listvalues)

def RunConsole():
	arg = ap.ArgumentParser(description='Converts C Enum to String.')
	arg.add_argument('-i', '--input', help='File path to read text from. ')
	arg.add_argument('-o', '--output', help='File path to write text to.')
	arg.add_argument('-t', '--type', default=type_function, choices=TYPE_VALUES, help='output String type')
	arg.add_argument('-e', '--eliminate', default='true', choices=['true', 'false'], help='eliminate common prefixes')
	arg.add_argument('-l', '--lowercase', default='true', choices=['true', 'false'], help='use lowercase strings')
	arg.add_argument('-r', '--regex', default=[], nargs = '*', help='re.sub([regex], \'\', [id]) is applied')
	cmd = arg.parse_args()
	
	if cmd.input:
		CEnumFile(cmd)
	else:
		Interactive(cmd)
	
	
	
if __name__ == '__main__':
	RunConsole()






















