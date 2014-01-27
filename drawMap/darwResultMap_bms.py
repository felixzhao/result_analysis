import matplotlib
import matplotlib.pyplot as plt
beam_width = list(range(5,55,5))
beam_search = [0.0482, 0.0733, 0.0909, 0.1141, 0.1391, 0.1598, 0.168, 0.1862, 0.1956, 0.2137]
base_line = [0.0294, 0.0526, 0.0689, 0.0946, 0.1166, 0.1316, 0.1473, 0.1692, 0.183, 0.1987]
plt.plot(beam_width, base_line, label = 'Base Line')
plt.plot(beam_width, beam_search, label = 'Beam Search' , linestyle = '--', color = 'r')
plt.xticks(beam_width)
#plt.gca().invert_xaxis()
plt.xlabel("beam width")
plt.ylabel("match rate")
plt.legend(loc = 2)
plt.savefig('BMS.png')
plt.close()