#!/bin/bash

cp .vimrc ~/
cp .tmux.conf ~/

if [[ "$OSTYPE" == "linux-gnu" ]]; then
	echo "using linux setup"
	sudo apt-get update
	sudo apt-get install tmux
elif [[ "$OSTYPE" == "darwin"* ]]; then
	echo "running OSX, updating brew"
	brew update
	brew install vim tmux
fi

vim +PluginInstall +qall