# Projeto e-diaristas

### Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/FrancisSI19/EdiaristasImersao.git'`

#### Instalar as dependências
`pip install -r requirements.txt'`

#### Alterar configurações do arquivo no BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome do banco de dados',
        'HOST': 'host do bd',
        'PORT': 'porta do bd',
        'USER': 'usuario do bd',
        'PASSWORD': 'senha do bd',
    }
}
```

#### Realizar migrações do banco de dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`