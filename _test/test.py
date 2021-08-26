########################################################################################################################################
#  Copyright (c) 2021 Alrick Grandison                                                                                                 #
#                                                                                                                                      #
#  This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable             #
#  for any damages arising from the use of this software. Permission is granted to anyone to use this software for any                 #
#  purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:      #
#                                                                                                                                      #
#  1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software.                 #
#     If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.  #
#  2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.           #
#  3. This notice may not be removed or altered from any source distribution.                                                          #
#                                                                                                                                      #
#                                                                                                                                      #
#  filename: test.py                                                                                                                   #
#  created: 2021-08-24 10:20 PM                                                                                                        #
#                                                                                                                                      #
#  description: Python Unit Testing                                                                                                    #
#                                                                                                                                      #
########################################################################################################################################

''' Should be called by run.sh '''

import unittest
import os

inputtext = '''
# Python Scripts for General Use
Python 3 Scripts for General Use.

Major scripts are found in the [MajorScripts](MajorScripts) folder.  They are kept in their own folder.
Major scripts are the most powerful scripts.
Examples of major scripts are:

* [MajorScripts/BinaryToCArray](MajorScripts/BinaryToCArray)
* [MajorScripts/CenterText](MajorScripts/CenterText)
* [MajorScripts/TextToCComment](MajorScripts/TextToCComment)
* [MajorScripts/TextToCString](MajorScripts/TextToCString)

Minor scripts are kept in the [MinorScripts](MinorScripts) folder.  They are small and solve very small problems.

Both major and minor scripts are available for use to solve a wide range of problems.

Call [run.sh](run.sh) to run all the tests.
'''

bytestext = [
	0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 
	0x00, 0x0d, 0x49, 0x48, 0x44, 0x52, 0x00, 0x00, 0x00, 0x10, 
	0x00, 0x00, 0x00, 0x10, 0x08, 0x06, 0x00, 0x00, 0x00, 0x1f, 
	0xf3, 0xff, 0x61, 0x00, 0x00, 0x00, 0x04, 0x73, 0x42, 0x49, 
	0x54, 0x08, 0x08, 0x08, 0x08, 0x7c, 0x08, 0x64, 0x88, 0x00, 
	0x00, 0x00, 0x09, 0x70, 0x48, 0x59, 0x73, 0x00, 0x00, 0x00, 
	0x93, 0x00, 0x00, 0x00, 0x93, 0x01, 0x2b, 0xfb, 0xab, 0x90, 
	0x00, 0x00, 0x00, 0x19, 0x74, 0x45, 0x58, 0x74, 0x53, 0x6f, 
	0x66, 0x74, 0x77, 0x61, 0x72, 0x65, 0x00, 0x77, 0x77, 0x77, 
	0x2e, 0x69, 0x6e, 0x6b, 0x73, 0x63, 0x61, 0x70, 0x65, 0x2e, 
	0x6f, 0x72, 0x67, 0x9b, 0xee, 0x3c, 0x1a, 0x00, 0x00, 0x00, 
	0x31, 0x49, 0x44, 0x41, 0x54, 0x38, 0x8d, 0x63, 0xdc, 0xbc, 
	0x79, 0xf3, 0x7f, 0x06, 0x3c, 0xc0, 0xd7, 0xc7, 0x17, 0x9f, 
	0x34, 0x03, 0x13, 0x5e, 0x59, 0x22, 0xc0, 0xa8, 0x01, 0x83, 
	0xc1, 0x00, 0x46, 0x06, 0x86, 0xff, 0xf8, 0xd3, 0x81, 0xaf, 
	0x1f, 0x6d, 0x5d, 0x30, 0x6a, 0xc0, 0x60, 0x30, 0x00, 0x00, 
	0x12, 0xde, 0x07, 0x03, 0x0b, 0xe6, 0xec, 0x2f, 0x00, 0x00, 
	0x00, 0x00, 0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82
]

def prepareForTesting():
	with open('_test/input.txt', 'w') as f:
		f.write(inputtext)
	with open('_test/image.png', 'wb') as f:
		f.write(bytearray(bytestext))

class Test(unittest.TestCase):
	print('Setting up for tests')
	if not (os.path.exists('_test/input.txt') or os.path.exists('_test/image.png')):
		prepareForTesting()

class TestMajorBinaryToCArray(unittest.TestCase):
	os.system('python3 MajorScripts/BinaryToCArray/BinaryToCArray.py -i_test/image.png -o_test/test1.txt -thex')

class TestMajorCenterText(unittest.TestCase):
	os.system('python3 MajorScripts/CenterText/CenterText.py -i_test/input.txt -o_test/test2.txt')

class TestMajorTextToCComment(unittest.TestCase):
	os.system('python3 MajorScripts/TextToCComment/TextToCComment.py -i_test/input.txt -o_test/test3.txt')

class TestMajorTextToCString(unittest.TestCase):
	os.system('python3 MajorScripts/TextToCString/TextToCString.py -i_test/input.txt -o_test/test4.txt')

		

if __name__ == '__main__':
	unittest.main()




