set t_Co=256
set laststatus=2
filetype plugin indent on
set mouse=a

" Encoding 
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=utf-8

" Copy/Paste/Cut
if has('unnamedplus')
    set clipboard=unnamed,unnamedplus
endif

" Fix backspace indent
set backspace=indent,eol,start

" Set line number
set number
set relativenumber

" Searching
set hlsearch
set incsearch
set ignorecase
set smartcase

" Tabs-related settings
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set fileformat=unix

" Plugin
call plug#begin('~/.config/nvim/plugged')
" Status line for Vim
Plug 'itchyny/lightline.vim'
" Dracula color scheme
Plug 'dracula/vim', { 'as': 'dracula' }
" Comment line in Vim (gc/gcc)
Plug 'tpope/vim-commentary'
" Automatic close quotes, parenthesis...
Plug 'Raimondi/delimitMate'
" File explorer for Vim
" Plug 'scrooloose/nerdtree'
call plug#end()

colorscheme dracula

" NERDTree settings
" map <C-b> :NERDTreeToggle<CR>
" map <C-i> :NERDTreeFind<CR>
" let g:NERDTreePatternMatchHighlightFullName = 1
" let NERDTreeAutoDeleteBuffer = 1
" let NERDTreeMinimalUI = 1
" let NERDTreeDirArrows = 1
" let g:NERDDefaultAlign = 'left'
" let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }
" let g:NERDTreeChDirMode=2
" let g:NERDTreeIgnore=['\.rbc$', '\~$', '\.pyc$', '\.db$', '\.sqlite$', '__pycache__', 'node_modules']
" let g:NERDTreeShowBookmarks=1

imap jk <Esc>
