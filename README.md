# TouchDown3

## Validação de credenciais do outlook através de arquivo.

### Um script simples escrito em python que valida credenciais através de um arquivo com email e senha e retorna as credenciais válidas e inválidas. 

### O script usa a biblioteca de selenium e o chrome como navegador para as verificações. Algumas funções exigem a versão mais recente do chrome. Como tal, certifique-se de que o navegador chrome é pelo menos a versão 97. Se não, então atualize o navegador (3 pontos no canto superior direito -> ajuda -> sobre o chrome).

Antes de executar o script, certifique-se de ter ou fazer um arquivo com uma lista de emails e senhas, o delimitador do script é ";" mas caso seja outro basta alterar no código. O script é escrito para e-mails do Outlook.

Se você não está tão familiarizado com python faça o seguinte:

1 - Baixe e instale python a partir de sua página oficial (https://www.python.org/downloads/) e certifique-se de que python é adicionado ao PATH (haverá uma escolha para adicioná-lo durante a instalação).

2- Abra o prompt de comando (ou terminal no mac/linux) e escreva "pip install selenium".

3- Uma vez concluída a instalação, adicione o chrome ao seu PATH onde se encontra o script.

4 - Executar o script. Ele deve começar com "Insira o caminho do seu arquivo" se funcionar corretamente. Meu método preferido é escrever "python3 script.py" no prompt de comando.

Tecnologias utilizadas:

<img src= "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
