
vidobj=VideoWriter('polzero.avi');
%vidobj.CompressionRatio=1;
vidobj.FrameRate=60;
%vidobj.FileFormat='mp4'
open(vidobj);
figure('units','pixels','position',[0 0 1920 1080])


[X,Y] = meshgrid(-10:.05:0,-10:.05:10);
s=X+1j.*Y;
Z=((s+3))./((s+1).*(s+5));
zero=(s+3);



%surf(X,Y,abs(Z))
%shading interp
%xlabel("sigma")
%ylabel("omega")
%zlabel("z")

surf(X,Y,abs(zero))
shading interp



pbaspect([1 0.83 0.5])

axis([-10 0 -10 10 0 5])
caxis([0 5])


%set(gca, 'YScale', 'log')
%set(gca, 'ZScale', 'log')

%m=[t' abs(e)'];
%csvwrite('sumof2rationals.csv',m)


set(gcf,'color','black')
    set(gca,'color',[0 0 0]);
    axis([-10 0 -10 10 0 5])
    caxis([0 5])
    
    
%set(gca, 'YScale', 'log')




    grid on;
    ax = gca % Get handle to current axes.
    ax.XColor = [0.7 0.7 0.7]; % Red
    ax.YColor = [0.7 0.7 0.7]; % Blue
    ax.ZColor = [0.7 0.7 0.7];
    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
    ax.XRuler.Axle.LineWidth = 3;
    ax.YRuler.Axle.LineWidth = 3;
    ax.ZRuler.Axle.LineWidth = 3;

    set(gca,'XMinorGrid','on')
    set(gca,'YMinorGrid','on')
    set(gca,'ZMinorGrid','on')

    axis_width_in_pixles=800;
    axis_height_in_pixles=800;
    x0=960-(axis_width_in_pixles/2);
    y0=540-(axis_height_in_pixles/2);
    width=1920;
    height=1080;
    set(gcf,'position',[0,0,width,height])
    set(gca, 'Units', 'pixels')
    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
    zticklabels([]);
    %view(-79,21)
    %view(-49,17)
    view(0,0)


    for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
    %view(-79,21)
    %view(-49,17)
    view(0,0)

    end












%__________ camera animation _______________________________________________________

az=0;
ev=0;

view(az,ev)
pause(1)
for k=1:50
    writeVideo(vidobj,getframe(gcf));
    az=az-1.58
    ev=ev+0.42;

    view(az,ev)
    pause(0.00001)



end
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end










t=linspace(0.001,1000,100000);

e1=0.5./(1j*t+1);
e2=0.5./(1j*t+5);
sum=e1+e2;

plot(t,rad2deg(angle(e1)))
set(gca, 'XScale', 'log')


%m1=[t',abs(e1)'];
%m2=[t',abs(e2)'];
%m3=[t',abs(sum)'];

%csvwrite('pole1_res.csv',m1)
%csvwrite('pole2_res.csv',m2)
%csvwrite('sum_of_2_poles_res.csv',m3)





%________________________________________________

%{
t=linspace(0,10,1000);

pulsewidth = 2;
pulseperiods = [0:10]*4;

x = pulstran(t,pulseperiods,@rectpuls,pulsewidth);

plot(t,x)
axis([0 10 0 1.1])
m=[t',x']
csvwrite('rect_train.csv',m)
%}


%[X,Y] = meshgrid(-7:.01:3,-50:0.01:50);
%s=X+1j.*Y;
%Z= frame(i)./(s+5);

vidobj=VideoWriter('polzero.avi');
%vidobj.CompressionRatio=1;
vidobj.FrameRate=60;
%vidobj.FileFormat='mp4'
open(vidobj);
figure('units','pixels','position',[0 0 1920 1080])


%frame=linspace(1,10,100);
%for i=1:length(frame);
%    Z(:,:,i)= frame(i)./(s+5);
%end

%surf(X,Y,abs(Z))
%pbaspect([1 0.83 0.5])
%shading interp
%
%set(gcf,'color','black')
%set(gca,'color',[0 0 0]);
%axis([-7 3 -20 20 0 0.6])
%caxis([0 0.6])
%
%
%
%
%grid on;
%ax = gca % Get handle to current axes.
%ax.XColor = [0.7 0.7 0.7]; % Red
%ax.YColor = [0.7 0.7 0.7]; % Blue
%ax.ZColor = [0.7 0.7 0.7];
%ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%ax.XRuler.Axle.LineWidth = 3;
%ax.YRuler.Axle.LineWidth = 3;
%ax.ZRuler.Axle.LineWidth = 3;
%
%set(gca,'XMinorGrid','on')
%set(gca,'YMinorGrid','on')
%set(gca,'ZMinorGrid','on')
%
%axis_width_in_pixles=800;
%axis_height_in_pixles=800;
%x0=960-(axis_width_in_pixles/2);
%y0=540-(axis_height_in_pixles/2);
%width=1920;
%height=1080;
%set(gcf,'position',[0,0,width,height])
%set(gca, 'Units', 'pixels')
%set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%    xticklabels([-7,-6,-5,-4,-3,-2,-1,0,1,2,3]);
%    yticks([-20,-15,-10,-5,0,5,10,15,20])
%    yticklabels([]);
%    zticks([2,4,6,8,10,12,14])
%    zticklabels([]);
%    %xlabel("sigma")
%    %ylabel("jw")
%    view(-221,33.15)









