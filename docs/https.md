# Hypertext Transfer Protocol Secure (HTTPS)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

## Descrição

O *Hypertext Transfer Protocol Secure (HTTPS)* é a versão segura do HTTP, que adiciona uma camada de criptografia utilizando SSL/TLS para proteger a comunicação. Embora também opere na Camada de Aplicação (Camada 7), o HTTPS se diferencia do HTTP por fornecer segurança adicional, garantindo a confidencialidade e a integridade dos dados transmitidos. A criptografia ocorre na Camada de Sessão (Camada 5) e na Camada de Transporte (Camada 4), onde os protocolos SSL/TLS operam para assegurar que os dados trocados entre o cliente e o servidor não possam ser lidos ou alterados por terceiros.

O HTTPS é essencial para proteger informações sensíveis, como senhas, dados bancários e transações financeiras, e tornou-se o padrão para qualquer site que deseje garantir a segurança de seus usuários. Ele utiliza a porta 443 por padrão e é fortemente recomendado para qualquer aplicação que lide com dados privados. Além de criptografar os dados, o HTTPS também garante a autenticidade do servidor, o que aumenta a confiança dos usuários ao interagir com a web.

## Referências

- [MDN Glossary about HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)
- [Amazon AWS about the difference between HTTP and HTTPS](https://aws.amazon.com/pt/compare/the-difference-between-https-and-http/)
- [Wikipedia about HTTPS](https://pt.wikipedia.org/wiki/Hyper_Text_Transfer_Protocol_Secure)
- [CloudFlare about HTTPS](https://www.cloudflare.com/pt-br/learning/ssl/what-is-https/)