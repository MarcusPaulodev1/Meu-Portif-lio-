"use client";

import { useEffect, useMemo, useState } from "react";

type Project = {
  title: string;
  description: string;
  category: "Web" | "Python" | "Dados" | "Mobile";
  stack: string[];
  accent: string;
  number: string;
  link: string;
  highlight: string;
  private?: boolean;
};

const projects: Project[] = [
  {
    title: "Chatbots de Atendimento",
    description: "Atendimento 24 horas com chatbots em Python, integrações por APIs, histórico em banco de dados e agendamento automatizado de clientes.",
    category: "Python",
    stack: ["Python", "APIs", "Banco de dados", "Agendamento"],
    accent: "#69d6c5",
    number: "01",
    link: "https://github.com/MarcusPaulodev1/Projetos",
    highlight: "Conversas transformadas em atendimentos e agendamentos organizados em um fluxo contínuo.",
    private: true,
  },
  {
    title: "Automação de Acompanhamento de Faturamento",
    description: "Automação para acompanhar o faturamento em banco de dados, consultar informações com Trino, publicar indicadores no Tableau e distribuir dados pelo SharePoint.",
    category: "Dados",
    stack: ["Banco de dados", "Trino", "Tableau", "SharePoint"],
    accent: "#f5c86b",
    number: "02",
    link: "https://github.com/MarcusPaulodev1/Projetos",
    highlight: "Dados de faturamento centralizados para reduzir trabalho manual e apoiar decisões.",
    private: true,
  },
  {
    title: "Acionamento de Clientes",
    description: "Automação de acionamento de clientes com base de dados, envio automático de e-mails e suporte a análises financeiras.",
    category: "Dados",
    stack: ["Banco de dados", "E-mail automático", "Análise financeira", "Automação"],
    accent: "#ff8ca1",
    number: "03",
    link: "https://github.com/MarcusPaulodev1/Projetos",
    highlight: "Base, comunicação e análise reunidas em um fluxo automatizado.",
    private: true,
  },
  {
    title: "Saldo",
    description: "PWA de finanças pessoais, privada e offline, com lançamentos, metas, recorrências, backup e um guia financeiro local.",
    category: "Web",
    stack: ["JavaScript", "IndexedDB", "PWA", "CSS"],
    accent: "#75a7ff",
    number: "04",
    link: "https://github.com/MarcusPaulodev1/Projetos",
    highlight: "Experiência offline-first, dados locais e fluxo financeiro completo.",
    private: true,
  },
  {
    title: "Inter Task Monitor",
    description: "Sistema web de gestão de tarefas com Kanban, indicadores, filtros, CRUD completo, API HTTP e persistência SQLite.",
    category: "Web",
    stack: ["Python", "SQLite", "REST API", "JavaScript"],
    accent: "#ff7a59",
    number: "05",
    link: "https://github.com/MarcusPaulodev1/teste-",
    highlight: "Produto funcional do banco de dados ao Kanban e aos indicadores.",
    private: true,
  },
  {
    title: "Clima OpenWeather",
    description: "Consulta climática em tempo real com histórico, tratamento de erros e arquitetura em camadas orientada a objetos.",
    category: "Python",
    stack: ["Python", "OpenWeather", "SQLAlchemy", "Pandas"],
    accent: "#69d6c5",
    number: "06",
    link: "https://github.com/MarcusPaulodev1/Meu-Portif-lio-",
    highlight: "Integração de API, persistência e análise de dados em camadas.",
  },
  {
    title: "Sistema de Usuários",
    description: "CRUD de usuários com persistência relacional, separação de responsabilidades e modelagem orientada a objetos.",
    category: "Python",
    stack: ["Python", "SQLAlchemy", "SQLite", "POO"],
    accent: "#c89cff",
    number: "07",
    link: "https://github.com/MarcusPaulodev1/Meu-Portif-lio-",
    highlight: "CRUD relacional com arquitetura simples, legível e testável.",
  },
  {
    title: "RPG de Faculdade",
    description: "RPG de terminal com criação de personagem, classes aleatórias, missões, batalha, progressão de nível e experiência.",
    category: "Python",
    stack: ["Python", "POO", "Game Logic"],
    accent: "#f5c86b",
    number: "08",
    link: "https://github.com/MarcusPaulodev1/Meu-Portif-lio-/tree/main/rpg-faculdade",
    highlight: "Regras de negócio, estados e progressão modelados com POO.",
  },
  {
    title: "Barber Academy",
    description: "Fluxo de agendamento para barbearia integrado ao WhatsApp, pensado para reduzir atrito entre escolha e contato.",
    category: "Web",
    stack: ["HTML", "CSS", "JavaScript", "WhatsApp"],
    accent: "#ff8ca1",
    number: "09",
    link: "https://github.com/MarcusPaulodev1/Meu-Portif-lio-",
    highlight: "Jornada curta entre intenção, agendamento e atendimento.",
  },
  {
    title: "Jogo da Forca",
    description: "Jogo clássico em Python estruturado com classes, controle de tentativas, validação de entrada e feedback de estado.",
    category: "Python",
    stack: ["Python", "POO", "CLI"],
    accent: "#9dd06f",
    number: "10",
    link: "https://github.com/MarcusPaulodev1/Meu-Portif-lio-",
    highlight: "Validação de entrada e lógica de jogo separadas por classes.",
  },
  {
    title: "Saldo iOS",
    description: "Experimento mobile para acompanhamento financeiro com foco em leitura rápida, privacidade e experiência nativa.",
    category: "Mobile",
    stack: ["SwiftUI", "iOS", "UX"],
    accent: "#78bfff",
    number: "11",
    link: "https://github.com/MarcusPaulodev1/Projetos",
    highlight: "Interface nativa focada em clareza, privacidade e uso diário.",
    private: true,
  },
];

