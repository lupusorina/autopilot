function handle = drawSpacecraftBody(pn, pe, pd, phi, theta, psi, handle, mode)
% define points on spacecraft in local NED coordinates


[V,F,patchcolors] = spacecraftVFC;
% rotate spacecraft by phi, theta, psi
V = rotate(V', phi, theta, psi)';
% translate spacecraft to pn,pe,pd
V = translate(V', pn, pe, pd)';
% transform vertices from NED to XYZ
R = [...
    0,1,0;...
    1,0,0;...
    0,0,-1;...
    ];

V = V*R;
%plot

if isempty(handle)
    handle = patch('Vertices', V, 'Faces', F, ...
                   'FaceVertexCData', patchcolors,...
                   'FaceColor', 'flat');
    hold on
else 
    set(handle, 'Vertices',V,'Faces',F)
end