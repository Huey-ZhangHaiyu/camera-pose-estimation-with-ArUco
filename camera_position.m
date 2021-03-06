% 452 project1
% Author:Haiyu Zhang
% last date:11/06/2019
%%this grogram calculates the camera's position in spatial frame
%% maker's position, we get these relation in marker_localization.m program
gsa=[0.175543991946175,-0.00128750892827047,0.984470745737201,-0.464162390219705;
    -0.00550417718257093,0.999982231499083,0.00228926181497291,-0.182819262752232;
    -0.984456200612878,-0.00582056757320526,0.175533786115328,0.0938214753708191;
    0,0,0,1];
gsb=[0.128384949465169,0.00308734578258893,0.991719604044835,-0.485246487687825;
    -0.0131085572690340,0.999913076755797,-0.00141585983800709,0.182031485125812;
    -0.991637771808411,-0.0128182381306933,0.128414260477854,0.312198277481697;
    0,0,0,1];
gsd=[-0.00425780197336358,-0.0379599519088322,0.999270190275600,-0.436620792833732;
    -0.681643805998138,0.731261226564692,0.0248744902957869,-0.0933887958531532;
    -0.731671779465854,-0.681040425066076,-0.0289887315881539,0.531592136789458;
    0,0,0,1];
%% a, use 'a' marker to get camera's position
wca=[3.12063757  0.05826803 -0.02756371];
pca=[0.12948015 0.18102237 0.76534956];
wca_hat=[0 -wca(3) wca(2);wca(3) 0 -wca(1);-wca(2) wca(1) 0];
Rca=expm(wca_hat);
gca=zeros(4,4);
gca(1:3,1:3)=Rca;
gca(1:3,4)=pca;
gca(4,4)=1;
gsca=gsa*inv(gca);
%% b, use 'b' marker to get camera's position
wcb=[-3.04324965 -0.08627191  0.06695387];
pcb=[-0.06473757 -0.18571389  0.77721297];
wcb_hat=[0 -wcb(3) wcb(2);wcb(3) 0 -wcb(1);-wcb(2) wcb(1) 0];
Rcb=expm(wcb_hat);
gcb=zeros(4,4);
gcb(1:3,1:3)=Rcb;
gcb(1:3,4)=pcb;
gcb(4,4)=1;
gscb=gsb*inv(gcb);
%% d, use 'd' marker to get camera's position
wcd=[-2.80389694 -1.18893446  0.329907];
pcd=[-0.10491403  0.08071888  0.74983183];
wcd_hat=[0 -wcd(3) wcd(2);wcd(3) 0 -wcd(1);-wcd(2) wcd(1) 0];
Rcd=expm(wcd_hat);
gcd=zeros(4,4);
gcd(1:3,1:3)=Rcd;
gcd(1:3,4)=pcd;
gcd(4,4)=1;
gscd=gsd*inv(gcd);
%% average
gsc=(gsca+gscb+gscd)/3;
