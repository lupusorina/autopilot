function [V, F, patchcolors] = spacecraftVFC

% User defined
fuse_l1     = 3
fuse_l2     = 1
fuse_l3     = 6
fuse_w      = 2
fuse_h      = 2

wing_l      = 2
wing_w      = 10

tail_wing_l = 1
tail_wing_w = 4
tail_h      = 2


V = [...
    fuse_l1         0           0;          % POINT 1 - nose of the plane
    fuse_l2         fuse_w/2    -fuse_h/2;  % Point 2 - fuselage
    fuse_l2         -fuse_w/2   -fuse_h/2;  % Point 3 - fuselage
    fuse_l2         -fuse_w/2   fuse_h/2;   % Point 4 - fuselage
    fuse_l2         fuse_w/2    fuse_h/2;   % Point 5 - fuselage
    -fuse_l3        0           0;          % Point 6 - fuselage
    
    0               wing_w/2    0;          % Point 7 - right wing
    -wing_l         wing_w/2    0;          % Point 8 - right wing
    -wing_l         -wing_w/2   0;          % Point 9 - left wing
    0               -wing_w/2   0;          % Point 10 - left wing
    
    -fuse_l3+tail_wing_l    tail_wing_w/2  0; % Point 11 - tail right wing
    -fuse_l3                tail_wing_w/2  0; % Point 12 - tail right wing
    -fuse_l3                -tail_wing_w/2 0; % Point 13 - tail left wing
    -fuse_l3+tail_wing_l    -tail_wing_w/2 0; % Point 14 - tail left wing
    
    -fuse_l3 + tail_wing_l 0 0;       % Point 15 - rudder down
    -fuse_l3               0 -tail_h; % Point 16 - rudder down

    ];

F = [...
    1, 2, 3, 3; % Nose
    1, 3, 4, 4; % Nose
    1, 4, 5, 5; % Nose
    1, 2, 5, 5; % Nose
    2, 3, 6, 6; % Fuselage
    3, 4, 6, 6; % Fuselage
    4, 5, 6, 6; % Fuselage
    5, 2, 6, 6; % Fuselage
    7, 8, 9, 10; % Wing
    11, 12, 13, 14; %Tail wing
    15, 16, 6, 6;... % Rudder
    ];


myred = [1,0,0];
mygreen = [0,1,0];
myblue = [0,0,1];
myyellow = [1,1,0];
mycyan = [0,1,1];

patchcolors = [...
    myred; ...
    myred;...
    myred; ...
    myred; ...
    mycyan; ...
    mycyan; ...
    mycyan; ...
    mycyan; ...
    myyellow; ...
    myblue;...
    mygreen; ...
    ];

