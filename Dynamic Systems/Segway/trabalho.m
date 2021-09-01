%{

Para o modelamento, as seguintes hipot�ses foram realizadas:

VEICULO

1) Massas m1, m2, m3 s�o ideias e pontuais
2) Molas com k1, k2, k5 s�o ideias e lineares
3) Molas com k3p, k4p e k6p sofrem deforma��o pl�stica e, portanto,
absorvem energia
4) Momentos de in�rcia das rodas dianteiras (J2) e traseiras (J3) s�o
desprez�veis
5) For�as de atrito de rolamento presentes nas rodas (FatR2 e FatR3) s�o
desprez�veis
6) For�a de arrasto presente no carro devido ao ar � desprez�vel
7) Dist�rbio gerados no carro por irregularidade do piso s�o desprez�veis
(piso horizontal ideal)
8) Choque sim�trico do carro contra a barreira r�gida (dire��o do carro n�o
muda, isto �, oscila��es no volante do carro s�o desprez�veis e, al�m
disso, tem-se barreira vertical ideal)

PESSOA

1) Massas m3', m4, m5 s�o ideias e pontuais
2) Molas com k8, kt1, kt2 s�o ideias e lineares
3) Amortecedor com b1 � ideal
4) F � gerada por fonte ideal
5) Desconsideramos que o dummy se mova em y (saia do banco)
6) Consideramos cinto como mola el�stica, pois durante o crash test o cinto
j� foi acionado (ou seja, "gap" de acionanmento do cinto foi desprezado)
7) Mesmo que a pessoa est� na dire��o ortogonal ao ve�culo, a dire��o da for�a gerada
pelo crash test � o que importa, n�o afetando os resultados

%}

close all; clear all; clc

% Declarando v�riaveis globais
global yy kp m Fy k Nmolas Nmassas

Nmassas = 5; % numero de massas
Nmolas = 4; % numero de molas que deformam plasticamente para as for�as com kp
yy =zeros(Nmolas , 1); % instancia vetor yy (armazena deformacao plastica em [m])
F = [];
E = [];

% Aqui dever� ser definido os dados do problema (m1, m2, m3, m4, m5, k1, k2, k5,
% k3p, k4p, k6p, k7p, Fy3, Fy4, Fy6, Fy7)
%Consulte o relat�rio anexo para saber mais de como os valores seguintes foram alcan�ados

m =[300; 125; 622.4; 5.6; 42]; % [m1, m2, m3, m4, m5]
k = [3.22e8; 6.44e8; 6.44e8; 5.64e6; 1e6; 1e6]; % [k1, k2, k5, k8, kt1, kt2]
kp = [6.44e8; 3.22e8; 4.83e6; 1.13e8]; % [k3p, k4p, k6p, k7p]
Fy = [141e3; 282e3; 36.66e3; 126.9e3]; %[Fy3, Fy4, Fy6, Fy7]

% Inicializando o vetor que conter� a posi��o e velocidade, utilizado na
% ode45.
X0 = [0; 0; 0; 0; 0];
V0 = [(56/3.6);  (56/3.6);  (56/3.6); (56/3.6); (56/3.6)];

%Organizando o vetor para a ODE45
x0=[X0(1), V0(1), X0(2), V0(2), X0(3), V0(3), X0(4), V0(4), X0(5), V0(5)];

% definindo o tempo de 0.15 segundo
tspan = [0 0.15];

% Resolvendo a equa��o diferencial pela ODE45
opcoes = odeset('OutputFcn',@funcaoElasticoPlastico);
[T,X] = ode45(@funcaoCrash, tspan, x0, opcoes);

auxiliar = size(X);
A = zeros(auxiliar(1) - 1, Nmassas);

% Derivando as velocidades para obter acelera��es
A(:, 1) = diff(X(:, 2))./diff(T);
A(:, 2) = diff(X(:, 4))./diff(T);
A(:, 3) = diff(X(:, 6))./diff(T);
A(:, 4) = diff(X(:, 8))./diff(T);
A(:, 5) = diff(X(:, 10))./diff(T);

% Obter for�as com F = m*A
for i=1:Nmassas
    F(:, i) = m(i)*A(:, i);
end

