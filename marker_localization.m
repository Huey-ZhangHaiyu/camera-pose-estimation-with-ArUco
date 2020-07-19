% 452 project1
% Author: Haiyu Zhang
% last date:11/06/2019
%%this program gives the makers position in the s frame
%% Gca1,assume id=1 maker is 'a' frame
wca1=[-2.64982004 -0.03993104 -1.7647248];% w and p should get from python program
pca1=[-0.16183371  0.23086657  0.83411458]';
wca1_hat=[0 -wca1(3) wca1(2);wca1(3) 0 -wca1(1);-wca1(2) wca1(1) 0];
Rca1=expm(wca1_hat);
gca1=zeros(4,4);
gca1(1:3,1:3)=Rca1;
gca1(1:3,4)=pca1;
gca1(4,4)=1;
%% Gcs13,assume id=13 maker is 'spatial' frame
wcs13=[2.52624569 -0.18739325 -1.04466273];
pcs13=[0.45375666 -0.15702111  0.89771882]';
wcs13_hat=[0 -wcs13(3) wcs13(2);wcs13(3) 0 -wcs13(1);-wcs13(2) wcs13(1) 0];
Rcs13=expm(wcs13_hat);
gcs13=zeros(4,4);
gcs13(1:3,1:3)=Rcs13;
gcs13(1:3,4)=pcs13;
gcs13(4,4)=1;
%% Gcb7,assume id=7 maker is 'b' frame
wcb7=[2.53688743 0.0529865  1.77801876];
pcb7=[-0.23087657 -0.1424681   0.6414923]';
wcb7_hat=[0 -wcb7(3) wcb7(2);wcb7(3) 0 -wcb7(1);-wcb7(2) wcb7(1) 0];
Rcb7=expm(wcb7_hat);
gcb7=zeros(4,4);
gcb7(1:3,1:3)=Rcb7;
gcb7(1:3,4)=pcb7;
gcb7(4,4)=1;
%% Gcd23,assume id=23 maker is 'd' frame
wcd23=[2.09377745 1.08209618 0.75764534];
pcd23=[-0.23271272 -0.11887292  0.80152168]';
wcd23_hat=[0 -wcd23(3) wcd23(2);wcd23(3) 0 -wcd23(1);-wcd23(2) wcd23(1) 0];
Rcd23=expm(wcd23_hat);
gcd23=zeros(4,4);
gcd23(1:3,1:3)=Rcd23;
gcd23(1:3,4)=pcd23;
gcd23(4,4)=1;
%% marker localization
gsa=inv(gcs13)*gca1;
gsb=inv(gcs13)*gcb7;
gsd=inv(gcs13)*gcd23;
