clear all
close all

%Mudar aqui quando quiser testar com diferentes quantidades de elementos
Numero_Elementos=2;
L1=2.0;
L2=3.0;
L3=4.0;
d1i=0.040; 
d1e=0.050;
d2i=0.090;
d2e=0.100;
A1=pi*(d1e^2-d1i^2)/4;
I1=pi*(d1e^4-d1i^4)/64;
A2=pi*(d2e^2-d2i^2)/4;
I2=pi*(d2e^4-d2i^4)/64;

vv = 0.29;
E = 2.10*10^11;
ro = 7650;

%Criaçao dos elementos
elementos=ElementsCreation(L1,A1,L2,A2,L3,I1,I2);

%Criação dos elementos - subdividindo as barras
[elementosfinais,Numero_Nos]=...
    RightElementsCreation(elementos,Numero_Elementos);

%Monta a matriz global
[M, K]=...
 MountMatrix( Numero_Nos,length(elementosfinais), elementosfinais, E, ro);

%Analise Modal
nospresos=find(elementosfinais(:,7)==0 & elementosfinais(:,9)==0);
nospresos=elementosfinais(nospresos(1),5);
nospresos2=find(elementosfinais(:,8)==4 & elementosfinais(:,10)==0);
nospresos(2)=elementosfinais(nospresos2(1),6);

if nospresos(1)<=nospresos(2)
    manter=[1:3*nospresos(1)-3 3*nospresos(1):3*nospresos(2)-2 ...
        3*nospresos(2):length(M)];
else
    manter=[1:3*nospresos(2)-2 3*nospresos(2):3*nospresos(1)-3 ...
        3*nospresos(1):length(M)];    
end

Kmodal=K(manter,manter);
Mmodal=M(manter,manter);

[autovetores, autovalores]=eigs(Kmodal,Mmodal,6,'smallestabs');

frequencias=sqrt(diag(autovalores))/(2*pi);

%Analise Transiente
alpha = 3e-1;
beta = 3e-2;
F = 8000; 
D = 2000; 
t1 = 2.0;
t2 = 8.0;

K(3*nospresos(1)-2:3*nospresos(1)-1,:)=0;
K(:,3*nospresos(1)-2:3*nospresos(1)-1)=0;
K(3*nospresos(1)-2,3*nospresos(1)-2)=1;
K(3*nospresos(1)-1,3*nospresos(1)-1)=1;
K(3*nospresos(2)-1,:)=0;
K(:,3*nospresos(2)-1)=0;
K(3*nospresos(2)-1,3*nospresos(2)-1)=1;

M(3*nospresos(1)-2:3*nospresos(1)-1,:)=0;
M(:,3*nospresos(1)-2:3*nospresos(1)-1)=0;
M(3*nospresos(1)-2,3*nospresos(1)-2)=1;
M(3*nospresos(1)-1,3*nospresos(1)-1)=1;
M(3*nospresos(2)-1,:)=0;
M(:,3*nospresos(2)-1)=0;
M(3*nospresos(2)-1,3*nospresos(2)-1)=1;

Cmatriz=alpha*M+beta*K;
beta=1/4;
gamma=1/2;
passo=100;
dt=10/passo;

distanciaC=10;
distanciaB=10;

for i=1:length(elementosfinais)
    distanciaC1=((elementosfinais(i,7)-2)^2+(elementosfinais(i,9)-1.71)^2);
    distanciaC2=((elementosfinais(i,8)-2)^2+(elementosfinais(i,10)-1.71)^2);
    distanciaB1=((elementosfinais(i,7)-2)^2+(elementosfinais(i,9)-4.71)^2);
    distanciaB2=((elementosfinais(i,8)-2)^2+(elementosfinais(i,10)-4.71)^2);
    if distanciaC1<distanciaC2
        if distanciaC1<distanciaC
            distanciaC=distanciaC1;
            pontoC=i;
            comecoC=1;
        end
    else
        if distanciaC2<distanciaC
            distanciaC=distanciaC2;
            pontoC=i;
            comecoC=2;
        end
    end
    if distanciaB1<distanciaB2
        if distanciaB1<distanciaB
            distanciaC=distanciaB1;
            pontoB=i;
            comecoB=1;
        end
    else
        if distanciaB2<distanciaB
            distanciaB=distanciaB2;
            pontoB=i;
            comecoB=2;
        end
    end