writeVideo(vidobj,getframe(gcf));
%
    [X,Y] = meshgrid(-7:.01:3,-50:0.01:50);
    s=X+1j.*Y;
    Z= 1./(s+5);

    surf(X,Y,abs(Z))
    pbaspect([1 0.83 0.5])
    shading interp

    set(gcf,'color','black')
    set(gca,'color',[0 0 0]);
    axis([-7 3 -20 20 0 0.6])
    caxis([0 0.6])




    grid on;
    ax = gca % Get handle to current axes.
    ax.XColor = [0.7 0.7 0.7]; % Red
    ax.YColor = [0.7 0.7 0.7]; % Blue
    ax.ZColor = [0.7 0.7 0.7];
    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
    ax.XRuler.Axle.LineWidth = 3;
    ax.YRuler.Axle.LineWidth = 3;
    ax.ZRuler.Axle.LineWidth = 3;

    set(gca,'XMinorGrid','on')
    set(gca,'YMinorGrid','on')
    set(gca,'ZMinorGrid','on')

    axis_width_in_pixles=800;
    axis_height_in_pixles=800;
    x0=960-(axis_width_in_pixles/2);
    y0=540-(axis_height_in_pixles/2);
    width=1920;
    height=1080;
    set(gcf,'position',[0,0,width,height])
    set(gca, 'Units', 'pixels')
    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])


    xticklabels([-7,-6,-5,-4,-3,-2,-1,0,1,2,3]);
    yticks([-20,-15,-10,-5,0,5,10,15,20])
    yticklabels([]);
    zticks([2,4,6,8,10,12,14])
    zticklabels([]);
    %xlabel("sigma")
    %ylabel("jw")
    view(221,33.15)









%___________________ animate increasing the jw axis from -5,5 to -20,20 __________________________
%jw=linspace(5,20,50)
%for i=1:50
%    writeVideo(vidobj,getframe(gcf));
%
%    surf(X,Y,abs(Z))
%    pbaspect([1 0.83 0.5])
%    shading interp
%
%    set(gcf,'color','black')
%    set(gca,'color',[0 0 0]);
%    axis([-7 3 -jw(i) jw(i) 0 15])
%    caxis([0 15])
%
%
%
%
%    grid on;
%    ax = gca % Get handle to current axes.
%    ax.XColor = [0.7 0.7 0.7]; % Red
%    ax.YColor = [0.7 0.7 0.7]; % Blue
%    ax.ZColor = [0.7 0.7 0.7];
%    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%    ax.XRuler.Axle.LineWidth = 3;
%    ax.YRuler.Axle.LineWidth = 3;
%    ax.ZRuler.Axle.LineWidth = 3;
%
%    set(gca,'XMinorGrid','on')
%    set(gca,'YMinorGrid','on')
%    set(gca,'ZMinorGrid','on')
%
%    axis_width_in_pixles=800;
%    axis_height_in_pixles=800;
%    x0=960-(axis_width_in_pixles/2);
%    y0=540-(axis_height_in_pixles/2);
%    width=1920;
%    height=1080;
%    set(gcf,'position',[0,0,width,height])
%    set(gca, 'Units', 'pixels')
%    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%    %xticklabels([]);
%    yticks([-20,-15,-10,-5,0,5,10,15,20])
%    yticklabels([0]);
%    zticklabels([]);
%    %xlabel("sigma")
%    %ylabel("jw")
%    view(-221,33.15)
%    pause(0.00001)
%end

%______________animating zooming the graph ______________

%jw=linspace(15,0.6,50)
%for i=1:50
%    writeVideo(vidobj,getframe(gcf));
%
%    surf(X,Y,abs(Z))
%    pbaspect([1 0.83 0.5])
%    shading interp
%
%    set(gcf,'color','black')
%    set(gca,'color',[0 0 0]);
%    axis([-7 3 -20 20 0 jw(i)])
%    caxis([0 jw(i)])
%
%
%
%
%    grid on;
%    ax = gca % Get handle to current axes.
%    ax.XColor = [0.7 0.7 0.7]; % Red
%    ax.YColor = [0.7 0.7 0.7]; % Blue
%    ax.ZColor = [0.7 0.7 0.7];
%    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%    ax.XRuler.Axle.LineWidth = 3;
%    ax.YRuler.Axle.LineWidth = 3;
%    ax.ZRuler.Axle.LineWidth = 3;
%
%    set(gca,'XMinorGrid','on')
%    set(gca,'YMinorGrid','on')
%    set(gca,'ZMinorGrid','on')
%
%    axis_width_in_pixles=800;
%    axis_height_in_pixles=800;
%    x0=960-(axis_width_in_pixles/2);
%    y0=540-(axis_height_in_pixles/2);
%    width=1920;
%    height=1080;
%    set(gcf,'position',[0,0,width,height])
%    set(gca, 'Units', 'pixels')
%    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%    %xticklabels([]);
%    yticks([-20,-15,-10,-5,0,5,10,15,20])
%    yticklabels([]);
%    zticks([2,4,6,8,10,12,14])
%    zticklabels([]);
%    %xlabel("sigma")
%    %ylabel("jw")
%    view(-221,33.15)
%    pause(0.00001)
%end

