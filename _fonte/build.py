import json
from urllib.parse import quote

WA_MSG = {
 "msp":"Olá! Acabei de preencher o formulário na página para MSPs e quero adiantar a conversa sobre revenda de cloud com a minha marca.",
 "csp":"Olá! Acabei de preencher o formulário na página para CSPs e quero adiantar a conversa sobre ampliar minha capacidade de nuvem.",
 "empresas":"Olá! Acabei de preencher o formulário na página para empresas e quero adiantar a conversa sobre servidores cloud para a minha operação.",
}
WA_MSG_LP = {
 "msp":"Olá! Vim da página para MSPs e quero saber mais sobre revender cloud com a minha marca.",
 "csp":"Olá! Vim da página para CSPs e quero saber mais sobre ampliar minha capacidade de nuvem.",
 "empresas":"Olá! Vim da página para empresas e quero saber mais sobre servidores cloud para a minha operação.",
}
PAGES = {
"msp": dict(
  file="msp.html", slug="msp", rd_id="lp-1-msp-6409565b6380a14dbd2e", nav="MSP",
  title="Cloud White Label para MSPs | Vituax", kw="cloud white label para MSP",
  desc="Painel white label, servidores prontos em minutos, infraestrutura e suporte N2/N3 por conta da Vituax. Receita recorrente sem data center e sem CAPEX.",
  h1="Revenda cloud com a sua marca e fature todo mês",
  sub="Painel white label, servidores prontos em minutos, infraestrutura e suporte por conta da Vituax. Sem data center, sem CAPEX.",
  bullets=["<b>Zero investimento inicial:</b> você paga só o que os clientes consomem",
           "<b>Margem definida por você</b> sobre o custo por recurso",
           "<b>Suporte de 2º e 3º nível</b> em português, 24x7, com a Vituax"],
  cta="Quero revender cloud",
  gainsH2="Tudo que um MSP precisa para vender cloud amanhã",
  gainsSub="Três coisas resolvidas de uma vez: produto, operação e margem.",
  gains=[
    ("panel","Painel com a sua marca","Seu logo, seu domínio, sua identidade. O cliente final vê só você. Crie contas, provisione VMs e acompanhe o consumo por cliente.",["Criação de VM em poucos cliques","Dashboards de custo e margem"]),
    ("shield","Infraestrutura e segurança por nossa conta","Backbone próprio, monitoramento 24x7, Anti-DDoS e firewall virtual em toda VM. Você não contrata engenheiro de infra.",["SLA de 99,95% de disponibilidade","Suporte técnico N2 e N3 em português"]),
    ("chart","Receita recorrente desde o primeiro cliente","Custo transparente por recurso; você define o preço final e fatura mensalmente sobre a sua base, sem investir em servidores.",["Sem investimento em hardware","Escala conforme a sua carteira cresce"]),
  ],
  processSub="Nenhuma tabela genérica. Entendemos a sua carteira antes de falar de número.",
  steps=[
    ("Conversa de diagnóstico","Um especialista entende sua base de clientes, o que você já vende e onde a nuvem entra no portfólio.","Em poucos minutos"),
    ("Desenho da parceria e demonstração","Mostramos o painel com a sua marca, definimos o modelo de operação e simulamos as margens do seu cenário real.","Ao vivo, 45 minutos"),
    ("Proposta e ativação","Você recebe preço fechado para o seu cenário. Aprovado, o painel é personalizado e a primeira VM sobe em minutos.","Preço só depois de entender você"),
  ],
  guar=[("Escala sem trava","Aumente ou reduza vCPU, RAM e disco pelo painel, quando a carteira pedir."),
        ("Migração assistida","Nosso time planeja e executa a migração dos seus clientes, de servidores físicos ou de outras nuvens."),
        ("Ativação em minutos","Provisionamento automático pelo painel. Nada de esperar dias por um servidor."),
        ("Gente do outro lado","Suporte 24x7 em português, com equipe técnica no Brasil.")],
  closeH2="Comece a vender cloud com a sua marca",
  closeSub="Conversa direta com um especialista: entendemos a sua base de clientes e desenhamos o modelo de parceria.",
  closeList=["Resposta em poucos minutos","Demonstração do painel ao vivo","Proposta fechada para o seu cenário"],
),
"csp": dict(
  file="csp.html", slug="csp", rd_id="lp-1-csp-5c0d6ccde37a4fa163c9", nav="CSP",
  title="Cloud para Cloud Service Providers | Vituax", kw="cloud para cloud service providers (CSP)",
  desc="Capacidade em São Paulo e nos EUA, painel multicloud que unifica a sua infraestrutura com a da Vituax e preço de atacado por recurso. Sua marca na frente.",
  h1="Amplie sua nuvem sem construir mais um data center",
  sub="Capacidade em São Paulo e nos EUA, painel multicloud que unifica a sua infraestrutura com a nossa, e preço de atacado por recurso. Sua marca na frente, a Vituax por baixo.",
  bullets=["<b>Nova região em semanas,</b> não em anos: expansão sem CAPEX",
           "<b>Multicloud em um painel:</b> sua infra e a Vituax na mesma interface white label",
           "<b>Atacado por recurso,</b> com margem preservada em cada VM revendida"],
  cta="Quero ampliar minha capacidade",
  gainsH2="Capacidade, alcance e operação para quem já vende nuvem",
  gainsSub="Cresça a carteira e a geografia sem crescer o CAPEX nem o time de infraestrutura.",
  gains=[
    ("chart","Capacidade elástica de atacado","Absorva picos, novos clientes e novas regiões sem comprar hardware. Provisione em São Paulo ou nos EUA e pague só pelo consumo.",["Presença nos maiores data centers das Américas","Escala para cima ou para baixo em minutos"]),
    ("panel","Multicloud unificado, com a sua marca","Nuvens públicas e privadas, suas e nossas, no mesmo painel white label. Um lugar para provisionar, monitorar e faturar.",["Visão em tempo real de todas as VMs","Controle de custo e lucro por cliente"]),
    ("shield","Rede e segurança de nível backbone","Integração direta ao backbone, latência ultra-baixa, Anti-DDoS e EdgeProtect em toda máquina, monitorados 24x7.",["SLA de 99,95% de disponibilidade","Suporte técnico N2 e N3 em português"]),
  ],
  processSub="Nenhuma tabela genérica. Entendemos a sua infraestrutura antes de falar de número.",
  steps=[
    ("Diagnóstico da infraestrutura","Um especialista mapeia sua capacidade atual, regiões, gargalos e onde a Vituax entra como extensão.","Em poucos minutos"),
    ("Integração e demonstração","Mostramos o painel multicloud unificando a sua infra com a nossa, com a sua marca, e desenhamos o modelo de operação.","Ao vivo, 45 minutos"),
    ("Proposta de atacado e ativação","Você recebe preço de atacado fechado para o seu volume. Aprovado, a integração é concluída e as primeiras VMs sobem em minutos.","Preço só depois de entender você"),
  ],
  guar=[("Sem lock-in de hardware","Amplie ou reduza capacidade conforme a demanda, sem ativo parado."),
        ("Migração assistida","Nosso time planeja e executa a migração de cargas entre a sua infra e a Vituax."),
        ("Ativação em minutos","Provisionamento automático pelo painel, em qualquer região disponível."),
        ("Gente do outro lado","Suporte 24x7 em português, com equipe técnica no Brasil.")],
  closeH2="Cresça sua nuvem sem crescer o CAPEX",
  closeSub="Conversa direta com um especialista: entendemos a sua infraestrutura e desenhamos a expansão com preço de atacado.",
  closeList=["Resposta em poucos minutos","Demonstração do painel multicloud ao vivo","Proposta de atacado para o seu volume"],
),
"empresas": dict(
  file="empresas.html", slug="empresas", rd_id="lp-1-empresas-0c92765278acf9d79cfb", nav="Empresas",
  title="Servidor Cloud para Empresas | Vituax", kw="servidor cloud para empresas",
  desc="Servidores cloud prontos em minutos, Anti-DDoS e firewall inclusos, data centers no Brasil e nos EUA, suporte 24x7 em português.",
  h1="Nuvem de alta performance, sem precisar de um time de nuvem",
  sub="Servidores prontos em minutos, Anti-DDoS e firewall inclusos, data centers no Brasil e nos EUA. Você controla tudo em um painel simples.",
  bullets=["<b>Ativação em minutos,</b> sem abrir ticket nem esperar aprovação",
           "<b>Latência local:</b> dados e servidores no Brasil",
           "<b>Custo previsível:</b> você paga só o que a operação usa"],
  cta="Quero uma proposta",
  gainsH2="Nuvem que você mesmo controla, sem depender de especialista",
  gainsSub="Painel simples, infraestrutura robusta e suporte que atende.",
  gains=[
    ("panel","Crie e gerencie sem ser especialista","Escolha sistema, tamanho e rede em poucos cliques. Acompanhe recursos em tempo real e ajuste quando precisar.",["VM ativa em minutos","Acesso remoto seguro de onde estiver"]),
    ("shield","Segurança e estabilidade inclusas","Anti-DDoS, firewall virtual, backups programáveis e monitoramento humano 24x7 em toda máquina.",["SLA de 99,95% de disponibilidade","Dados em data centers no Brasil"]),
    ("chart","Custo previsível, sem surpresa","Você paga pelos recursos que a operação usa, com escala para cima ou para baixo quando o negócio pedir.",["Sem taxa de tráfego","Sem contrato mínimo por recurso"]),
  ],
  processSub="Nenhuma tabela genérica. Entendemos a sua operação antes de falar de número.",
  steps=[
    ("Conversa de diagnóstico","Um especialista entende sua operação atual: sistemas, cargas, picos e o que hoje trava o crescimento.","Em poucos minutos"),
    ("Configuração e demonstração","Desenhamos os servidores certos para o seu cenário e mostramos o painel ao vivo, incluindo o plano de migração.","Ao vivo, 45 minutos"),
    ("Proposta e ativação","Você recebe preço fechado para a configuração desenhada. Aprovado, migramos e a operação sobe em minutos.","Preço só depois de entender você"),
  ],
  guar=[("Escala sem trava","Aumente ou reduza vCPU, RAM e disco pelo painel, quando o negócio pedir."),
        ("Migração assistida","Nosso time planeja e executa a migração de servidores físicos ou de outras nuvens."),
        ("Ativação em minutos","Provisionamento automático pelo painel. Nada de esperar dias por um servidor."),
        ("Gente do outro lado","Suporte 24x7 em português, com equipe técnica no Brasil.")],
  closeH2="Leve sua operação para a nuvem sem dor de cabeça",
  closeSub="Conversa direta com um especialista: entendemos a sua operação e indicamos a configuração certa, incluindo a migração.",
  closeList=["Resposta em poucos minutos","Demonstração do painel ao vivo","Proposta fechada para a sua operação"],
),
}

