function PlotTower(elementostotal)
    figure()
    d1i=0.040; 
    d1e=0.050;
    I1=pi*(d1e^4-d1i^4)/64;
    
    grossas=find(elementostotal(:,3)~=I1);
    finas=find(elementostotal(:,3)==I1);
    elementosgrossos=elementostotal(grossas,:);
    elementosfinos=elementostotal(finas,:);
    
    for i=1:length(elementosgrossos(:,1))
        plot([elementosgrossos(i,7) elementosgrossos(i,8)],...
            [elementosgrossos(i,9) elementosgrossos(i,10)],'r-','LineWidth',2)
        hold on
    end
    
    for j=1:length(elementosfinos(:,1))
        plot([elementosfinos(j,7) elementosfinos(j,8)],...
            [elementosfinos(j,9) elementosfinos(j,10)],'b-','LineWidth',1)
        hold on  
    end

    axis equal
    if length(elementostotal)==27
        title('Torre completa')
        xlabel('X')
        ylabel('Y')
        saveas(gcf,'torrecompletacarazzi.jpg')
    else
        scatter(elementosgrossos(:,7),elementosgrossos(:,9),16,'y','filled')
        scatter(elementosgrossos(:,8),elementosgrossos(:,10),16,'y','filled')    
        scatter(elementosfinos(:,7), elementosfinos(:,9),16,'y','filled')
        scatter(elementosfinos(:,8),elementosfinos(:,10),16,'y','filled')
        title('Torre com divisão de elementos')
        xlabel('X')
        ylabel('Y')
        saveas(gcf,'torrecomelementoscarazzi.jpg')
    end
end