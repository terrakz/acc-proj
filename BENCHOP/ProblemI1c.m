% Copyright (c) 2015, BENCHOP, Slobodan Milovanović
% All rights reserved.
% This MATLAB code has been written for the BENCHOP project.
% Redistribution and use in source and binary forms, with or without
% modification, are permitted provided that the following conditions are
% met:
%    * Redistributions of source code must retain the above copyright
%       notice, this list of conditions and the following disclaimer.
%    * Redistributions in binary form must reproduce the above copyright
%       notice, this list of conditions and the following disclaimer in
%       the documentation and/or other materials provided with the distribution
%    * BENCHOP article is properly cited by the user of the BENCHOP codes when publishing/reporting related scientific results.
% 
% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
% AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
% IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
% ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
% LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
% CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
% SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
% INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
% CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
% ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
% POSSIBILITY OF SUCH DAMAGE.

function[tBSupoutCallI, rBSupoutCallI] = ProblemI1c()
clear
close all

format long

% addpath(genpath('./')); %adds all the functions from subfolders to the path
% mfiles=getfilenames('./','BSeuCallU*.m')

warning off

Methods={'MC','MC-S','QMC-S','MLMC','MLMC-A',...
    'FFT','FGL','COS',...
    'FD','FD-NU','FD-AD',...
    'RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT'};

%% Problem 1 c) I

display('Problem 1 c) I');
rootpath=pwd;
S=[90,100,110]; K=100; T=1.0; r=0.03; sig=0.15; B=1.25*K;
U=[1.822512255945242 3.294086516281595 3.221591131246868];

filepathsBSupoutCallI=getfilenames('./','BSupoutCallI_*.m');
par={S,K,T,r,sig,B};
[timeBSupoutCallI,relerrBSupoutCallI] = executor(rootpath,filepathsBSupoutCallI,U,par)

tBSupoutCallI=NaN(numel(Methods),1); rBSupoutCallI=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSupoutCallI)
        a=filepathsBSupoutCallI{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSupoutCallI(ii)=timeBSupoutCallI(jj);
            rBSupoutCallI(ii)=relerrBSupoutCallI(jj);
        end
    end
end

cd(rootpath);

tBSupoutCallI, rBSupoutCallI

end
