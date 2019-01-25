import math
const = (math.pi/180)
print("%70s"%'Pulse Code Modulation of Sinusoidal Wave')
w = int(input('Enter the frequency of input signal(rad/s)\n'))  #frequncy
a = int(input('Enter the amplitude of sin wave\n'))     #amplitude
fi = int(input('Enter the phase angle(in degrees)\n'))  #phase
sf = int(input('Enter the sampling frequency\n'))      #sampling frequency
if sf < 1:
    print('Error')
    exit(1)
n = int(input('Enter the no. of quantization levels\n'))
if n < 1:
    print('Error in input')
    exit(1)
print('Input Signal -')
print('%dsin(%dt+rad(%d))'%(a, w, fi))
digits = math.ceil(math.log(n, 2))
t = 0.0
theta = w*t+fi*const
val = []
add = 1/sf
for i in range(sf):
    val.append(a*math.ceil(math.sin(w*t+fi*const)*100)/100)
    t += add
print('Sampled values (for one time period)- ')
print(val)
add2 = 2*a/(n-1)
levels = []
for i in range(n):
    levels.append(math.ceil((-a+i*add2)*100)/100)
print('Quantization levels - ')
print(levels)
encoded = val.copy()
binary = []
for i in range(sf):
    for j in range(n-1):
        mid = (levels[j]+levels[j+1])/2
        if levels[j]<= val[i] and val[i] < mid:
            encoded[i] = levels[j]
            binary.append(j)
            break
        elif mid <= val[i] and val[i] <= levels[j+1]:
            encoded[i] = levels[j+1]
            binary.append(j+1)
            break
print('Quantized values - ')
print(encoded)
print('Corresponding level no. (starting from 0)-')
print(binary)
print('Encoded binary message')
for i in range(sf):
    temp = format(binary[i], 'b')
    while len(temp) < digits:
        temp = '0'+temp
    print(temp, end=' ')
x = input('\nPress enter to exit\n')
