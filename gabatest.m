tau = 15;
tau2 = 3;
t = 0:.01:100;
g = exp(-t/tau) - exp(-t/tau2);
plot(t,g)