% C�lculo da energia potencial das molas
E(:, 1) = k(1)*((X(:, 3) - X(:, 1)).^2)/2;
E(:, 2) = k(2)*((X(:, 5) - X(:, 3)).^2)/2;
E(:, 3) = kp(1)*((X(:, 5) - X(:, 1)).^2)/2;
E(:, 4) = kp(2)*((X(:, 5)).^2)/2;
E(:, 5) = k(3)*((X(:, 3)).^2)/2;
E(:, 6) = kp(3)*((X(:, 1)).^2)/2;
E(:, 7) = kp(4)*((X(:, 1)).^2)/2;
E(:, 8) = k(4)*((X(:, 9) - X(:, 5)).^2)/2;
E(:, 9) = k(5)*((X(:, 9) - X(:, 7)).^2)/2;
E(:, 10) = k(6)*((X(:, 9) - X(:, 5)).^2)/2;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GRAFICOS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%POSI��ES DAS MASSAS 1, 2, 3, 4 e 5
figure1 = figure(1)
plot(T, [X(:,1) X(:, 3) X(:, 5) X(:, 7) X(:, 9)]);
grid on
title('Gr�fico das Posi��es das Massas em Fun��o do Tempo');
str = {'$$ x1 $$', '$$ x2 $$', '$$ x3 $$', '$$ x4 $$', '$$ x5 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Posi��o das Massas [m]');

% VELOCIDADE DA MASSA 1
figure2 = figure(2)
plot(T, X(:, 2));
grid on
title('Gr�fico da Velocidade da Massa 1 em Fun��o do Tempo');
str = {'$$ v1 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Velocidade da Massa 1 [m/s]');

%VELOCIDADE DA MASSA 2
figure3 = figure(3)
plot(T, X(:, 4), 'r');
grid on
title('Gr�fico da Velocidade da Massa 2 em Fun��o do Tempo');
str = {'$$ v2 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Velocidade da Massa 2 [m/s]');

%VELOCIDADE DA MASSA 3
figure4 = figure(4)
plot(T, X(:, 6), 'y');
grid on
title('Gr�fico da Velocidade da Massa 3 em Fun��o do Tempo');
str = {'$$ v3 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Velocidade da Massa 3 [m/s]');

%VELOCIDADE DA MASSA 4
figure5 = figure(5)
plot(T, X(:, 8), 'm');
grid on
title('Gr�fico da Velocidade da Massa 4 em Fun��o do Tempo');
str = {'$$ v4 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Velocidade da Massa 4 [m/s]');

%VELOCIDADE DA MASSA 5
figure6 = figure(6)
plot(T, X(:, 10), 'g');
grid on
title('Gr�fico da Velocidade da Massa 5 em Fun��o do Tempo');
str = {'$$ v5 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Velocidade da Massa 5 [m/s]');

% VELOCIDADES JUNTAS
figure7 = figure(7)
subplot(5, 1, 1)
% Para o caso da velocidade da massa 1
plot(T, X(:, 2));
grid on
title('Gr�ficos das Velocidades Fun��o do Tempo');
xlabel('Tempo [s]');
ylabel('v1 [m/s]');

subplot(5, 1, 2)
% Para o caso da velocidade da massa 2
plot(T, X(:, 4), 'r');
grid on
xlabel('Tempo [s]');
ylabel('v2 [m/s]');

subplot(5, 1, 3)
% Para o caso da velocidade da massa 3
plot(T, X(:, 6), 'y');
grid on
xlabel('Tempo [s]');
ylabel('v3 [m/s]');

subplot(5, 1, 4)
% Para o caso da velocidade da massa 4
plot(T, X(:, 8), 'm');
grid on
xlabel('Tempo [s]');
ylabel('v4 [m/s]');

subplot(5, 1, 5)
% Para o caso da velocidade da massa 5
plot(T, X(:, 10), 'g');
grid on
xlabel('Tempo [s]');
ylabel('v5 [m/s]');

% ACELERA��O DA MASSA 1
figure8 = figure(8)
auxiliar2 = size(A);
Taux = T(1: auxiliar2(1));
plot(Taux, A(:, 1))
grid on
title('Gr�fico da Acelera��o da Massa 1 em Fun��o do Tempo');
str = {'$$ a1 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Acelera��o da Massa 1 [m/s^2]');

% ACELERA��O DA MASSA 2
figure9 = figure(9)
plot(Taux, A(:, 2), 'r')
grid on
title('Gr�fico da Acelera��o da Massa 2 em Fun��o do Tempo');
str = {'$$ a2 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Acelera��o da Massa 2 [m/s^2]');

% ACELERA��O DA MASSA 3
figure10 = figure(10)
plot(Taux, A(:, 3), 'y')
grid on
title('Gr�fico da Acelera��o da Massa 3 em Fun��o do Tempo');
str = {'$$ a3 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Acelera��o da Massa 3 [m/s^2]');

% ACELERA��O DA MASSA 4
figure11 = figure(11)
plot(Taux, A(:, 4), 'm')
grid on
title('Gr�fico da Acelera��o da Massa 4 em Fun��o do Tempo');
str = {'$$ a4 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Acelera��o da Massa 4 [m/s^2]');

