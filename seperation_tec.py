import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0,1, 1001)
## michal testttttttttttttttt

x_feed = 0.05

## Stripping
x_strip = np.linspace(0.013739,x_feed,100)
y_strip = 2.019*x_strip - 0.014

## Rectifying Line
x_rect = np.linspace(x_feed, 0.6, 100)
y_rect = 0.93*x_rect + 0.04

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

plt.vlines(0.05, ymin=0, ymax=1, label = 'Feed - Line')
#plotting starting and ending point (if we want to add them)
# plt.plot(0.05 , start_point, 'o') 

def func_loop(xxxxxx):
    output = (-5000*xxxxxx)/(4773*xxxxxx-9730)
    return output
def func_loop2(xx):
    return 0.93*xx + 0.04

#Staircase
ini_val_loop = 0.6
ymin_storage = 0.6
xmin_val = func_loop(ini_val_loop)
plt.hlines(ini_val_loop, xmax=ini_val_loop, xmin=xmin_val)
for i in range(7):
    xmin_val = func_loop(ini_val_loop)
    plt.vlines(xmin_val, ymax=ini_val_loop, ymin=func_loop2(xmin_val))
    dummy_var =  func_loop(0.93*xmin_val+ 0.04)
    plt.hlines(func_loop2(xmin_val), xmax=xmin_val, xmin=dummy_var)   
    ini_val_loop = 0.93*xmin_val+ 0.04






plt.minorticks_on()
plt.grid(which = 'major', linewidth = 1)
plt.grid(which ='minor', linewidth = 0.1 )
plt.legend()
plt.title('')
plt.ylabel('xb,w')
plt.xlabel('xb,i')
plt.xlim(0.04,0.6)
plt.ylim(0.08,0.62)
plt.show()

