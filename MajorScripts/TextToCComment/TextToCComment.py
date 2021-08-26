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

#TextToCComment.py
#This script converts any binary data into a 'C array'.  This array can be accessed normally in 'C code'.

import os
import argparse as ap
import sys

def Read(Path):
	if Path:
		with open(Path, 'r') as f:
			return f.read()
	else:
		return input('Enter string: ')

def Write(Path, Text):
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

def GetMaxLengthFromStringList(StringList):
	maxlength = 0
	for string in StringList:
		length = len(string)
		if length > maxlength: maxlength = length
	return maxlength

def GetCenterOffsetForString(String, MaxLength):
	length = len(String)
	return int(round((MaxLength / 2.0 - length / 2.0), 0))

def CreateCenteredText(Text):
	centeredtextList = []
	lines = Text.splitlines()
	maxlength = GetMaxLengthFromStringList(lines)
	for line in lines:
		offset = GetCenterOffsetForString(line, maxlength)
		string = (' ' * offset) + line
		centeredtextList.append(string)
	return CreateStringFromStringList(centeredtextList, '\n')

def CenterText(Text, Center):
	if Center: 
		return CreateCenteredText(Text)
	return Text

def CreateCommentedString(String, Type):
	if Type == 'line': return '//' + String
	if Type == 'line-fancy': return '//  ' + String + '  //'
	if Type == 'block': return String
	if Type == 'block-fancy': return '/* ' + String + ' */'
	print ('TextToCComment.py::Error: unknown type [%s]' % Type)
	exit()

def CreateCommentBegin(Type, MaxLength):
	if Type == 'line': return ''
	if Type == 'line-fancy': return '//' + ('/' * (MaxLength + 4)) + '//'
	if Type == 'block': return '/*'
	if Type == 'block-fancy': return '/*' + ('*' * (MaxLength + 2)) + '*/'
	print ('TextToCComment.py::Error: unknown type [%s]' % Type)
	exit()

def CreateCommentEnd(Type, MaxLength):
	if Type == 'line': return ''
	if Type == 'line-fancy': return '//' + ('/' * (MaxLength + 4)) + '//'
	if Type == 'block': return '*/'
	if Type == 'block-fancy': return '/*' + ('*' * (MaxLength + 2)) + '*/'
	print ('TextToCComment.py::Error: unknown type [%s]' % Type)
	exit()

def CreateComment(Text, Type):
	commentList = []
	Text = Text.expandtabs()
	lines = Text.splitlines()
	maxlength = GetMaxLengthFromStringList(lines)
	begin = CreateCommentBegin(Type, maxlength)
	end = CreateCommentEnd(Type, maxlength)
	for line in lines:
		string = line + (' ' * (maxlength - len(line)))
		commentedstring = CreateCommentedString(string, Type)
		commentList.append(commentedstring)
	if begin: commentList.insert(0, begin)
	if end: commentList.append(end)
	return CreateStringFromStringList(commentList, '\n')

def RunConsole():
	arg = ap.ArgumentParser(description='Converts a text to C comment.')
	arg.add_argument('-i', '--input', help='File path to read text from.')
	arg.add_argument('-o', '--output', help='File path to write text to.')
	arg.add_argument('-t', '--type', default='line', choices=['line', 'block', 'block-fancy', 'line-fancy'], help='Comment type. Default:\'line\'', type=str)
	arg.add_argument('-c', '--center', action='store_true', help='Center text. Default:False.')
	cmd = arg.parse_args()
	text = Read(cmd.input)
	text = CenterText(text, cmd.center)
	comment = CreateComment(text, cmd.type)
	Write(cmd.output, comment)

if __name__ == '__main__':
	RunConsole()
