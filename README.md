# Portfólio — Marcus Moura

Portfólio pessoal de Marcus Moura, desenvolvido para apresentar projetos de desenvolvimento web, Python, automação, dados e aplicações mobile. A página combina narrativa profissional, cases técnicos, contato direto e uma interface responsiva com movimento sutil.

## O que foi entregue

- Hero com posicionamento profissional e CTA para contato.
- Seção de projetos com filtros por `Web`, `Python`, `Dados` e `Mobile`.
- 11 projetos mapeados, incluindo:
  - chatbots de atendimento 24 horas com Python, APIs, banco de dados e agendamento;
  - automação de acompanhamento de faturamento com Trino, Tableau e SharePoint;
  - acionamento automatizado de clientes, e-mails e análises financeiras;
  - projetos web, APIs, CRUDs, jogos e aplicativo iOS.
- Cards com stack técnica, destaque de entrega e indicação de cases privados.
- Contato por e-mail, LinkedIn, GitHub e WhatsApp.
- Layout responsivo para desktop e mobile.
- Motion design em CSS: entrada progressiva, hover dos cards, brilho e navegação suave.
- Estados acessíveis nos filtros (`aria-pressed`) e atualização de resultados (`aria-live`).

## Stack

- Next.js/vinext e React
- TypeScript
- HTML semântico
- CSS responsivo e animações nativas
- Node.js e pnpm
- Node Test Runner para validação do HTML renderizado
- ESLint

## Executar localmente

Pré-requisito: Node.js `>=22.13.0`.

```bash
pnpm install
pnpm dev
```

Para validar produção:

```bash
pnpm lint
pnpm test
pnpm build
```

## Estrutura principal

```text
app/page.tsx                  Conteúdo, filtros e interações do portfólio
app/globals.css               Tokens visuais, layout responsivo e motion
tests/rendered-html.test.mjs  Testes de conteúdo e renderização
public/                       Favicon, imagem Open Graph e assets públicos
.openai/hosting.json          Configuração de publicação no Sites
```

## Publicação

Site publicado em:

<https://marcus-moura-portfolio.mpfagundesmoura.chatgpt.site>

## Contato

- E-mail: [mpfagundesmoura@gmail.com](mailto:mpfagundesmoura@gmail.com)
- WhatsApp: [(31) 99355-5554](https://wa.me/5531993555554)
- GitHub: <https://github.com/MarcusPaulodev1>

## Licença

Conteúdo e código pertencem a Marcus Moura. Consulte antes de reutilizar textos, identidade visual ou dados de contato.