ICONS = {
 "panel":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19V5M4 15l5-5 4 4 7-7"/></svg>',
}


# ===================== CONFIGURAÇÃO (edite aqui) =====================
BASE        = "https://lp.vituax.space/"
GTM_ID      = "GTM-TQ527DJM"                        # mesmo container do site atual
EMAIL       = "contato@vituax.com"                  # confirme o e-mail comercial
PRIVACY_URL = "https://www.vituax.com/pt/privacidade"   # troque pela URL real da política
TERMS_URL   = "https://www.vituax.com/pt/termos"         # troque pela URL real dos termos
WHATSAPP    = "5511250010 10".replace(" ","")   # número do comercial no WhatsApp (só dígitos, com 55). Confirme!
CONSENT_DEFAULT = "granted"  # mede tudo desde o carregamento; o aviso de cookies é apenas informativo
# =====================================================================

ASSETS = BASE+"assets/"
LOGO=(f'<picture><source srcset="{ASSETS}logo-branco.png" media="(prefers-color-scheme: dark)">'
      f'<img src="{ASSETS}logo-roxo-escuro.png" alt="Vituax" width="720" height="161" decoding="async"></picture>')
LOGO_WHITE=f'<img src="{ASSETS}logo-branco.png" alt="Vituax" width="720" height="161" decoding="async">'

