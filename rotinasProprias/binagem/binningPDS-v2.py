#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Ellipse
import matplotlib as mpl
import os; os.getcwd(); os.walk('.')
from matplotlib import rcParams
rcParams['ps.fonttype'] = 42 

from scipy.fftpack import fft, ifft

#### ======================= About this routine ============================= ####
####                                                                          ####
#### This is a routine to rebin data from a PDS previously created. There are ####
#### the linear rebin and the log-rebin subroutines.                          ####
####                                                                          ####
#### This Python routine is inspired in the old XANA and CROSSANA codes from  ####
#### the X-ray group from Univ. Amsterdam and Univ. Groningen and associates. ####
####                                                                          ####
#### We ackowledge prof. Mariano Méndez from Univ. Groningen for providing    ####
#### the FORTRAN 77 rebin code.                                               ####
####                                                                          ####
#### Author: Dr. Marcio G B de Avellar - astrophysicist and data scientist,   ####
#### learning python.                                                         ####
####                                                                          ####
#### Collaborator: Dr. Rodrigo A. de Souza - professional programmer, friend  ####
#### and teacher. Also an astrophysicist.                                     ####
####                                                                          ####
#### Ps. In the main function the user provides the rebinFactor variable that ####
####     must be an integer. We use the int() formatting to ensure this.      ####
####                                                                          ####
#### Ps. The input file can have a header, but must begin with a character to ####
####     differentiate the header lines, e.g., a "(" or a "#" etc, In which   ####
####     case the user must adapt the line "if line.startswith("("):" in MAIN. ###
####                                                                          ####
#### Ps. The input file, besides the header, must be structured in columns of ####
####     data. If it is a PDS, then the columns must be organized in one of   ####
####     the following ways that will be tested by the code:                  ####
####     - frequency, error in frequency, power, error in power               ####
####     - frequency, power, error in power (most commom case)                ####
####     - frequency, power                                                   ####
####                                                                          ####
#### Ps. This code can be improved. Suggestions are welcome.                  ####  
#### ======================================================================== ####


#### ======================= Begin defining functions =======================

def is_number(s):

    # Funtion for testing if a variable is a string or a number. Ps. Not used so far.

    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def linBinLogBin(s):

	# Funtion for testing if the rebin factor is positive (linear rebin flag) or negative (log-rebin flag)

	if (s == 0 or s == 1):
	
		print 'Rebin factor 0 or 1. No rebin at all. Nothing done, no output file generated.'
		sys.exit('Exit')

	elif (s > 1):

		print 'Rebin factor greater than 1. Linear rebinning.'
		print('\n')
		return True

	else:

		print 'Rebin factor less than 0. Logarithmic rebinning.'
		print('\n')
		return False

def LinearRebin(x,sx,y,sy,n,nr,irf):

	# Linear rebinning function

	# Receives the frequencies, their errors, the power, their errors, the number of data points, number of lines in the original file (is this necessary?) and the rebin factor

	xr = []
	yr = []
	sxr = []
	syr = []

	nrd = int(n / irf)

	if (nrd > nr):

		nrd = -1
		sys.exit('Error: binned number of lines greater than number of lines of the original file.')

	for i in range(0,nrd):  

		xs = 0.0
		ys = 0.0
		sx2 = 0.0
		sy2 = 0.0
		iss = 0.0

		for j in range(0,irf):

			if (float(sx[(i)*irf + j]) < 0):

				continue

			if (float(sy[(i)*irf + j]) < 0):

				continue


			xs = xs + float(x[(i)*irf + j])
			ys = ys + float(y[(i)*irf + j])
			sx2 = sx2 + float(sx[(i)*irf + j]) ** 2
			sy2 = sy2 + float(sy[(i)*irf + j]) ** 2
			iss = iss + 1

		if (iss > 0):

			xr.append( xs / float(iss) )
			yr.append( ys / float(iss) )
			sxr.append( np.sqrt(sx2) / float(iss) )
			syr.append( np.sqrt(sy2) / float(iss) )

		else:

			xr.append(0)
			yr.append(0)
			sxr.append(-1)
			syr.append(-1)



	return (xr, sxr, yr, syr, nrd)

