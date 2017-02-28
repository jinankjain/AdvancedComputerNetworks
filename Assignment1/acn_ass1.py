import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
import sys
import os

def throughput(rtt):
	ans = 128.0/(rtt+0.128)
	return ans

def plot():
	rtt =  np.linspace(0.01, 2, num=10000)
	tps = []
	for r in rtt:
		tps.append(throughput(r))
	plt.plot(rtt, tps)
	plt.xlabel('RTT in seconds', fontsize=19, fontweight='bold')
	plt.ylabel('Throughput (Mbps)', fontsize=19, fontweight='bold')
	plt.grid(True)
	plt.show()

plot()