FAVICON_OLD = "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpolygon points='8,20 8,80 60,50' fill='%23647AF2' opacity='.85'/%3E%3Cpolygon points='36,12 36,88 92,50' fill='%23647AF2' opacity='.55'/%3E%3Cpolygon points='36,34 36,66 64,50' fill='%233D04A8'/%3E%3C/svg%3E"

def consent_head(page_type,seg):
    return f"""<script>
/* Consent Mode v2 — sinal fixo (público BR); o aviso de cookies é só informativo */
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}
dataLayer.push({{page_type:'PAGE_TYPE',page_segment:'PAGE_SEGMENT',brand:'vituax'}});
gtag('consent','default',{{ad_storage:'{CONSENT_DEFAULT}',ad_user_data:'{CONSENT_DEFAULT}',ad_personalization:'{CONSENT_DEFAULT}',analytics_storage:'{CONSENT_DEFAULT}'}});
</script>""".replace('PAGE_TYPE',page_type).replace('PAGE_SEGMENT',seg)

GTM_HEAD = f"""<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- End Google Tag Manager -->"""
GTM_BODY = f"""<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>"""

ORG = {
 "@type":"Organization","@id":BASE+"#org","name":"Vituax","url":"https://www.vituax.com/pt",
 "logo":ASSETS+"logo-roxo-escuro.png",
 "telephone":"+55-11-2500-1010","email":EMAIL,
 "address":{"@type":"PostalAddress","streetAddress":"Av. Prefeito Carlos Ferreira Lopes, 703, Sala 1106","addressLocality":"Mogi das Cruzes","addressRegion":"SP","postalCode":"08773-490","addressCountry":"BR"},
 "sameAs":["https://www.linkedin.com/company/vituax/","https://www.instagram.com/vituax_br/","https://www.youtube.com/@Vituax_cloud_brasil"]
}
def jsonld(p):
    return {"@context":"https://schema.org","@graph":[ORG,
      {"@type":"WebPage","@id":BASE+p["slug"],"url":BASE+p["slug"],"name":p["title"],"description":p["desc"],"inLanguage":"pt-BR","isPartOf":{"@id":BASE+"#org"}},
      {"@type":"Service","name":p["title"].split(" | ")[0],"serviceType":"Cloud computing (IaaS)","provider":{"@id":BASE+"#org"},"areaServed":["BR","US"],"description":p["desc"],
       "audience":{"@type":"BusinessAudience","name":p["nav"]}}]}

