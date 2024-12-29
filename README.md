## Práticando a criação de um ransomware com python

Utilizando Python e a biblioteca pypaes podemos criptografar e descriptografar arquivos baseados em uma senha.

### O que é um ransomware

Ransomware é um tipo de malware (software malicioso) projetado para sequestrar ou bloquear o acesso a sistemas, arquivos ou dados e, em seguida, exigir um resgate para liberá-los. 

### Ferramentas

Python
Pyaes
VSCode
Github + Git

### Como usar

- Crie um novo ambiente virtual
- Edite o teste.txt (Opcional)
- Edite a key nos arquivos encrypter.py e decrypter.py
- Execute o encrypter.py
- Execute o decrypter.py

### Estrutura de arquivos

__init__.py
|
decrypter.py    # Criptografa o arquivo
|
encrypter.py    # Descriptografa o arquivo
|
teste.txt       # Arquivo que será cripto/descriptografado
|
requeriments.txt    # Dependências necessárias
|
README.md