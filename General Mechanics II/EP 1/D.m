clear all;clc;close all;
m=10;
k=3553;
c=37.7;
g=9.81;

dt=0.0001;
t=0:dt:5;

x0=0;
v0=0;
f = @(T) 1000*sin(pi*T+pi/2);

x=zeros(length(t),1);
v=zeros(length(t),1);
vdot=zeros(length(t),1);
F=zeros(length(t),1);
%xPorV=zeros(length(t),1);
x(1)=x0;
v(1)=v0;

for i = 1:length(t)-1
	x(i+1) = x(i) + dt*v(i);
	F(i) = f(t(i));
	vdot(i) = dt*(F(i) - k*x(i) - c*v(i))/m;
	v(i+1) = v(i) + vdot(i);
	%xPorV(i) = x(i)/v(i);
end;


figure1 = figure(1)
plot(t, x, 'r')
grid on
title({'$x$'}, 'Interpreter','latex');
hold off
xlabel('tempo [s]', 'Interpreter','latex');
ylabel('$x [m]$', 'Interpreter','latex');

figure2 = figure(2)
plot(t, v, 'r')
grid on
title({'$\dot{x}$'}, 'Interpreter','latex');
hold off
xlabel('tempo [s]', 'Interpreter','latex');
ylabel('$\dot{x} [m/s]$', 'Interpreter','latex');

figure3 = figure(3)
plot(t, vdot, 'r')
grid on
title({'$\ddot{x}$'}, 'Interpreter','latex');
hold off
xlabel('tempo [s]', 'Interpreter','latex');
ylabel('$\ddot{x} [m/s^{2}]$', 'Interpreter','latex');

figure4 = figure(4)
plot(v, x, 'r')
grid on
title({'$x por \dot{x} $'}, 'Interpreter','latex');
hold off
xlabel('$\dot{x} [m/s]$', 'Interpreter','latex');
ylabel('$x [m]$', 'Interpreter','latex');

figure5 = figure(5)
plot(t, F, 'r')
grid on
title({'$F$'}, 'Interpreter','latex');
hold off
xlabel('tempo [s]', 'Interpreter','latex');
ylabel('$F$', 'Interpreter','latex');


saveas(figure1,'D-x(t).jpg');
saveas(figure2,'D-v(t).jpg');
saveas(figure3,'D-a(t).jpg');
saveas(figure4,'D-x(v(t)).jpg');
saveas(figure5,'D-F(t).jpg');
