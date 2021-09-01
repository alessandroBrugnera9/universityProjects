function [nos, elementos] = criaNos(elementos)
    no.x = 0;
    no.y = 0;
    nos=[no];

    %cria um ponto se nao estiver na lista
    for i = 1:length(elementos)
        elementos(i).xm =  (elementos(i).x1 + elementos(i).x2 + elementos(i).x3)/3;
        elementos(i).ym =  (elementos(i).y1 + elementos(i).y2 + elementos(i).y3)/3;
        elemento = elementos(i);
        %vertice 1
        elementos(i).no1 = -1;
        noParcial.x = elemento.x1;
        noParcial.y = elemento.y1;
        for j = 1:length(nos) 
            if isequal(noParcial, nos(j))
                elementos(i).no1 = j;
                break
            end        
        end
        
        if elementos(i).no1 == -1
                nos = [nos, noParcial];
                elementos(i).no1 = j+1;
        end
        %vertice 2
        elementos(i).no2 = -1;
        noParcial.x = elemento.x2;
        noParcial.y = elemento.y2;
        for j = 1:length(nos)        
            if isequal(noParcial, nos(j))
                elementos(i).no2 = j;
            end

        end
        if elementos(i).no2 == -1
                nos = [nos, noParcial];
                elementos(i).no2 = j+1;
        end
        %vertice 3
        elementos(i).no3 = -1;
        noParcial.x = elemento.x3;
        noParcial.y = elemento.y3;
        for j = 1:length(nos)        
            if isequal(noParcial, nos(j))
                elementos(i).no3 = j;
            end        
        end
        if elementos(i).no3 == -1
            nos = [nos, noParcial];
            elementos(i).no3 = j+1;
        end
    end
    
end