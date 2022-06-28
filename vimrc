
set mouse=a		" Enable mouse usage (all modes)
set showmatch		" Show matching brackets.
set ignorecase		" Do case insensitive matching
set ruler
set autoindent          " New lines inherit the indentation of previous lines.
set expandtab           " Convert tabs to spaces.
set shiftround          " When shifting lines, round the indentation to the nearest multiple of “shiftwidth.”
set shiftwidth=4        

" Allow saving of files as sudo when I forgot to start vim using sudo.
cmap w!! w !sudo tee > /dev/null %

colo desert
syntax on