CSS = open('style.css').read()

def rd_slot(n, rd_id):
    return f'''<div class="rd-slot" data-rd-slot="hero">
        <div role="main" id="{rd_id}"></div>
        <p class="rd-status" id="rdStatus">Não conseguimos carregar o formulário. Atualize a página ou desative bloqueadores de anúncio.</p>
      </div>'''

def form_card(id_, n, rd_id):
    return f'''<div class="form-card" id="{id_}" data-form-position="{"hero" if n==1 else "fechamento"}">
      <h3>Fale com um especialista</h3>
      <p class="lead-in">Resposta em poucos minutos, pelo WhatsApp.</p>
      {rd_slot(n, rd_id)}
      <small class="privacy">Sem spam. Seus dados são usados só para retornar o contato.</small>
    </div>'''

def build(key):
    p = PAGES[key]
    nav = ''.join(f'<li><a href="{BASE}{PAGES[k]["slug"]}"{" aria-current=\"page\"" if k==key else ""}>{PAGES[k]["nav"]}</a></li>' for k in ["msp","csp","empresas"])
    nav_plain = ''.join(f'<li><a href="{BASE}{PAGES[k]["slug"]}">Para {PAGES[k]["nav"]}</a></li>' for k in ["msp","csp","empresas"])
    bullets = ''.join(f'<li>{b}</li>' for b in p["bullets"])
    gains = ''.join(f'''<article class="gain"><div class="ic">{ICONS[ic]}</div><h3>{t}</h3><p>{d}</p><ul class="tri">{''.join(f"<li>{x}</li>" for x in l)}</ul></article>''' for ic,t,d,l in p["gains"])
    steps = ''.join(f'<div class="step"><div class="n">{i+1}</div><h3>{t}</h3><p>{d}</p><span class="when">{w}</span></div>' for i,(t,d,w) in enumerate(p["steps"]))
    guar = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in p["guar"])
    closeList = ''.join(f'<li>{x}</li>' for x in p["closeList"])
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{BASE}{p["slug"]}">
<meta name="theme-color" content="#3D04A8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F0A24" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" sizes="32x32" href="{ASSETS}favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{ASSETS}favicon-64.png">
<link rel="apple-touch-icon" href="{ASSETS}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vituax">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{BASE}{p["slug"]}">
<meta property="og:image" content="{ASSETS}og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p["title"]}">
<meta name="twitter:description" content="{p["desc"]}">
<meta name="twitter:image" content="{ASSETS}og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://d335luupugsy2.cloudfront.net">
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>
<style>
{CSS}
</style>
{consent_head("lp",key)}
{GTM_HEAD}
<script type="application/ld+json">
{json.dumps(jsonld(p), ensure_ascii=False, indent=1)}
</script>
</head>
<body data-segment="{key}">
{GTM_BODY}
<a class="skip" href="#topo">Pular para o conteúdo</a>

