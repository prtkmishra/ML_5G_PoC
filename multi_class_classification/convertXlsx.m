 data=load('data1.m');
 f=fieldnames(data);
 for k=1:size(f,1)
   xlswrite('data1.xlsx',data.(f{k}),f{k})
 end