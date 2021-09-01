clear all;
close all;
clc

% Constantes
h = 2;    
r = 26; 
miAr = 1.2566E-6;
miSolo = 2*1.2567E-6;
sigmaAr = 1E-10;
sigmaSolo = 1E-2;
iMax = 200;
rc = 0.02;
vMax = 500;
alturaCarro=1.5;
lCarro=4;



% gera a malha
x = 0;
y = 0;
elementos = []; %matriz de elementos
%criacao dos elementos triangulares a partir de coordenadas
while  y < r % enquanto esta dentro do raio
    x=0;
    xMax = (r^2 - y^2)^(1/2);    
    while x< xMax+1
        %representando cada triangulo de cada elemento
        %Triangulo debaixo no  ar
        t1.x1 = x;
        t1.y1 = y;
        t1.x2 = x+h;
        t1.y2 = y;
        t1.x3 = x+h;
        t1.y3 = y+h;       
        %Triangulo de cima no  ar
        t2.x1 = x;
        t2.y1 = y;
        t2.x2 = x+h;
        t2.y2 = y+h;
        t2.x3 = x;
        t2.y3 = y+h;
        %Triangulo de cima no  solo
        t3.x1 = x;
        t3.y1 = -y;
        t3.x2 = x+h;
        t3.y2 = -y-h;
        t3.x3 = x+h;
        t3.y3 = -y;        
        %Triangulo debaixo no  solo
        t4.x1 = x;
        t4.y1 = -y;
        t4.x2 = x;
        t4.y2 = -y-h;
        t4.x3 = x+h;
        t4.y3 = -y-h;
        
        elementos = [elementos t1 t2 t3 t4];
        x = x+h; %proximo passo
    end
    y = y+h; %proximo passo
end
%cria nohs nos elemetnos
[nos, elementos] = criaNos(elementos);

% nos onde  estao as fontes
Asource = - miAr*iMax/(2*pi*rc);
fonte1x = 4;
fonte2x = 6;
fonte1y = 14;
fonte2y = 10;

%mi e sigma aos elementos
for i = 1:length(elementos)
    if elementos(i).y3 > 0
        elementos(i).sigma = sigmaAr;
        elementos(i).mi = miAr;
    else        
        elementos(i).sigma = sigmaSolo;
        elementos(i).mi = miSolo;
    end
end

%Potencial 0 nos pontos da borda
for i = 1:length(nos)
    no = nos(i);
    nRad = ((no.x)^2 + (no.y)^2)^(1/2);
    if (nos(i).x == fonte1x && nos(i).y == fonte1y)||(nos(i).x == fonte2x && nos(i).y == fonte2y)
        nos(i).V = vMax;
        nos(i).ASource = Asource;
    end 
    % carro
    if (nos(i).x <=lCarro/2 && nos(i).y >=0 && nos(i).y <=alturaCarro)
        nos(i).V = 0;
    end
    % fontes
    if nRad >= r
        nos(i).V = 0;
        nos(i).A = 0;
    end
end









% pot eletrico e magnetico
F = zeros(length(nos),1);
K = matrizGlobal(elementos,length(nos),1);
FA = zeros(length(nos),1);
KA = matrizGlobal(elementos,length(nos),0);

% matrizes F
for i = 1:length(nos)
    % matriz FV
    if  ~isempty(nos(i).V)
        for j = 1:length(K)
            F(j) = F(j) - K(j,i) * nos(i).V;
            K(i,j) = 0;
            K(j,i) = 0;                       
        end
        F(i) = nos(i).V;
        K(i,i) = 1;       
    end
    % Matriz FA
    if  ~isempty(nos(i).ASource)       
        FA(i) = nos(i).ASource;             
    end
    % Borda
    if  ~isempty(nos(i).A)
        for j = 1:length(K)
            FA(j) = FA(j) - KA(j,i) * nos(i).A;
            KA(i,j) = 0;
            KA(j,i) = 0;                       
        end
        FA(i) = nos(i).V;
        KA(i,i) = 1;       
    end
end

% solucao
V = linsolve(K, F);
A = linsolve(KA, FA);

% valores nos nohs
for i = 1:length(nos)
    nos(i).V = V(i);
    nos(i).A = A(i);
end

% derivando
for i = 1:length(elementos)
    [dx_,dy_] = derivaElemento(elementos(i), nos, 1);
    elementos(i).Ex = -dx_;
    elementos(i).Ey = -dy_;
    [dxA_,dyA_] = derivaElemento(elementos(i), nos, 0);
    elementos(i).Bx = dyA_;
    elementos(i).By = -dxA_;
    elementos(i).Hx = elementos(i).Bx/elementos(i).mi;
    elementos(i).Hy = elementos(i).By/elementos(i).mi;
