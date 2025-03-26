import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()


year =[1972,1982,1992,2002,2012]
e_india = [100.6 , 158.61,305.54,394.3,724.5]
e_bangladesh = [10.5,25.21,58.65,64.1 , 100.3]
plt.plot(year,e_india, color = 'orange',linestyle = 'dashed', linewidth = 2 , label = 'India')
plt.plot(year , e_bangladesh , color = 'g' ,marker = 's' , markersize =8, label = 'Bangladesh')
plt.xlabel('Years')
plt.ylabel('Power consumption in  kWh')
plt.legend()
plt.title('Electricity consumption in India and Bangladesh')