<header>
  <div class="wrap nav">
    <a href="#topo" class="logo" aria-label="Vituax">{LOGO}</a>
    <nav aria-label="Soluções por perfil">
      <ul class="menu">{nav}</ul>
    </nav>
    <div class="nav-right">
      <a class="btn btn-primary" href="#form-topo" data-cta="header">Falar com especialista</a>
    </div>
  </div>
</header>

<main id="topo">

<section class="hero">
  <div class="deco" aria-hidden="true"></div>
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Vituax · {p["kw"]}</p>
      <h1>{p["h1"]}</h1>
      <p class="sub">{p["sub"]}</p>
      <ul class="tri">{bullets}</ul>
    </div>
    {form_card("form-topo",1,p["rd_id"])}
  </div>
</section>

<div class="proof">
  <div class="wrap">
    <ul>
      <li><b>99,95%</b><span>de disponibilidade garantida por SLA</span></li>
      <li><b>Brasil + EUA</b><span>servidores nos maiores data centers das Américas</span></li>
      <li><b>Anti-DDoS</b><span>e firewall inclusos em toda máquina</span></li>
      <li><b>24x7</b><span>suporte técnico em português</span></li>
    </ul>
  </div>
</div>

<section id="ganhos">
  <div class="wrap">
    <div class="head"><h2>{p["gainsH2"]}</h2><p class="sub">{p["gainsSub"]}</p></div>
    <div class="gains">{gains}</div>
  </div>
</section>

<section class="alt" id="como">
  <div class="wrap">
    <div class="head"><h2>Como começamos juntos</h2><p class="sub">{p["processSub"]}</p></div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section id="garantias">
  <div class="wrap">
    <div class="head"><h2>O que você não precisa se preocupar</h2></div>
    <div class="guar">{guar}</div>
  </div>
</section>

