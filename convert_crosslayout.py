#!/usr/bin/python


def convert_lefttop_modify(fname_read, fname_write, crossvalue):
	fw = open(fname_write, 'w')
	f = open(fname_read)
	data1 = f.read()
	f.close()

	lines1 = data1.split('\n') 
	for line in lines1:
		indexLeft = line.find('  Left = ')
		indexTop = line.find('  Top = ')
		indexWidth = line.find('  Width = ')
		indexHeight = line.find('  Height = ')
		indexFontHeight = line.find('  Font.Height = -')
		indexClientHeight = line.find('  ClientHeight = ')
		indexClientWidth = line.find('  ClientWidth = ')
		indexDefaultRowHeight = line.find('  DefaultRowHeight = ')
		indexDefaultColWidth = line.find('  DefaultColWidth = ')
		if indexLeft > -1:
			strval = line[indexLeft+9:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  Left = ' + str(int(val)) +'\n')
		elif indexTop > -1:
			strval = line[indexTop+8:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  Top = ' + str(int(val)) +'\n')
		elif indexWidth > -1:
			strval = line[indexWidth+10:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  Width = ' + str(int(val)) +'\n')
		elif indexHeight > -1:
			strval = line[indexHeight+11:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  Height = ' + str(int(val)) +'\n')
		elif indexFontHeight > -1:
			strval = line[indexFontHeight+17:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  Font.Height = -' + str(int(val)) +'\n')
		elif indexClientHeight > -1:
			strval = line[indexClientHeight+17:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  ClientHeight = ' + str(int(val)) +'\n')
		elif indexClientWidth > -1:
			strval = line[indexClientWidth+16:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  ClientWidth = ' + str(int(val)) +'\n')
		elif indexDefaultRowHeight > -1:
			strval = line[indexDefaultRowHeight+21:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  DefaultRowHeight = ' + str(int(val)) +'\n')
		elif indexDefaultColWidth > -1:
			strval = line[indexDefaultColWidth+20:]
			val = int(strval)
			val = val*crossvalue
			fw.write('  DefaultColWidth = ' + str(int(val)) +'\n')
		else:
			print (line)
			fw.write(line+'\n')

	
