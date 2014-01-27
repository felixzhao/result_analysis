import matplotlib
import matplotlib.pyplot as plt
beam_width = [4, 3, 2, 1]
beam_search = [0.1141, 0.1868, 0.3354, 0.4489]
base_line =   [0.0526, 0.0946, 0.0946, 0.0946]
plt.plot(beam_width, base_line, label = 'Base Line')
plt.plot(beam_width, beam_search, label = 'Beam Search' , linestyle = '--', color = 'r')
plt.xticks(beam_width)
plt.gca().invert_xaxis()
plt.xlabel("beam width")
plt.ylabel("match rate")
plt.legend(loc = 2)
plt.savefig('BMS_SF_trand1.png')
plt.close()