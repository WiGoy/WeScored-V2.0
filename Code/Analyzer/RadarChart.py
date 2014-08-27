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

import Global


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

	
def GetRadarChartFp():
	'''
	生成雷达图的文件名
	'''
	chars = random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 8)
	fnMap = ''
	for char in chars:
		fnMap += str(char)
	
	fpMap = Global.Dir_RadarChart + fnMap + '.png'
	return fpMap
	

def Drawing(playerNames, data):
	'''
	根据数据绘制雷达图
	'''
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
	
	legend = plt.legend(playerNames, loc=(0.85, 1))
	plt.setp(legend.get_texts(), fontsize='small')
	
	fpMap = GetRadarChartFp()
	filePng = open(fpMap, 'w')
	savefig(filePng)
	filePng.close()
	
	return fpMap