end








%--------------------------------------------------------------------------------------
% graficos
Vlinha = zeros(56/h, 30/h);
Alinha = zeros(56/h, 30/h);
for k = 1:length(nos)
  x = nos(k).x;
  y = nos(k).y;
  j = 1 + x/h;
  i = 1+(y+28)/h;
  Vlinha(i,j) = V(k);
  Alinha(i,j) = A(k);
end
Vlinha = [fliplr(Vlinha) Vlinha];
Alinha = [fliplr(Alinha) Alinha];

[X,Y] = meshgrid(0:h:28, -28:h:27); 
xFlip = [-fliplr(X) X];
yFlip = [fliplr(Y) Y];

% V
figure;
contour(xFlip, yFlip, Vlinha, 'ShowText','off', 'LabelSpacing',500);
title("Potencial Elétrico (V)");
c = colorbar;
c.Label.String = 'V [kV]';
xlabel("x [m]");
ylabel("y [m]");
ylim([-5 30]);



% A
figure;
contour(xFlip, yFlip, Alinha,16, 'ShowText','off', 'LabelSpacing',500);            
title("Potencial Magnético (A)");
c = colorbar;
c.Label.String = 'A'; 
xlabel("x [m]");
ylabel("y [m]");
ylim([-30 30]);



% E
figure();
xms = zeros(length(elementos),1);
yms = zeros(length(elementos),1);
Exs = zeros(length(elementos),1);
Eys = zeros(length(elementos),1);
for i = 1:length(elementos)
    xms(i) = elementos(i).xm;
    yms(i) = elementos(i).ym; 
    Exs(i) = elementos(i).Ex;
    Eys(i) = elementos(i).Ey;      
end
quiver([-fliplr(xms) xms],[fliplr(yms) yms],[-fliplr(Exs) Exs],[fliplr(Eys) Eys], 0.1);
title("Campo de Energia (E)");
xlabel("x [m]");
ylabel("y [m]");
ylim([-5 30]);



% B
figure();
Bxs = zeros(length(elementos),1);
Bys = zeros(length(elementos),1);
Hxs = zeros(length(elementos),1);
Hys = zeros(length(elementos),1);
for i = 1:length(elementos)
    Bxs(i) = elementos(i).Bx;
    Bys(i) = elementos(i).By;    
    Hxs(i) = elementos(i).Hx;
    Hys(i) = elementos(i).Hy;  
end
quiver([-fliplr(xms) xms],[fliplr(yms) yms],[fliplr(Bxs) Bxs],[-fliplr(Bys) Bys], 0.1);
title("Fluxo Magnético (B)");
xlabel("x [m]");
ylabel("y [m]");
ylim([-30 30]);



% H
figure;
quiver([-fliplr(xms) xms],[fliplr(yms) yms],[fliplr(Hxs) Hxs],[-fliplr(Hys) Hys], 0.1);
title("Campo Magnético (H)");
xlabel("x [m]");
ylabel("y [m]");
ylim([-30 30]);



%magneticos
figure;
contour(xFlip, yFlip, Alinha,16, 'ShowText','off', 'LabelSpacing',500);            
title("Potencial Magnético (A) e Fluxo magnético (B) ");
c = colorbar;
c.Label.String = 'A [Wb/m]';
xlabel("x [m]");
ylabel("y [m]");
axis equal;

hold on;
quiver([-fliplr(xms) xms],[fliplr(yms) yms],[fliplr(Hxs) Hxs],[-fliplr(Hys) Hys], 0.1);
legend({'A ', "B [T] "},'Location','southwest');
ylim([-30 30]);


%eletricos
figure;
contour(xFlip, yFlip, Vlinha, 'ShowText','off', 'LabelSpacing',500);            
title("Potencial elétrico (V) e Vetor Campo Elétrico (E)");
c = colorbar;
c.Label.String = 'V [kV]';
xlabel("x [m]");
ylabel("y [m]");
axis equal;

hold on;
quiver([-fliplr(xms) xms],[fliplr(yms) yms],[-fliplr(Exs) Exs],[fliplr(Eys) Eys], 0.1);
legend({'V ', "Exy "},'Location','southwest');
ylim([-5 30]);





% Vsurf
figure;
surf(xFlip, yFlip, Vlinha);
title("Potencial Elétrico (V)");
c = colorbar;
c.Label.String = 'V [kV]';
xlabel("x [m]");
ylabel("y [m]");
ylim([-5 30]);



% Asurf
figure;
surf(xFlip, yFlip, Alinha);            
title("Potencial Magnético (A)");
c = colorbar;
c.Label.String = 'A'; 
xlabel("x [m]");
ylabel("y [m]");
ylim([-30 30]);