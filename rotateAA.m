function [rot3] = rotateAA(aa)
%ROTATEAA Summary of this function goes here
%   Detailed explanation goes here
rot1 = [];
rot2 = [];
theta = deg2rad(360-rad2deg(atan2(aa(3,2),aa(3,1)))+180);
rotmatz = [cos(theta),-sin(theta),0;sin(theta),cos(theta),0;0,0,1];
for i = 1:size(aa,1)
    vec = aa(i,:);
    rotated = rotmatz*vec';
    rot1(i,:) = rotated';
end

theta = atan2(rot1(3,3),rot1(3,1));
rotmaty = [cos(theta), 0, sin(theta);0 1 0; -sin(theta), 0, cos(theta)];
for i = 1:size(aa,1)
    vec = rot1(i,:);
    rotated = rotmaty*vec';
    rot2(i,:) = rotated';
end


theta = deg2rad((360-(rad2deg(atan2(rot2(2,3),rot2(2,2)))+180))+90);
rotmatx = [1, 0, 0; 0, cos(theta), -sin(theta); 0, sin(theta), cos(theta)];
for i = 1:size(aa,1);
    vec = rot2(i,:);
    rotated = rotmatx*vec';
    rot3(i,:) = rotated';
end

