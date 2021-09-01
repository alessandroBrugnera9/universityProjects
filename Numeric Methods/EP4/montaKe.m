function [K_el] = montaKe(elemento, ehSigma)
    % Montagem da matriz K do elemento
    x1 = elemento.x1;
    x2 = elemento.x2;
    x3 = elemento.x3;
    y1 = elemento.y1;
    y2 = elemento.y2;
    y3 = elemento.y3;

    b1 = y2 - y3;
    b2 = y3 - y1;
    b3 = y1 - y2;
    c1 = x3 - x2;
    c2 = x1 - x3;
    c3 = x2 - x1;
    
    Ae = (b1*c2 - b2*c1)/2;
    
    if ehSigma
        const = elemento.sigma;
    else
        const = elemento.mi;
    end 
    
    K_el = 1/(4*Ae)*const*[b1*b1+c1*c1 b1*b2+c1*c2 b1*b3+c1*c3;
                           b1*b2+c1*c2 b2*b2+c2*c2 b2*b3+c2*c3;
                           b1*b3+c1*c3 b2*b3+c2*c3 b3*b3+c3*c3];
end