%___________________________________________

%_________________________ animating camera _________________________

az=-221;
ev=33.15;
view(az,ev)
pause(1)
for k=1:50
    writeVideo(vidobj,getframe(gcf));
    az=az-1.48
    ev=ev-0.432

    view(az,ev)
    pause(0.00001)



end

%_________________________________________

%_____________animating reducing the surface from 3 to 0__________

%jw=linspace(1,-7,28)
%for i=1:24
%
%
%    writeVideo(vidobj,getframe(gcf));
%
%    [X,Y] = meshgrid(jw(i):.01:0,-50:0.01:50);
%    s=X+1j.*Y;
%    Z= frame(i)./(s+5);
%
%    surf(X,Y,abs(Z))
%    pbaspect([1 0.83 0.5])
%    shading interp
%
%    set(gcf,'color','black')
%    set(gca,'color',[0 0 0]);
%    axis([-7 3 -20 20 0 0.6])
%    caxis([0 0.6])
%
%
%
%
%    grid on;
%    ax = gca % Get handle to current axes.
%    ax.XColor = [0.7 0.7 0.7]; % Red
%    ax.YColor = [0.7 0.7 0.7]; % Blue
%    ax.ZColor = [0.7 0.7 0.7];
%    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%    ax.XRuler.Axle.LineWidth = 3;
%    ax.YRuler.Axle.LineWidth = 3;
%    ax.ZRuler.Axle.LineWidth = 3;
%
%    set(gca,'XMinorGrid','on')
%    set(gca,'YMinorGrid','on')
%    set(gca,'ZMinorGrid','on')
%
%    axis_width_in_pixles=800;
%    axis_height_in_pixles=800;
%    x0=960-(axis_width_in_pixles/2);
%    y0=540-(axis_height_in_pixles/2);
%    width=1920;
%    height=1080;
%    set(gcf,'position',[0,0,width,height])
%    set(gca, 'Units', 'pixels')
%    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%    xticklabels([-7,-6,-5,-4,-3,-2,-1,0,1,2,3]);
%    yticks([-20,-15,-10,-5,0,5,10,15,20])
%    yticklabels([]);
%    zticks([2,4,6,8,10,12,14])
%    zticklabels([]);
%    %xlabel("sigma")
%    %ylabel("jw")
%    view(65,12)
%
%end

%__________________________________

%axx=linspace(15,0.5,50);



%for k=1:50
%    writeVideo(vidobj,getframe(gcf));
%    [X,Y] = meshgrid(-7:.01:3,-50:0.01:50);
%    s=X+1j.*Y;
%    Z= 1./(s+5);
%
%    surf(X,Y,abs(Z))
%    shading interp
%
%
%    pbaspect([1 0.83 0.5])
%    shading interp
%
%    set(gcf,'color','black')
%    set(gca,'color',[0 0 0]);
%    %axis([-7 axx(k) -5 5 0 15])
%    axis([-7 3 -5 5 0 axx(k)])
%
%    %caxis([0 15])
%    caxis([0 axx(k)])
%
%
%    grid on;
%    ax = gca % Get handle to current axes.
%    ax.XColor = [0.7 0.7 0.7]; % Red
%    ax.YColor = [0.7 0.7 0.7]; % Blue
%    ax.ZColor = [0.7 0.7 0.7];
%    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%    ax.XRuler.Axle.LineWidth = 3;
%    ax.YRuler.Axle.LineWidth = 3;
%    ax.ZRuler.Axle.LineWidth = 3;
%
%    set(gca,'XMinorGrid','on')
%    set(gca,'YMinorGrid','on')
%    set(gca,'ZMinorGrid','on')
%
%    axis_width_in_pixles=800;
%    axis_height_in_pixles=800;
%    x0=960-(axis_width_in_pixles/2);
%    y0=540-(axis_height_in_pixles/2);
%    width=1920;
%    height=1080;
%    set(gcf,'position',[0,0,width,height])
%    set(gca, 'Units', 'pixels')
%    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%    xticks([-7 -6 -5 -4 -3 -2 -1 0 1 2 3])
%    xticklabels([-7 -6 -5 -4 -3 -2 -1 0 1 2 3]);
%    yticklabels([]);
%    zticks([2,4,6,8,10,12,14])
%    zticklabels([]);
%    %xlabel("sigma")
%    %ylabel("jw")
%%    view(65,12)
%   view(-221,33.15)
%%    view(-221,0)
%
%    pause(0.00001)
%
%
%end
%pause(1)


