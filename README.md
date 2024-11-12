# Glossário

Este glossário foi desenvolvido para facilitar a compreensão dos principais termos e conceitos usados em TI e no ambiente corporativo, oferecendo definições objetivas e acessíveis. Cada entrada foi cuidadosamente elaborada para proporcionar uma visão clara e rápida sobre temas que, muitas vezes, podem parecer complexos ou técnicos.

A proposta é que este material sirva como uma referência prática para iniciantes e profissionais, permitindo uma consulta rápida e confiável. Para quem deseja se aprofundar, incluímos referências e sugestões de leitura adicional, ampliando o entendimento e a aplicação de cada termo no dia a dia profissional.

Vale ressaltar que os conceitos aqui abordados, foram pesquisados pelos autores, e podem ter utilizado IAs generativas e/ou buscas, em geral as referências são buscas manuais.

![Forks](https://img.shields.io/github/forks/leonardopangaio/NagaipoTests.svg) - 
![Stats](https://img.shields.io/github/stars/leonardopangaio/NagaipoTests.svg) - 
![Watchers](https://img.shields.io/github/watchers/leonardopangaio/NagaipoTests.svg) - 
![Followers](https://img.shields.io/github/followers/leonardopangaio.svg?style=social&label=Follow&maxAge=2592000)

Artigo atualizado em: XXXX

<!-- início glossário -->

---
## Hypertext Transfer Protocol (HTTP)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Hypertext Transfer Protocol (HTTP)* é o protocolo de comunicação padrão para a transferência de documentos na web, utilizado para carregar páginas HTML, imagens e outros recursos. Ele opera na Camada de Aplicação (Camada 7) do modelo OSI, a camada mais próxima do usuário. O HTTP é baseado em uma arquitetura cliente-servidor, onde o navegador solicita recursos ao servidor web e o servidor responde com os dados solicitados. Ele é simples, sem criptografia ou autenticação, o que significa que os dados trocados podem ser interceptados.

No contexto do modelo OSI, a Camada de Aplicação lida com as interações diretas dos usuários com os serviços da rede, incluindo a transferência de arquivos, emails e, no caso do HTTP, o acesso à web. Embora seja amplamente utilizado, o HTTP por si só não oferece segurança e, por isso, é comum usá-lo em situações onde a proteção dos dados não é uma preocupação central, como o carregamento de conteúdo estático.

### Referências

- [MDN Web Docs about HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [MDN Web Docs overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Wikipedia about HTTP](https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [CloudFlare about HTTP](https://www.cloudflare.com/pt-br/learning/ddos/glossary/hypertext-transfer-protocol-http/)

---
## Hypertext Transfer Protocol Secure (HTTPS)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Hypertext Transfer Protocol Secure (HTTPS)* é a versão segura do HTTP, que adiciona uma camada de criptografia utilizando SSL/TLS para proteger a comunicação. Embora também opere na Camada de Aplicação (Camada 7), o HTTPS se diferencia do HTTP por fornecer segurança adicional, garantindo a confidencialidade e a integridade dos dados transmitidos. A criptografia ocorre na Camada de Sessão (Camada 5) e na Camada de Transporte (Camada 4), onde os protocolos SSL/TLS operam para assegurar que os dados trocados entre o cliente e o servidor não possam ser lidos ou alterados por terceiros.

O HTTPS é essencial para proteger informações sensíveis, como senhas, dados bancários e transações financeiras, e tornou-se o padrão para qualquer site que deseje garantir a segurança de seus usuários. Ele utiliza a porta 443 por padrão e é fortemente recomendado para qualquer aplicação que lide com dados privados. Além de criptografar os dados, o HTTPS também garante a autenticidade do servidor, o que aumenta a confiança dos usuários ao interagir com a web.

### Referências

- [MDN Glossary about HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)
- [Amazon AWS about the difference between HTTP and HTTPS](https://aws.amazon.com/pt/compare/the-difference-between-https-and-http/)
- [Wikipedia about HTTPS](https://pt.wikipedia.org/wiki/Hyper_Text_Transfer_Protocol_Secure)
- [CloudFlare about HTTPS](https://www.cloudflare.com/pt-br/learning/ssl/what-is-https/)

---
## Internet Control Message Protocol (ICMP)

### Descrição

O *Internet Control Message Protocol (ICMP)*, por sua vez, é um protocolo de comunicação usado para enviar mensagens de controle e erro entre dispositivos de rede. Ele opera na Camada de Rede (Camada 3) do modelo OSI, a camada responsável pelo roteamento de pacotes de dados entre redes. O ICMP é fundamental para o diagnóstico e resolução de problemas de rede, sendo amplamente utilizado em ferramentas como o ping e traceroute, que ajudam a verificar a conectividade e rastrear o caminho dos pacotes na rede.

O ICMP não é utilizado para a transferência de dados de usuário, mas sim para a comunicação de controle entre dispositivos. Ele permite que roteadores e hosts informem sobre erros de entrega, como pacotes não encontrados ou falhas de rede, e forneçam informações sobre a rede, como latência e a rota que os pacotes estão seguindo. Um exemplo típico de mensagem ICMP é o "Destination Unreachable" (destino inalcançável), enviado quando um pacote não pode chegar ao destino. Embora o ICMP seja essencial para o diagnóstico da rede, ele também pode ser usado em ataques como o DoS (Denial of Service), se não for gerenciado corretamente.

### Referências

- [Amazon AWS about ICMP](https://aws.amazon.com/pt/what-is/icmp/)
- [CloudFlare about ICMP](https://www.cloudflare.com/pt-br/learning/ddos/glossary/internet-control-message-protocol-icmp/)
- [Fortinet about ICMP](https://www.fortinet.com/br/resources/cyberglossary/internet-control-message-protocol-icmp)
- [Wikipedia about ICMP](https://pt.wikipedia.org/wiki/Internet_Control_Message_Protocol)

---
## Internet Protocol (IP)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Internet Protocol (IP)* é um protocolo fundamental para a comunicação entre dispositivos em redes, sendo responsável pelo endereçamento e roteamento de pacotes de dados entre sistemas. Ele opera na Camada de Rede (Camada 3) do modelo OSI, que é responsável pela determinação do melhor caminho para os pacotes de dados de um dispositivo a outro em uma rede ou entre redes distintas, como a internet. O IP permite que dispositivos se identifiquem de forma única em uma rede, através de um endereço IP, que pode ser tanto IPv4 quanto IPv6.

O IPv4 utiliza um sistema de endereçamento de 32 bits, o que resulta em cerca de 4 bilhões de endereços únicos, enquanto o IPv6, com seu endereçamento de 128 bits, oferece um número praticamente ilimitado de endereços. O protocolo IP é crucial para a transmissão de dados em redes locais e globais, realizando o encaminhamento dos pacotes, garantindo que cada pacote seja enviado de forma eficiente e chegue ao destino correto. Embora o IP não seja responsável por garantir a entrega dos pacotes, ele trabalha em conjunto com protocolos de transporte, como TCP e UDP, que asseguram a confiabilidade e o controle dos dados durante a transmissão.

### Referências

- [Wikipedia about IP](https://pt.wikipedia.org/wiki/Endere%C3%A7o_IP)
- [CloudFlare about IP](https://www.cloudflare.com/pt-br/learning/network-layer/internet-protocol/)

---
## Open Systems Interconnection (OSI Model)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

Modelo OSI (*Open Systems Interconnection*) é um modelo de referência para redes de computadores que define um conjunto de regras e protocolos para permitir a comunicação entre sistemas diferentes. Desenvolvido pela ISO (International Organization for Standardization), o modelo OSI divide o processo de comunicação em sete camadas, cada uma com funções específicas. A ideia do modelo é tornar mais fácil o entendimento de como os dados são transmitidos e como os protocolos interagem entre si.

#### Camada 1 - Física (*Physical Layer*)

A camada física é responsável pela transmissão dos bits brutos de dados através de um meio físico, como cabos ou ondas de rádio. Ela trata da conversão dos dados em sinais elétricos, ópticos ou de rádio e define os aspectos físicos do hardware de rede, como conectores, voltagem e a taxa de transmissão. Exemplos de tecnologias dessa camada incluem Ethernet, USB, e Wi-Fi.

#### Camada 2 - Enlace de Dados (*Data Link Layer*)

A camada de enlace de dados é responsável pela transferência de dados entre dois dispositivos diretamente conectados e garante a integridade dos dados ao verificar e corrigir erros. Ela lida com o controle de fluxo e a formação de quadros (frames) para enviar pacotes de dados. Exemplos de protocolos dessa camada incluem Ethernet, PPP (Point-to-Point Protocol) e HDLC (High-Level Data Link Control).

#### Camada 3 - Rede (*Network Layer*)

A camada de rede gerencia o endereçamento e o roteamento dos dados através de redes diferentes. Ela decide qual caminho os dados devem seguir até o destino, considerando fatores como congestionamento e distância. O principal protocolo dessa camada é o IP (Internet Protocol), mas outros protocolos incluem ICMP (Internet Control Message Protocol) e ARP (Address Resolution Protocol).

#### Camada 4 - Transporte (*Transport Layer*)

A camada de transporte garante que os dados sejam entregues de forma confiável entre os dispositivos de origem e destino. Ela segmenta os dados, controla o fluxo e assegura que os pacotes sejam entregues sem erros e na ordem correta. Protocolos dessa camada incluem o TCP (Transmission Control Protocol), que oferece uma comunicação confiável, e o UDP (User Datagram Protocol), que é mais rápido, mas sem garantias de entrega.

#### Camada 5 - Sessão (*Session Layer*)

A camada de sessão gerencia a abertura, controle e fechamento das sessões de comunicação entre aplicativos. Ela permite que os dados sejam sincronizados entre dispositivos e controla o fluxo de dados durante a comunicação, garantindo que a troca de dados ocorra sem interferências. Exemplos de protocolos dessa camada incluem NetBIOS e RPC (Remote Procedure Call).

#### Camada 6 - Apresentação (*Presentation Layer*)

A camada de apresentação é responsável pela formatação e tradução dos dados que serão enviados entre os sistemas. Ela garante que os dados sejam apresentados de forma compreensível para o aplicativo, realizando funções como criptografia, compressão e conversão de formato de dados. Exemplos de protocolos dessa camada incluem SSL/TLS (para criptografia) e JPEG, MPEG (para formatação de mídia).

#### Camada 7 - Aplicação (*Application Layer*)

A camada de aplicação é onde os usuários interagem diretamente com a rede. Ela define os protocolos que os aplicativos utilizam para se comunicar pela rede, como navegadores, e-mails e outros serviços. Exemplos de protocolos dessa camada incluem HTTP (para navegação na web), FTP (para transferência de arquivos), SMTP (para envio de e-mails), e DNS (para resolução de nomes de domínio).

### Referências

- [Wikipedia about OSI Model](https://pt.wikipedia.org/wiki/Modelo_OSI)
- [Alura about OSI Model](https://www.alura.com.br/artigos/conhecendo-o-modelo-osi?srsltid=AfmBOoqJISb98rbDxr1dq9q1P989R40QlGegUB05RdtDsgXakhIYZvk8)
- [CloudFlare about OSI Model](https://www.cloudflare.com/pt-br/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [Amazon AWS about OSI Model](https://aws.amazon.com/pt/what-is/osi-model/)
- [CISCO about OSI Model](https://community.cisco.com/t5/artigos-gerais/modelo-osi-e-suas-camadas/ta-p/5052369)

---
## Secure Shell (SSH)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Secure Shell (SSH)* é um protocolo de rede amplamente utilizado em ambientes Linux e macOS para acesso remoto seguro a servidores e dispositivos. Ele permite a execução de comandos e a transferência de arquivos com segurança, protegendo os dados por meio de criptografia. O SSH opera, por padrão, na porta 22 e oferece diferentes métodos de autenticação, incluindo o uso de credenciais (usuário e senha) e chaves criptográficas, que fornecem uma camada adicional de segurança. Em ambientes corporativos e de desenvolvimento, o SSH substitui protocolos mais vulneráveis, como Telnet, garantindo a privacidade e a integridade das operações remotas.

### Referências

- [CloudFlare about SSH](https://www.cloudflare.com/pt-br/learning/access-management/what-is-ssh/)
- [Wikipedia about SSH](https://pt.wikipedia.org/wiki/Secure_Shell)

---
## Secure Sockets Layer (SSL)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Secure Sockets Layer (SSL)* é um protocolo de segurança criado para proteger a comunicação entre servidores e clientes na internet, garantindo que os dados transmitidos permaneçam privados e protegidos contra interceptações. Ele utiliza criptografia para codificar os dados durante a transmissão, assegurando que apenas o servidor e o cliente possam entender o conteúdo. O SSL passou por diversas atualizações para melhorar a segurança, até que foi gradualmente substituído pelo TLS, devido a vulnerabilidades encontradas nas versões anteriores. Mesmo assim, o termo “SSL” ainda é amplamente usado para se referir às camadas de segurança na web.

### Referências

- [Amazon AWS About SSL Certificate](https://aws.amazon.com/pt/what-is/ssl-certificate/)
- [CloudFlare About SSL Certificate](https://www.cloudflare.com/pt-br/learning/ssl/what-is-ssl/)
- [Wikipedia About SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)

---
## Simple Network Management Protocol (SNMP)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Simple Network Management Protocol (SNMP)* é um protocolo utilizado para gerenciar e monitorar dispositivos de rede, como roteadores, switches, servidores e impressoras. Ele opera na Camada de Aplicação (Camada 7) do modelo OSI, que é responsável pela interação com as aplicações de rede. O SNMP permite que administradores de rede coletem informações detalhadas sobre o status dos dispositivos, como a utilização de CPU, memória, temperatura, tráfego de rede, entre outros, e ainda possibilita o controle remoto desses dispositivos.

O SNMP utiliza uma arquitetura cliente-servidor, onde os dispositivos de rede, chamados de "agentes", enviam informações para um "gerente" central que coleta e armazena esses dados. Ele pode ser configurado para enviar alertas ou traps quando há falhas ou problemas na rede, permitindo que os administradores tomem ações corretivas. SNMP é amplamente usado para monitoramento de redes, configuração de dispositivos e solução de problemas em ambientes corporativos, e é essencial para manter a integridade e a performance da infraestrutura de TI.

### Referências

- [Wikipedia about SNMP](https://pt.wikipedia.org/wiki/Simple_Network_Management_Protocol)
- [4Linux about SNMP](https://4linux.com.br/o-que-e-snmp/)

---
## Transmission Control Protocol (TCP)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Transmission Control Protocol (TCP)* é um protocolo orientado à conexão utilizado para garantir a entrega confiável de dados entre os sistemas. Ele pertence à Camada de Transporte (Camada 4) do modelo OSI. O TCP estabelece uma conexão entre o cliente e o servidor antes de iniciar a transmissão de dados, utilizando um processo de "handshake" de três vias para garantir que a comunicação seja estável e segura. Essa camada é responsável por segmentar os dados, garantir a entrega correta e ordenar as mensagens, caso cheguem fora de sequência.

O protocolo TCP é amplamente utilizado em aplicações que exigem alta confiabilidade, como navegação na web (HTTP/HTTPS), transferência de arquivos (FTP) e e-mails. Além disso, ele oferece controle de fluxo e de congestionamento, o que ajuda a regular a taxa de transmissão, evitando sobrecargas na rede. A camada de transporte, onde o TCP opera, é essencial para garantir a integridade e a confiabilidade na comunicação de dados entre sistemas.

### Referências

- [Wikipedia about TCP](https://pt.wikipedia.org/wiki/Protocolo_de_Controle_de_Transmiss%C3%A3o)
- [CloudFlare about TCP](https://www.cloudflare.com/pt-br/learning/ddos/glossary/tcp-ip/)

---
## Transport Layer Security (TLS)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *Transport Layer Security (TLS)* é a evolução do SSL e o protocolo atualmente recomendado para proteger a transmissão de dados pela internet. Ele oferece melhorias em termos de velocidade e segurança em comparação com o SSL, usando criptografia avançada para garantir a privacidade e a integridade dos dados trocados. TLS é amplamente utilizado em sites, emails e outros serviços online que exigem confidencialidade. Uma das características fundamentais do TLS é a autenticação mútua, que permite confirmar a identidade tanto do cliente quanto do servidor, sendo essencial para uma comunicação segura.

### Referências

- [Wikipedia about TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [Wikipedia about TLS (pt-br)](https://pt.wikipedia.org/wiki/Transport_Layer_Security)
- [CloudFlare about TLS](https://www.cloudflare.com/pt-br/learning/ssl/transport-layer-security-tls/)
- [Amazon AWS about the difference between SSL and TLS](https://aws.amazon.com/pt/compare/the-difference-between-ssl-and-tls/)

---
## User Datagram Protocol (UDP)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

### Descrição

O *User Datagram Protocol (UDP)*, por sua vez, também opera na Camada de Transporte (Camada 4) do modelo OSI, mas de uma maneira diferente do TCP. Ao contrário do TCP, o UDP é um protocolo não orientado à conexão, o que significa que ele envia dados sem verificar se o destinatário recebeu corretamente ou se houve falhas na transmissão. Ele é ideal para situações que exigem rapidez e onde a perda de alguns pacotes de dados não compromete a aplicação, como em transmissões de vídeo ao vivo, chamadas VoIP ou jogos online.

Apesar de sua falta de confiabilidade, o UDP é mais rápido do que o TCP, pois não realiza o processo de handshake nem o controle de fluxo. A Camada de Transporte, onde o UDP está posicionado, é responsável por gerenciar a comunicação entre sistemas de forma eficiente, e o UDP é uma escolha comum quando o desempenho em tempo real é mais importante que a precisão na entrega dos dados.

### Referências

- [CloudFlare about UDP](https://www.cloudflare.com/pt-br/learning/ddos/glossary/user-datagram-protocol-udp/)
- [Wikipedia about UDP](https://pt.wikipedia.org/wiki/Protocolo_de_datagrama_do_usu%C3%A1rio)
- [IBM about UDP](https://www.ibm.com/docs/pt-br/aix/7.3?topic=protocols-user-datagram-protocol)

<!-- término glossário -->

## Referências Gerais

- [Glossário Lucio](https://rlucio01.notion.site/Gloss-rio-Corporativo-9688bde8db034960a1d8938d27565a87)
- [MDN Web Docs Glossary](https://developer.mozilla.org/en-US/docs/Glossary)

<!-- Bloco de perfis -->
[1]: https://www.linkedin.com/in/leonardo-pangaio/