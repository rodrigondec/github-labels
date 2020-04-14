# Instalação
É necessário ter algum python a cima da versão 3.6 siga a 
[documentação oficial](https://www.python.org/downloads/) para instalar.

## Criando um ambiente virtual
Existem maneiras diferentes de fazer isso.

Utilizando Python3.6, basta executar:

    python3 -m venv {{nome_do_seu_venv}}

Onde `{{nome_do_seu_venv}}` deve ser substituído por um nome de sua escolha.

Agora, será necessário ativar este ambiente execute o comando referente ao seu SO:
```shell script
source {{nome_do_seu_venv}}/bin/activate
```

Para mais informações sobre o assunto, basta ler a [
documentação oficial](https://docs.python.org/3/library/venv.html).

## Instalando dependências
```shell script
pip install -r requirements.txt
```

# Executando
basta executar o comendo
```shell script
python manager.py
```

# Referências
## artigo
https://medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63
## github labels
https://github.com/anavallasuiza/github-labels
https://github.com/Relequestual/sensible-github-labels
https://github.com/azu/github-label-setup
https://github.com/abdonrd/github-labels
https://github.com/yoshuawuyts/github-standard-labels
https://github.com/himynameisdave/git-labelmaker
## ferramentas
https://github.com/dwyl/labels