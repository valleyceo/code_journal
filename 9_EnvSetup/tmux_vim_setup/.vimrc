""" My VIMRC configuration """

set nocompatible
syntax on
set nowrap
set encoding=utf8

""" begin vundle configuration """

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

""" begin plugins """
call vundle#begin()

" Utilities
Plugin 'VundleVim/Vundle.vim' " let Vundle manage Vundle, required
Plugin 'scrooloose/nerdtree'  " nerdtree

" Generic Programming Support 
Plugin 'honza/vim-snippets'
Plugin 'Townk/vim-autoclose'
Plugin 'tomtom/tcomment_vim'
Plugin 'tobyS/vmustache'
Plugin 'janko-m/vim-test'
Plugin 'maksimr/vim-jsbeautify'
Plugin 'vim-syntastic/syntastic'
Plugin 'neomake/neomake'

" Color scheme
Plugin 'flazz/vim-colorschemes'

" Markdown / Writting
Plugin 'reedes/vim-pencil'
Plugin 'tpope/vim-markdown'
Plugin 'jtratner/vim-flavored-markdown'
Plugin 'LanguageTool'

" Git Support
Plugin 'kablamo/vim-git-log'
Plugin 'gregsexton/gitv'
Plugin 'tpope/vim-fugitive'
Plugin 'Xuyuanp/nerdtree-git-plugin' " keep track of git status

" Word completion
" Plugin 'Valloric/YouCompleteMe'

""" end of plugs """
call vundle#end()            " required
filetype plugin indent on    " required

""" configuration section """

" make new window split to right and below
set splitright
set splitbelow

""" COLOR CONFIG """
colorscheme molokai

set number
set linespace=3
set guifont=Fira\ Code:h12
set cursorline
set tabstop=4                       " show existing tab with 4 spaces
set shiftwidth=4                    " indents will have a width of 4

""" NERDTREE CONFIG """
" enable mouse click in NERDTree
set mouse=a                         " n or a works
set ttymouse=xterm2                 " needed when you use tmux
let g:NERDTreeMouseMode=3 

" let NERDTreeMapOpenInTab='<ENTER>'  " (or <ENTER>) open new window
map <C-n> :NERDTreeToggle<CR>       " add nerdtree toggle
"let g:NERDTreeWinPos = "left"       " always keep nerdtree on the left

""" (open by default) This creates error """
" autocmd vimenter * NERDTree         " automatically open when starting vim
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
"""
" remove press ? for help sign on top
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1

" make backspace work
set backspace=indent,eol,start
