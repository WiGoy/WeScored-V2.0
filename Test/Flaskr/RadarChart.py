'''
生成雷达图
'''
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.pyplot import plot, savefig


def radar_factory(num_vars, frame='circle'):
	
	'''
	Create a radar chart with `num_vars` axes.
	This function creates a RadarAxes projection and registers it.
	Parameters
	----------
	num_vars : int
		Number of variables for radar chart.
	frame : {'circle' | 'polygon'}
		Shape of frame surrounding axes.
	'''
	
	# calculate evenly-spaced axis angles
	theta = 2 * np.pi * np.linspace(0, 1-1./num_vars, num_vars)
	# rotate theta such that the first axis is at the top
	theta += np.pi / 2
	
	def draw_poly_patch(self):
		verts = unit_poly_verts(theta)
		return plt.Polygon(verts, closed=True, edgecolor='k')
	
	def draw_circle_patch(self):
		# unit circle centered on (0.5, 0.5)
		return plt.Circle((0.5, 0.5), 0.5)
	
	patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
	if frame not in patch_dict:
		raise ValueError('unknown value for `frame`: %s' % frame)
	
	class RadarAxes(PolarAxes):
		name = 'radar'
		# use 1 line segment to connect specified points
		RESOLUTION = 1
		# define draw_frame method
		draw_patch = patch_dict[frame]
		
		def fill(self, *args, **kwargs):
			'''
			Override fill so that line is closed by default
			'''
			closed = kwargs.pop('closed', True)
			return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)
		
		def plot(self, *args, **kwargs):
			'''
			Override plot so that line is closed by default'''
			lines = super(RadarAxes, self).plot(*args, **kwargs)
			for line in lines:
				self._close_line(line)
		
		def _close_line(self, line):
			x, y = line.get_data()
			# FIXME: markers at x[0], y[0] get doubled-up
			if x[0] != x[-1]:
				x = np.concatenate((x, [x[0]]))
				y = np.concatenate((y, [y[0]]))
				line.set_data(x, y)
		
		def set_varlabels(self, labels):
			self.set_thetagrids(theta * 180/np.pi, labels)
		
		def _gen_axes_patch(self):
			return self.draw_patch()
		
		def _gen_axes_spines(self):
			if frame == 'circle':
				return PolarAxes._gen_axes_spines(self)
            # The following is a hack to get the spines (i.e. the axes frame)
            # to draw correctly for a polygon frame.
            # spine_type must be 'left', 'right', 'top', 'bottom', or `circle`.
			spine_type = 'circle'
			verts = unit_poly_verts(theta)
			# close off polygon by repeating first vertex
			verts.append(verts[0])
			path = Path(verts)
			
			spine = Spine(self, spine_type, path)
			spine.set_transform(self.transAxes)
			return {'polar': spine}
	
	register_projection(RadarAxes)
	return theta


def unit_poly_verts(theta):
	'''
	Return vertices of polygon for subplot axes.
    This polygon is circumscribed by a unit circle centered at (0.5, 0.5)
    '''
	x0, y0, r = [0.5] * 3
	verts = [(r * np.cos(t) + x0, r * np.sin(t) + y0) for t in theta]
	return verts


def example_data():
	data = {
		'column names':
			['goal_assist_openplay', 'att_assist_openplay', 'big_chance_created', 'accurate_through_ball', 'accurate_layoffs', 'successful_final_third_passes', 'goal_normal', 'was_fouled', 'won_contest', 'touches per turnover','crossing %', 'passing %'],
		'Max':
			[0.44, 2.4, 0.75, 0.67, 7.35, 28.25, 0.94, 3.75, 4.94, 98.2, 43.54, 92.62],
		'Min':
			[0, 0, 0, 0, 0, 0.12, 0, 0, 0, 13.457, 12.94, 62.71],
		'PlayerStats':
			[[0.26, 2.26, 0.41, 0.59, 4.33, 27.96, 0.26, 1.52, 1.07, 71.5088, 31.49, 87.21],
			[0.09, 1.42, 0.39, 0.39, 1.64, 15.58, 0.15, 1.24, 1.79, 45.9083, 31.11, 79.89],
			[0.17, 2.4, 0.26, 0.2, 1.97, 21.14, 0.29, 2.54, 3.77, 35.1724, 14.67, 83.03],
			[0.25, 2.04, 0.18, 0.36, 3.61, 28.25, 0.18, 0.89, 1.75, 33.9912, 37.3, 87.29]]}
			
	return data


def GetRandomFn():
	
	chars = random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 8)
	fnMap = ''
	for char in chars:
		fnMap += str(char)
	
	return fnMap
	

def ShowMap(data):

	spokeLabels = data.pop('Property')
	max = data.pop('Max')
	min = data.pop('Min')
	playerStatistics = data.pop('PlayerStatistics')
	N = len(spokeLabels)
	
	valueShow = []
	for player in playerStatistics:
		valuePlayer = []
		for n in range(N):
			y = round(((player[n] - min[n]) / (max[n] - min[n])) * 100, 2)
			valuePlayer.append(y)
		valueShow.append(valuePlayer)
	
	theta = radar_factory(N, frame='polygon')
	fig = plt.figure(figsize=(10, 10))
	colors = ['b', 'r']
	
	ax = fig.add_subplot(1, 1, 1, projection='radar')
	
	ax.set_ylim(0, 100)
	
	for d, color in zip(valueShow, colors):
		ax.plot(theta, d, color=color)
		ax.fill(theta, d, facecolor=color, alpha=0.2)
	
	ax.set_varlabels(spokeLabels)
	
	labels = ('Luis Suárez', 'Lionel Messi')
	legend = plt.legend(labels, loc=(0.85, 1))
	plt.setp(legend.get_texts(), fontsize='small')
	
	
	fpMap = 'static/' + GetRandomFn() + '.png'
	filePng = open(fpMap, 'w')
	savefig(filePng)
	filePng.close()
	
	return fpMap
#	plt.show()

	
if __name__ == '__main__':
	N = 12
	theta = radar_factory(N, frame='polygon')
	
	data = example_data()
	spoke_labels = data.pop('column names')
	max =  data.pop('Max')
	min =  data.pop('Min')
	playerStats = data.pop('PlayerStats')
	
	fig = plt.figure(figsize=(10, 10))
	
	colors = ['b', 'r', 'black', 'y']
	
	ax = fig.add_subplot(1, 1, 1, projection='radar')
	ax.set_varlabels(spoke_labels)
	ax.set_ylim(0, 100)
	playerNewStats = []
	for player in playerStats:
		playernew = []
		for n in range(N):
			y = round(((player[n] - min[n]) / (max[n] - min[n])) * 100, 2)
			playernew.append(y)
		
		playerNewStats.append(playernew)
	for d, color in zip(playerNewStats, colors):
		ax.plot(theta, d, color=color)
		ax.fill(theta, d, facecolor=color, alpha=0.1)
		print(d)
	
	labels = ('David Silva', 'Philippe Coutinho', 'Eden Hazard', 'Mesut Özil')
	legend = plt.legend(labels, loc=(0.9, .95), labelspacing=0.1)
	plt.setp(legend.get_texts(), fontsize='small')
	'''
	for d, color in zip(playerNewStats, colors):
		print(d)
		ax.plot(theta, d, color=color)
		#ax.fill(theta, d, facecolor=color, alpha=0.25)
		break
	'''
	plt.show()