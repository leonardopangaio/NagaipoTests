# Internet Control Message Protocol (ICMP)

## Descrição

O *Internet Control Message Protocol (ICMP)*, por sua vez, é um protocolo de comunicação usado para enviar mensagens de controle e erro entre dispositivos de rede. Ele opera na Camada de Rede (Camada 3) do modelo OSI, a camada responsável pelo roteamento de pacotes de dados entre redes. O ICMP é fundamental para o diagnóstico e resolução de problemas de rede, sendo amplamente utilizado em ferramentas como o ping e traceroute, que ajudam a verificar a conectividade e rastrear o caminho dos pacotes na rede.

O ICMP não é utilizado para a transferência de dados de usuário, mas sim para a comunicação de controle entre dispositivos. Ele permite que roteadores e hosts informem sobre erros de entrega, como pacotes não encontrados ou falhas de rede, e forneçam informações sobre a rede, como latência e a rota que os pacotes estão seguindo. Um exemplo típico de mensagem ICMP é o "Destination Unreachable" (destino inalcançável), enviado quando um pacote não pode chegar ao destino. Embora o ICMP seja essencial para o diagnóstico da rede, ele também pode ser usado em ataques como o DoS (Denial of Service), se não for gerenciado corretamente.

## Referências

- [Amazon AWS about ICMP](https://aws.amazon.com/pt/what-is/icmp/)
- [CloudFlare about ICMP](https://www.cloudflare.com/pt-br/learning/ddos/glossary/internet-control-message-protocol-icmp/)
- [Fortinet about ICMP](https://www.fortinet.com/br/resources/cyberglossary/internet-control-message-protocol-icmp)
- [Wikipedia about ICMP](https://pt.wikipedia.org/wiki/Internet_Control_Message_Protocol)