<section class="close" id="contato">
  <div class="deco" aria-hidden="true"></div>
  <div class="wrap">
    <div>
      <h2>{p["closeH2"]}</h2>
      <p class="sub">{p["closeSub"]}</p>
      <ul class="tri">{closeList}</ul>
    </div>
    <div class="close-cta">
      <a class="btn btn-light btn-xl" href="#form-topo" data-cta="fechamento">{p["cta"]}</a>
      <p class="small-alt">O formulário está no topo da página. Leva menos de um minuto.</p>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap foot">
    <div class="foot-brand">
      <a href="#topo" class="logo" aria-label="Vituax">{LOGO}</a>
      <p>Cloud de alta performance com painel multicloud próprio. Servidores nos maiores data centers da América Latina e dos Estados Unidos.</p>
    </div>
    <div>
      <h4>Soluções</h4>
      <ul>{nav_plain}<li><a href="https://vituax.cloud/" rel="noopener">Já sou cliente</a></li></ul>
    </div>
    <div>
      <h4>Contato</h4>
      <ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="https://www.linkedin.com/company/vituax/" rel="noopener">LinkedIn</a> · <a href="https://www.instagram.com/vituax_br/" rel="noopener">Instagram</a></li>
      </ul>
    </div>
    <div>
      <h4>Legal</h4>
      <ul>
        <li><a href="{PRIVACY_URL}" rel="noopener">Política de privacidade</a></li>
        <li><a href="{TERMS_URL}" rel="noopener">Termos de uso</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal">
    <span>Vituax Brasil LTDA · CNPJ 06.980.218/0001-36</span>
    <span>Av. Prefeito Carlos Ferreira Lopes, 703, Sala 1106 · Mogi das Cruzes, SP · 08773-490</span>
    <span>© 2026 Vituax. Todos os direitos reservados.</span>
  </div>
</footer>

<div class="consent" id="consent" role="status" aria-label="Aviso de cookies" hidden>
  <p>Usamos cookies para medir o desempenho desta página e das nossas campanhas. <a href="{PRIVACY_URL}" rel="noopener">Política de privacidade</a></p>
  <button type="button" class="btn btn-primary" onclick="vtxNotice.ok()">Entendi</button>
</div>

<div class="sticky"><a class="btn btn-primary" href="#form-topo" data-cta="sticky">{p["cta"]}</a></div>

