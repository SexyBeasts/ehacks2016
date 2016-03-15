import wave
import numpy as np
# Read in a WAV and find the freq's
def freqCount(filename):
	noteFrequencyList = []
	chunk = 8192
	# open up a wave
	wf = wave.open(filename, 'rb')
	swidth = wf.getsampwidth()
	RATE = wf.getframerate()
	# use a Blackman window
	window = np.blackman(chunk)
	# read some data
	data = wf.readframes(chunk)
	# play stream and find the frequency of each chunk
	FrequencyList = []
	while  len(data) == chunk*swidth*wf.getnchannels():
	  # unpack the data and times by the hamming window
	  indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),data))*window
	  # Take the fft and square each value
	  fftData=abs(np.fft.rfft(indata))**2
	  # find the maximum
	  which = fftData[1:].argmax() + 1
	  # use quadratic interpolation around the max
	  if which != len(fftData)-1:
		  y0,y1,y2 = np.log(fftData[which-1:which+2:])
		  x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
		  # find the frequency and output it
		  thefreq = (which + x1) * RATE / chunk
		  FrequencyList.append(thefreq)
	  else:
		  thefreq = which*RATE/chunk
		  FrequencyList.append(thefreq)
	  # read some more data
	  data = wf.readframes(chunk)
	
	for i in range(len(FrequencyList)):
		if((FrequencyList[1] < 16.835) or ((FrequencyList[i]>31.78) and (FrequencyList[i]<33.67)) or ((FrequencyList[i]>63.575) and (FrequencyList[i]<67.355))or((FrequencyList[i]>127.14) and (FrequencyList[i]<134.705)) or ((FrequencyList[i]>254.285) and (FrequencyList[i]<269.405)) or ((FrequencyList[i]>508.565) and (FrequencyList[i]<538.805)) or ((FrequencyList[i]>1017.135) and (FrequencyList[i]<1077.615)) or ((FrequencyList[i]>2034.27) and (FrequencyList[i]<2155.235)) or ((FrequencyList[i]>4068.54) and (FrequencyList[i]<4310.465)) or ((FrequencyList[i]>8137.076) and (FrequencyList[i]<8620.93)) or (FrequencyList[i]>16000)):
			noteFrequencyList.append('C')
		elif((FrequencyList[i]>16.835 and FrequencyList[i]<17.835) or (FrequencyList[i]>33.67 and FrequencyList[i]<35.675)or(FrequencyList[i]>67.355 and FrequencyList[i]<71.36) or (FrequencyList[i]>134.705 and FrequencyList[i]<142.715) or (FrequencyList[i]>269.405 and FrequencyList[i]<285.42) or (FrequencyList[i]>538.805 and FrequencyList[i]<570.845) or (FrequencyList[i]>1077.615 and FrequencyList[i]<1141.69) or (FrequencyList[i]>2155.235 and FrequencyList[i]<2283.39) or (FrequencyList[i]>4310.465 and FrequencyList[i]<4566.78) or (FrequencyList[i]>8620.93 and FrequencyList[i]<9133.555)):
			noteFrequencyList.append('C#')
		elif((FrequencyList[i]>17.835 and FrequencyList[i]<18.895) or (FrequencyList[i]>35.675 and FrequencyList[i]<37.805)or(FrequencyList[i]>71.36 and FrequencyList[i]<75.6) or (FrequencyList[i]>142.715 and FrequencyList[i]<151.195) or (FrequencyList[i]>285.42 and FrequencyList[i]<302.395) or (FrequencyList[i]>570.845 and FrequencyList[i]<604.79) or (FrequencyList[i]>1141.69 and FrequencyList[i]<1209.58) or (FrequencyList[i]>2283.39 and FrequencyList[i]<2419.17) or (FrequencyList[i]>4566.78 and FrequencyList[i]<4838.335) or (FrequencyList[i]>9133.555 and FrequencyList[i]<9676.665)):
			noteFrequencyList.append('D')
		elif((FrequencyList[i]>18.895 and FrequencyList[i]<20.02) or (FrequencyList[i]>37.805 and FrequencyList[i]<40.05)or(FrequencyList[i]>75.6 and FrequencyList[i]<80.095) or (FrequencyList[i]>151.195 and FrequencyList[i]<160.185) or (FrequencyList[i]>302.395 and FrequencyList[i]<320.375) or (FrequencyList[i]>604.79 and FrequencyList[i]<640.75) or (FrequencyList[i]>1209.58 and FrequencyList[i]<1281.51) or (FrequencyList[i]>2419.17 and FrequencyList[i]<2563.02) or (FrequencyList[i]>4838.335 and FrequencyList[i]<5126.035) or (FrequencyList[i]>9676.665 and FrequencyList[i]<10252.07)):
			noteFrequencyList.append('D#')
		elif((FrequencyList[i]>20.02 and FrequencyList[i]<21.215) or (FrequencyList[i]>40.05 and FrequencyList[i]<42.425)or(FrequencyList[i]>80.095 and FrequencyList[i]<84.86) or (FrequencyList[i]>160.185 and FrequencyList[i]<169.71) or (FrequencyList[i]>320.375 and FrequencyList[i]<339.42) or (FrequencyList[i]>640.75 and FrequencyList[i]<678.85) or (FrequencyList[i]>1281.51and FrequencyList[i]<1357.71) or (FrequencyList[i]>2563.02 and FrequencyList[i]<2715.425) or (FrequencyList[i]>5126.035 and FrequencyList[i]<5430.845) or (FrequencyList[i]>10252.07 and FrequencyList[i]<10861.69)):
			noteFrequencyList.append('E')
		elif((FrequencyList[i]>21.215 and FrequencyList[i]<22.475) or (FrequencyList[i]>42.425 and FrequencyList[i]<44.945)or(FrequencyList[i]>84.86 and FrequencyList[i]<89.905) or (FrequencyList[i]>169.71 and FrequencyList[i]<179.805) or (FrequencyList[i]>339.42 and FrequencyList[i]<359.605) or (FrequencyList[i]>678.85 and FrequencyList[i]<719.22) or (FrequencyList[i]>1357.71 and FrequencyList[i]<1438.445) or (FrequencyList[i]>2715.425 and FrequencyList[i]<2876.895) or (FrequencyList[i]>5430.845 and FrequencyList[i]<5753.78) or (FrequencyList[i]>10861.69 and FrequencyList[i]<11507.56)):
			noteFrequencyList.append('F')
		elif((FrequencyList[i]>22.475 and FrequencyList[i]<23.81) or (FrequencyList[i]>44.945 and FrequencyList[i]<47.62)or(FrequencyList[i]>89.905 and FrequencyList[i]<95.25) or (FrequencyList[i]>179.805 and FrequencyList[i]<190.5) or (FrequencyList[i]>359.605 and FrequencyList[i]<380.99) or (FrequencyList[i]>719.22 and FrequencyList[i]<761.99) or (FrequencyList[i]>1438.445 and FrequencyList[i]<1523.98) or (FrequencyList[i]>2876.895 and FrequencyList[i]<3047.96) or (FrequencyList[i]>5753.78 and FrequencyList[i]<6095.92) or (FrequencyList[i]>11507.56 and FrequencyList[i]<12191.8)):
			noteFrequencyList.append('F#')
		elif((FrequencyList[i]>23.81 and FrequencyList[i]<25.23) or (FrequencyList[i]>47.62 and FrequencyList[i]<50.455)or(FrequencyList[i]>95.25 and FrequencyList[i]<100.915) or (FrequencyList[i]>190.5 and FrequencyList[i]<201.825) or (FrequencyList[i]>380.99 and FrequencyList[i]<403.65) or (FrequencyList[i]>761.99 and FrequencyList[i]<807.3) or (FrequencyList[i]>1523.98 and FrequencyList[i]<1614.6) or (FrequencyList[i]>3047.96 and FrequencyList[i]<3229.2) or (FrequencyList[i]>6095.92 and FrequencyList[i]<6458.405) or (FrequencyList[i]>12191.8 and FrequencyList[i]<12916.8)):
			noteFrequencyList.append('G')
		elif((FrequencyList[i]>25.23 and FrequencyList[i]<26.73) or (FrequencyList[i]>50.455 and FrequencyList[i]<53.455)or(FrequencyList[i]>100.915 and FrequencyList[i]<106.915) or (FrequencyList[i]>201.825 and FrequencyList[i]<213.825) or (FrequencyList[i]>403.65 and FrequencyList[i]<427.655) or (FrequencyList[i]>807.3 and FrequencyList[i]<855.305) or (FrequencyList[i]>1614.6 and FrequencyList[i]<1710.61) or (FrequencyList[i]>3229.2 and FrequencyList[i]<3421.22) or (FrequencyList[i]>6458.405 and FrequencyList[i]<6824.44) or (FrequencyList[i]>12916.8 and FrequencyList[i]<13684.88)):
			noteFrequencyList.append('G#')
		elif((FrequencyList[i]>26.73 and FrequencyList[i]<28.3175) or (FrequencyList[i]>53.455 and FrequencyList[i]<56.635)or(FrequencyList[i]>106.915 and FrequencyList[i]<113.27) or (FrequencyList[i]>213.825 and FrequencyList[i]<226.54) or (FrequencyList[i]>427.655 and FrequencyList[i]<453.082) or (FrequencyList[i]>855.305 and FrequencyList[i]<906.165) or (FrequencyList[i]>1710.61 and FrequencyList[i]<1812.33) or (FrequencyList[i]>3421.22 and FrequencyList[i]<3624.555) or (FrequencyList[i]>6824.44 and FrequencyList[i]<7249.31) or (FrequencyList[i]>13684.88 and FrequencyList[i]<13684.88)):
			noteFrequencyList.append('A')
		elif((FrequencyList[i]>28.3175 and FrequencyList[i]<29.9975) or (FrequencyList[i]>56.635 and FrequencyList[i]<60.005)or(FrequencyList[i]>113.27 and FrequencyList[i]<120.005) or (FrequencyList[i]>226.54 and FrequencyList[i]<240.01) or (FrequencyList[i]>453.082 and FrequencyList[i]<480.022) or (FrequencyList[i]>906.165 and FrequencyList[i]<960.05) or (FrequencyList[i]>1812.33 and FrequencyList[i]<1920.095) or (FrequencyList[i]>3624.555 and FrequencyList[i]<3840.19) or (FrequencyList[i]>7249.31 and FrequencyList[i]<7680.376) or (FrequencyList[i]>13684.88 and FrequencyList[i]<14498.5)):
			noteFrequencyList.append('A#')
		else:
			noteFrequencyList.append('B')
	
	return noteFrequencyList