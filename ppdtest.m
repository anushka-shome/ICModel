a1 = 1;
tauF = .4157;
tauR = 16;

td = linspace(0,50,5000);
y = 1 - a1*exp(-td/tauR); 

plot(td,y)
hold on
a1 = 1;
tauF = .3;
tauR = 50;
y2 = 1 - a1*exp(-td/tauR); 
plot(td,y2,'r')

