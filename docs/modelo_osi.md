# Open Systems Interconnection (OSI Model)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

## Descrição

Modelo OSI (*Open Systems Interconnection*) é um modelo de referência para redes de computadores que define um conjunto de regras e protocolos para permitir a comunicação entre sistemas diferentes. Desenvolvido pela ISO (International Organization for Standardization), o modelo OSI divide o processo de comunicação em sete camadas, cada uma com funções específicas. A ideia do modelo é tornar mais fácil o entendimento de como os dados são transmitidos e como os protocolos interagem entre si.

### Camada 1 - Física (*Physical Layer*)

A camada física é responsável pela transmissão dos bits brutos de dados através de um meio físico, como cabos ou ondas de rádio. Ela trata da conversão dos dados em sinais elétricos, ópticos ou de rádio e define os aspectos físicos do hardware de rede, como conectores, voltagem e a taxa de transmissão. Exemplos de tecnologias dessa camada incluem Ethernet, USB, e Wi-Fi.

### Camada 2 - Enlace de Dados (*Data Link Layer*)

A camada de enlace de dados é responsável pela transferência de dados entre dois dispositivos diretamente conectados e garante a integridade dos dados ao verificar e corrigir erros. Ela lida com o controle de fluxo e a formação de quadros (frames) para enviar pacotes de dados. Exemplos de protocolos dessa camada incluem Ethernet, PPP (Point-to-Point Protocol) e HDLC (High-Level Data Link Control).

### Camada 3 - Rede (*Network Layer*)

A camada de rede gerencia o endereçamento e o roteamento dos dados através de redes diferentes. Ela decide qual caminho os dados devem seguir até o destino, considerando fatores como congestionamento e distância. O principal protocolo dessa camada é o IP (Internet Protocol), mas outros protocolos incluem ICMP (Internet Control Message Protocol) e ARP (Address Resolution Protocol).

### Camada 4 - Transporte (*Transport Layer*)

A camada de transporte garante que os dados sejam entregues de forma confiável entre os dispositivos de origem e destino. Ela segmenta os dados, controla o fluxo e assegura que os pacotes sejam entregues sem erros e na ordem correta. Protocolos dessa camada incluem o TCP (Transmission Control Protocol), que oferece uma comunicação confiável, e o UDP (User Datagram Protocol), que é mais rápido, mas sem garantias de entrega.

### Camada 5 - Sessão (*Session Layer*)

A camada de sessão gerencia a abertura, controle e fechamento das sessões de comunicação entre aplicativos. Ela permite que os dados sejam sincronizados entre dispositivos e controla o fluxo de dados durante a comunicação, garantindo que a troca de dados ocorra sem interferências. Exemplos de protocolos dessa camada incluem NetBIOS e RPC (Remote Procedure Call).

### Camada 6 - Apresentação (*Presentation Layer*)

A camada de apresentação é responsável pela formatação e tradução dos dados que serão enviados entre os sistemas. Ela garante que os dados sejam apresentados de forma compreensível para o aplicativo, realizando funções como criptografia, compressão e conversão de formato de dados. Exemplos de protocolos dessa camada incluem SSL/TLS (para criptografia) e JPEG, MPEG (para formatação de mídia).

### Camada 7 - Aplicação (*Application Layer*)

A camada de aplicação é onde os usuários interagem diretamente com a rede. Ela define os protocolos que os aplicativos utilizam para se comunicar pela rede, como navegadores, e-mails e outros serviços. Exemplos de protocolos dessa camada incluem HTTP (para navegação na web), FTP (para transferência de arquivos), SMTP (para envio de e-mails), e DNS (para resolução de nomes de domínio).

## Referências

- [Wikipedia about OSI Model](https://pt.wikipedia.org/wiki/Modelo_OSI)
- [Alura about OSI Model](https://www.alura.com.br/artigos/conhecendo-o-modelo-osi?srsltid=AfmBOoqJISb98rbDxr1dq9q1P989R40QlGegUB05RdtDsgXakhIYZvk8)
- [CloudFlare about OSI Model](https://www.cloudflare.com/pt-br/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [Amazon AWS about OSI Model](https://aws.amazon.com/pt/what-is/osi-model/)
- [CISCO about OSI Model](https://community.cisco.com/t5/artigos-gerais/modelo-osi-e-suas-camadas/ta-p/5052369)