#matplotlib.rcParams.find_all('tic')

from matplotlib import rcParams

ax_tick_width = 0.6
fontsize = 14

params = {
    ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    ## FIGURE
    ##

    #'figure.figsize': (x_size_in,y_size_in),
    #'figure.dpi': 200,
    

    ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    ## LINES
    ##
   
    'lines.linewidth': 2,
    'axes.color_cycle': ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange'],
    #'lines.markeredgewidth': 0.3
    #'lines.markersize': 8,
		

    ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    ## Axes, grid, legend
    ##

    # Legend frame:
    #patch.facecolor        : blue
    #patch.edgecolor        : bcbcbc #eeeeee
    #patch.antialiased      : True
    'legend.fancybox': True,
    'legend.loc': 'best',
    'patch.linewidth': ax_tick_width,    # legend frame thickness
    
    'axes.facecolor': 'white',      # axes background color
    'axes.edgecolor': 'black',      # axes edge color
    'axes.axisbelow': True,         # grid below plot lines
    'axes.linewidth': ax_tick_width,
    'axes.grid': True,

    'grid.linewidth': ax_tick_width,
    'grid.linestyle': '-',
    'grid.color': '#bcbcbc',
    
    'xtick.direction': 'in',
    
    'xtick.major.size': 6,
    'xtick.major.width': ax_tick_width,
    'xtick.major.pad': 4,       # distance to major tick label in points

    'xtick.minor.size': 2,
    'xtick.minor.width': 0.5,
    'xtick.minor.pad': 4,       # distance to the minor tick label in points

    'ytick.direction': 'in',
    
    'ytick.major.size': 6,
    'ytick.major.width': ax_tick_width,
    'ytick.major.pad': 4,       # distance to major tick label in points

    'ytick.minor.size': 2,
    'ytick.minor.width': 0.5,
    'ytick.minor.pad': 4,       # distance to the minor tick label in points
    
    
    ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    ## FONTS
    ##
   
    #'font.family': 'Arial',
    'font.sans-serif' : ['Arial', 'Liberation Sans'],
    'font.size' : fontsize,
    'xtick.labelsize' : fontsize,
    'ytick.labelsize' : fontsize,
    'axes.labelsize' : fontsize,
    'legend.fontsize' : fontsize - 1,
    #'font.serif': 'FreeSerif',
    #'font.size': 6,
    'axes.titlesize': fontsize,
    #'axes.labelsize': 6,
    #'ytick.labelsize': 6,  # fontsize for yticks
    #'xtick.labelsize': 6,  # fontsize for xticks
    #'legend.fontsize': 6,
    'text.usetex': False,
    #'mathtext.mit' : 'cmtt10.ttf',

}
rcParams.update(params)
