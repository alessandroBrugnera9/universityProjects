% Aqui será definido uma função responsável por realizar a provisão
% plástica ou elática.

function status = funcaoElasticoPlastico(t,y,flag)
% 'OutputFnc' eh a opcao em ODE45 e eh fechado:
% input variaveis: tempo(t), output de ODE45(y), e o estado informacao (flag
% = 'inicio' primeiro passo (estado de inicializacao), 
% = 'fim' ultimo passo (estado final), 
% = [ ] nos outros passos)

%Aqui, o eh usado para calcular a deformacao plastica e armazena-las nas variaveis yy

 global tt yy kp Fy Nmolas
 
 % Variável contador verifica se global está certo [verificado] e se passa
 % pelas funções for e ifs. Também estão funcionando
 
 % Para o teste da professora coloque comentários em yp(3) e yp(2)
 
 % Modo oficial
 yp(1)=yy(1,end);
 yp(2)=yy(2,end);
 yp(3)=yy(3,end);
 yp(4)=yy(4,end);
 
 if isempty(flag)    % [] - empty flag
 % PREVISAO ELASTICA
    
   % Previsão oficial
   Ft(1) = kp(1)*(y(5) - y(1) - yp(1));
   Ft(2) = kp(2)*(y(5) - yp(2));
   Ft(3) = kp(3)*(y(1) - yp(3));
   Ft(4) = kp(4)*(y(1) - yp(4));
   
   for i=1:Nmolas
     phi=Ft(i)-Fy(i);
     if phi <= 0
        yp_new=yp(i);
        
     else
% CORRECAO PLASTICA
        yp_new=yp(i)+phi/kp(i);
     end
     tt = [tt t];
     yy(i,end)= yp_new;
   end
else
  switch(flag) %flag — Estado atual do algoritmo
  case 'inicio'   % 'inicio' — Estado inicial
  fprintf('start\n');
  tt = t(1);
  case 'fim'   % 'fim' — Estado final
  fprintf('fim\n');
 end
end
status = 0;