function yponto = funcaoCrash(t,y)
% instancia array yponto
global yy kp m k 
% Para o caso do nosso exercício 
yponto = zeros(10,1);

% Para o caso do nosso exercício
% VEICULO
F1 = k(1)*(y(3) - y(1));
F2 = k(2)*(y(5) - y(3));
F3 = kp(1)*(y(5) - y(1) - yy(1,end));
F4 = kp(2)*(y(5) - yy(2,end));
F5 = k(3)*(y(3));
F6 = kp(3)*(y(1) - yy(3,end));
F7 = kp(4)*(y(1) - yy(4,end));

% PESSOA
F8 = k(4)*(y(5) - y(9)); % Cinto de segurança
Ft1 = k(5)*(y(7) - y(9)); % Pescoço
Ft2 = k(6)*(y(5) - y(9)); % Coluna

b1 = 1100;
Fb14 = b1*(y(6) - y(8)); % Aibag cabeça
Fb15 = b1*(y(6) - y(10)); % Airbag tronco

% O sefuguinte é válido para a resolução do nosso exercício
yponto(1)=y(2);
yponto(3)=y(4);
yponto(5)=y(6);
yponto(7)=y(8);
yponto(9)=y(10);
%
yponto(2)=(1/m(1))*(-F6-F7+F3-F1);
yponto(4)=(1/m(2))*(F1-F5+F2);
yponto(6)=(1/m(3))*((-F4-F3-F2)-Fb14-Fb15-F8+Ft2);
yponto(8) = (1/m(4))*(Fb14-Ft1);
yponto(10) = (1/m(5))*(Ft1+Fb15+F8-Ft2);
end