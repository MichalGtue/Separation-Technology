import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0,1, 1001)
## michal testttttttttttttttt

x_feed = 0.05
Aiso = 4.861
Biso = 1357.427
Ciso = -75.814
Aw = 5.0768
Bw = 1659.793
Cw = -45.854
Piso = 10**(Aiso - (Biso)/(Ciso + 81+273))
Pw = 10**(Aw - (Bw)/(Cw + 81+273))
alpha = Piso/Pw
print(alpha)
## Stripping
x_strip = np.linspace(0.013739,x_feed,100)
#y_strip = 2.019*x_strip - 0.014
y_strip = (185.96/92.1)*x_strip - ((93.86/92.1)*0.014)

## Rectifying Line
x_rect = np.linspace(x_feed, 0.6, 100)
#y_rect = 0.93*x_rect + 0.04
y_rect = (14.124/15.124)*x_rect + (0.6/15)

#equlibrium line
y = (1.946*x_values)/(1 + (1.9546-1)*x_values)


#rectafying line
def func_y_1(x):
    if x <= 0.6: 
        return 0.93*x + 0.04

y_1 = []

for i in range(len(x_values)):
    y_1.append(func_y_1(x_values[i]))

#starting point
start_point = (1.946*0.05)/(1 + (1.9546-1)*0.05)

#stripping line
def func_y_2(x):
    if x <= 0.3:
        return 2.019*x - 0.014

y_2 = []

for i in range(len(x_values)):
    y_2.append(func_y_2(x_values[i]))


#plotting the curves
plt.plot(x_values, y, label= 'Equlibrium Line', color = 'purple')
plt.plot(x_values, x_values, label = 'XY Line', color = 'black')
plt.plot(x_rect, y_rect, label = 'Rectifying Line', color = 'orange')
plt.plot(x_strip, y_strip, label = 'Stripping Line', color = 'green')

#feed line/ q- line 


plt.vlines(0.05, ymin=0, ymax=1, linestyles='dashed', label = 'Feed - Line')
#plotting starting and ending point (if we want to add them)
# plt.plot(0.05 , start_point, 'o') 

#Staircase

def func1(x):
    return (-5000 * x) / (4773 * x - 9730)
def func2(x):
    return 0.93 * x + 0.04
def func3(x):
    return (185.96/92.1)*x - ((93.86/92.1)*0.014)
initial_value = 0.6
y_min_storage = 0.6

x_min_value = func1(initial_value)
plt.hlines(initial_value, xmax=initial_value, xmin=x_min_value)

for _ in range(7):
    x_min_value = func1(initial_value)
    plt.vlines(x_min_value, ymax=initial_value, ymin=func2(x_min_value))
    new_y_value = func2(x_min_value)
    plt.hlines(new_y_value, xmax=x_min_value, xmin=func1(0.93 * x_min_value + 0.04))
    initial_value = 0.93 * x_min_value + 0.04

for _ in range(8):
    x_min_value = func1(initial_value)
    plt.vlines(x_min_value, ymax=initial_value, ymin=func3(x_min_value))
    new_y_value = func3(x_min_value)
    if _ <7:
        plt.hlines(new_y_value, xmax=x_min_value, xmin=func1((185.96/92.1)*x_min_value - ((93.86/92.1)*0.014)))
    initial_value = (185.96/92.1)*x_min_value - ((93.86/92.1)*0.014)

plt.vlines(0.014, ymin=0, ymax=1, linestyles='dashed', colors='teal', label='x-bottom')
# Show the plot
plt.minorticks_on()
plt.grid(which = 'major', linewidth = 1)
plt.grid(which ='minor', linewidth = 0.1 )
plt.legend()
plt.title('')
plt.ylabel('x, i')
plt.xlabel('y,i')
plt.xlim(0.04,0.6)
plt.ylim(0.08,0.62)
plt.show()