<script>
/* Aviso de cookies — informativo, sem efeito na medição */
window.vtxNotice={{ok(){{try{{localStorage.setItem('vtx_notice','1')}}catch(_){{}}document.getElementById('consent').hidden=true}}}};
try{{if(!localStorage.getItem('vtx_notice'))document.getElementById('consent').hidden=false}}catch(_){{document.getElementById('consent').hidden=false}}
/* ---- Eventos de engajamento para o GTM (GA4 / Ads / Meta) ---- */
const seg=document.body.dataset.segment, push=o=>dataLayer.push(Object.assign({{page_segment:seg}},o));
document.addEventListener('click',e=>{{
  const cta=e.target.closest('[data-cta]'); if(cta) push({{event:'cta_click',cta_position:cta.dataset.cta,cta_text:cta.textContent.trim()}});
  const seq=e.target.closest('.menu a'); if(seq) push({{event:'segment_switch',to_segment:seq.textContent.trim().toLowerCase()}});
}});
/* form_start: primeiro foco em um campo do formulário RD (uma vez por posição) */
const started=new Set();
document.addEventListener('focusin',e=>{{
  const card=e.target.closest('.form-card'); if(!card||!e.target.matches('input,select,textarea'))return;
  const pos=card.dataset.formPosition; if(started.has(pos))return; started.add(pos);
  push({{event:'form_start',form_position:pos}});
}});
/* Guarda o e-mail digitado (1ª parte) para Conversões Aprimoradas na página de obrigado */
document.addEventListener('submit',e=>{{
  const card=e.target.closest('.form-card'); if(!card)return;
  const em=card.querySelector('input[type="email"],input[name*="email"]');
  const ph=card.querySelector('input[type="tel"],input[name*="phone"],input[name*="telefone"],input[name*="celular"]');
  try{{sessionStorage.setItem('vtx_lead',JSON.stringify({{email:em?em.value.trim().toLowerCase():'',phone:ph?ph.value.replace(/[^0-9]/g,''):'',form_position:card.dataset.formPosition}}))}}catch(_){{}}
  push({{event:'form_submit',form_position:card.dataset.formPosition}});
}},true);
</script>
<script>
/* Barra fixa (celular): só aparece quando o formulário sai da tela */
(function(){{var st=document.querySelector('.sticky'),f=document.getElementById('form-topo');if(!st||!f||!('IntersectionObserver' in window))return;
st.classList.add('is-hidden');
new IntersectionObserver(function(es){{st.classList.toggle('is-hidden',es[0].isIntersecting)}},{{threshold:0.15}}).observe(f);}})();
/* Âncoras internas — isolado dos demais scripts para nunca depender do RD. Rola a JANELA, nunca um bloco interno. */
document.addEventListener('click',function(e){{
  var a=e.target.closest('a[href^="#"]'); if(!a)return;
  var href=a.getAttribute('href'); var t=document.querySelector(href); if(!t)return;
  e.preventDefault();
  var top=href==='#topo'?0:t.getBoundingClientRect().top+window.pageYOffset-16;
  window.scrollTo({{top:Math.max(0,top),behavior:'smooth'}});
  if(href==='#form-topo'){{var f=t.querySelector('input:not([type=hidden]):not(.vtx-hidden input)');if(f)setTimeout(function(){{f.focus({{preventScroll:true}})}},450)}}
}},true);
</script>
<script src="https://d335luupugsy2.cloudfront.net/js/rdstation-forms/stable/rdstation-forms.min.js" onerror="var r=document.getElementById('rdStatus');if(r)r.classList.add('show')"></script>
<script>
(function(){{
  const RD_ID='{p["rd_id"]}', seg=document.body.dataset.segment;

  /* ---------- 1. Parâmetros de campanha: captura na chegada e persiste (first-touch da sessão) ---------- */
  const KEYS=['utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_id','gclid','fbclid','li_fat_id'];
  const qs=new URLSearchParams(location.search);
  let saved={{}};try{{saved=JSON.parse(sessionStorage.getItem('vtx_params')||'{{}}')}}catch(_){{}}
  KEYS.forEach(k=>{{const v=qs.get(k);if(v)saved[k]=v}});
  const cookie=n=>(document.cookie.match('(^|;)\\s*'+n+'=([^;]*)')||[])[2]||'';
  if(!saved.fbclid&&cookie('_fbc'))saved.fbclid=decodeURIComponent(cookie('_fbc'));
  saved.url_pagina_cadastro=location.href;
  try{{sessionStorage.setItem('vtx_params',JSON.stringify(saved))}}catch(_){{}}

  /* ---------- 2. Preenche e oculta os campos técnicos assim que o RD renderiza ---------- */
  const HIDE=[...KEYS,'url_pagina_cadastro','perfil','segmento'];
  const norm=t=>(t||'').toLowerCase().replace(/[^a-z_]/g,'');
  function fieldKey(input){{
    const n=norm(input.name)+' '+norm(input.id);
    const lab=input.closest('.bricks-form__field')?.querySelector('label');
    const l=norm(lab?lab.textContent:'');
    return HIDE.find(k=>n.includes(k)||l===k||l.includes(k));
  }}
  function process(root){{
    root.querySelectorAll('.rd-slot input:not([type=hidden]):not([data-vtx])').forEach(i=>{{
      const k=fieldKey(i); if(!k)return;
      i.dataset.vtx=k;
      i.value=(k==='perfil'||k==='segmento')?seg:(saved[k]||'');
      i.dispatchEvent(new Event('input',{{bubbles:true}}));
      (i.closest('.bricks-form__field')||i).classList.add('vtx-hidden');
    }});
  }}
  new MutationObserver(m=>process(document)).observe(document.body,{{childList:true,subtree:true}});
  process(document);

  /* ---------- 3. Guarda e-mail/telefone no clique de envio (Conversões Aprimoradas na página de obrigado) ---------- */
  document.addEventListener('click',e=>{{
    const btn=e.target.closest('.rd-slot button,.rd-slot input[type=submit]'); if(!btn)return;
    const card=btn.closest('.form-card');
    const em=card.querySelector('input[type="email"]'), ph=card.querySelector('input[type="tel"],input[name*="phone"],input[name*="telefone"],input[name*="celular"]');
    try{{sessionStorage.setItem('vtx_lead',JSON.stringify({{email:em?em.value.trim().toLowerCase():'',phone:ph?ph.value.replace(/[^0-9]/g,''):'',form_position:card.dataset.formPosition}}))}}catch(_){{}}
  }},true);

  /* ---------- 4. Renderiza o formulário RD (uma vez, no hero) ---------- */
  try{{new RDStationForms(RD_ID,'null').createForm()}}catch(err){{console.error('RD Station:',err)}}
  setTimeout(function(){{if(!document.querySelector('#'+RD_ID.replace(/[^a-zA-Z0-9_-]/g,'')+' form')){{var r=document.getElementById('rdStatus');if(r)r.classList.add('show')}}}},6000);

}})();
</script>
</body>
</html>
'''

import shutil,os
os.makedirs('/mnt/user-data/outputs/assets',exist_ok=True)
for f in os.listdir('assets'): shutil.copy('assets/'+f,'/mnt/user-data/outputs/assets/'+f)
for k in PAGES:
    open(f'/mnt/user-data/outputs/{PAGES[k]["file"]}','w').write(build(k))

def obrigado(k):
    p=PAGES[k]
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>Recebido — Vituax</title>
<link rel="canonical" href="{BASE}obrigado-{p["slug"]}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/png" sizes="32x32" href="{ASSETS}favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{ASSETS}favicon-64.png">
<link rel="apple-touch-icon" href="{ASSETS}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap" rel="stylesheet">
<style>
{CSS}
.thanks{{min-height:calc(100vh - 72px);display:grid;place-items:center;text-align:center;background:linear-gradient(160deg,var(--violet-ink),var(--violet-deep) 50%,var(--violet));color:#fff}}
.thanks h1{{color:#fff;margin:18px 0 12px}}
.thanks .sub{{color:#D8D0F5;margin:0 auto 28px}}
.btn-wa{{background:#25D366;color:#0B2E1A;min-height:56px;padding:16px 28px;font-size:1.05rem}}
.btn-wa:hover{{background:#1EBE5A}}
.thanks .ok{{width:72px;height:72px;border-radius:50%;background:rgba(255,255,255,.12);display:grid;place-items:center;margin:0 auto}}
</style>
{consent_head("obrigado",k)}
{GTM_HEAD}
</head>
<body>
{GTM_BODY}
<header class="on-dark"><div class="wrap nav"><a href="{BASE}{p["slug"]}" class="logo" aria-label="Vituax">{LOGO_WHITE}</a></div></header>
<main class="thanks">
  <div class="wrap">
    <div class="ok"><svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true"><path d="m14 25 7 7 13-15" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <h1>Recebido. Um especialista falará com você em poucos minutos.</h1>
    <p class="sub">O contato vem pelo WhatsApp informado. Quer furar a fila? Toque no botão abaixo e fale agora com o comercial.</p>
    <a class="btn btn-wa" href="https://wa.me/{WHATSAPP}?text={quote(WA_MSG[k])}" target="_blank" rel="noopener" data-cta="whatsapp_obrigado">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.6 3.1.5a2.6 2.6 0 0 0 1.7-1.2 2.1 2.1 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>
      Falar agora no WhatsApp
    </a>
  </div>
</main>
<script>
/* Evento de conversão para o GTM/Google Ads — perfil fixo desta página de obrigado */
window.dataLayer=window.dataLayer||[];
(function(){{
  var lead={{}};try{{lead=JSON.parse(sessionStorage.getItem('vtx_lead')||'{{}}');sessionStorage.removeItem('vtx_lead')}}catch(_){{}}
  var phone=lead.phone?('+55'+lead.phone.replace(/^55/,'')):'';
  dataLayer.push({{
    event:'lead_conversion', perfil:'{p["slug"]}', form_position:lead.form_position||'', value:1, currency:'BRL',
    /* user_data em texto puro: o GTM faz o hash (Google Ads Conversões Aprimoradas / Meta Advanced Matching) */
    user_data:{{ email:lead.email||'', phone_number:phone }}
  }});
  document.addEventListener('click',function(e){{var a=e.target.closest('[data-cta]');if(a)dataLayer.push({{event:'cta_click',cta_position:a.dataset.cta,page_segment:'{p["slug"]}'}})}});
}})();
</script>
</body>
</html>
'''
for k in PAGES:
    open(f'/mnt/user-data/outputs/obrigado-{k}.html','w').write(obrigado(k))
print("ok")