% ACELERA��O DA MASSA 5
figure12 = figure(12)
plot(Taux, A(:, 5), 'g')
grid on
title('Gr�fico da Acelera��o da Massa 5 em Fun��o do Tempo');
str = {'$$ a5 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Acelera��o da Massa 5 [m/s^2]');

% ACELERA��ES JUNTAS
figure13 = figure(13)
subplot(5, 1, 1)
% Para o caso da acelera��o da massa 1
plot(Taux, A(:, 1))
grid on
title('Gr�ficos das Acelera��es Fun��o do Tempo');
xlabel('Tempo [s]');
ylabel('a1 [m/s^2]');

subplot(5, 1, 2)
% Para o caso da acelera��o da massa 2
plot(Taux, A(:, 2), 'r')
grid on
xlabel('Tempo [s]');
ylabel('a2 [m/s^2]');

subplot(5, 1, 3)
% Para o caso da acelera��o da massa 3
plot(Taux, A(:, 3), 'y')
grid on
xlabel('Tempo [s]');
ylabel('a3 [m/s^2]');

subplot(5, 1, 4)
% Para o caso da acelera��o da massa 4
plot(Taux, A(:, 4), 'm')
grid on
xlabel('Tempo [s]');
ylabel('a4 [m/s^2]');

subplot(5, 1, 5)
% Para o caso da acelera��o da massa 5
plot(Taux, A(:, 5), 'g')
grid on
xlabel('Tempo [s]');
ylabel('a5 [m/s^2]');

