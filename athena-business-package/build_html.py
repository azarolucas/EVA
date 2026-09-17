# -*- coding: utf-8 -*-
"""Gera Athena_Business_Package.html — app self-contained: capta info + gera o pacote."""
import base64
logo = base64.b64encode(open("athena_logo.png","rb").read()).decode()

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Athena — Business Package</title>
<style>
:root{--slate:#444D56;--slate2:#3a424b;--grey:#EDECEC;--blue:#E9EFF6;--gold:#8A6D1A;--ink:#2A2E33;--line:#C9C9C9;}
*{box-sizing:border-box}
body{font-family:Calibri,'Segoe UI',Arial,sans-serif;color:var(--ink);margin:0;background:#f4f5f7}
.wrap{max-width:1000px;margin:0 auto;padding:0 16px 60px}
.top{background:var(--slate);color:#fff;display:flex;align-items:center;gap:16px;padding:12px 18px;position:sticky;top:0;z-index:20}
.top img{height:34px}
.top .t{font-weight:bold;font-size:15px;letter-spacing:.5px}
.top .sp{flex:1}
.nav{display:flex;gap:6px;background:#fff;border-bottom:1px solid var(--line);position:sticky;top:58px;z-index:19;padding:8px 16px;flex-wrap:wrap}
.nav button{border:1px solid var(--line);background:#fff;padding:7px 12px;border-radius:6px;cursor:pointer;font-size:13px;font-weight:600;color:var(--slate)}
.nav button.active{background:var(--slate);color:#fff;border-color:var(--slate)}
.tab{display:none;background:#fff;border:1px solid var(--line);border-top:none;padding:18px}
.tab.show{display:block}
.sec{background:var(--slate);color:#fff;font-weight:bold;padding:6px 10px;margin:16px 0 10px;border-left:5px solid var(--gold);font-size:13px}
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:8px 10px}
.f{display:flex;flex-direction:column;gap:3px}
.f label{font-size:11px;font-weight:700;color:var(--slate)}
.f input,.f select,.f textarea{border:1px solid var(--line);background:var(--grey);padding:6px 8px;font-size:13px;border-radius:4px;font-family:inherit}
.f.team input,.f.team select{background:var(--blue)}
.c1{grid-column:span 1}.c2{grid-column:span 2}.c3{grid-column:span 3}.c4{grid-column:span 4}
.c5{grid-column:span 5}.c6{grid-column:span 6}.c8{grid-column:span 8}.c12{grid-column:span 12}
.socio{border:1px solid var(--line);border-radius:8px;padding:12px;margin:10px 0;background:#fafbfc}
.socio .head{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.chk{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;color:var(--slate);background:#fff;border:1px dashed var(--gold);padding:6px 8px;border-radius:6px}
.chk input{width:18px;height:18px}
.btn{border:none;border-radius:8px;padding:10px 16px;font-weight:700;cursor:pointer;font-size:14px}
.btn.p{background:var(--slate);color:#fff}.btn.g{background:var(--gold);color:#fff}.btn.s{background:#e7e9ec;color:var(--slate)}
.btn.sm{padding:6px 10px;font-size:12px}
.bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0}
.val{background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:10px 0}
.val h4{margin:0 0 6px;font-size:13px;color:var(--slate)}
.v{display:flex;align-items:center;gap:8px;font-size:12.5px;margin:3px 0}
.pill{font-size:11px;font-weight:800;padding:2px 8px;border-radius:20px}
.ok{background:#C6EFCE;color:#1c6b2b}.err{background:#FFC7CE;color:#9c2029}.warn{background:#FFEB9C;color:#7a5c00}
.hint{font-size:11px;color:#6B7785;margin:2px 0 8px}
/* ---- documentos ---- */
#docs{margin-top:20px}
.doc{background:#fff;border:1px solid var(--line);box-shadow:0 1px 4px rgba(0,0,0,.06);max-width:820px;margin:0 auto 22px;padding:46px 54px;font-size:12.5px;line-height:1.45}
.doc .lhband{background:var(--slate);display:flex;justify-content:space-between;align-items:center;padding:10px 16px;border-bottom:3px solid var(--gold);margin-bottom:18px}
.doc .lhband img{height:30px}
.doc .lhband .lhr{color:#dfe4ea;font-size:8.3px;text-align:right;line-height:1.4}
.doc h1{font-family:Georgia,serif;color:var(--slate);text-align:center;font-size:20px;margin:4px 0}
.doc h2{color:var(--slate);font-size:13px;margin:12px 0 3px;border-bottom:1px solid #e2e2e2;padding-bottom:2px}
.doc p{margin:4px 0;text-align:justify}
.doc .ctr{text-align:center}.doc .gold{color:var(--gold);font-weight:bold}
.doc .note{color:var(--gold);font-style:italic;font-size:10.5px;margin:3px 0}
.doc table{border-collapse:collapse;width:100%;font-size:11px;margin:8px 0}
.doc td,.doc th{border:1px solid #9aa;padding:4px 6px}.doc th{background:var(--slate);color:#fff}
.doc .cert{border:2px solid var(--slate);border-radius:8px;padding:22px;text-align:center;margin:14px 0}
.doc .cert .big{font-size:16px;font-weight:bold;color:var(--slate)}
.doc .cert .pct{font-size:15px;font-weight:bold;color:var(--gold)}
.doc .stockcert{border:3px double #2f5aa8;padding:26px 30px;position:relative;margin-top:6px}
.doc .stockcert h1{color:#2f5aa8;font-family:Georgia,serif}
.doc .stocknum,.doc .stockint{position:absolute;top:16px;font-size:8.5px;text-align:center;color:#2f5aa8;font-weight:bold;border:1px solid #2f5aa8;padding:3px 10px;border-radius:3px}
.doc .stocknum{left:26px}.doc .stockint{right:26px}
.doc .crev th{background:#eef1f5;color:var(--slate)}
.doc .decl{border:1px solid var(--line);background:#fafbfc;border-radius:6px;padding:12px;margin-top:12px}
.doc .decl .cb{display:inline-block;width:14px;height:14px;border:1px solid #444;text-align:center;line-height:14px;font-weight:bold;margin-right:6px}
.sig{margin-top:10px}
@media print{
  body{background:#fff}
  .top,.nav,.tab,.bar,.val,.hint,#genbar{display:none !important}
  .wrap{padding:0;max-width:none}
  #docs{margin:0}
  .doc{box-shadow:none;border:none;margin:0;max-width:none;padding:14mm 16mm;page-break-after:always}
}
</style></head>
<body>
<div class="top"><img src="data:image/png;base64,__LOGO__"><span class="t">BUSINESS PACKAGE</span><span class="sp"></span><span style="font-size:11px;opacity:.85">abertura de empresa · fonte única</span></div>
<div class="nav">
  <button id="n1" class="active" onclick="tab(1)">1 · Dados do Cliente</button>
  <button id="n2" onclick="tab(2)">2 · Decisões da Empresa</button>
  <button id="n3" onclick="tab(3)">Conferência</button>
  <button class="btn g sm" onclick="gen()">⚙ Gerar Business Package</button>
  <span class="sp"></span>
  <button class="btn s sm" onclick="save()">Salvar</button>
  <button class="btn s sm" onclick="expJSON()">Exportar</button>
  <label class="btn s sm" style="cursor:pointer">Importar<input type="file" onchange="impJSON(event)" hidden></label>
</div>
<div class="wrap">

<!-- ============ TAB 1: CLIENTE ============ -->
<div id="t1" class="tab show">
  <div class="hint">Esta aba pode ser entregue ao cliente para preenchimento, ou preenchida pela equipe.</div>
  <div class="sec">REGISTRO</div>
  <div class="grid">
    <div class="f c6"><label>Nome da Empresa (opção 1)</label><input id="LLC_NAME"></div>
    <div class="f c6"><label>Nome alternativo (opção 2)</label><input id="LLC_NAME_ALT"></div>
    <div class="f c4"><label>Estado</label><input id="STATE"></div>
    <div class="f c4"><label>Tipo</label><select id="ENTITY_TYPE"><option>LLC</option><option>CORP</option></select></div>
    <div class="f c4"><label>Offshore?</label><select id="OFFSHORE"><option>NAO</option><option>SIM</option></select></div>
    <div class="f c12"><label>Atividade da empresa</label><input id="BUSINESS_PURPOSE"></div>
  </div>
  <div class="sec">ENDEREÇO DA EMPRESA</div>
  <div class="grid">
    <div class="f c8"><label>Endereço</label><input id="PRINCIPAL_ADDRESS"></div>
    <div class="f c4"><label>Cidade</label><input id="PRINCIPAL_CITY"></div>
    <div class="f c2"><label>Estado</label><input id="PRINCIPAL_STATE"></div>
    <div class="f c3"><label>CEP</label><input id="PRINCIPAL_ZIP"></div>
    <div class="f c7"><label>&nbsp;</label><label class="chk"><input type="checkbox" id="USE_ATHENA_ADDR" checked> Usar endereço da Athena</label></div>
  </div>
  <div class="sec">SÓCIOS</div>
  <div class="hint">Marque “autorizado a gerenciar (assina)” em quem entra no SunBiz e assina pela empresa. A soma dos % deve dar 100.</div>
  <div id="socios"></div>
  <button class="btn s sm" onclick="addSocio()">+ Adicionar sócio</button>
  <div class="sec">CONTATO PRINCIPAL (deve ser sócio)</div>
  <div class="grid">
    <div class="f c5"><label>Nome</label><input id="CONTACT_NAME"></div>
    <div class="f c3"><label>Telefone</label><input id="CONTACT_PHONE"></div>
    <div class="f c4"><label>E-mail</label><input id="CLIENT_EMAIL"></div>
  </div>
  <div class="sec">CONFIRMAÇÃO DO CLIENTE</div>
  <label class="chk" style="width:100%"><input type="checkbox" id="CLIENT_CONFIRM"> Declaro que revisei e confirmo os dados e as decisões acima para a abertura da empresa.</label>
</div>

<!-- ============ TAB 2: DECISÕES ============ -->
<div id="t2" class="tab">
  <div class="hint">Preenchido/validado pela equipe da Athena ao abrir a empresa. Estas decisões mudam o texto dos documentos.</div>
  <div class="sec">ADMINISTRAÇÃO E REGISTRO</div>
  <div class="grid">
    <div class="f team c4"><label>Administração</label><select id="MANAGEMENT"><option value="MEMBER-MANAGED">Member-managed (pelos sócios)</option><option value="MANAGER-MANAGED">Manager-managed (por gestor)</option></select></div>
    <div class="f team c5"><label>Gestor(es) — se manager-managed</label><input id="MANAGER_NAME"></div>
    <div class="f team c3"><label>Nº SunBiz (document number)</label><input id="SUNBIZ_NUMBER"></div>
    <div class="f team c4"><label>EIN já emitido?</label><select id="EIN_ISSUED"><option>NAO</option><option>SIM</option></select></div>
    <div class="f team c4"><label>Certificate of Status incluído? (opcional)</label><select id="CERT_STATUS_INCLUDED"><option>NAO</option><option>SIM</option></select></div>
    <div class="f team c4"><label>Mailbox contratado?</label><select id="MAILBOX_HIRED"><option>SIM</option><option>NAO</option></select></div>
  </div>
  <div class="sec">AUTORIDADE PARA ASSINAR</div>
  <div class="grid">
    <div class="f team c6"><label>Autoridade</label><select id="AUTHORITY_MODE"><option value="SINGLE">SINGLE — qualquer sócio autorizado</option><option value="DUAL">DUAL — dois acima do limite</option></select></div>
    <div class="f team c6"><label>Limite p/ dupla assinatura (US$) — se DUAL</label><input id="DUAL_THRESHOLD_USD"></div>
    <div class="f team c12"><label>Disposição de imóveis (Operating Agreement, VII.3) — quem decide</label><select id="RE_APPROVAL"><option value="MAJORITY">A maioria dos sócios interessados</option><option value="ALL">Todos os sócios COLETIVAMENTE</option><option value="ANY">Qualquer sócio</option></select></div>
  </div>
  <div class="sec">TRIBUTAÇÃO E DATAS</div>
  <div class="grid">
    <div class="f team c4"><label>Classificação tributária</label><select id="TAX_CLASSIFICATION"><option>PARTNERSHIP</option><option>S-CORPORATION</option><option>C-CORPORATION</option><option>DISREGARDED ENTITY</option></select></div>
    <div class="f team c4"><label>Ano fiscal</label><input id="TAX_YEAR"></div>
    <div class="f team c4"><label>Método contábil</label><select id="ACCOUNTING_METHOD"><option>CASH</option><option>ACCRUAL</option></select></div>
    <div class="f team c4"><label>Data de abertura</label><input id="ABERTURA_DATA"></div>
    <div class="f team c4"><label>Data do protocolo (Articles)</label><input id="ARTICLES_FILED_DATE"></div>
    <div class="f team c4"><label>Data de assinatura do acordo</label><input id="AGREEMENT_DATE"></div>
    <div class="f team c4"><label>Prazo de aporte de capital</label><input id="CONTRIBUTION_DUE_DATE"></div>
    <div class="f team c4"><label>EIN (se emitido)</label><input id="EIN"></div>
    <div class="f team c4"><label>Atendido por</label><input id="SERVICED_BY"></div>
  </div>
  <div class="sec">AGENTE REGISTRADOR</div>
  <div class="grid">
    <div class="f team c6"><label>Nome do agente</label><input id="REGISTERED_AGENT"></div>
    <div class="f team c6"><label>Endereço do agente</label><input id="REGISTERED_AGENT_ADDRESS"></div>
    <div class="f team c5"><label>Cidade</label><input id="AGENT_CITY"></div>
    <div class="f team c2"><label>Estado</label><input id="AGENT_STATE"></div>
    <div class="f team c3"><label>CEP</label><input id="AGENT_ZIP"></div>
  </div>
  <div class="sec">MAILBOX</div>
  <div class="grid">
    <div class="f team c3"><label>Valor anual (US$)</label><input id="MAILBOX_FEE_USD"></div>
    <div class="f team c6"><label>Período coberto</label><input id="MAILBOX_PERIOD"></div>
    <div class="f team c3"><label>Validade final</label><input id="MAILBOX_VALID_UNTIL"></div>
  </div>
</div>

<!-- ============ TAB 3: CONFERÊNCIA ============ -->
<div id="t3" class="tab"><div id="valpanel" class="val"></div></div>

<div class="bar" id="genbar">
  <button class="btn g" onclick="gen()">⚙ Gerar Business Package</button>
  <button class="btn p" onclick="window.print()">🖨 Imprimir / Salvar PDF</button>
  <span class="hint">Gera todos os documentos abaixo. Use “Imprimir/PDF” para exportar (cada documento em sua página).</span>
</div>
<div id="docs"></div>
</div>

<script>
var LOGO="data:image/png;base64,__LOGO__";
var SOCIO_FIELDS=[["POSICAO","Posição","c3"],["PERCENT","% Particip.","c1"],["APORTE","Aporte US$","c2"],["VOTO","Voto % (se ≠)","c2"],["NOME","Nome completo","c4"],
  ["SSN","SSN/ITIN/EIN","c3"],["DOB","Nascimento","c3"],["ENDERECO","Endereço","c4"],
  ["CIDADE","Cidade","c2"],["ESTADO","UF","c1"],["CEP","CEP","c2"],["TELEFONE","Telefone","c3"],["EMAIL","E-mail","c3"]];
var socioList=[];

function el(id){return document.getElementById(id);}
function esc(s){return (s==null?"":String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

function socioHTML(i,s){
  s=s||{};
  var f=SOCIO_FIELDS.map(function(fd){
    var opts= fd[0]=="POSICAO" ? ' list="posl"' : '';
    return '<div class="f '+fd[2]+'"><label>'+fd[1]+'</label><input data-si="'+i+'" data-sk="'+fd[0]+'"'+opts+' value="'+esc(s[fd[0]]||"")+'"></div>';
  }).join("");
  return '<div class="socio"><div class="head"><b style="color:#444D56">Sócio '+(i+1)+'</b>'+
    '<label class="chk"><input type="checkbox" data-si="'+i+'" data-sk="GERENTE" '+(s.GERENTE?'checked':'')+'> autorizado a gerenciar (assina)</label>'+
    '<span style="flex:1"></span><button class="btn s sm" onclick="delSocio('+i+')">remover</button></div>'+
    '<div class="grid">'+f+'</div></div>';
}
function renderSocios(){
  el("socios").innerHTML='<datalist id="posl"><option>Managing Member</option><option>Member</option></datalist>'+
    socioList.map(function(s,i){return socioHTML(i,s);}).join("");
}
function collectSocios(){
  document.querySelectorAll('[data-si]').forEach(function(inp){
    var i=+inp.getAttribute('data-si'),k=inp.getAttribute('data-sk');
    if(!socioList[i])socioList[i]={};
    socioList[i][k]= inp.type=="checkbox"?inp.checked:inp.value;
  });
}
function addSocio(){collectSocios();socioList.push({});renderSocios();}
function delSocio(i){collectSocios();socioList.splice(i,1);renderSocios();}

var FIELDS=["LLC_NAME","LLC_NAME_ALT","STATE","ENTITY_TYPE","OFFSHORE","BUSINESS_PURPOSE",
"PRINCIPAL_ADDRESS","PRINCIPAL_CITY","PRINCIPAL_STATE","PRINCIPAL_ZIP","USE_ATHENA_ADDR",
"CONTACT_NAME","CONTACT_PHONE","CLIENT_EMAIL","AUTHORITY_MODE","DUAL_THRESHOLD_USD",
"TAX_CLASSIFICATION","TAX_YEAR","ACCOUNTING_METHOD","ABERTURA_DATA","ARTICLES_FILED_DATE",
"AGREEMENT_DATE","CONTRIBUTION_DUE_DATE","EIN","SERVICED_BY","REGISTERED_AGENT",
"REGISTERED_AGENT_ADDRESS","AGENT_CITY","AGENT_STATE","AGENT_ZIP","MAILBOX_FEE_USD",
"MAILBOX_PERIOD","MAILBOX_VALID_UNTIL",
"MANAGEMENT","MANAGER_NAME","SUNBIZ_NUMBER","EIN_ISSUED","CERT_STATUS_INCLUDED","MAILBOX_HIRED",
"RE_APPROVAL","CLIENT_CONFIRM"];
function collect(){
  collectSocios();
  var d={};FIELDS.forEach(function(k){var e=el(k);if(!e)return;d[k]=e.type=="checkbox"?e.checked:e.value;});
  d.socios=socioList.map(function(s){return Object.assign({},s);});
  return d;
}
function fill(d){
  FIELDS.forEach(function(k){var e=el(k);if(!e||d[k]==null)return;if(e.type=="checkbox")e.checked=!!d[k];else e.value=d[k];});
  socioList=(d.socios&&d.socios.length)?d.socios:[{}];renderSocios();
}

/* ---------- número por extenso ---------- */
var ONES=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
var TENS=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];
function words(n){n=Math.round(+n||0);if(n==100)return"ONE HUNDRED";var s;if(n<20)s=ONES[n];else{var t=Math.floor(n/10),o=n%10;s=TENS[t]+(o?"-"+ONES[o]:"");}return s.toUpperCase();}

/* ---------- validação ---------- */
function validate(d){
  var out=[];
  function row(lbl,st,det){out.push({lbl:lbl,st:st,det:det||""});}
  var soc=(d.socios||[]).filter(function(s){return (s.NOME||"").trim();});
  var sum=soc.reduce(function(a,s){return a+(parseFloat(s.PERCENT)||0);},0);
  var ger=soc.filter(function(s){return s.GERENTE;}).length;
  row("Nome da empresa", d.LLC_NAME?"OK":"ERRO", d.LLC_NAME||"");
  row("Estado", d.STATE?"OK":"ERRO", d.STATE||"");
  row("Data de abertura", d.ABERTURA_DATA?"OK":"ERRO", d.ABERTURA_DATA||"");
  row("Agente registrador", d.REGISTERED_AGENT?"OK":"ERRO","");
  row("Nº de sócios", soc.length>0?"OK":"ERRO", soc.length+" sócio(s)");
  row("Soma das participações = 100%", Math.abs(sum-100)<0.01?"OK":"ERRO","soma = "+sum+"%");
  row("Pelo menos 1 sócio que assina", ger>=1?"OK":"ERRO", ger+" gerente(s)");
  var cls=(d.TAX_CLASSIFICATION||"");
  var clsok = !((soc.length==1&&cls=="PARTNERSHIP")||(soc.length>1&&cls=="DISREGARDED ENTITY"));
  row("Classificação x nº de sócios", clsok?"OK":"REVISAR", "1→Disregarded · 2+→Partnership. Atual: "+cls);
  row("EIN", d.EIN?"OK":"PENDENTE", d.EIN||"emitir/anexar depois");
  return out;
}
function renderVal(){
  var d=collect(),v=validate(d);
  el("valpanel").innerHTML="<h4>Conferência</h4>"+v.map(function(x){
    var cls=x.st=="OK"?"ok":(x.st=="ERRO"?"err":"warn");
    return '<div class="v"><span class="pill '+cls+'">'+x.st+'</span> '+esc(x.lbl)+
      (x.det?' <span style="color:#6B7785">— '+esc(x.det)+'</span>':'')+'</div>';
  }).join("");
  return v;
}

/* ---------- helpers de documento ---------- */
function addr(s){return [s.ENDERECO,s.CIDADE,s.ESTADO,s.CEP].filter(Boolean).join(", ");}
function role(s){return s.GERENTE?"AUTHORIZED MEMBER":"MEMBER ONLY";}
function princ(d){return [d.PRINCIPAL_ADDRESS,d.PRINCIPAL_CITY,d.PRINCIPAL_STATE,d.PRINCIPAL_ZIP].filter(Boolean).join(", ");}
function agent(d){return [d.REGISTERED_AGENT_ADDRESS,d.AGENT_CITY,d.AGENT_STATE,d.AGENT_ZIP].filter(Boolean).join(", ");}
function lh(d){return '<div class="lhband"><img src="'+LOGO+'" alt="Athena">'+
  '<div class="lhr">7680 Universal Blvd, Ste 100 · Orlando, FL 32819<br>(407) 777-2501 · manager@athenataxadvisors.com'+
  (d.SUNBIZ_NUMBER?'<br>SunBiz Doc.: '+esc(d.SUNBIZ_NUMBER):'')+'</div></div>';}
function foot(d){return '<div style="border-top:1px solid #ddd;margin-top:14px;padding-top:5px;font-size:8px;color:#9098a1;text-align:center">'+
  esc(d.LLC_NAME)+(d.SUNBIZ_NUMBER?' · SunBiz '+esc(d.SUNBIZ_NUMBER):'')+' · CONFIDENTIAL · Athena Business &amp; Tax Advisors</div>';}
function sig(list){return list.map(function(s){return '<div class="sig">Signature: __________________________________<br><b>Printed Name: '+esc(s.NOME)+'</b> <span style="color:#6B7785">('+role(s)+')</span></div>';}).join("");}

/* ---------- os documentos ---------- */
function coverIndex(d){
  var it=[];
  it.push(d.EIN_ISSUED=="SIM"?"EIN (CP-575)":"EIN — a emitir");
  it.push("SunBiz Page (Articles of Organization)");
  if(d.CERT_STATUS_INCLUDED=="SIM") it.push("Certificate of Status");
  it.push("Operating Agreement","Statement of Authority","Membership Ledger","Membership Certificates");
  if(d.MAILBOX_HIRED=="SIM") it.push("Mailbox Agreement");
  var extra = d.CERT_STATUS_INCLUDED!="SIM" ? '<br><span style="color:#6B7785;font-size:9px">(Certificate of Status é opcional na Flórida — não incluído neste pacote)</span>' : '';
  return it.map(function(x){return '• '+esc(x);}).join('<br>') + extra;
}
function docCapa(d,soc){
  var taxdl = d.TAX_CLASSIFICATION=="PARTNERSHIP" ? "Form 1065 + K-1 (IRC §6698)"
    : (d.TAX_CLASSIFICATION=="S-CORPORATION"?"Form 1120-S":(d.TAX_CLASSIFICATION=="C-CORPORATION"?"Form 1120":"na declaração do sócio (disregarded)"));
  return '<div class="doc">'+lh(d)+
   '<p class="ctr gold" style="font-size:12px">BUSINESS PACKAGE</p>'+
   '<p class="ctr" style="color:#6B7785">DOCUMENTS OF</p>'+
   '<h1>'+esc(d.LLC_NAME)+'</h1>'+
   '<p class="ctr" style="font-style:italic;color:#6B7785">A '+esc(d.STATE)+' Limited Liability Company'+(d.SUNBIZ_NUMBER?' · SunBiz '+esc(d.SUNBIZ_NUMBER):'')+'</p>'+
   '<h2>Conteúdo do pacote</h2>'+
   '<p>'+coverIndex(d)+'</p>'+
   '<h2>Obrigações após a abertura</h2>'+
   '<p>Annual Report: 1º jan – 1º maio (multa US$ 400 — valor estadual fixo). Imposto federal: '+taxdl+' — prazos e multas conforme o ano-calendário; confirmar o valor vigente no IRS.</p>'+
   '<p style="font-size:9px;color:#6B7785;font-style:italic">A Athena Business &amp; Tax Advisors é contabilidade e não presta serviços jurídicos.</p>'+foot(d)+'</div>';
}
function docOA(d,soc){
  var reo=(d.RE_APPROVAL||"MAJORITY");
  function rb(v){return reo===v?"[ X ]":"[&nbsp;&nbsp;&nbsp;&nbsp; ]";}
  var managerMgd = d.MANAGEMENT=="MANAGER-MANAGED";
  var title = managerMgd ? "Operating Agreement for A Manager-Managed Limited Liability Company"
                         : "Operating Agreement for A Member-Managed Limited Liability Company";
  var mgmtClause = managerMgd
    ? '3. Management: This LLC shall be managed by the following manager(s), designated by the authorized members: '+esc(d.MANAGER_NAME||"(designar)")+'. The members of this company are the ones listed below:'
    : '3. Management: This LLC shall be managed by all of its members. The members of this company are the ones listed below:';
  var memBlocks=soc.map(function(s){return '<p style="margin:4px 0">Name: '+esc(s.NOME)+'<br>Address: '+esc(s.ENDERECO)+'<br>'+esc([s.CIDADE,s.ESTADO,s.CEP].filter(Boolean).join(", "))+'<br>'+role(s)+'</p>';}).join("");
  var capRows='<table><tr><th>Name</th><th>Contribution</th><th>Fair Market Value</th><th>Percentage Interest in LLC</th></tr>'+
    soc.map(function(s){return '<tr><td>'+esc(s.NOME)+'</td><td>CASH</td><td>'+(String(s.APORTE||"").trim()?('$'+esc(s.APORTE)):'')+'</td><td>'+esc(s.PERCENT)+'%</td></tr>';}).join("")+'</table>';
  var sigs=soc.map(function(s){return '<div class="sig">Signature: ______________________________________________<br>Printed Name: <b>'+esc(s.NOME)+'</b><br>'+role(s)+'</div>';}).join("");
  return '<div class="doc">'+lh(d)+
   '<h1>'+esc(d.LLC_NAME)+'</h1>'+
   '<p class="ctr" style="font-style:italic;color:#6B7785">'+title+'</p>'+
   '<h2>I. Preliminary Provisions</h2>'+
   '<p>1. FORMATION. The members hereby form a limited liability company (“company”) subject to the provisions of the limited liability company act as currently in effect as of '+esc(d.ABERTURA_DATA)+'. The articles of organization were filed with the filing office of the state of '+esc(d.STATE)+' on '+esc(d.ARTICLES_FILED_DATE)+'.</p>'+
   '<p>2. NAME. The name of the company shall be: '+esc(d.LLC_NAME)+'</p>'+
   '<p>3. PRINCIPAL PLACE OF BUSINESS. The location of the principal place of business of the Company shall be: '+esc(princ(d))+'</p>'+
   '<p>3.1. MAILING ADDRESS. The mailing address of the Company shall be: '+esc(d.MAILING_ADDRESS||princ(d))+'</p>'+
   '<p>4. Name: The formal name of this LLC is as stated above. However, this LLC may do business under a different name by complying with the state’s fictitious or assumed business name statutes and procedures.</p>'+
   '<p>5. Registered Office and Agent: The registered office of this LLC and the registered agent at this address are as follows: '+esc(d.REGISTERED_AGENT)+', located at '+esc(agent(d))+'. The registered office and agent may be changed from time to time as the members may see fit, by filing a change of registered agent or office form with the state LLC filing office.</p>'+
   '<p>6. Business Purposes: The specific business purposes and activities contemplated by the founders of this LLC at the time of initial signing of this agreement consist of the following: '+esc(d.BUSINESS_PURPOSE)+'.</p>'+
   '<p>It is understood that the foregoing statement of purposes shall not serve as a limitation on the powers or abilities of this LLC, which shall be permitted to engage in any and all lawful business activities. If this LLC intends to engage in business activities outside the state of its formation that require the qualification of the LLC in other states, it shall obtain such qualification before engaging in such out-of-state activities.</p>'+
   '<p>7. Duration of LLC: The duration of this LLC shall be PERPETUAL.</p>'+
   '<p>Further, this LLC shall terminate when a proposal to dissolve the LLC is adopted by the membership of this LLC or when this LLC is otherwise terminated in accordance with law.</p>'+
   '<h2>II. Membership Provisions</h2>'+
   '<p>1. Nonliability of Members: No member of this LLC shall be personally liable for the expenses, debts, obligations, or liabilities of the LLC, or for claims made against it.</p>'+
   '<p>2. Reimbursement for Organizational Costs: Members shall be reimbursed by the LLC for organizational expenses paid by the members. The LLC shall be authorized to elect to deduct and amortize organizational expenses and start-up expenditures as permitted by the Internal Revenue Code and as may be advised by the LLC’s tax adviser.</p>'+
   '<p>'+mgmtClause+'</p>'+memBlocks+
   '<p>4. Members’ Percentage Interests: Each member’s percentage interest in this LLC is fixed as set forth in Article IV (Capital Provisions) of this agreement and shall be expressed as a percentage, called each member’s “percentage interest” in this LLC. A member’s percentage interest shall not fluctuate with the balance of the member’s capital account, and may be changed only by a written amendment to this agreement signed by all members or upon an admission, withdrawal, or transfer effected in accordance with this agreement.</p>'+
   '<p>5. Membership Voting: Except as otherwise may be required by the articles of organization, certificate of formation, or a similar organizational document, by other provisions of this operating agreement, or under the laws of this state, each member shall vote on any matter submitted to the membership for approval in proportion to the member’s percentage interest in this LLC. Further, unless defined otherwise for a particular provision of this operating agreement, the phrase “majority of members” means the vote of members whose combined votes equal more than 50% of the votes of all members in this LLC, and a majority of members, so defined, may approve any item of business brought before the membership for a vote unless a different vote is required under this operating agreement or state law.</p>'+
   '<p>6. Compensation: Members shall not be paid as members of the LLC for performing any duties associated with such membership, including management of the LLC. Members may be paid, however, for any services rendered in any other capacity for the LLC, whether as officers, employees, independent contractors, or otherwise.</p>'+
   '<p>7. Members’ Meetings: The LLC shall not provide for regular members’ meetings. However, any member may call a meeting by communicating his or her wish to schedule a meeting to all other members. Such notification may be in person or in writing, or by telephone, facsimile machine, or other form of electronic communication reasonably expected to be received by a member, and the other members shall then agree, either personally, in writing, or by telephone, facsimile machine, or other form of electronic communication to the member calling the meeting, to meet at a mutually acceptable time and place. Notice of the business to be transacted at the meeting need not be given to members by the member calling the meeting, and any business may be discussed and conducted at the meeting.</p>'+
   '<p>If all members cannot attend a meeting, it shall be postponed to a date and time when all members can attend, unless all members who do not attend have agreed in writing to the holding of the meeting without them. If a meeting is postponed, and the postponed meeting cannot be held either because all members do not attend the postponed meeting or the nonattending members have not signed a written consent to allow the postponed meeting to be held without them, a second postponed meeting may be held at a date and time announced at the first postponed meeting. The date and time of the second postponed meeting shall also be communicated to any members not attending the first postponed meeting. The second postponed meeting may be held without the attendance of all members as long as a majority of the percentage interests of the membership of this LLC is in attendance at the second postponed meeting. Written notice of the decisions or approvals made at this second postponed meeting shall be mailed or delivered to each nonattending member promptly after the holding of the second postponed meeting.</p>'+
   '<p>Written minutes of the discussions and proposals presented at a members’ meeting, and the votes taken and matters approved at such meeting, shall be taken by one of the members or a person designated at the meeting. A copy of the minutes of the meeting shall be placed in the LLC’s records book after the meeting.</p>'+
   '<p>8. Membership Certificates: This LLC shall be authorized to obtain and issue certificates representing or certifying membership interests in this LLC. Each certificate shall show the name of the LLC and the name of the member, and state that the person named is a member of the LLC and is entitled to all the rights granted members of the LLC under the articles of organization, certificate of formation, or a similar organizational document; this operating agreement; and provisions of law. Each membership certificate shall be consecutively numbered and signed by one or more officers of this LLC. The certificates shall include any additional information considered appropriate for inclusion by the members on membership certificates.</p>'+
   '<p>In addition to the above information, all membership certificates shall bear a prominent legend on their face or reverse side stating, summarizing, or referring to any transfer restrictions that apply to memberships in this LLC under the articles of organization, certificate of formation, or a similar organizational document, and/or this operating agreement, as well as the address where a member may obtain a copy of these restrictions upon request from this LLC.</p>'+
   '<p>The records book of this LLC shall contain a list of the names and addresses of all persons to whom certificates have been issued, show the date of issuance of each certificate, and record the date of all cancellations or transfers of membership certificates.</p>'+
   '<p>9. Other Business by Members: There is no restriction for members to own an interest in, manage, or work for other businesses, enterprises, or similar endeavors. However, it is an obligation of every member of the company to provide the maximum effort to accomplish this LLC’s business goals, profitability, productivity, and performance in managing the business of this LLC.</p>'+
   '<h2>III. Tax and Financial Provisions</h2>'+
   '<p>1. Tax Classification of LLC: The members of this LLC intend that this LLC be initially classified as a '+esc(d.TAX_CLASSIFICATION)+' for federal and, if applicable, state income tax purposes. It is understood that, subject to federal and state law requirements, all members may agree to change the tax treatment of this LLC by signing, or authorizing the signature of, IRS Form 8832, Entity Classification Election, and filing it with the IRS and, if applicable, the state tax department within the prescribed time limits.</p>'+
   '<p>2. Tax Year and Accounting Method: The tax year of this LLC shall be '+esc(d.TAX_YEAR)+'. The LLC shall use the '+esc(d.ACCOUNTING_METHOD)+' method of accounting. Both the tax year and the accounting period of the LLC may be changed with the consent of all members if the LLC qualifies for such change, and may be effected by the filing of appropriate forms with the IRS and state tax authorities.</p>'+
   '<p>3. Partnership Representative: If this LLC is subject to the centralized partnership audit regime enacted by the Bipartisan Budget Act of 2015, it shall designate a “Partnership Representative” (and, if required, a designated individual) in accordance with Internal Revenue Code Section 6223 and corresponding regulations, who will be the spokesperson for the LLC in dealings with the IRS and will report to the members on the progress and outcome of these dealings. Where eligible, the LLC may elect out of the centralized audit regime under Internal Revenue Code Section 6221(b) for any tax year.</p>'+
   '<p>4. Annual Income Tax Returns and Reports: Within 60 days after the end of each tax year of the LLC, a copy of the LLC’s state and federal income tax returns for the preceding tax year shall be mailed or otherwise provided to each member of the LLC, together with any additional information and forms necessary for each member to complete his or her individual state and federal income tax returns. If this LLC is classified as a partnership for income tax purposes, this additional information shall include a federal (and, if applicable, state) Schedule K-1 (Form 1065, Partner’s Share of Income, Deductions, Credits, etc.) or equivalent income tax reporting form. This additional information shall also include a financial report, which shall include a balance sheet and profit and loss statement for the prior tax year of the LLC.</p>'+
   '<p>5. Bank Accounts: The LLC shall designate one or more banks or other institutions for the deposit of the funds of the LLC, and shall establish savings, checking, investment, and other such accounts as are reasonable and necessary for its business and investments. One or more members of the LLC shall be designated with the consent of all members to deposit and withdraw funds of the LLC, and to direct the investment of funds from, into, and among such accounts. The funds of the LLC, however and wherever deposited or invested, shall not be commingled with the personal funds of any members of the LLC.</p>'+
   '<p>6. Title to Assets: All personal and real property of this LLC shall be held in the name of the LLC, not in the names of individual members.</p>'+
   '<h2>IV. Capital Provisions</h2>'+
   '<p>1. Capital Contributions by Members: Members shall make the following contributions of cash, property, or services; unless otherwise noted, cash and property are paid or delivered to the LLC on or by '+esc(d.CONTRIBUTION_DUE_DATE)+'. The fair market values of items of property or services are as agreed between the LLC and the contributing member. The percentage interest in the LLC that each member shall receive in return for his or her capital contribution is also indicated for each member below.</p>'+capRows+
   '<p>2. Additional Contributions by Members: The members may agree, from time to time by unanimous vote, to require the payment of additional capital contributions by the members, on or by a mutually agreeable date.</p>'+
   '<p>3. Failure to Make Contributions: If a member fails to make a required capital contribution within the time agreed for a member’s contribution, the remaining members may, by unanimous vote, agree to reschedule the time for payment of the capital contribution by the late-paying member, setting any additional repayment terms, such as a late payment penalty, rate of interest to be applied to the unpaid balance, or other monetary amount to be paid by the delinquent member, as the remaining members decide. Alternatively, the remaining members may, by unanimous vote, agree to cancel the membership of the delinquent member, provided any prior partial payments of capital made by the delinquent member are refunded by the LLC to the member promptly after the decision is made to terminate the membership of the delinquent member.</p>'+
   '<p>4. No Interest on Capital Contributions: No interest shall be paid on funds or property contributed as capital to this LLC, or on funds reflected in the capital accounts of the members.</p>'+
   '<p>5. Capital Account Bookkeeping: A capital account shall be set up and maintained on the books of the LLC for each member. It shall reflect each member’s capital contribution to the LLC, increased by each member’s share of profits in the LLC, decreased by each member’s share of losses and expenses of the LLC, and adjusted as required in accordance with applicable provisions of the Internal Revenue Code and corresponding income tax regulations.</p>'+
   '<p>6. Consent to Capital Contribution Withdrawals and Distributions: Members shall not be allowed to withdraw any part of their capital contributions or to receive distributions, whether in property or cash, except as otherwise allowed by this agreement and, in any case, only if such withdrawal is made with the written consent of all members.</p>'+
   '<p>7. Allocations of Profits and Losses: No member shall be given priority or preference with respect to other members in obtaining a return of capital contributions, distributions, or allocations of the income, gains, losses, deductions, credits, or other items of the LLC. The profits and losses of the LLC, and all items of its income, gain, loss, deduction, and credit shall be allocated to members according to each member’s percentage interest in this LLC.</p>'+
   '<p>8. Allocation and Distribution of Cash to Members: Cash from LLC business operations, as well as cash from a sale or other disposition of LLC capital assets, may be distributed from time to time to members in accordance with each member’s percentage interest in the LLC, as may be decided by a majority of the members.</p>'+
   '<p>9. Allocation of Noncash Distributions: If proceeds consist of property other than cash, the members shall decide the value of the property and allocate such value among the members in accordance with each member’s percentage interest in the LLC. If such noncash proceeds are later reduced to cash, such cash may be distributed among the members as otherwise provided in this agreement.</p>'+
   '<p>10. Allocation and Distribution of Liquidation Proceeds: Regardless of any other provision in this agreement, if there is a distribution in liquidation of this LLC, or when any member’s interest is liquidated, all items of income and loss shall be allocated to the members’ capital accounts, and all appropriate credits and deductions shall then be made to these capital accounts before any final distribution is made. A final distribution shall be made to members only to the extent of, and in proportion to, any positive balance in each member’s capital account.</p>'+
   '<h2>V. Membership Withdrawal and Transfer Provisions</h2>'+
   '<p>1. Withdrawal of Members: A member may withdraw from this LLC by giving written notice to all other members at least THIRTY days before the date the withdrawal is to be effective.</p>'+
   '<p>2. Restrictions on the Transfer of Membership: A member may not transfer his or her membership in the LLC to another member without the approval of other members. A member shall not transfer his or her membership in the LLC to a non-member unless all non-transferring members in the LLC first agree to approve the admission of the transferee into this LLC. Further, no member may encumber a part or all of his or her membership in the LLC by mortgage, pledge, granting of a security interest, or otherwise, unless the encumbrance has first been approved in writing by all other members of the LLC.</p>'+
   '<p>3. Death of Member. Commencing upon the death of a Member, the surviving Members shall for a period of ninety (90) days have the option to purchase all or any portion of the deceased Member’s Membership Interest at Fair Value (determined as of the date of the death of the Member); provided, however, the exercise of said option shall require the approval of the unanimous consent of the surviving Members. Upon the expiration of ninety (90) days after the death of a Member, the Company shall be obligated to purchase all, and not less than all, of the deceased Member’s Membership Interest at fair value determined by the members and an accountant, which the surviving Members do not elect to purchase pursuant to the option granted in the preceding sentence. The representative of the deceased Member (which may include spouse and executors or administrators of the deceased Member) shall sell all of the deceased Member’s Membership Interest to the Company and/or the other Members in accordance with the option or obligation established by this paragraph. This buy-sell procedure shall govern the death of a Member, and the death of a Member shall not by itself cause the dissolution of the LLC.</p>'+
   '<p>4. Member Wishes to Sell Membership Interest. If a Member wishes to sell all or a portion of the Member’s interest in the Company, the Company shall for a period of thirty (30) days have the option to purchase all or any portion of the Member’s Membership Interest at Fair Value (determined as of the date of offer to sell by Member); provided, however, the exercise of said option shall require the approval of the unanimous consent of the other Members. Upon the expiration of thirty (30) days after the offer to sell by a Member, if the Company fails to exercise the option to purchase, the selling Member may sell his interest in the Company to other Members or a third party, subject to a unanimous vote of all Members.</p>'+
   '<h2>VI. Dissolution Provisions</h2>'+
   '<p>1. Events That Trigger Dissolution of the LLC: The following events shall trigger a dissolution of the LLC, except as provided:</p>'+
   '<p>(a) the death, incapacity, bankruptcy, retirement, resignation, or expulsion of a member; provided that the buy-sell provisions of Article V shall govern the death, withdrawal, or dissociation of a member, and within THIRTY DAYS of the happening of any of these events all remaining members of the LLC may vote to continue the legal existence of the LLC, in which case the LLC shall not dissolve;</p>'+
   '<p>(b) the expiration of the term of existence of the LLC if such term is specified in the articles of organization, certificate of formation, or a similar organizational document, or this operating agreement;</p>'+
   '<p>(c) the written agreement of all members to dissolve the LLC; or</p>'+
   '<p>(d) entry of a decree of dissolution of the LLC under state law.</p>'+
   '<h2>VII. General Provisions</h2>'+
   '<p>1. Officers: The LLC may designate one or more officers, such as a president, vice president, secretary, and treasurer, CEO, General Manager, Operations Manager, etc. Persons who fill these positions need not be members of the LLC. Such positions may be compensated or non-compensated according to the nature and extent of the services rendered for the LLC as a part of the duties of each office. Ministerial services only as a part of any officer position will normally not be compensated, such as the performance of officer duties specified in this agreement, but any officer may be reimbursed by the LLC for out-of-pocket expenses paid by the officer in carrying out the duties of his or her office.</p>'+
   '<p>2. Records: The LLC shall keep at its principal business address a copy of all proceedings of membership meetings, as well as books of account of the LLC’s financial transactions. A list of the names and addresses of the current membership of the LLC also shall be maintained at this address, with notations on any transfers of members’ interests to nonmembers or persons being admitted into membership in the LLC. Copies of the LLC’s articles of organization; a signed copy of this operating agreement; and the LLC’s tax returns for the preceding three tax years shall be kept at the principal business address of the LLC. Any member may inspect any and all records maintained by the LLC upon reasonable notice to the LLC. Copying of the LLC’s records by members is allowed, but copying costs shall be paid for by the requesting member.</p>'+
   '<p>3. Disposition of Real Estate: A decision to sell, convey, gift, mortgage, grant a security interest in, exchange, and otherwise encumber or dispose of all or a part of LLC real estate equities shall be taken by:</p>'+
   '<p style="margin-left:16px">'+rb("ALL")+' All LLC members COLLECTIVELY<br>'+
     rb("ANY")+' Any LLC member<br>'+
     rb("MAJORITY")+' The majority of members interested</p>'+
   '<p>and shall be registered in an appropriate Minute of Meeting that shall also designate a member and/or officer to represent the LLC in the transaction.</p>'+
   '<p>4. All Other Necessary Acts: The members and officers of this LLC are authorized to perform all acts necessary to perfect the organization of this LLC and to carry out its business operations expeditiously and efficiently. The secretary of the LLC, or other officers, or any member of the LLC, may certify to other businesses, financial institutions, and individuals as to the authority of one or more members or officers of this LLC to transact specific items of business on behalf of the LLC.</p>'+
   '<p>5. Mediation and Arbitration of Disputes Among Members: In any dispute over the provisions of this operating agreement and in other disputes among the members, if the members cannot resolve the dispute to their mutual satisfaction, the matter shall be submitted to mediation. The terms and procedure for mediation shall be arranged by the parties to the dispute.</p>'+
   '<p>If good-faith mediation of a dispute proves impossible or if an agreed-upon mediation outcome cannot be obtained by the members who are parties to the dispute, the dispute shall be submitted to binding arbitration in accordance with the rules of the American Arbitration Association. Any party may commence arbitration of the dispute by sending a written request for arbitration to all other parties to the dispute. All parties shall initially share the cost of arbitration, but the prevailing party or parties may be awarded attorneys’ fees, costs, and other expenses of arbitration. All arbitration decisions shall be final, binding, and conclusive on all the parties to arbitration, and legal judgment may be entered based upon such decision in accordance with applicable law in any court having jurisdiction to do so.</p>'+
   '<p>6. Entire Agreement: This operating agreement represents the entire agreement among the members of this LLC, and it shall not be amended, modified, or replaced except by a written instrument executed by all the parties to this agreement who are current members of this LLC as well as any and all additional parties who became members of this LLC after the adoption of this agreement. This agreement replaces and supersedes all prior written and oral agreements among any and all members of this LLC.</p>'+
   '<p>7. Severability: If any provision of this agreement is determined by a court or arbitrator to be invalid, unenforceable, or otherwise ineffective, that provision shall be severed from the rest of this agreement, and the remaining provisions shall remain in effect and enforceable.</p>'+
   '<h2>VIII. Signatures of Members</h2>'+
   '<p>1. Execution of Agreement: In witness whereof, the members of this LLC sign and adopt this agreement as the operating agreement of this LLC.</p>'+
   '<p>Date: '+esc(d.AGREEMENT_DATE)+'</p>'+sigs+foot(d)+'</div>';
}
function docAuth(d,soc){
  var dual=d.AUTHORITY_MODE=="DUAL",thr=d.DUAL_THRESHOLD_USD||"";
  var body=dual?
   'AUTHORITY (DUAL-CONTROL): Each Authorized Member may sign in the ordinary course up to US$ '+esc(thr)+'. Transactions at or above US$ '+esc(thr)+', including borrowing and any purchase, sale, or encumbrance of real property, require TWO Authorized Members.'
   :'AUTHORITY (SINGLE-SIGNER): Each Authorized Member is authorized to open bank accounts, buy and sell property, and sign checks, withdrawals, contracts, and any other document on behalf of the Company. The signature of one Authorized Member is sufficient.';
  var auth=soc.filter(function(s){return s.GERENTE;});
  return '<div class="doc">'+lh(d)+
   '<h1>STATEMENT OF AUTHORITY</h1><p class="ctr gold" style="font-size:12px">of '+esc(d.LLC_NAME)+'</p>'+
   '<p class="ctr" style="font-size:9px;color:#6B7785;font-style:italic">(Autorização interna de signatários — não é o Certificate of Authority de LLC estrangeira, §605.0902)</p>'+
   '<p>The members state the authority of the following persons to act for the Company:</p>'+
   auth.map(function(s){return '<p>• '+esc(s.NOME)+' — '+esc(addr(s))+' — '+role(s)+'</p>';}).join("")+
   '<p>'+body+'</p>'+
   '<p style="font-style:italic">Consistent with, and subject to, the Operating Agreement. Third parties may rely on it until superseded. Date: '+esc(d.ABERTURA_DATA)+'.</p>'+
   sig(auth)+foot(d)+'</div>';
}
function docLedger(d,soc){
  var rows=soc.map(function(s,i){return '<tr><td>'+(i+1)+'</td><td>'+esc(s.NOME)+'</td><td>'+esc(d.ABERTURA_DATA)+'</td><td>'+esc(d.ABERTURA_DATA)+'</td><td>'+esc(s.PERCENT)+'%</td></tr>';}).join("");
  return '<div class="doc">'+lh(d)+
   '<h1 style="font-size:16px">INTEREST CERTIFICATE LEDGER</h1><p class="ctr" style="font-weight:bold;color:#444D56">'+esc(d.LLC_NAME)+'</p>'+
   '<table><tr><th>No.</th><th>Name of Member</th><th>Effective Date</th><th>Date of Cert.</th><th>Interests</th></tr>'+rows+'</table>'+
   sig(soc)+foot(d)+'</div>';
}
function docCerts(d,soc){
  return '<div class="doc">'+lh(d)+ soc.map(function(s,i){
    return '<div class="cert"><div class="gold">CERTIFICATE No. 0'+(i+1)+'</div>'+
     '<h1 style="margin:4px 0">MEMBERSHIP CERTIFICATE</h1>'+
     '<div style="font-weight:bold;color:#444D56;font-size:15px">'+esc(d.LLC_NAME)+'</div>'+
     '<p>This certifies that</p><div class="big">'+esc(s.NOME)+'</div>'+
     '<p>holds a membership interest of</p><div class="pct">'+esc(s.PERCENT)+'%  ('+words(s.PERCENT)+' PERCENT)</div>'+
     '<p style="font-size:10px">subject to the Operating Agreement. Issued on '+esc(d.ABERTURA_DATA)+', Orlando, Florida.</p>'+
     '<p>______________________   ______________________<br><span style="font-size:9px;color:#6B7785">Authorized Member &nbsp;&nbsp;&nbsp; Authorized Member</span></p></div>';
  }).join("")+foot(d)+'</div>';
}
function docMailbox(d,soc){
  return '<div class="doc">'+lh(d)+
   '<h1 style="font-size:15px">CONTRATO DE SERVIÇOS DE CAIXA POSTAL</h1>'+
   '<p><b>Empresa:</b> '+esc(d.LLC_NAME)+' &nbsp; <b>E-mail:</b> '+esc(d.CLIENT_EMAIL)+' &nbsp; <b>Telefone:</b> '+esc(d.CONTACT_PHONE)+'</p>'+
   '<p><b>Endereço:</b> '+esc(princ(d))+'</p>'+
   '<p>CLÁUSULA I — Prestação de serviços de Caixa Postal pela Athena Business and Tax Advisors ao cliente acima.</p>'+
   '<p>CLÁUSULA II — O Cliente não utilizará os serviços para fins ilegais ou proibidos pelas normas postais dos EUA.</p>'+
   '<p>CLÁUSULA III — Valor de US$ '+esc(d.MAILBOX_FEE_USD)+',00, referente ao período de '+esc(d.MAILBOX_PERIOD)+', pago no ato da assinatura.</p>'+
   '<p>CLÁUSULA IV — Vigência por '+esc(d.MAILBOX_PERIOD)+', válido até '+esc(d.MAILBOX_VALID_UNTIL)+' (coincide com o período pago). Renovação por novo acordo e pagamento.</p>'+
   '<p class="note">Correção: período pago = vigência (vindos da ficha).</p>'+
   '<p>CLÁUSULA V — Autoriza a Athena a abrir correspondências e descartar propaganda/spam.</p>'+
   '<p>CLÁUSULA VI — Não é permitido encomendas volumosas; apenas cartas e documentos, sem armazenamento físico.</p>'+
   '<p>CLÁUSULA VII — Correspondência digitalizada e enviada ao e-mail; mediante solicitação, encaminhamento físico (correio) ao endereço registrado em até 24h.</p>'+
   '<p class="note">Correção: separado digitalização (e-mail) de encaminhamento físico (correio).</p>'+
   '<p style="margin-top:14px"><b>Assinatura:</b> __________________________ &nbsp; <b>Data:</b> ____/____/______</p>'+foot(d)+'</div>';
}

function docStock(d,soc){
  return soc.map(function(s,i){
    return '<div class="doc">'+lh(d)+
     '<div class="stockcert">'+
     '<div class="stocknum">NUMBER<br>0'+(i+1)+'</div>'+
     '<div class="stockint">INTEREST<br>'+esc(s.PERCENT)+'%</div>'+
     '<h1 class="ctr" style="margin-top:6px">'+esc(d.LLC_NAME)+'</h1>'+
     '<p class="ctr" style="font-size:9px;color:#6B7785;letter-spacing:1px">A '+esc(d.STATE)+' LIMITED LIABILITY COMPANY · INTEREST CERTIFICATE</p>'+
     '<p style="margin-top:22px">This Certifies That <b>'+esc(s.NOME)+'</b> is the owner of <b>'+words(s.PERCENT)+' PERCENT ('+esc(s.PERCENT)+'%)</b> Interest of the above named Limited Liability Company transferable only on the books of the Company by the holder hereof in person or by duly authorized Attorney upon surrender of this Certificate properly endorsed. The transfer of the Interest in this Limited Liability Company is subject to restrictions set forth in the Limited Liability Company Operating Agreement and the transfer of the related ownership rights may be effected only upon the unanimous consent of members or compliance with any procedure provided in the Operating Agreement.</p>'+
     '<p>In Witness Whereof, the said Limited Liability Company has caused this Certificate to be executed on its behalf by its duly authorized manager(s), member(s), officer(s) or agent(s), this '+esc(d.ABERTURA_DATA)+'.</p>'+
     '<div style="margin-top:30px;text-align:center">______________________________________<br><span style="font-size:9px;color:#6B7785">Authorized Member / Officer</span></div>'+
     '</div>'+foot(d)+'</div>';
  }).join("");
}
function docClientReview(d,soc){
  var confirmed = d.CLIENT_CONFIRM===true || d.CLIENT_CONFIRM==="true";
  var rows=soc.map(function(s){return '<tr><td>'+esc(s.NOME)+'</td><td>'+esc(s.PERCENT)+'%</td><td>'+(s.GERENTE?'Sim':'Não')+'</td></tr>';}).join("");
  function kv(k,v){return '<tr><td style="width:38%;color:#6B7785">'+k+'</td><td><b>'+esc(v||"—")+'</b></td></tr>';}
  return '<div class="doc">'+lh(d)+
   '<h1 style="font-size:17px">FICHA DE CONFERÊNCIA DO CLIENTE</h1>'+
   '<p class="ctr" style="font-size:9.5px;color:#6B7785">Revise os dados abaixo e confirme antes da emissão dos documentos.</p>'+
   '<h2>Dados da empresa</h2><table class="crev">'+
   kv("Nome da empresa (1)",d.LLC_NAME)+kv("Nome alternativo (2)",d.LLC_NAME_ALT)+
   kv("Estado / Tipo",(d.STATE||"")+" · "+(d.ENTITY_TYPE||""))+kv("Atividade",d.BUSINESS_PURPOSE)+
   kv("Endereço",princ(d))+kv("Agente registrador",d.REGISTERED_AGENT)+'</table>'+
   '<h2>Sócios</h2><table class="crev"><tr><th>Nome</th><th>% Particip.</th><th>Autorizado a gerenciar</th></tr>'+rows+'</table>'+
   '<h2>Decisões da empresa</h2><table class="crev">'+
   kv("Administração",d.MANAGEMENT)+kv("Autoridade p/ assinar",d.AUTHORITY_MODE+(d.AUTHORITY_MODE=="DUAL"?(" (US$ "+(d.DUAL_THRESHOLD_USD||"")+")"):""))+
   kv("Disposição de imóveis",({MAJORITY:"Maioria dos sócios",ALL:"Todos coletivamente",ANY:"Qualquer sócio"})[d.RE_APPROVAL||"MAJORITY"])+
   kv("Classificação tributária",d.TAX_CLASSIFICATION)+kv("Mailbox contratado",d.MAILBOX_HIRED)+'</table>'+
   '<div class="decl"><b>Declaração do cliente</b><br>'+
   '<p style="margin:6px 0"><span class="cb">'+(confirmed?"X":"&nbsp;")+'</span> Declaro que revisei as informações e decisões acima e as confirmo como corretas para a abertura da empresa.</p>'+
   '<p style="margin-top:18px">Assinatura do cliente: ______________________________________ &nbsp; Data: ____/____/______</p></div>'+
   foot(d)+'</div>';
}
function gen(){
  var d=collect();
  var v=renderVal();
  var errs=v.filter(function(x){return x.st=="ERRO";});
  var soc=(d.socios||[]).filter(function(s){return (s.NOME||"").trim();});
  var warn = errs.length? '<div class="doc" style="border:2px solid #FFC7CE"><b style="color:#9c2029">Atenção:</b> há '+errs.length+' item(ns) em ERRO na Conferência ('+errs.map(function(e){return esc(e.lbl);}).join(", ")+'). O pacote foi gerado mesmo assim para conferência — corrija antes de entregar.</div>':'';
  var out = docClientReview(d,soc)+docCapa(d,soc)+docOA(d,soc)+docAuth(d,soc)+docLedger(d,soc)+docStock(d,soc);
  if(d.MAILBOX_HIRED!="NAO") out += docMailbox(d,soc);
  el("docs").innerHTML = warn + out;
  el("docs").scrollIntoView({behavior:"smooth"});
}

/* ---------- tabs / persistência ---------- */
function tab(n){[1,2,3].forEach(function(i){el("t"+i).classList.toggle("show",i==n);el("n"+i).classList.toggle("active",i==n);});if(n==3)renderVal();}
function save(){localStorage.setItem("athena_bp",JSON.stringify(collect()));alert("Dados salvos neste navegador.");}
function expJSON(){var b=new Blob([JSON.stringify(collect(),null,2)],{type:"application/json"});var a=document.createElement("a");a.href=URL.createObjectURL(b);a.download=(el("LLC_NAME").value||"empresa")+"_dados.json";a.click();}
function impJSON(ev){var f=ev.target.files[0];if(!f)return;var r=new FileReader();r.onload=function(){try{fill(JSON.parse(r.result));}catch(e){alert("JSON inválido");}};r.readAsText(f);}

/* ---------- prefill Vivelle ---------- */
var DEMO={LLC_NAME:"VIVELLE LLC",STATE:"Florida",ENTITY_TYPE:"LLC",OFFSHORE:"NAO",
BUSINESS_PURPOSE:"ANY AND ALL LAWFUL BUSINESS",PRINCIPAL_ADDRESS:"7680 UNIVERSAL BLVD STE 100",
PRINCIPAL_CITY:"ORLANDO",PRINCIPAL_STATE:"FL",PRINCIPAL_ZIP:"32819",USE_ATHENA_ADDR:true,
CONTACT_NAME:"CAIO ANDRE MENEGAO",AUTHORITY_MODE:"SINGLE",DUAL_THRESHOLD_USD:"10000",
TAX_CLASSIFICATION:"PARTNERSHIP",TAX_YEAR:"CALENDAR YEAR",ACCOUNTING_METHOD:"CASH",
ABERTURA_DATA:"02/25/2026",ARTICLES_FILED_DATE:"02/25/2026",AGREEMENT_DATE:"02/25/2026",
CONTRIBUTION_DUE_DATE:"DECEMBER 31, 2026",EIN:"",REGISTERED_AGENT:"ATHENA BUSINESS AND TAX ADVISORS LLC",
REGISTERED_AGENT_ADDRESS:"7680 UNIVERSAL BLVD SUITE 100",AGENT_CITY:"ORLANDO",AGENT_STATE:"FL",AGENT_ZIP:"32819",
MAILBOX_FEE_USD:"380",MAILBOX_PERIOD:"JANEIRO A DEZEMBRO DE 2026",MAILBOX_VALID_UNTIL:"31/12/2026",
MANAGEMENT:"MEMBER-MANAGED",MANAGER_NAME:"",SUNBIZ_NUMBER:"",EIN_ISSUED:"NAO",CERT_STATUS_INCLUDED:"NAO",MAILBOX_HIRED:"SIM",RE_APPROVAL:"MAJORITY",CLIENT_CONFIRM:false,
socios:[
{POSICAO:"Managing Member",PERCENT:"50",APORTE:"50",NOME:"CAIO ANDRE MENEGAO",ENDERECO:"5197 VINELAND RD",CIDADE:"ORLANDO",ESTADO:"FL",CEP:"32811",GERENTE:true},
{POSICAO:"Managing Member",PERCENT:"25",APORTE:"25",NOME:"ANDRE LUIS MARQUES PEREIRA",ENDERECO:"5197 VINELAND RD",CIDADE:"ORLANDO",ESTADO:"FL",CEP:"32811",GERENTE:true},
{POSICAO:"Managing Member",PERCENT:"25",APORTE:"25",NOME:"ISABEL CRISTINA MENEGAO MARQUES PEREIRA",ENDERECO:"5197 VINELAND RD",CIDADE:"ORLANDO",ESTADO:"FL",CEP:"32811",GERENTE:true}
]};
(function init(){
  var saved=null;try{saved=JSON.parse(localStorage.getItem("athena_bp"));}catch(e){}
  fill(saved&&saved.LLC_NAME?saved:DEMO);
})();
</script>
</body></html>"""

open("Athena_Business_Package.html","w",encoding="utf-8").write(HTML.replace("__LOGO__",logo))
print("Saved Athena_Business_Package.html", len(HTML))
