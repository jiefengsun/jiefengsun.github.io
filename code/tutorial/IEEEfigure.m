%% IEEE Standard Figure Configuration - Version 2.0
% Rvised by Jiefeng Sun 11/11/2022
% run this code before the plot command

%%
% According to the standard of IEEE Transactions and Journals: 

% Times New Roman is the suggested font in labels. 

% For a singlepart figure, labels should be in 8 to 10 points,
% whereas for a multipart figure, labels should be in 8 points.
% Width: column width: 8.8 cm; page width: 18.1 cm.

%% width & hight of the figure
function IEEEfigure(varargin)

Defaults = {1.1,0.78,1};
Defaults(1:nargin) = varargin;
k_scaling = Defaults{1};       % scaling factor of the figure, if 1, two figures in a row, if 0.7 three figures in a row
% (You need to plot a figure which has a width of (8.8 * k_scaling)
% in MATLAB, so that when you paste it into your paper, the width will be
% scalled down to 8.8 cm  which can guarantee a preferred clearness.
k_width_hight = Defaults{2};%0.5; % or goes to 
% Absolute size of the font, depends on how many figures we want to put a row. 
fontSize = 10.5* k_scaling*Defaults{3}; % 13 for 3 figure in a row in whole row, 16 for 4 page, 10.5 for 2 figure in  a row; need to use latex interpolation
width = 3.5*2.54 * k_scaling;
hight = width * k_width_hight;
Font  =  'Times New Roman';%'Calibri';% 
%% figure margins
top = 0.6;  % normalized top margin
bottom = (fontSize+5)/10; 	% normalized bottom margin
left =(fontSize+5)/10 ; 	% normalized left margin
right =0.7;  % normalized right margin
box on
%% set default figure configurations
set(0,'defaultFigureUnits','centimeters');
set(0,'defaultFigurePosition',[8 5 width hight]);

set(0,'defaultLineLineWidth',1.5); %% to make sure the line have the same thickness no matter what plot size we use. 
set(0,'defaultAxesLineWidth',0.8);

set(0,'defaultAxesGridLineStyle',':');
set(0,'defaultAxesYGrid','on');
set(0,'defaultAxesXGrid','on');

set(0,'defaultAxesFontName',Font);
set(0,'defaultAxesFontSize',fontSize);

set(0,'defaultTextFontName',Font);
set(0,'defaultTextFontSize',fontSize);

set(0,'defaultLegendFontName',Font);
set(0,'defaultLegendFontSize',fontSize);

set(0,'defaultAxesUnits','normalized');
set(0,'defaultAxesPosition',[left/width bottom/hight (width-left-right)/width  (hight-bottom-top)/hight]);

set(0,'defaultAxesColorOrder',[0 0 0]);
set(0,'defaultAxesTickDir','out');

set(0,'defaultFigurePaperPositionMode','auto');

% you can change the Legend Location to whatever as you wish
set(0,'defaultLegendLocation','northwest'); % southwest southwest northwest northeast
set(0,'defaultLegendBox','on');
set(0,'defaultLegendOrientation','vertical');
box on
set(gca, 'color', 'none');