def LogRebin(x,sx,y,sy,n,nr,irf):

	# Logarithmic rebinning function

	# Receives the frequencies, their errors, the power, their errors, the number of data points, number of lines in the original file (is this necessary?) and the rebin factor

	xr = []
	yr = []
	sxr = []
	syr = []
        
        i = 0
        nres = 1
        factor = 10.0 ** (1.0/(np.abs(float(irf))))
        
        nrd = 1 
        
        xend = float(x[i])
        
        while(xend == 0.0):
                
                xr.append(float(x[i]))
                yr.append(float(y[i]))
                sxr.append(float(sx[i]))
                syr.append(float(sy[i]))
                
                i = i + 1
                xend = float(x[i])
                
                nres = nres + 1
                if(nres > nr):
                    nrd = -1
                    sys.exit('nres > nr. Exit.')
                        
        else:
            
            xend = float(x[i]) * factor
            xs = float(x[i])
            ys = float(y[i])
            sx2 = float(sx[i]) ** 2
            sy2 = float(sy[i]) ** 2
            ns = 1
              
        while(i < n):
            
            for j in range(1,n):
            
                i = i + 1
                
                if(float(x[i-1]) > xend or i >= n):
                                        
                    xr.append(xs / float(ns))
                    yr.append(ys / float(ns))
                    sxr.append(np.sqrt(sx2) / float(ns))
                    syr.append(np.sqrt(sy2) / float(ns))
                    
                    nres = nres + 1
                    if(nres > nr):
                        nrd = -1
                        sys.exit('nres> nr. Exit')
                                            
                    xend = float(x[i-1]) * factor
                    xs = float(x[i-1])
                    ys = float(y[i-1])
                    sx2 = float(sx[i-1]) ** 2
                    sy2 = float(sy[i-1]) ** 2
                    
                    ns = 1
                    
                    break   
 
                else:
                    
                    xs = xs + float(x[i-1])
                    ys = ys + float(y[i-1])
                    sx2 = sx2 + float(sx[i-1]) ** 2
                    sy2 = sy2 + float(sy[i-1]) ** 2
                    ns = ns + 1
            
        # nres does in the log rebin function the role of nrd in the linear rebin function
	return (xr, sxr, yr, syr, nres)

#### ======================= End defining functions =======================

