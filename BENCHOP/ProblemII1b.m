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

function[tBSamPutUII, rBSamPutUII] = ProblemII1b()

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

%% Problem 1 b) II

display('Problem 1 b) II');
rootpath=pwd;
S=[97,98,99]; K=100; T=0.25; r=0.1; sig=0.01;
U=[3.000000000000682 2.000000000010786   1.000000000010715];

filepathsBSamPutUII=getfilenames('./','BSamPutUII_*.m');
par={S,K,T,r,sig};
[timeBSamPutUII,relerrBSamPutUII] = executor(rootpath,filepathsBSamPutUII,U,par)

tBSamPutUII=NaN(numel(Methods),1); rBSamPutUII=NaN(numel(Methods),1);
for ii=1:numel(Methods)
    for jj=1:numel(filepathsBSamPutUII)
        a=filepathsBSamPutUII{jj}(3:3+numel(Methods{ii}));
        b=[Methods{ii},'/'];
        if strcmp(a,b)
            tBSamPutUII(ii)=timeBSamPutUII(jj);
            rBSamPutUII(ii)=relerrBSamPutUII(jj);
        end
    end
end

cd(rootpath);

tBSamPutUII, rBSamPutUII
