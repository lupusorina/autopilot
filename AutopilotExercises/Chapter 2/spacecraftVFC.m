function [V, F, patchcolors] = spacecraftVFC

V = [...
    1   1   0; 
    1   -1  0;
    -1  -1  0;
    -1  1   0;
    1   1   -2;
    1   -1  -2;
    -1  -1  -2;
    -1  1   -2;
    1.5 1.5  0;
    1.5 -1.5 0;
    -1.5 -1.5 0;
    -1.5 1.5 0;
    ];

F = [...
    1, 2, 6, 5;
    4, 3, 7, 8;
    1, 5, 8, 4;
    2, 6, 7, 3;
    5, 6, 7, 8;
    9, 10, 11, 12;
    ];


myred = [1,0,0];
mygreen = [0,1,0];
myblue = [0,0,1];
myyellow = [1,1,0];
mycyan = [0,1,1];

patchcolors = [...
    myred; ...
    mygreen;...
    myblue; ...
    myyellow; ...
    mycyan; ...
    mycyan; ...
    ];

