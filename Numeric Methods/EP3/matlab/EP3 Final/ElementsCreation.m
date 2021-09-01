function elementostotal=ElementsCreation(L1,A1,L2,A2,L3,I1,I2)
%elemento=[L A I theta Nó1 Nó2 PosX1 PosX2 Pos Y1 PosY2]

elemento1=[L1 A2 I2 0 1 2 1 3 14 14];
elemento2=[L1 A2 I2 pi/2 3 1 1 1 12 14];
elemento3=[sqrt(2)*L1 A1 I1 3*pi/4 4 1 3 1 12 14];
elemento4=[L1 A2 I2 pi/2 4 2 3 3 12 14];
elemento5=[L1 A1 I1 0 3 4 1 3 12 12];
elemento6=[L1 A2 I2 pi/2 5 3 1 1 10 12];
elemento7=[sqrt(2)*L1 A1 I1 pi/4 5 4 1 3 10 12];
elemento8=[L1 A2 I2 pi/2 6 4 3 3 10 12];
elemento9=[L1 A1 I1 0 5 6 1 3 10 10];
elemento10=[L1 A2 I2 pi/2 7 5 1 1 8 10];
elemento11=[sqrt(2)*L1 A1 I1 3*pi/4 8 5 3 1 8 10];
elemento12=[L1 A2 I2 pi/2 8 6 3 3 8 10];
elemento13=[L1 A1 I1 0 7 8 1 3 8 8];
elemento14=[L1 A2 I2 pi/2 9 7 1 1 6 8];
elemento15=[sqrt(2)*L1 A1 I1 pi/4 9 8 1 3 6 8];
elemento16=[L1 A2 I2 pi/2 10 8 3 3 6 8];
elemento17=[L1 A1 I1 0 9 10 1 3 6 6];
elemento18=[sqrt(3^2+0.5^2) A2 I2 atan(6) 11 9 0.5 1 3 6];
elemento19=[sqrt(3^2+2.5^2) A1 I1 atan(1.2) 11 10 0.5 3 3 6];
elemento20=[sqrt(3^2+0.5^2) A2 I2 pi-atan(6) 12 10 3.5 3 3 6];
elemento21=[sqrt(3^2+2.5^2) A1 I1 pi-atan(6) 12 9 3.5 1 3 6];
elemento22=[3 A1 I1 0 11 12 0.5 3.5 3 3];
elemento23=[sqrt(3^2+0.5^2) A2 I2 atan(6) 13 11 0 0.5 0 3];
elemento24=[5 A1 I1 atan(3/4) 13 12 0 3.5 0 3];
elemento25=[sqrt(3^2+0.5^2) A2 I2 pi-atan(6) 14 12 4 3.5 0 3];
elemento26=[5 A1 I1 pi-atan(3/4) 14 11 4 0.5 0 3];
elemento27=[L3 A2 I2 0 13 14 0 4 0 0];

elementostotal=[elemento1;elemento2;elemento3;elemento4;elemento5;...
    elemento6;elemento7;elemento8;elemento9;elemento10;...
    elemento11;elemento12;elemento13;elemento14;elemento15;elemento16;...
    elemento17;elemento18;elemento19;elemento20;elemento21;elemento22;...
    elemento23;elemento24;elemento25;elemento26;elemento27];

PlotTower(elementostotal)

end