%______________________________________________________________________




%________ camera animation and recording video_________
%{
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end




az=0;
ev=0;
view(az,ev)
pause(1)
for k=1:221
    writeVideo(vidobj,getframe(gcf));
    az=az-1
    ev=ev+0.15
    
    view(az,ev)
    pause(0.00001)
    

    
end
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end
%}
%{
for k=1:100
    writeVideo(vidobj,getframe(gcf));
    az=az+0.51
    ev=ev-0.68
    view(az,ev)
    pause(0.00001)
    
end
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end
close(vidobj);
%}

%{
set(gca,'ZGrid','off')
set(gca,'YGrid','off')
set(gca,'XGrid','off')
set(gca,'XMinorGrid','on')
set(gca,'XMinorGrid','off')
set(gca,'LineWidth',2)
set(gca,'YColor','w')
set(gca,'XColor','w')
set(gca,'ZColor','w')
set(gca,'color',[0 0 0])
%axis off
%set(gca, 'CameraPosition', [100 5000 2000]);


axis([-7 7 -7 7 -2 10]);
%}
%________making the axes in the middle and removing the grid ______
%{
box off;
grid off;
hAxis = gca;
hAxis.XRuler.FirstCrossoverValue  = 0; % X crossover with Y axis
hAxis.XRuler.SecondCrossoverValue  = 0; % X crossover with Z axis
hAxis.YRuler.FirstCrossoverValue  = 0; % Y crossover with X axis
hAxis.YRuler.SecondCrossoverValue  = 0; % Y crossover with Z axis
hAxis.ZRuler.FirstCrossoverValue  = 0; % Z crossover with X axis
hAxis.ZRuler.SecondCrossoverValue = 0; % Z crossover with Y axis
hAxis.XTickLabel= [];
hAxis.YTickLabel= [];
hAxis.ZTickLabel= [];

%}







%vidobj=VideoWriter('polzero.avi');
%%vidobj.CompressionRatio=1;
%vidobj.FrameRate=60;
%%vidobj.FileFormat='mp4'
%open(vidobj);
%figure('units','pixels','position',[0 0 1920 1080])
%
%[X,Y] = meshgrid(-7:.01:3,-20:0.01:20);
%s=X+1j.*Y;
%frame=linspace(5,1,50);
%for i=1:length(frame);
%    Z(:,:,i)= frame(i)./(s+5);
%end
%surf(X,Y,abs(Z(:,:,1)))
%pbaspect([1 0.83 0.5])
%shading interp
%
%set(gcf,'color','black')
%set(gca,'color',[0 0 0]);
%axis([-7 3 -5 5 0 15])
%caxis([0 15])
%
%
%
%
%grid on;
%ax = gca % Get handle to current axes.
%ax.XColor = [0.7 0.7 0.7]; % Red
%ax.YColor = [0.7 0.7 0.7]; % Blue
%ax.ZColor = [0.7 0.7 0.7];
%ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%ax.XRuler.Axle.LineWidth = 3;
%ax.YRuler.Axle.LineWidth = 3;
%ax.ZRuler.Axle.LineWidth = 3;
%
%set(gca,'XMinorGrid','on')
%set(gca,'YMinorGrid','on')
%set(gca,'ZMinorGrid','on')
%
%axis_width_in_pixles=800;
%axis_height_in_pixles=800;
%x0=960-(axis_width_in_pixles/2);
%y0=540-(axis_height_in_pixles/2);
%width=1920;
%height=1080;
%set(gcf,'position',[0,0,width,height])
%set(gca, 'Units', 'pixels')
%set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%%xticklabels([]);
%yticklabels([0]);
%zticklabels([]);
%%xlabel("sigma")
%%ylabel("jw")
%yticks([0])
%
%view(-221,33.15)


%for k=1:50
%    writeVideo(vidobj,getframe(gcf));
%    surf(X,Y,abs(Z(:,:,k)))
%    shading interp
%    caxis([0 15])
%
%    pbaspect([1 0.83 0.5])
%    shading interp
%
%    set(gcf,'color','black')
%    set(gca,'color',[0 0 0]);
%    axis([-7 3 -5 5 0 15])
%
%
%    grid on;
%    ax = gca % Get handle to current axes.
%    ax.XColor = [0.7 0.7 0.7]; % Red
%    ax.YColor = [0.7 0.7 0.7]; % Blue
%    ax.ZColor = [0.7 0.7 0.7];
%    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%    ax.XRuler.Axle.LineWidth = 3;
%    ax.YRuler.Axle.LineWidth = 3;
%    ax.ZRuler.Axle.LineWidth = 3;
%
%    set(gca,'XMinorGrid','on')
%    set(gca,'YMinorGrid','on')
%    set(gca,'ZMinorGrid','on')
%
%    axis_width_in_pixles=800;
%    axis_height_in_pixles=800;
%    x0=960-(axis_width_in_pixles/2);
%    y0=540-(axis_height_in_pixles/2);
%    width=1920;
%    height=1080;
%    set(gcf,'position',[0,0,width,height])
%    set(gca, 'Units', 'pixels')
%    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%
%    %xticklabels([]);
%    yticklabels([]);
%    zticklabels([]);
%    %xlabel("sigma")
%    %ylabel("jw")
%    view(-221,33.15)
%
%    pause(0.00001)
%
%
%end
%pause(1)