end

if comecoB==1
    B=elementosfinais(pontoB,5);
else
    B=elementosfinais(pontoB,6);
end
if comecoC==1
    C=elementosfinais(pontoC,5);
else
    C=elementosfinais(pontoC,6);
end

A=1; %Primeiro nó que definimos sempre

deslocA=zeros(2,passo);
deslocB=zeros(2,passo);
deslocD=zeros(2,passo);
deslocE=zeros(2,passo);

Mtrans=M+dt*gamma*Cmatriz+dt^2*beta*K;

Forca=zeros(length(M),1);

Ac=Mtrans\Forca;
% velocidades e deslocamentos nulos
Vel=zeros(length(M), 1);
Del=zeros(length(M), 1);

D=find(elementosfinais(:,7)==0.25 & elementosfinais(:,9)==1.5);
E=find(elementosfinais(:,7)==3 & elementosfinais(:,9)==7);
if length(D)==0
    D=find(elementosfinais(:,8)==0.25 & elementosfinais(:,10)==1.5);
    D=elementosfinais(D(1),6);
else
    D=elementosfinais(D(1),5);
end
if length(E)==0
    E=find(elementosfinais(:,8)==3 & elementosfinais(:,10)==7);
    E=elementosfinais(E(1),6);
else
    E=elementosfinais(E(1),5);
end

coordAvizinho=[1+2/Numero_Elementos 14];
noAviz=find(elementosfinais(:,8)==coordAvizinho(1) & ...
    elementosfinais(:,10)==coordAvizinho(2));
noAviz=elementosfinais(noAviz(1),6);

if comecoB==1
    Bvizinhox=elementosfinais(pontoB,7)+2.5/Numero_Elementos;
    Bvizinhoy=elementosfinais(pontoB,9)+3/Numero_Elementos;
else
    Bvizinhox=elementosfinais(pontoB,8)+2.5/Numero_Elementos;
    Bvizinhoy=elementosfinais(pontoB,10)+3/Numero_Elementos;    
end
coordBvizinho=[Bvizinhox Bvizinhoy];

noBviz=find(elementosfinais(:,8)==coordBvizinho(1) &...
    elementosfinais(:,10)==coordBvizinho(2));
noBviz=elementosfinais(noBviz(2),6);

deslocAvizinho=zeros(2,passo);
deslocBvizinho=zeros(2,passo);

for i=1:passo
    if t1<=i*dt && i*dt<=t2
        Forca([1 7 13 19 25])=5*D;
    else
        Forca([1 7 13 19 25])=0;
    end
    Forca([2 5])=2*F*sin(2*pi*i*dt);
    Ftrans=Forca-Cmatriz*(Vel+dt*(1-gamma)*Ac) ...
       -K*(Del+dt*Vel+(dt^2/2)*(1-2*beta)*Ac);
    Ac_novo=Mtrans\Ftrans;
    Del=Del+dt*Vel+(dt^2/2)*((1-2*beta)*Ac+2*beta*Ac_novo);
    Vel=Vel+dt*((1-gamma)*Ac+gamma*Ac_novo);

    deslocA(i,1)=Del(3*A-2);
    deslocA(i,2)=Del(3*A-1);
    deslocB(i,1)=Del(3*B-2);
    deslocB(i,2)=Del(3*B-1); 
    
    deslocAvizinho(i,1)=Del(3*noAviz-2);
    deslocAvizinho(i,2)=Del(3*noAviz-1);
    deslocBvizinho(i,1)=Del(3*noBviz-2);
    deslocBvizinho(i,2)=Del(3*noBviz-1);
    
    deslocD(i,1)=Del(3*D-2);
    deslocE(i,1)=Del(3*E-2);
    deslocD(i,2)=Del(3*D-1);
    deslocE(i,2)=Del(3*E-1);
