# MERMAID

## Descrição

```mermaid
sequenceDiagram
    autonumber
    participant Usuario as Analista Financeiro
    participant Sistema as Sistema de Conciliação
    participant API as API Bancária
    participant BD as Banco de Dados
    participant Notificacao as Serviço de Notificação

    Usuario->>Sistema: Solicitar Conciliação
    Sistema->>API: Requisitar Extrato Bancário
    API-->>Sistema: Retornar Extrato Bancário
    Sistema->>Sistema: Processar Conciliação
    Sistema->>BD: Armazenar Resultado da Conciliação
    Sistema->>Notificacao: Notificar Resultado
    Notificacao-->>Usuario: Enviar E-mail com Resultado
```