def main(argv):

	headers = []
	values = []

	nu = []
	errNu = []
	power = []
	errPower = []

	bNu = []
	bErrNu = []
	bPower = []
	bErrPower = []

	nrd = 0

	XX = []
	YY = []

	bXX = []
	bYY = []

	print('\n')

	with open("60032-01-19-00Comparison.asc", "r") as ins:

		for line in ins:
			#print line[0]
			
			if line.startswith("("):
				
				#header = re.sub('[!()]', '', line).strip()
				#header_items = re.split(r'\s{2,}', header)
				#headers.append(header_items)

				# Ps. the lines above were changed to the line below. We are not spliting the header anymore.
				
				header = line
				headers.append(header)
				
				#print(header_items)
				#print(headers)
			else:
				line_items = re.split(r' ', line.strip())
				values.append(line_items)
				#print(line_items)

				
	#print('Header[0] => {0} : {1}'.format(headers[0][0], headers[0][1]) )
	print('Header[0] Header[last line] => {0} , {1}'.format(headers[0], headers[len(headers)-1]) )
	print('\n')	
	print('Values[0] => col 0: {0}, col 1: {1}, col 2: {2}'.format(values[0][0], values[0][1], values[0][2]) )
	print('\n')
	
	numberCols = len(values[0])
	numberLines = len(values)

	# HERE THE USER PROVIDES THE REBINFACTOR: IF POSITIVE, THE ROUTINE WILL REBIN LINEARLY WITH THE FACTOR PROVIDED;
	# IF NEGATIVE, THE ROUTINE WILL REBIN LOGARITHMICALLY WITH THE FACTOR PROVIDED. 

	rebinFactor = int(-50)

	# BELOW, TESTING THE NUMBER OF COLUMNS OF DATA AND EXECUTING THE BINNING; WRITING IN AN OUTPUT FILE

	if (numberCols == 2):

		print 'Assuming columns [nu power]'
		print('\n')

		for i in range(0,numberLines):

			nu.append(float(values[i][0]))
			errNu = np.zeros(numberLines)
			power.append(float(values[i][1]))	
			errPower = np.zeros(numberLines)	

		if (linBinLogBin(rebinFactor)):

			bNu, bErrNu, bPower, bErrPower, nrd = LinearRebin(nu,errNu,power,errPower,numberLines,numberLines+len(headers),rebinFactor)

			file = open('BinnedData.asc', 'w+')

        		for i in range(0, len(headers)):
            			file.write('%s %s' % ('#', headers[i]))                
                
                
        		file.write('\n')

        		for i in range(0,nrd-1):

            			file.write("%5.5f \t %3.10f\n" % (bNu[i], bPower[i]) )
            
        		file.close()

		else:

			bNu, bErrNu, bPower, bErrPower, nrd = LogRebin(nu,errNu,power,errPower,numberLines,numberLines+len(headers),rebinFactor)

			file = open('BinnedData.asc', 'w+')

        		for i in range(0, len(headers)):
            			file.write('%s %s' % ('#', headers[i]))                
                
                
        		file.write('\n')

        		for i in range(0,nrd-1):

            			file.write("%5.5f \t %3.10f\n" % (bNu[i], bPower[i]) )
            
        		file.close()

	elif (numberCols == 3):

		print 'Assuming columns [nu power errPower]'
		print('\n')
		
		for i in range(0,numberLines):

			nu.append(float(values[i][0]))
			errNu = np.zeros(numberLines)
			power.append(float(values[i][1]))
			errPower.append(float(values[i][2]))
			
		if (linBinLogBin(rebinFactor)):

			bNu, bErrNu, bPower, bErrPower, nrd = LinearRebin(nu,errNu,power,errPower,numberLines,numberLines+len(headers),rebinFactor)

			file = open('BinnedData.asc', 'w+')

        		for i in range(0, len(headers)):
            			file.write('%s %s' % ('#', headers[i]))                
                
                
        		file.write('\n')

        		for i in range(0,nrd-1):

            			file.write("%5.5f \t %3.10f \t %3.10f\n" % (bNu[i], bPower[i], bErrPower[i]) )
            
        		file.close()

		else:
                        bNu, bErrNu, bPower, bErrPower, nrd = LogRebin(nu,errNu,power,errPower,numberLines,numberLines+len(headers),rebinFactor)

			file = open('BinnedData.asc', 'w+')

        		for i in range(0, len(headers)):
            			file.write('%s %s' % ('#', headers[i]))                
                
                
        		file.write('\n')

        		for i in range(0,nrd-1):

            			file.write("%5.5f \t %3.10f \t %3.10f\n" % (bNu[i], bPower[i], bErrPower[i]) )
            
        		file.close()

	elif (numberCols == 4):

		print 'Assuming columns [nu errNu power errPower]'
		print('\n')

		for i in range(0,numberLines):

			nu.append(float(values[i][0]))
			errNu.append(float(values[i][1]))
			power.append(float(values[i][2]))
			errPower.append(float(values[i][3]))

		if (linBinLogBin(rebinFactor)):

			bNu, bErrNu, bPower, bErrPower, nrd = LinearRebin(nu,errNu,power,errPower,numberLines,numberLines+len(headers),rebinFactor)

			file = open('BinnedData.asc', 'w+')

        		for i in range(0, len(headers)):
            			file.write('%s %s' % ('#', headers[i]))                
                
                
        		file.write('\n')

        		for i in range(0,nrd-1):

            			file.write("%5.5f \t %5.5f \t %3.10f \t %3.10f\n" % (bNu[i], bErrNu, bPower[i], bErrPower[i]) )
            
        		file.close()

		else:

			bNu, bErrNu, bPower, bErrPower, nrd = LogRebin(nu,errNu,power,errPower,numberLines,numberLines+len(headers),rebinFactor)

			file = open('BinnedData.asc', 'w+')

        		for i in range(0, len(headers)):
            			file.write('%s %s' % ('#', headers[i]))                
                
                
        		file.write('\n')

        		for i in range(0,nrd-1):

            			file.write("%5.5f \t %5.5f \t %3.10f \t %3.10f\n" % (bNu[i], bErrNu, bPower[i], bErrPower[i]) )
            
        		file.close()

	else:

		print 'Invalid file format in column numbers.'
		print 'Reshape your input file.'
		sys.exit('Exit')

	XX = np.asarray(nu)
	YY = np.asarray(power)

	bXX = np.asarray(bNu)
	bYY = np.asarray(bPower)

	fig1=plt.figure()
	#plt.axis([1, int(XX[nrd-2]), -0.01, 0.03])   # For axis in linear scale
	plt.axis([0.1, 5*int(bXX[nrd-2]), 0.000001, 1.0])   # For axis in log-scale
	plt.xlabel(r"$\nu$ [Hz]")
	plt.ylabel(r'Power')
	plt.title(r'Binned PDS')
	plt.plot(XX[1:len(nu)-1], XX[1:len(nu)-1]*YY[1:len(nu)-1], linestyle='steps', color='blue')
	plt.plot(bXX[1:nrd-2], bXX[1:nrd-2]*bYY[1:nrd-2], linestyle='steps', color='red')
	plt.yscale('log')
	plt.xscale('log')

	#fig1.savefig('fig_binned_data.png')
	fig1.savefig('fig_binned_data.pdf', format='pdf', dpi=1000)


if __name__ == "__main__":
    main(sys.argv[1:])