end

figure()
plot(dt*(1:passo),10^3*deslocD(:,1));
title 'Deslocamento horizontal do ponto D'
xlabel 'Tempo (s)'
ylabel 'Deslocamento (mm)'

figure()
plot(dt*(1:passo),10^3*deslocE(:,1));
title 'Deslocamento horizontal do ponto E'
xlabel 'Tempo (s)'
ylabel 'Deslocamento (mm)'

figure()
plot(dt*(1:passo),10^3*deslocD(:,2));
title 'Deslocamento vertical do ponto D'
xlabel 'Tempo (s)'
ylabel 'Deslocamento (mm)'

figure()
plot(dt*(1:passo),10^3*deslocE(:,2));
title 'Deslocamento vertical do ponto E'
xlabel 'Tempo (s)'
ylabel 'Deslocamento (mm)'

figure()
plot(dt*(1:passo),sqrt((10^3*deslocD(:,2)).^2+(10^3*deslocD(:,1)).^2));
title 'Módulo do deslocamento do ponto D'
xlabel 'Tempo (s)'
ylabel 'Deslocamento (mm)'

figure()
plot(dt*(1:passo),sqrt((10^3*deslocE(:,2)).^2+(10^3*deslocE(:,1)).^2));
title 'Modulo do deslocamento do ponto E'
xlabel 'Tempo (s)'
ylabel 'Deslocamento (mm)'

LA=sqrt((1-coordAvizinho(1)).^2+(14-coordAvizinho(2)).^2);
if comecoB==1
    noBx=elementosfinais(pontoB,7);
    noBy=elementosfinais(pontoB,9);
    LB=sqrt((elementosfinais(pontoB,7)-coordBvizinho(1)).^2+...
        (elementosfinais(pontoB,9)-coordBvizinho(2)).^2);
else
    noBx=elementosfinais(pontoB,8);
    noBy=elementosfinais(pontoB,10);    
    LB=sqrt((elementosfinais(pontoB,8)-coordBvizinho(1)).^2+...
        (elementosfinais(pontoB,10)-coordBvizinho(2)).^2);    
end

deslAfinal=sqrt((1+deslocA(:,1)-...
(coordAvizinho(1)+deslocAvizinho(:,1))).^2+(14+deslocA(:,2)-...
(coordAvizinho(2)+deslocAvizinho(:,2))).^2);

deslBfinal=sqrt((noBx+deslocB(:,1)-...
(coordBvizinho(1)+deslocBvizinho(:,1))).^2+(noBy+deslocB(:,2)-...
(coordBvizinho(2)+deslocBvizinho(:,2))).^2);

figure()
plot(dt:dt:10,E*(LB-deslBfinal)/LB)
hold on
plot(dt:dt:10,E*(LA-deslAfinal)/LA)
xlabel('Tempo (s)')
ylabel('Tensão')
title('Tensão nos nós A e B')
legend('B','A')

%Análise Harmônica
moduloB = zeros(1,length(1:0.01:45));
moduloC = zeros(1,length(1:0.01:45));


F0=zeros(length(M),1);
F0(2)=2*F; 
F0(5)=2*F;
%Varia a frequência, para calcular análise modal usa a amplitude da força

for f = 1:0.01:45
    A=-(2*pi*f)^2*M+K;
    respostas=A\F0;
    moduloB(i)=sqrt(respostas(3*B-2)^2+respostas(3*B-1)^2);
    moduloC(i)=sqrt(respostas(3*C-2)^2+respostas(3*C-1)^2);
end

figure()
plot(1:0.01:45,moduloB)
hold on
plot(1:0.01:45,moduloC)
legend('C','B')
xlabel('Frequência (Hz)')
ylabel('Deslocamento (m)')
title('Deslocamentos na Análise Harmônica')
