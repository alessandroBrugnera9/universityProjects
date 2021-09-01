function [elementosfinais Num_Nos]=...
    RightElementsCreation(elementostotal,Numero_elementos)
    d1i=0.040; 
    d1e=0.050;
    d2i=0.090;
    d2e=0.100;
    A1=pi*(d1e^2-d1i^2)/4;
    I1=pi*(d1e^4-d1i^4)/64;
    A2=pi*(d2e^2-d2i^2)/4;
    I2=pi*(d2e^4-d2i^4)/64;
    %elementosfinais=[L A I theta Nó1 Nó2 PosX1 PosX2 Pos Y1 PosY2]

    Num_Nos=14;

    elementosfinais=zeros(length(elementostotal)*Numero_elementos,10);

    for i=1:length(elementostotal)
        Coord_xinit=elementostotal(i,7);
        Coord_yinit=elementostotal(i,9);
        Coord_xinit2=elementostotal(i,8);
        Coord_yinit2=elementostotal(i,10);
        for j=1:Numero_elementos
            if j==1
                Coord_x1=Coord_xinit;
                Coord_y1=Coord_yinit;
                posno=find(elementostotal(:,7)==Coord_x1 & ...
                    elementostotal(:,9)==Coord_y1);
                if length(posno)~=0
                    noanterior=elementostotal(posno(1),5);                
                else
                    posno=find(elementostotal(:,8)==Coord_x1 &...
                        elementostotal(:,10)==Coord_y1);
                    noanterior=elementostotal(posno(1),6);
                end
            else
                Coord_x1=Coord_x2;
                Coord_y1=Coord_y2;
            end
            Coord_x2=Coord_xinit+(j/Numero_elementos)*(Coord_xinit2-Coord_xinit);
            Coord_y2=Coord_yinit+(j/Numero_elementos)*(Coord_yinit2-Coord_yinit);
            Coord_L=sqrt((Coord_x2-Coord_x1)^2+(Coord_y2-Coord_y1)^2);
            if Coord_x1>Coord_x2
                Coord_Ang=pi-atan((Coord_y2-Coord_y1)/(Coord_x1-Coord_x2));
            else
                Coord_Ang=atan((Coord_y2-Coord_y1)/(Coord_x2-Coord_x1));
            end
            No_Novo_x=find(elementostotal(:,7)==Coord_x2);
            No_Novo_x2=find(elementostotal(:,8)==Coord_x2);
            No_Novo_y=find(elementostotal(:,9)==Coord_y2);
            No_Novo_y2=find(elementostotal(:,10)==Coord_y2);
            [novo,onde]=ismember(No_Novo_y,No_Novo_x);
            [novo2,onde2]=ismember(No_Novo_y2,No_Novo_x2);
            if sum(novo)~=0
                %Tem o mesmo valor nos dois
                plau=find(novo==1);
                noatual=elementostotal(No_Novo_y(plau(1)),5);
            elseif sum(novo2)~=0
                %Tem o mesmo valor nos dois
                plau2=find(novo2==1);
                noatual=elementostotal(No_Novo_y2(plau2(1)),6);
            else
                Num_Nos=Num_Nos+1;
                noatual=Num_Nos;
            end
            if elementostotal(i,3)==I1
                elementosfinais(i*Numero_elementos+j-Numero_elementos,:)=...
                    [Coord_L,A1,I1,Coord_Ang noanterior noatual...
                    Coord_x1 Coord_x2 Coord_y1 Coord_y2];
            else
                elementosfinais(i*Numero_elementos+j-Numero_elementos,:)=...
                    [Coord_L,A2,I2,Coord_Ang noanterior noatual...
                    Coord_x1 Coord_x2 Coord_y1 Coord_y2];            
            end
            noanterior=noatual;
        end
    end


    PlotTower(elementosfinais);
end