const filters = ["Todos", "Web", "Python", "Dados", "Mobile"] as const;
const whatsappUrl = "https://wa.me/5531993555554?text=Ol%C3%A1%2C%20Marcus!%20Vi%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar%20sobre%20uma%20oportunidade.";

export default function Home() {
  const [filter, setFilter] = useState<(typeof filters)[number]>("Todos");
  const [light, setLight] = useState(false);
  const [copied, setCopied] = useState(false);

  const visible = useMemo(
    () => projects.filter((project) => filter === "Todos" || project.category === filter),
    [filter],
  );

  useEffect(() => {
    document.documentElement.dataset.theme = light ? "light" : "dark";
  }, [light]);

  useEffect(() => {
    if (!("IntersectionObserver" in window)) return;

    const observer = new IntersectionObserver(
      (entries) => entries.forEach((entry) => entry.isIntersecting && entry.target.classList.add("is-visible")),
      { threshold: 0.12 },
    );
    document.documentElement.classList.add("motion-ready");
    document.querySelectorAll(".reveal").forEach((node) => observer.observe(node));
    return () => observer.disconnect();
  }, [filter]);

  useEffect(() => {
    const precisePointer = window.matchMedia("(pointer: fine)").matches;
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!precisePointer || reducedMotion) return;

    const hero = document.querySelector<HTMLElement>(".hero");
    const stage = document.querySelector<HTMLElement>(".code-stage");
    const card = stage?.querySelector<HTMLElement>(".code-card");
    if (!hero || !stage || !card) return;

    let heroFrame = 0;
    let tiltFrame = 0;
    let heroX = 0;
    let heroY = 0;
    let tiltX = 2;
    let tiltY = -7;

    const moveLight = (event: PointerEvent) => {
      const bounds = hero.getBoundingClientRect();
      heroX = event.clientX - bounds.left;
      heroY = event.clientY - bounds.top;
      if (heroFrame) return;
      heroFrame = window.requestAnimationFrame(() => {
        hero.style.setProperty("--pointer-x", `${heroX}px`);
        hero.style.setProperty("--pointer-y", `${heroY}px`);
        heroFrame = 0;
      });
    };

    const tiltCard = (event: PointerEvent) => {
      const bounds = stage.getBoundingClientRect();
      const x = (event.clientX - bounds.left) / bounds.width - 0.5;
      const y = (event.clientY - bounds.top) / bounds.height - 0.5;
      tiltX = 2 - y * 7;
      tiltY = -7 + x * 10;
      if (tiltFrame) return;
      tiltFrame = window.requestAnimationFrame(() => {
        card.style.setProperty("--tilt-x", `${tiltX.toFixed(2)}deg`);
        card.style.setProperty("--tilt-y", `${tiltY.toFixed(2)}deg`);
        tiltFrame = 0;
      });
    };

    const resetTilt = () => {
      card.style.setProperty("--tilt-x", "2deg");
      card.style.setProperty("--tilt-y", "-7deg");
    };

    hero.addEventListener("pointermove", moveLight, { passive: true });
    stage.addEventListener("pointermove", tiltCard, { passive: true });
    stage.addEventListener("pointerleave", resetTilt);
    return () => {
      hero.removeEventListener("pointermove", moveLight);
      stage.removeEventListener("pointermove", tiltCard);
      stage.removeEventListener("pointerleave", resetTilt);
      if (heroFrame) window.cancelAnimationFrame(heroFrame);
      if (tiltFrame) window.cancelAnimationFrame(tiltFrame);
    };
  }, []);

  async function copyEmail() {
    try {
      await navigator.clipboard.writeText("mpfagundesmoura@gmail.com");
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1800);
    } catch {
      window.location.href = "mailto:mpfagundesmoura@gmail.com";
    }
  }

  return (
    <main>
      <a className="skip-link" href="#conteudo">Pular para o conteúdo</a>
      <header className="site-header">
        <a className="brand" href="#inicio" aria-label="Início">
          <span>MM</span><i />
        </a>
        <nav aria-label="Navegação principal">
          <a href="#projetos">Projetos</a>
          <a href="#sobre">Sobre</a>
          <a href="#contato">Contato</a>
        </nav>
        <button className="theme-toggle" onClick={() => setLight((value) => !value)} aria-label="Alternar tema">
          <span>{light ? "Escuro" : "Claro"}</span><b aria-hidden="true">{light ? "◐" : "◑"}</b>
        </button>
      </header>

      <section className="hero" id="inicio" aria-labelledby="hero-title">
        <div className="hero-aurora" aria-hidden="true"><i /><i /></div>
        <div className="hero-copy reveal is-visible">
          <p className="eyebrow"><span /> Aberto a vagas júnior, projetos freelance e colaborações</p>
          <h1 id="hero-title">Desenvolvedor Python & Web. <em>Software que resolve.</em></h1>
          <p className="hero-lead">Construo aplicações completas, APIs e automações — da regra de negócio à interface — com foco em clareza, confiabilidade e uso real.</p>
          <div className="hero-actions">
            <a className="button primary" href="#projetos">Conhecer projetos <span>↘</span></a>
            <a className="button ghost whatsapp-button" href={whatsappUrl} target="_blank" rel="noreferrer">Chamar no WhatsApp <span>↗</span></a>
          </div>
          <ul className="value-list" aria-label="Principais competências">
            <li><strong>Python</strong><span>Back-end e dados</span></li>
            <li><strong>Web</strong><span>Interfaces responsivas</span></li>
            <li><strong>APIs</strong><span>Integrações e automação</span></li>
          </ul>
        </div>

        <div className="code-stage" aria-label="Resumo visual de código">
          <div className="orbit orbit-one" /><div className="orbit orbit-two" />
          <article className="code-card">
            <div className="code-top"><span /><span /><span /><small>portfolio.py</small></div>
            <pre><code><i>class</i> <b>MarcusMoura</b>:{"\n"}  skills = [{"\n"}    <mark>&quot;Python&quot;</mark>, <mark>&quot;Web&quot;</mark>,{"\n"}    <mark>&quot;APIs&quot;</mark>, <mark>&quot;Automação&quot;</mark>{"\n"}  ]{"\n\n"}  <i>def</i> <b>build</b>(idea):{"\n"}    <strong>return</strong> idea.to_product()</code></pre>
            <div className="terminal"><span>›</span> status: pronto para construir <b>●</b></div>
          </article>
          <div className="float-tag tag-one">{projects.length.toString().padStart(2, "0")} projetos</div>
          <div className="float-tag tag-two">Python + Web</div>
        </div>
        <a className="scroll-note" href="#projetos"><span /> role para explorar</a>
      </section>

      <section className="projects-section" id="projetos" aria-labelledby="conteudo">
        <div className="section-heading reveal">
          <div><p className="section-kicker">Trabalhos selecionados</p><h2 id="conteudo">Projetos que saíram<br />do papel.</h2></div>
          <p>Cada case destaca problema, entrega e decisões técnicas — de ferramentas internas a aplicações pessoais.</p>
        </div>
        <div className="filter-bar reveal" role="group" aria-label="Filtrar projetos">
          {filters.map((item) => <button key={item} className={filter === item ? "active" : ""} aria-pressed={filter === item} onClick={() => setFilter(item)}>{item}</button>)}
          <span aria-live="polite">{visible.length.toString().padStart(2, "0")} resultados</span>
        </div>
        <div className="project-grid">
          {visible.map((project) => (
            <article className="project-card reveal" key={project.title} style={{ "--accent": project.accent } as React.CSSProperties}>
              <div className="project-visual">
                <span className="project-number">{project.number}</span>
                <div className="visual-window"><i /><i /><i /><div className="visual-lines"><b /><b /><b /><b /></div></div>
                <small>{project.category}</small>
              </div>
              <div className="project-body">
                <div className="project-title-row"><h3>{project.title}</h3>{project.private && <span className="private-badge">case privado</span>}</div>
                <p>{project.description}</p>
                <p className="project-proof"><small>Entrega</small>{project.highlight}</p>
                <div className="tags">{project.stack.map((item) => <span key={item}>{item}</span>)}</div>
                <a
                  href={project.private ? `mailto:mpfagundesmoura@gmail.com?subject=Demonstração%20do%20projeto%20${encodeURIComponent(project.title)}` : project.link}
                  target={project.private ? undefined : "_blank"}
                  rel={project.private ? undefined : "noreferrer"}
                  aria-label={project.private ? `Solicitar demonstração de ${project.title}` : `Abrir ${project.title} no GitHub`}
                >{project.private ? "Solicitar demonstração" : "Ver código no GitHub"} <span>↗</span></a>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="about-section" id="sobre">
        <div className="about-intro reveal">
          <p className="section-kicker">Sobre mim</p>
          <h2>Curiosidade técnica.<br /><em>Entrega prática.</em></h2>
        </div>
        <div className="about-content reveal">
          <p className="about-lead">Sou Marcus Moura, estudante de Engenharia de Software e desenvolvedor Python & Web.</p>
          <p>Posso contribuir em times de desenvolvimento ou projetos freelance criando back-ends, APIs, automações, bancos de dados e interfaces responsivas. Trabalho com escopo claro, código legível e validação prática.</p>
          <div className="stats">
            <div><strong>{projects.length.toString().padStart(2, "0")}</strong><span>projetos mapeados</span></div>
            <div><strong>05</strong><span>repositórios analisados</span></div>
            <div><strong>∞</strong><span>vontade de aprender</span></div>
          </div>
        </div>
      </section>

      <section className="contact-section" id="contato">
        <p className="section-kicker reveal">Vagas • Freelance • Colaborações</p>
        <div className="contact-main reveal">
          <h2>Precisa de alguém<br /><em>que entregue?</em></h2>
          <a className="contact-arrow" href={whatsappUrl} target="_blank" rel="noreferrer" aria-label="Conversar com Marcus pelo WhatsApp">↗</a>
        </div>
        <div className="contact-grid reveal">
          <button onClick={copyEmail}><small>E-mail</small><span>{copied ? "Copiado!" : "mpfagundesmoura@gmail.com"}</span></button>
          <a href={whatsappUrl} target="_blank" rel="noreferrer" aria-label="Abrir conversa com Marcus no WhatsApp"><small>WhatsApp</small><span>(31) 99355-5554 ↗</span></a>
          <a href="https://www.linkedin.com/in/marcus-paulo-00a2833a6" target="_blank" rel="noreferrer"><small>LinkedIn</small><span>/in/marcus-paulo ↗</span></a>
          <a href="https://github.com/MarcusPaulodev1" target="_blank" rel="noreferrer"><small>GitHub</small><span>@MarcusPaulodev1 ↗</span></a>
        </div>
      </section>

      <footer><span>Marcus Moura © {new Date().getFullYear()}</span><span>Feito com HTML, CSS, JavaScript + café.</span><a href="#inicio">Voltar ao topo ↑</a></footer>
    </main>
  );
}