%________ camera animation and recording video_________

%for k=1:60
%    writeVideo(vidobj,getframe(gcf));
%    pause(0.1)
%end


%__________ camera animation _______________________________________________________

%az=-221;
%ev=33.15;
%view(az,ev)
%pause(1)
%for k=1:50
%    writeVideo(vidobj,getframe(gcf));
%    az=az-2.78
%    ev=ev+1.137
%
%    view(az,ev)
%    pause(0.00001)
%
%
%
%end
%for k=1:60
%    writeVideo(vidobj,getframe(gcf));
%    pause(0.1)
%end

%__________________
%}
%{
for k=1:100
    writeVideo(vidobj,getframe(gcf));
    az=az+0.51
    ev=ev-0.68
    view(az,ev)
    pause(0.00001)
    
end
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end
close(vidobj);
%}

%{
set(gca,'ZGrid','off')
set(gca,'YGrid','off')
set(gca,'XGrid','off')
set(gca,'XMinorGrid','on')
set(gca,'XMinorGrid','off')
set(gca,'LineWidth',2)
set(gca,'YColor','w')
set(gca,'XColor','w')
set(gca,'ZColor','w')
set(gca,'color',[0 0 0])
%axis off
%set(gca, 'CameraPosition', [100 5000 2000]);


axis([-7 7 -7 7 -2 10]);
%}
%________making the axes in the middle and removing the grid ______
%{
box off;
grid off;
hAxis = gca;
hAxis.XRuler.FirstCrossoverValue  = 0; % X crossover with Y axis
hAxis.XRuler.SecondCrossoverValue  = 0; % X crossover with Z axis
hAxis.YRuler.FirstCrossoverValue  = 0; % Y crossover with X axis
hAxis.YRuler.SecondCrossoverValue  = 0; % Y crossover with Z axis
hAxis.ZRuler.FirstCrossoverValue  = 0; % Z crossover with X axis
hAxis.ZRuler.SecondCrossoverValue = 0; % Z crossover with Y axis
hAxis.XTickLabel= [];
hAxis.YTickLabel= [];
hAxis.ZTickLabel= [];

%}

%___________________________ shifting the location of the poles _____________________________

vidobj=VideoWriter('polzero.avi');
%vidobj.CompressionRatio=1;
vidobj.FrameRate=60;
%vidobj.FileFormat='mp4'
open(vidobj);
figure('units','pixels','position',[0 0 1920 1080])

[X,Y] = meshgrid(-7:.01:3,-20:0.01:20);
s=X+1j.*Y;
Z=1./(s+5);
frame=linspace(0.5,5,50);
for i=1:50
    Z(:,:,i)= 1./(s + frame(i));
end

for i=1:50
writeVideo(vidobj,getframe(gcf));
surf(X,Y,abs(Z(:,:,i)))
pbaspect([1 0.83 0.5])
shading interp

set(gcf,'color','black')
set(gca,'color',[0 0 0]);
axis([-7 3 -20 20 0 15])
caxis([0 15])




grid on;
ax = gca % Get handle to current axes.
ax.XColor = [0.7 0.7 0.7]; % Red
ax.YColor = [0.7 0.7 0.7]; % Blue
ax.ZColor = [0.7 0.7 0.7];
ax.GridAlpha = 0.7;  % Make grid lines less transparent.
ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
ax.XRuler.Axle.LineWidth = 3;
ax.YRuler.Axle.LineWidth = 3;
ax.ZRuler.Axle.LineWidth = 3;

set(gca,'XMinorGrid','on')
set(gca,'YMinorGrid','on')
set(gca,'ZMinorGrid','on')

axis_width_in_pixles=800;
axis_height_in_pixles=800;
x0=960-(axis_width_in_pixles/2);
y0=540-(axis_height_in_pixles/2);
width=1920;
height=1080;
set(gcf,'position',[0,0,width,height])
set(gca, 'Units', 'pixels')
set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])

%set(gca, 'YScale', 'log')
%xticklabels([]);
yticklabels([0]);
zticklabels([]);
%xlabel("sigma")
%ylabel("jw")
yticks([0])

view(-221,33.15)
pause(0.0001)

end

%___________________________________

%_____________ camera rotation _________________________________