% FOR�A 1
figure14 = figure(14)
plot(Taux, F(:, 1))
grid on
title('Gr�fico da For�a da Massa 1 em Fun��o do Tempo');
str = {'$$ F1 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('F1 [N]');

% FOR�A 2
figure15 = figure(15)
plot(Taux, F(:, 2), 'r')
grid on
title('Gr�fico da For�a da Massa 2 em Fun��o do Tempo');
str = {'$$ F2 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('F2 [N]');

% FOR�A 3
figure16 = figure(16)
plot(Taux, F(:, 3), 'y')
grid on
title('Gr�fico da For�a da Massa 3 em Fun��o do Tempo');
str = {'$$ F3 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('F3 [N]');

% FOR�A 4
figure17 = figure(17)
plot(Taux, F(:, 4), 'm')
grid on
title('Gr�fico da For�a da Massa 4 em Fun��o do Tempo');
str = {'$$ F4 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('F4 [N]');

% FOR�A 5
figure18 = figure(18)
plot(Taux, F(:, 5), 'g')
grid on
title('Gr�fico da For�a da Massa 5 em Fun��o do Tempo');
str = {'$$ F5 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('F5 [N]');

% FOR�AS JUNTAS
figure19 = figure(19)
subplot(5, 1, 1)
% Para o caso da for�a da massa 1
plot(Taux, F(:, 1))
grid on
title('Gr�ficos das For�as Fun��o do Tempo');
xlabel('Tempo [s]');
ylabel('F1 [N]');

subplot(5, 1, 2)
% Para o caso da for�a da massa 2
plot(Taux, F(:, 2), 'r')
grid on
xlabel('Tempo [s]');
ylabel('F2 [N]');

subplot(5, 1, 3)
% Para o caso da for�a da massa 3
plot(Taux, F(:, 3), 'y')
grid on
xlabel('Tempo [s]');
ylabel('F3 [N]');

subplot(5, 1, 4)
% Para o caso da for�a da massa 4
plot(Taux, F(:, 4), 'm')
grid on
xlabel('Tempo [s]');
ylabel('F4 [N]');

subplot(5, 1, 5)
% Para o caso da for�a da massa 5
plot(Taux, F(:, 5), 'g')
grid on
xlabel('Tempo [s]');
ylabel('F5 [N]');

% ENERGIAS POTENCIAIS DE CADA MOLA
figure20 = figure(20)
plot(T, E);
grid on
title('Gr�fico da Energia Potencial das Molas pelo Tempo');
str = {'$$ E1 $$', '$$ E2 $$', '$$ E3 $$', '$$ E4 $$', '$$ E5 $$', '$$ E6 $$', '$$ E7 $$', '$$ E8 $$', '$$ E9 $$', '$$ E10 $$'};
h = legend(str, 'Interpreter','latex', 'Location','NW');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('Energia potencial das molas [J]');


Taux=T(2:end);
intervalos=[]; %cria os intervalos para separacao a cada 15ms
index=1;
len=size(Taux);
limite=((tspan/.015)-1);
limite=limite(2);
HICt=[0.0075]; %vetor para plotar HIT em funcao do tempo
for i=1:limite
	HICt=[HICt;(HICt(end)+.015)];
	while Taux(index)<(i*.015)
		index=index+1;
	end
	intervalos=[intervalos;(index-1)];
	i;
	j;
	intervalos;
end
intervalos=[intervalos;len(1)];


%calcula HIC15 em funcao do tempo e plota os graficos
lineSpec= [":^" ":^r" ":^y" ":^m" ":^g"]; %cor do plot
HICs=[];
for j = 1:5
	HIC=[];
	indexAux=1;
	for i = transpose(intervalos)
		integral=trapz(Taux(indexAux:i,:),A(indexAux:i,j));
		HIC=[HIC;integral]; %integra aceleracao com tempo com intervalo de 0,015s e vai gerando a media temporal de aceleracao
		trapz(Taux(indexAux:i,:),A(indexAux:i,j));
		indexAux=i;
	end
	HIC=HIC./0.015;
	HIC=abs(HIC);
	HIC=HIC./9.78;
	HIC=HIC.^2.5;
	HIC=HIC.*0.015; %Operacoes na media da aceleracao para calcular HIC
	HICs=[HICs HIC]; %Junta vetores de HIC para comparacao

	%plota os graficos de HIC
	fig='figure';
	str=int2str(j+20);
	figureHic = figure(j+20);
	plot(HICt, HIC,lineSpec(j));
	grid on
	title(sprintf('Gr�fico do HIC15 da Massa %.0f em Fun��o do Tempo', j));
	maxHIC=max(HIC); %anotacao para maior HIC de cada massa
	str = {sprintf('$$ HIC%.0f $$', j)};
	anot=sprintf('Maior HIC = %0.1f',maxHIC);
	dim=[.2 .5 .3 .3];
	annotation('textbox', dim, 'String', anot, 'FitBoxToText','on');
	h = legend(str, 'Interpreter','latex', 'Location','NE'); 
	set(h, 'FontSize', 12);
	xlabel('Tempo [s]');
	ylabel(sprintf('HIC da Massa %.0f []',j));
	%nome=strcat(fig,str);
	nome=sprintf('HIC %d.jpg',j);
	saveas(figureHic,nome);
end

figure26 = figure(26)
plot(HICt, HICs);
grid on
title('Gr�fico dos HICs 15 pelo Tempo');
str = {'$$ HIC1 $$', '$$ HIC2 $$', '$$ HIC3 $$', '$$ HIC4 $$', '$$ HIC5 $$'};
maxHIC=max(HICs);
maxHIC=max(maxHIC);
[linha, coluna] = find (HICs==maxHIC);
anot=sprintf('Maior HIC = %0.1f, da massa %d',maxHIC, coluna);
dim=[.2 .5 .3 .3];
annotation('textbox', dim, 'String', anot, 'FitBoxToText','on');
h = legend(str, 'Interpreter','latex', 'Location','NE');
set(h, 'FontSize', 12);
xlabel('Tempo [s]');
ylabel('HICs 15 das massas []');


%armazena respostas
ftime = fopen('Response.dat','wt');
for ii = 1:size(T)
    fprintf(ftime,'%g %g %g %g \t',T(ii),X(ii,1),X(ii,3),X(ii,5));
    fprintf(ftime,'\n');
    
end
fclose(ftime)

% Salva as figuras
saveas(figure1,'Posicoes.jpg')  
saveas(figure2,'Velocidade 1.jpg')
saveas(figure3,'Velocidade 2.jpg')
saveas(figure4,'Velocidade 3.jpg')
saveas(figure5,'Velocidade 4.jpg')
saveas(figure6,'Velocidade 5.jpg')
saveas(figure7,'Velocidades.jpg')
saveas(figure8,'Aceleracao 1.jpg')
saveas(figure9,'Aceleracao 2.jpg')
saveas(figure10,'Aceleracao 3.jpg')
saveas(figure11,'Aceleracao 4.jpg')
saveas(figure12,'Aceleracao 5.jpg')
saveas(figure13,'Aceleracoes.jpg')
saveas(figure14,'Forca 1.jpg')
saveas(figure15,'Forca 2.jpg')
saveas(figure16,'Forca 3.jpg')
saveas(figure17,'Forca 4.jpg')
saveas(figure18,'Forca 5.jpg')
saveas(figure19,'Forcas.jpg')
saveas(figure20,'Energias potenciais.jpg')
saveas(figure26,'HICs.jpg')



Aabs = abs(A);
for i=1:Nmassas
    Amax(i) = max(Aabs(:, i));
    Fmax(i) = m(i)*Amax(i);
end

Amax
Fmax