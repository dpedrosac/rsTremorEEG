function mesh = decouplesurf(mesh)
for ii = 1:length(mesh)-1
  % Despite what the instructions for surfboolean says, surfaces should be ordered from inside-out!!
  [newnode, newelem] = surfboolean(mesh(ii+1).pos, mesh(ii+1).tri, 'decouple', mesh(ii).pos,mesh(ii).tri);
   mesh(ii+1).tri =newelem;
   mesh(ii+1).pos = newnode;
end % for