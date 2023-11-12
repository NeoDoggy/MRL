function [PN] = Label_box2(t,S_n)

PN = -ones(S_n,1);

if t==1
    PN(23) = 1;
    return;
elseif t==2
    PN(21) = 1;
    return;
elseif t==3
    PN(25) = 1;
    return;
elseif t==4
    PN(26) = 1;
    return;
elseif t==5
    PN(20) = 1;
    return;
elseif t==6
    PN(15) = 1;
    return;
elseif t==7
    PN(12) = 1;
    return;
elseif t==8
    PN(12) = 1;
    return;
elseif t==9
    PN(8) = 1;
    return;
elseif t==10
    PN(6) = 1;
    return;
elseif t==11
    PN(5) = 1;
    return;
elseif t==12
    PN(4) = 1;
    return;
elseif t==13
    PN(6) = 1;
    return;
elseif t==14
    PN(3) = 1;
    return;
elseif t==15
    PN(3) = 1;
    return;
elseif t==16
    PN(2) = 1;
    PN(3) = 1;
    return;
elseif t==17
    PN(51) = 1;
    return;
elseif t==18
    PN(48) = 1;
    return;
elseif t==19
    PN(50) = 1;
    return;
elseif t==20
    PN(49) = 1;
    return;
elseif t==21
    PN(48) = 1;
    return;
elseif t==22
    PN(50) = 1;
    return;
elseif t==23
    PN(49) = 1;
    return;
elseif t==24
    PN(39) = 1;
    return;
elseif t==25
    PN(37) = 1;
    return;
elseif t==26
    PN(32) = 1;
    return;
elseif t==27
    PN(41) = 1;
    return;
elseif t==28
    PN(44) = 1;
    return;
elseif t==29
    PN(56) = 1;
    return;
elseif t==30
    PN(48) = 1;
    return;
elseif t==31
    PN(1) = 1;
    return;
elseif t==32
    PN(2) = 1;
    return;
elseif t==33
    PN(5) = 1;
    return;
elseif t==34
    PN(8) = 1;
    return;
elseif t==35
    PN(8) = 1;
    return;
elseif t==36
    PN(8) = 1;
    return;
elseif t==37
    PN(11) = 1;
    return;
elseif t==38
    PN(10) = 1;
    return;
elseif t==39
    PN(12) = 1;
    return;
elseif t==40
    PN(9) = 1;
    return;
end

end