%vidobj=VideoWriter('polzero.avi');
%%vidobj.CompressionRatio=1;
%vidobj.FrameRate=60;
%%vidobj.FileFormat='mp4'
%open(vidobj);
%figure('units','pixels','position',[0 0 1920 1080])
%
%[X,Y] = meshgrid(-7:.01:3,-20:0.01:20);
%s=X+1j.*Y;
%Z=1./(s+5);
%frame=linspace(5,0.5,50);
%for i=1:50
%    Z(:,:,i)= 1./(s + frame(i));
%end
%ez=65;
%ev=15;
%for i=1:50
%writeVideo(vidobj,getframe(gcf));
%surf(X,Y,abs(Z(:,:,50)))
%pbaspect([1 0.83 0.5])
%shading interp
%
%set(gcf,'color','black')
%set(gca,'color',[0 0 0]);
%axis([-7 0 -20 20 0 3])
%caxis([0 3])
%
%
%
%
%grid on;
%ax = gca % Get handle to current axes.
%ax.XColor = [0.7 0.7 0.7]; % Red
%ax.YColor = [0.7 0.7 0.7]; % Blue
%ax.ZColor = [0.7 0.7 0.7];
%ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%ax.XRuler.Axle.LineWidth = 3;
%ax.YRuler.Axle.LineWidth = 3;
%ax.ZRuler.Axle.LineWidth = 3;
%
%set(gca,'XMinorGrid','on')
%set(gca,'YMinorGrid','on')
%set(gca,'ZMinorGrid','on')
%
%axis_width_in_pixles=800;
%axis_height_in_pixles=800;
%x0=960-(axis_width_in_pixles/2);
%y0=540-(axis_height_in_pixles/2);
%width=1920;
%height=1080;
%set(gcf,'position',[0,0,width,height])
%set(gca, 'Units', 'pixels')
%set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%%set(gca, 'YScale', 'log')
%%xticklabels([]);
%yticklabels([0]);
%zticklabels([]);
%%xlabel("sigma")
%%ylabel("jw")
%yticks([0])
%
%ez=ez+0.1;
%ev=ev+0.5;
%
%view(ez,ev)
%pause(0.0001)
%end




vidobj=VideoWriter('polzero.avi');
%vidobj.CompressionRatio=1;
vidobj.FrameRate=60;
%vidobj.FileFormat='mp4'
open(vidobj);
figure('units','pixels','position',[0 0 1920 1080])

w=linspace(-20,1000,100000);
E=1./(5+1j*w);
plot(w,abs(E))


frame=linspace(5,0.5,50);
for i=1:50
    E(:,:,i)= 1./(1j*w + frame(i));
end

for i=1:50
writeVideo(vidobj,getframe(gcf));
plot(w,abs(E(:,:,i)),'LineWidth',3)
pbaspect([1 0.4 0.5])

%pbaspect([1 0.83 0.5])
%shading interp

set(gcf,'color','black')
set(gca,'color',[0 0 0]);
set(gca, 'XScale', 'log')

axis([0 100000 0 2])
%caxis([0 3])




grid on;
ax = gca % Get handle to current axes.
ax.XColor = [0.7 0.7 0.7]; % Red
ax.YColor = [0.7 0.7 0.7]; % Blue
ax.ZColor = [0.7 0.7 0.7];
ax.GridAlpha = 0.7;  % Make grid lines less transparent.
ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
ax.XRuler.Axle.LineWidth = 3;
ax.YRuler.Axle.LineWidth = 3;
%ax.ZRuler.Axle.LineWidth = 3;

set(gca,'XMinorGrid','on')
set(gca,'YMinorGrid','on')
%set(gca,'ZMinorGrid','on')

axis_width_in_pixles=800;
axis_height_in_pixles=800;
x0=960-(axis_width_in_pixles/2);
y0=540-(axis_height_in_pixles/2);
width=1920;
height=1080;
set(gcf,'position',[0,0,width,height])
set(gca, 'Units', 'pixels')
set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])

%set(gca, 'YScale', 'log')
%xticklabels([]);
yticklabels([]);
%zticklabels([]);
%xlabel("sigma")
%ylabel("jw")
%yticks([0])

%view(70,40)
pause(0.0001)

end




%vidobj=VideoWriter('polzero.avi');
%%vidobj.CompressionRatio=1;
%vidobj.FrameRate=60;
%%vidobj.FileFormat='mp4'
%open(vidobj);
%figure('units','pixels','position',[0 0 1920 1080])
%
%w=linspace(-20,1000,100000);
%E=1./(5+1j*w);
%plot(w,abs(E))
%
%
%frame=linspace(0.5,5,50);
%for i=1:50
%    E(:,:,i)= 1./(1j*w + frame(i));
%end
%
%for i=1:50
%writeVideo(vidobj,getframe(gcf));
%plot(w,abs(E(:,:,i)),'LineWidth',3)
%
%pbaspect([1 0.4 0.5])
%%shading interp
%
%set(gcf,'color','black')
%set(gca,'color',[0 0 0]);
%set(gca, 'XScale', 'log')
%
%axis([0 100000 0 2])
%%caxis([0 3])
%
%
%
%
%grid on;
%ax = gca % Get handle to current axes.
%ax.XColor = [0.7 0.7 0.7]; % Red
%ax.YColor = [0.7 0.7 0.7]; % Blue
%ax.ZColor = [0.7 0.7 0.7];
%ax.GridAlpha = 0.7;  % Make grid lines less transparent.
%ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
%ax.XRuler.Axle.LineWidth = 3;
%ax.YRuler.Axle.LineWidth = 3;
%%ax.ZRuler.Axle.LineWidth = 3;
%
%set(gca,'XMinorGrid','on')
%set(gca,'YMinorGrid','on')
%%set(gca,'ZMinorGrid','on')
%
%axis_width_in_pixles=800;
%axis_height_in_pixles=800;
%x0=960-(axis_width_in_pixles/2);
%y0=540-(axis_height_in_pixles/2);
%width=1920;
%height=1080;
%set(gcf,'position',[0,0,width,height])
%set(gca, 'Units', 'pixels')
%set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])
%
%%set(gca, 'YScale', 'log')
%%xticklabels([]);
%yticklabels([]);
%%zticklabels([]);
%%xlabel("sigma")
%%ylabel("jw")
%%yticks([0])
%
%%view(70,40)
%pause(0.0001)
%
%end






