function drawSC(u)
    pn = u(1)
    pe = u(2)
    pd = u(3)
    phi = u(4)
    theta = u(5)
    psi = u(6)
    t = u(7)
  
    persistent spacecraft_handle
    
    if t == 0
        figure(1), clf  
        spacecraft_handle = drawSpacecraftBody(pn, pe, pd, phi, theta, psi, [], 'normal'); 
        grid on
        axis([-5 5 -5 5 -5 5])
    else
        drawSpacecraftBody(pn, pe, pd, phi, theta, psi, spacecraft_handle); 
    end
    