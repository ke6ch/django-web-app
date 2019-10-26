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

# Server

```
python -c 'exec("try:import SimpleHTTPServer as m\nexcept:import http.server as m");m.test(HandlerClass=m.SimpleHTTPRequestHandler)'

localhost:8000
```

# django

```
pip install django

import django
print(django.get_version())
```

```
django-admin startproject [myproject]
cd [myproject]
python manage.py runserver

localhost:8000
```
