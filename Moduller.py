import numpy as np
import matplotlib.pyplot as matplot

maasListesi = np.random.normal(4000,10,300)
print(np.mean(maasListesi))

matplot.hist(maasListesi,50)
matplot.show()

