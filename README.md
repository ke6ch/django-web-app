# Install python

```
brew install pyenv
pyenv -v

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

pyenv install --list
pyenv install 3.8.0
pyenv versions
pyenv global 3.8.0
python --version
```

# venv

```
python -m venv .venv
source .venv/bin/activate
```

```
pip install -r requestments.txt
python manage.py runserver

localhost:8000
```
