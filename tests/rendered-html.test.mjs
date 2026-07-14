import assert from "node:assert/strict";
import test from "node:test";

async function render(requestHeaders = {}) {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  return worker.fetch(new Request("http://localhost/", { headers: { accept: "text/html", ...requestHeaders } }), {
    ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) },
  }, { waitUntil() {}, passThroughOnException() {} });
}

test("renderiza portfólio completo", async () => {
  const response = await render();
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /Marcus Moura/);
  assert.match(html, /Desenvolvedor Python &amp; Web/);
  assert.match(html, /Solicitar demonstração/);
  assert.match(html, /Inter Task Monitor/);
  assert.match(html, /Clima OpenWeather/);
  assert.match(html, /Chatbots de Atendimento/);
  assert.match(html, /Atendimento 24 horas/);
  assert.match(html, /agendamento automatizado de clientes/);
  assert.match(html, /Automação de Acompanhamento de Faturamento/);
  assert.match(html, /Trino/);
  assert.match(html, /Tableau/);
  assert.match(html, /SharePoint/);
  assert.match(html, /Acionamento de Clientes/);
  assert.match(html, /envio automático de e-mails/);
  assert.match(html, /análises financeiras/);
  assert.match(html, /11(?:<!-- -->)? resultados/);
  assert.match(html, /mpfagundesmoura@gmail.com/);
  assert.match(html, /\(31\) 99355-5554/);
  assert.match(html, /wa\.me\/5531993555554/);
  assert.doesNotMatch(html, /estágio/i);
  assert.doesNotMatch(html, /codex-preview|SkeletonPreview|react-loading-skeleton/);
});

test("ignora host encaminhado não confiável", async () => {
  const response = await render({ "x-forwarded-host": "host inválido, attacker.example" });
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /marcus-moura-portfolio\.mpfagundesmoura\.chatgpt\.site/);
  assert.doesNotMatch(html, /attacker\.example/);
});
