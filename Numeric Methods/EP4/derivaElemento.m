function [dx,dy] = derivaElemento(elemento, nos, ehSigma)
    %Calcula as derivadas parciais em um elemento
        x1 = elemento.x1;
        x2 = elemento.x2;
        x3 = elemento.x3;
        y1 = elemento.y1;
        y2 = elemento.y2;
        y3 = elemento.y3;
        
        if ehSigma
            V1 = nos(elemento.no1).V;
            V2 = nos(elemento.no2).V;
            V3 = nos(elemento.no3).V;
        else
            V1 = nos(elemento.no1).A;
            V2 = nos(elemento.no2).A;
            V3 = nos(elemento.no3).A;
        end
        b1= y2 - y3;
        b2= y3 - y1;
        b3= y1 - y2;
        c1= x3 - x2;
        c2= x1 - x3;
        c3= x2 - x1;
        Ae= (b1*c2 - b2*c1)/2;
        dx = (1/(2*Ae))* (b1*V1 + b2*V2 + b3*V3);
        dy = (1/(2*Ae))* (c1*V1 + c2*V2 + c3*V3);
    end