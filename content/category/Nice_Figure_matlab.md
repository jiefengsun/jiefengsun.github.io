Title: Plot a figure for IEEE Conference or Journals 
Date: 2022-11-11 08:00
Modified: 2021-11-11 10:50
Category: Research Tricks & Tools

### Plot a figure for IEEE Conference or Journals 

<!-- Please download `IEEEfigure.m` from this [link]({static}/code/tutorial/IEEEfigure.m). -->
Here is a code that you can see how I use it. 



#### Export figures with transprant background from matlab
If we directly copy the plot form the figure window of Matlab, it will be mate data with a transparent background.
But the resolution of the figure is not high. 

I personally prefer the following commands to export plots from matlab. 

1.  `print('-f1', 'namg', '-dpng', '-r300')`
2.  `copygraphics(gcf,'Resolution',300)`
3.  `exportgraphics(gcf,'force_conv.png', 'Resolution',300)`

However, these methods are not able to export png with a transparent background. 

To solve this problme, 

1. Import into `photoshop` to remove the background.
2. Use `export_fig` library
3. Export as eps with a transparent background.






