function K = matrizGlobal(elementos, lenNos, ehSigma)
    K = zeros(lenNos);
    for i = 1:length(elementos)    
        matrizLocal = montaKe(elementos(i),ehSigma);
        n1 = elementos(i).no1;
        n2 = elementos(i).no2;
        n3 = elementos(i).no3;
        K(n1,n1) = K(n1,n1) + matrizLocal(1,1);
        K(n1,n2) = K(n1,n2) + matrizLocal(1,2);
        K(n1,n3) = K(n1,n3) + matrizLocal(1,3);
        K(n2,n1) = K(n2,n1) + matrizLocal(2,1);
        K(n2,n2) = K(n2,n2) + matrizLocal(2,2);
        K(n2,n3) = K(n2,n3) + matrizLocal(2,3);
        K(n3,n1) = K(n3,n1) + matrizLocal(3,1);
        K(n3,n2) = K(n3,n2) + matrizLocal(3,2);
        K(n3,n3) = K(n3,n3) + matrizLocal(3,3);
    end 
end