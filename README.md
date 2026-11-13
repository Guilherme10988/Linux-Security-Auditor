Linux Security Auditor

Projeto de segurança e análise de sistemas Linux utilizando Python.

Sobre o projeto

O Linux Security Auditor é uma ferramenta desenvolvida em Python para realizar verificações básicas de segurança em sistemas Linux, identificando possíveis configurações inseguras e apresentando os resultados de uma auditoria.

Funcionalidades

- Informações do sistema: coleta informações sobre o sistema operacional, versão, kernel e arquitetura.
- Análise de usuários: verifica a existência de contas não root com UID 0.
- Verificação de permissões: analisa permissões de arquivos importantes do sistema.
- Firewall: verifica se o firewall UFW está ativo ou inativo.
- Configuração SSH: identifica algumas configurações que podem representar riscos de segurança.

Tecnologias utilizadas

- Python 3
- Linux Ubuntu
- Git e GitHub

Ambiente de testes

Projeto desenvolvido e testado em uma máquina virtual Ubuntu utilizando VirtualBox.

Como executar

1. Clonar o repositório

git clone https://github.com/Guilherme10988/linux-security-auditor.git

2. Entrar na pasta do projeto

cd linux-security-auditor

3. Executar a ferramenta

sudo python3 main.py

O uso de "sudo" permite realizar verificações em arquivos protegidos do sistema.

Relatórios

A ferramenta gera relatórios em formato JSON contendo informações do sistema, resultados das verificações, evidências e classificações de risco.

Um exemplo de relatório está disponível na pasta "examples/".

Evidências dos testes

Na pasta "docs/" estão disponíveis capturas de tela demonstrando a execução do projeto com o firewall UFW ativo e inativo.

Limitações

- Realiza verificações básicas de segurança.
- Não realiza correções automáticas.
- Não substitui uma auditoria profissional.
- A análise da configuração SSH possui limitações e não considera todas as regras efetivas do serviço.