t=linspace(0,10,10000);
w=linspace(0,20,10000);
ce=exp(-(0.5+j*2*pi*7).*t);
plot3(real(ce),t,imag(ce))
xlabel("x");
ylabel("y");
zlabel("z");





[X,Y] = meshgrid(-2:.02:0,0:0.02:50);
s=X+1j.*Y;
Z= 1./((s-(-1)));
surf(X,Y,mag2db(abs(Z)))
pbaspect([1 0.83 0.5])
set(gca, 'YScale', 'log')
%set(gca, 'ZScale', 'log')

grid on;
ax = gca % Get handle to current axes.
ax.XColor = [0.7 0.7 0.7]; % Red
ax.YColor = [0.7 0.7 0.7]; % Blue
ax.ZColor = [0.7 0.7 0.7];
ax.GridAlpha = 0.7;  % Make grid lines less transparent.
ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
ax.XRuler.Axle.LineWidth = 3;
ax.YRuler.Axle.LineWidth = 3;
ax.ZRuler.Axle.LineWidth = 3;
set(gcf,'color','black')
set(gca,'color',[0 0 0]);

shading interp
xlabel("sigma")
ylabel("frequency")
zlabel("mag")
view(90,0)





t=linspace(0,2,400);
w=linspace(-20,20,400);
a=5;
b=10;
c=30;
e1=exp(-a*t);
e2=exp(-b*t);
e3=exp(-c*t);
e=e1+e2+e3;
E1=1./(a+1j*w);
E2=1./(b+1j*w);
E3=1./(c+1j*w);
E=E1+E2+E3;
figure(1)
plot(t,e1)
hold on
plot(t,e2)
hold on
plot(t,e3)
hold on
plot(t,e,'color','red')
figure(2)
plot(w,abs(E1))
set(gca, 'XScale', 'log')
hold on
plot(w,abs(E2))
hold on 
plot(w,abs(E3))
hold on 
plot(w,abs(E),'color','red')
figure(3)
[X,Y] = meshgrid(-35:.05:0,-20:0.05:20);
s=X+1j.*Y;
Z1=1./(a+s);
Z2=1./(b+s);
Z3=1./(c+s);
Z=Z1+Z2+Z3;
surf(X,Y,abs(Z))
pbaspect([1 0.83 0.5])
shading interp
%axis([-35 0 -20 20 0 1])

%set(gca, 'YScale', 'log')
%set(gca, 'ZScale', 'log')






vidobj=VideoWriter('polzero.avi');
%vidobj.CompressionRatio=1;
vidobj.FrameRate=60;
%vidobj.FileFormat='mp4'
open(vidobj);
figure('units','pixels','position',[0 0 1920 1080])

t=linspace(-10,10,1000);

e1=1./(t+2);
e2=1./(t+3);
e=e1+e2;




[X,Y] = meshgrid(-10:.05:5,0:.05:10);
s=X+1j.*Y;
Z1=1./(s- -3);
Z2=1./(s- -2);
Z3=1./(s- -5-3j);
zz=(s+1)./((s+3).*(s+7));
Z=Z1+Z2;
%figure(1)
%plot(t,abs(e1))
%hold on
%plot(t,abs(e2))
%hold on
%plot(t,abs(e))
%axis([-10 10 0 10])
%
%figure(2)

surf(X,Y,abs(Z))
shading interp
%xlabel("sigma")
%ylabel("omega")
%zlabel("z")



pbaspect([1 0.83 0.5])

axis([-10 10 -10 10 0 10])
caxis([0 10])


%set(gca, 'YScale', 'log')
%set(gca, 'ZScale', 'log')

%m=[t' abs(e)'];
%csvwrite('sumof2rationals.csv',m)


