export TERM='xterm-256color'
export EDITOR='/usr/bin/vim'
alias rm='rm -i'
export PS1="\[\033[38;5;2m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;2m\]\h\[$(tput sgr0)\]:\w:\$?\\$ \[$(tput sgr0)\]"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/app/lib:$HOME/local/lib"
export PATH="$HOME/local/bin/:$HOME/app/:$PATH"
export MANPATH="$HOME/local/man:$HOME/local/share/man:$MANPATH"