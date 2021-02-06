# x - x axis value
# y - corresponding y axis value
class plot:
    def __init__(self, xlabel='x- axis', ylabel='y- axis', title='1 line plot', name='plot.png'):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.name = name
        
    def lineplot(self, plt, x, y, legend=''):
        
        # plotting the points  
        plt.plot(x, y, marker='o', label = legend)
        
        # naming the x axis 
        plt.xlabel(self.xlabel) 
        # naming the y axis 
        plt.ylabel(self.ylabel) 
        
        # giving a title to my graph 
        plt.title(self.title)
        
        # set a legend
        plt.legend()
        
        # function to show the plot 
        plt.savefig(self.name)
        
    def scatter(self, plt, x, y, legend=''):
        
        # plotting the points  
        plt.scatter(x, y, marker='o', label = legend)
        
        # naming the x axis 
        plt.xlabel(self.xlabel) 
        # naming the y axis 
        plt.ylabel(self.ylabel) 
        
        # giving a title to my graph 
        plt.title(self.title)
        
        # set a legend
        plt.legend()
        
        # function to show the plot 
        plt.savefig(self.name)

        