set(gcf,'color','black')
    set(gca,'color',[0 0 0]);
    axis([-10 10 -10 10 0 10])
    caxis([0 10])




    grid on;
    ax = gca % Get handle to current axes.
    ax.XColor = [0.7 0.7 0.7]; % Red
    ax.YColor = [0.7 0.7 0.7]; % Blue
    ax.ZColor = [0.7 0.7 0.7];
    ax.GridAlpha = 0.7;  % Make grid lines less transparent.
    ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
    ax.XRuler.Axle.LineWidth = 3;
    ax.YRuler.Axle.LineWidth = 3;
    ax.ZRuler.Axle.LineWidth = 3;

    set(gca,'XMinorGrid','on')
    set(gca,'YMinorGrid','on')
    set(gca,'ZMinorGrid','on')

    axis_width_in_pixles=800;
    axis_height_in_pixles=800;
    x0=960-(axis_width_in_pixles/2);
    y0=540-(axis_height_in_pixles/2);
    width=1920;
    height=1080;
    set(gcf,'position',[0,0,width,height])
    set(gca, 'Units', 'pixels')
    set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])

    for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
    view(28,42)

    end






r=1;
n = 0:40;
nc = 0:0.01:40;
f = 1/2;
phase = 0;
A = 1.5;
x = A*cos(r*2*pi*f*n - phase);
xc=A*cos(r*2*pi*f*nc - phase);
y=(exp(r*1i*2*pi*f*n));
yc=(exp(r*1i*2*pi*f*nc));
figure(1)
clf; % Clear old graph
stem(n,x); % Plot the generated sequence
hold on
plot(nc,xc);
axis([0 40 -2 2]);
grid;
title('Sinusoidal Sequence');
xlabel('Time index n');
ylabel('Amplitude');
axis;
figure(2)
stem3(real(y),imag(y),n)
xlabel("real")
ylabel("imag")
zlabel("n")
hold on 
plot3(real(yc),imag(yc),nc)






vidobj=VideoWriter('polzero.avi');
vidobj.FrameRate=60;
open(vidobj);
figure('units','pixels','position',[0 0 1920 1080])

[X,Y] = meshgrid(-3:.01:3,-3:0.01:3);
s=X+1j.*Y;
Z= 1./((s-2).*(s+1));
surf(X,Y,abs(Z))
pbaspect([1 0.83 0.5])
shading interp

set(gcf,'color','black')
set(gca,'color',[0 0 0]);
axis([-3 3 -3 3 0 15])



grid on;
ax = gca % Get handle to current axes.
ax.XColor = [0.7 0.7 0.7]; % Red
ax.YColor = [0.7 0.7 0.7]; % Blue
ax.ZColor = [0.7 0.7 0.7];
ax.GridAlpha = 0.7;  % Make grid lines less transparent.
ax.GridColor = [0.2 0.2 0.2]; % Dark Green.
ax.XRuler.Axle.LineWidth = 3;
ax.YRuler.Axle.LineWidth = 3;
ax.ZRuler.Axle.LineWidth = 3;

set(gca,'XMinorGrid','on')
set(gca,'YMinorGrid','on')
set(gca,'ZMinorGrid','on')

axis_width_in_pixles=800;
axis_height_in_pixles=800;
x0=960-(axis_width_in_pixles/2);
y0=540-(axis_height_in_pixles/2);
width=1920;
height=1080;
set(gcf,'position',[0,0,width,height])
set(gca, 'Units', 'pixels')
set(gca,'position',[x0,y0,axis_width_in_pixles,axis_height_in_pixles])


%xticklabels([]);
%yticklabels([]);
zticklabels([]);


%________ camera animation and recording video_________




az=37;
ev=60;
view(az,ev)
for k=1:100
    writeVideo(vidobj,getframe(gcf));
    az=az-0.37
    ev=ev+0.30
    view(az,ev)
    pause(0.00001)
    

    
end
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end

for k=1:100
    writeVideo(vidobj,getframe(gcf));
    az=az+0.51
    ev=ev-0.68
    view(az,ev)
    pause(0.00001)
    
end
for k=1:60
    writeVideo(vidobj,getframe(gcf));
    pause(0.1)
end
close(vidobj);


%{
set(gca,'ZGrid','off')
set(gca,'YGrid','off')
set(gca,'XGrid','off')
set(gca,'XMinorGrid','on')
set(gca,'XMinorGrid','off')
set(gca,'LineWidth',2)
set(gca,'YColor','w')
set(gca,'XColor','w')
set(gca,'ZColor','w')
set(gca,'color',[0 0 0])
%axis off
%set(gca, 'CameraPosition', [100 5000 2000]);


axis([-7 7 -7 7 -2 10]);
%}
%________making the axes in the middle and removing the grid ______
%{
box off;
grid off;
hAxis = gca;
hAxis.XRuler.FirstCrossoverValue  = 0; % X crossover with Y axis
hAxis.XRuler.SecondCrossoverValue  = 0; % X crossover with Z axis
hAxis.YRuler.FirstCrossoverValue  = 0; % Y crossover with X axis
hAxis.YRuler.SecondCrossoverValue  = 0; % Y crossover with Z axis
hAxis.ZRuler.FirstCrossoverValue  = 0; % Z crossover with X axis
hAxis.ZRuler.SecondCrossoverValue = 0; % Z crossover with Y axis
hAxis.XTickLabel= [];
hAxis.YTickLabel= [];
hAxis.ZTickLabel= [];

%}









