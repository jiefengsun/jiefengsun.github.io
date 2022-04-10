Title: Generate Nice Figures - Procedures
Date: 2020-07-11 08:00
Modified: 2020-07-25 10:50
Category: Research Tricks & Tools


### Raw figures
There are three types of raw figures:

1. Photos taken using a camera. 
2. An illustrative figure draw by PowerPoint, CAD software, or Illustrator.
3. Figures plotted using Matlab.

 

### Ordinary paper

When I say "ordinary paper", I mean the paper does not require very nice images, i.e., journals that have a IF less than 10.
Most of engineering papers, even very prestigious ones such as T-RO and T-Mech don't require very nice images. 

#### Tools
I use PowerPoint to draw figure and export to different formats.

Pros: Easy to use, especially it has an equation editor

Cons: It cannot export very high-resolution figures. I don’t know why, but my PowerPoint can only export 150 DPI which is not a high as others can do. 

For publication on IEEE, PowerPoint might be well enough. But some material Journals might need high resolution.

#### Is Adobe Illustrator better?

Pros: very powerful.

Cons: Need to import equations from other sources. 

#### Nice rendered pictures

It is good to explore the rendering function of Solidworks. It can also generate Carton style rendering files. The point is not to make a very realistic rendering figure. It is to make a good schematic that people can understand. 

#### Export out 300 DPI using PowerPoint

The only way to export 300 DPI is **not** using the quick export function found in the right click. To export 300 dpi, we need to use the save as function in the File manual. But it will export the whole slid, then we need to crop the figure using Edit of the Windows,

#### 

#### Export plot with transprant background from matlab
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

### High Impact Journals

### Tools

Illustrator. 

#### General procedure. 

First generate plots in Matlab, then export with `exportgraphics(gcf,'file_name.eps', 'ContentType','vector')`, sometimes we will need to force Matlab to export it as a vector figure.

Assembling photos and plots in illustrators. 

#### Settings in Matlab


#### Some tricks

1. 



