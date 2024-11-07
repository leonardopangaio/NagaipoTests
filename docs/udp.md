# User Datagram Protocol (UDP)

Autor: [Leonardo Pangaio][1] - Data: 2024-11-06

## Descrição

O *User Datagram Protocol (UDP)*, por sua vez, também opera na Camada de Transporte (Camada 4) do modelo OSI, mas de uma maneira diferente do TCP. Ao contrário do TCP, o UDP é um protocolo não orientado à conexão, o que significa que ele envia dados sem verificar se o destinatário recebeu corretamente ou se houve falhas na transmissão. Ele é ideal para situações que exigem rapidez e onde a perda de alguns pacotes de dados não compromete a aplicação, como em transmissões de vídeo ao vivo, chamadas VoIP ou jogos online.

Apesar de sua falta de confiabilidade, o UDP é mais rápido do que o TCP, pois não realiza o processo de handshake nem o controle de fluxo. A Camada de Transporte, onde o UDP está posicionado, é responsável por gerenciar a comunicação entre sistemas de forma eficiente, e o UDP é uma escolha comum quando o desempenho em tempo real é mais importante que a precisão na entrega dos dados.

## Referências

- [CloudFlare about UDP](https://www.cloudflare.com/pt-br/learning/ddos/glossary/user-datagram-protocol-udp/)
- [Wikipedia about UDP](https://pt.wikipedia.org/wiki/Protocolo_de_datagrama_do_usu%C3%A1rio)
- [IBM about UDP](https://www.ibm.com/docs/pt-br/aix/7.3?topic=protocols-user-datagram-protocol)