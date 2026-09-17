# -*- coding: utf-8 -*-
"""
FICHA DE ABERTURA — ATHENA  (padrão visual da empresa + fonte única)
Uma só planilha, com a cara do formulário da Athena, que alimenta o gerador
de documentos. Um mapa de chaves oculto (_KEYS) liga cada campo à sua célula.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image as XLImage

SLATE="444D56"; GREY="EDECEC"; BLUE="E9EFF6"; INK="2A2E33"; WHITE="FFFFFF"
slate_fill=PatternFill("solid",fgColor=SLATE)
grey_fill=PatternFill("solid",fgColor=GREY)
blue_fill=PatternFill("solid",fgColor=BLUE)
thin=Side(style="thin",color="C9C9C9")
box=Border(left=thin,right=thin,top=thin,bottom=thin)
bot=Border(bottom=Side(style="thin",color="B0B0B0"))
F=lambda **k: Font(name="Calibri", **k)

wb=openpyxl.Workbook()
ws=wb.active; ws.title="1. ABERTURA"; ws.sheet_view.showGridLines=False
KV=[]  # (key, coord) pairs -> hidden _KEYS sheet

# column grid (A hidden for spacing balance)
widths=[2,17,13,11,10,11,10,10,12,12,13]
for i,w in enumerate(widths,start=1):
    ws.column_dimensions[get_column_letter(i)].width=w
LASTCOL="K"

def coord(c,r): return f"{get_column_letter(c)}{r}"

def bar(r,text,two=False):
    ws.merge_cells(f"B{r}:{LASTCOL}{r}")
    c=ws[f"B{r}"]; c.value=text; c.fill=slate_fill
    c.font=F(size=11,bold=True,color=WHITE)
    c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True)
    ws.row_dimensions[r].height=32 if two else 20

def title(r,text):
    ws.merge_cells(f"B{r}:{LASTCOL}{r}")
    c=ws[f"B{r}"]; c.value=text; c.font=F(size=10,bold=True,color=INK)
    c.alignment=Alignment(horizontal="center",vertical="center")
    ws.row_dimensions[r].height=18

def label(r,c,text,bold=False,col=INK,size=9.5,align="left"):
    cell=ws.cell(row=r,column=c,value=text)
    cell.font=F(size=size,bold=bold,color=col)
    cell.alignment=Alignment(horizontal=align,vertical="center",indent=1 if align=="left" else 0)
    return cell

def inp(r,c1,c2,key=None,value=""):
    if c2>c1: ws.merge_cells(start_row=r,start_column=c1,end_row=r,end_column=c2)
    cell=ws.cell(row=r,column=c1,value=value)
    cell.fill=grey_fill; cell.border=box
    cell.font=F(size=9.5,color=INK); cell.alignment=Alignment(vertical="center",indent=1)
    if key: KV.append((key,coord(c1,r)))
    ws.row_dimensions[r].height=16
    return cell

def chk(r,key,text,value=""):
    b=ws.cell(row=r,column=2,value=value); b.border=box; b.fill=PatternFill("solid",fgColor=WHITE)
    b.alignment=Alignment(horizontal="center",vertical="center"); b.font=F(size=10,bold=True,color=INK)
    ws.column_dimensions["B"].width=17
    ws.merge_cells(f"C{r}:{LASTCOL}{r}")
    t=ws.cell(row=r,column=3,value=text); t.font=F(size=9,bold=True,color=INK)
    t.alignment=Alignment(vertical="center",indent=1)
    if key: KV.append((key,coord(2,r)))
    ws.row_dimensions[r].height=15

# ---------- HEADER: logo block + note box ----------
for rr in range(2,6):
    for cc in range(2,6): ws.cell(row=rr,column=cc).fill=slate_fill
ws.merge_cells("B2:E5")
try:
    img=XLImage("athena_logo.png"); img.width=250; img.height=32
    ws.add_image(img,"B3")
except Exception as e:
    ws["B3"]="ATHENA business & tax advisors"; ws["B3"].font=F(size=12,bold=True,color=WHITE)
ws.merge_cells("G2:K5")
nb=ws["G2"]; nb.value=("Querido usuário,\nSalve esta planilha no seu computador e somente depois "
                       "preencha os campos. Transmita para o nosso escritório o arquivo.")
nb.fill=blue_fill; nb.font=F(size=8.5,color=INK); nb.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True)
nb.border=box
for rr in range(2,6): ws.row_dimensions[rr].height=17

# ---------- REGISTRO ----------
bar(7,"ABERTURA DE EMPRESA\nLLC | CORPORATION",two=True)
title(9,"REGISTRO")
label(10,2,"Data da Abertura:"); inp(10,3,5,"ABERTURA_DATA","02/25/2026")
label(10,7,"Offshore:",align="right"); inp(10,8,9,"OFFSHORE","NAO")
label(11,2,"Estado:"); inp(11,3,5,"STATE","Florida")
label(11,8,"LLC/CORP:",align="right"); inp(11,9,10,"ENTITY_TYPE","LLC")
label(12,2,"Nome da Empresa:"); label(12,3,"1-",align="right"); inp(12,4,11,"LLC_NAME","VIVELLE LLC")
label(13,3,"2-",align="right"); inp(13,4,11,"LLC_NAME_ALT","")

# ---------- ATIVIDADE ----------
bar(15,"ATIVIDADE DA EMPRESA")
label(16,2,"Atividade da Empresa:"); inp(16,4,11,"BUSINESS_PURPOSE","ANY AND ALL LAWFUL BUSINESS")

# ---------- ENDEREÇO ----------
bar(18,"ENDEREÇO DA EMPRESA")
label(19,2,"Endereço da Empresa:")
chk(20,"USE_ATHENA_ADDR","Marque com X caso for usar o endereço da Athena Business and Tax Advisors.","X")
inp(21,3,11,"PRINCIPAL_ADDRESS","7680 UNIVERSAL BLVD STE 100")
label(22,2,"Cidade:"); inp(22,3,4,"PRINCIPAL_CITY","ORLANDO")
label(22,5,"Estado:",align="right"); inp(22,6,6,"PRINCIPAL_STATE","FL")
label(22,7,"CEP:",align="right"); inp(22,8,9,"PRINCIPAL_ZIP","32819")
label(23,2,"Endereço de Correspondência:")
chk(24,"MAILING_SAME","Marque com X caso for utilizar o mesmo endereço para correspondência.","X")
inp(25,3,11,"MAILING_ADDRESS","")
label(26,2,"Cidade:"); inp(26,3,4,"MAILING_CITY","")
label(26,5,"Estado:",align="right"); inp(26,6,6,"MAILING_STATE","")
label(26,7,"CEP:",align="right"); inp(26,8,9,"MAILING_ZIP","")

# ---------- AGENTE ----------
bar(28,"AGENTE REGISTRADOR")
chk(29,"USE_ATHENA_AGENT","Marque com X caso for usar a Athena Business and Tax Advisors.","X")
label(30,2,"Nome do agente:"); inp(30,4,11,"REGISTERED_AGENT","ATHENA BUSINESS AND TAX ADVISORS LLC")
label(31,2,"Endereço do agente:"); inp(31,4,11,"REGISTERED_AGENT_ADDRESS","7680 UNIVERSAL BLVD SUITE 100")
label(32,2,"Cidade:"); inp(32,3,4,"AGENT_CITY","ORLANDO")
label(32,5,"Estado:",align="right"); inp(32,6,6,"AGENT_STATE","FL")
label(32,7,"CEP:",align="right"); inp(32,8,9,"AGENT_ZIP","32819")

# ---------- SÓCIOS (inline, 4 blocos) ----------
bar(34,"SÓCIOS")
socio_pct=[]; socio_name=[]; socio_ger=[]
r=35
def socio_block(r,n,pre=None):
    global socio_pct,socio_name,socio_ger
    chk(r,f"S{n}_GERENTE","Marque com X: colocar no SunBiz como pessoa autorizada a gerenciar a empresa (assina).",
        (pre or {}).get("ger","")); socio_ger.append(coord(2,r)); r+=1
    label(r,2,"Posição:"); c=inp(r,3,5,f"S{n}_POSICAO",(pre or {}).get("pos",""))
    label(r,6,"Percentual:",align="right"); p=inp(r,7,8,f"S{n}_PERCENT",(pre or {}).get("pct","")); label(r,9,"%")
    socio_pct.append(coord(7,r)); r+=1
    label(r,2,"Nome Completo:"); nm=inp(r,4,11,f"S{n}_NOME",(pre or {}).get("nome","")); socio_name.append(coord(4,r)); r+=1
    label(r,2,"SSN/ITIN/EIN:"); inp(r,4,7,f"S{n}_SSN",""); r+=1
    label(r,2,"Data de Nascimento:"); inp(r,4,7,f"S{n}_DOB",""); r+=1
    label(r,2,"Endereço:"); inp(r,4,11,f"S{n}_ENDERECO",(pre or {}).get("end","")); r+=1
    label(r,2,"Cidade:"); inp(r,3,4,f"S{n}_CIDADE",(pre or {}).get("cid",""))
    label(r,5,"Estado:",align="right"); inp(r,6,6,f"S{n}_ESTADO",(pre or {}).get("uf",""))
    label(r,7,"CEP:",align="right"); inp(r,8,9,f"S{n}_CEP",(pre or {}).get("cep","")); r+=1
    label(r,2,"Telefone:"); inp(r,3,5,f"S{n}_TELEFONE","")
    label(r,6,"E-mail:",align="right"); inp(r,7,11,f"S{n}_EMAIL",""); r+=1
    ws.row_dimensions[r].height=6; r+=1
    return r

pres=[
 {"ger":"X","pos":"Managing Member","pct":50,"nome":"CAIO ANDRE MENEGAO","end":"5197 VINELAND RD","cid":"ORLANDO","uf":"FL","cep":"32811"},
 {"ger":"X","pos":"Managing Member","pct":25,"nome":"ANDRE LUIS MARQUES PEREIRA","end":"5197 VINELAND RD","cid":"ORLANDO","uf":"FL","cep":"32811"},
 {"ger":"X","pos":"Managing Member","pct":25,"nome":"ISABEL CRISTINA MENEGAO MARQUES PEREIRA","end":"5197 VINELAND RD","cid":"ORLANDO","uf":"FL","cep":"32811"},
]
for n in range(1,5):
    r=socio_block(r,n, pres[n-1] if n-1<len(pres) else None)

# ---------- CONTATO ----------
bar(r,"CONTATO (pessoa principal — deve ser sócio)"); r+=1
label(r,2,"Nome:"); inp(r,4,11,"CONTACT_NAME","CAIO ANDRE MENEGAO"); r+=1
label(r,2,"Telefone:"); inp(r,4,7,"CONTACT_PHONE",""); r+=1
label(r,2,"Endereço:"); inp(r,4,11,"CONTACT_ADDRESS",""); r+=1
label(r,2,"E-mail:"); inp(r,4,11,"CLIENT_EMAIL",""); r+=1
r+=1

# ---------- CONFIG DO PACOTE (EQUIPE) ----------
bar(r,"CONFIG DO PACOTE  —  preenchido/validado pela EQUIPE ao abrir"); r+=1
def teamrow(r,key,lbl,val,dd=None):
    label(r,2,lbl); cc=inp(r,5,9,key,val); cc.fill=PatternFill("solid",fgColor="DCE6F2")
    if dd:
        dv=DataValidation(type="list",formula1=dd,allow_blank=True); ws.add_data_validation(dv); dv.add(cc)
    return r+1
r=teamrow(r,"TAX_CLASSIFICATION","Classificação tributária:","PARTNERSHIP",'"PARTNERSHIP,S-CORPORATION,C-CORPORATION,DISREGARDED ENTITY"')
r=teamrow(r,"TAX_YEAR","Ano fiscal:","CALENDAR YEAR")
r=teamrow(r,"ACCOUNTING_METHOD","Método contábil:","CASH",'"CASH,ACCRUAL"')
r=teamrow(r,"CONTRIBUTION_DUE_DATE","Prazo de aporte de capital:","DECEMBER 31, 2026")
r=teamrow(r,"AGREEMENT_DATE","Data de assinatura do Operating Agreement:","02/25/2026")
r=teamrow(r,"ARTICLES_FILED_DATE","Data do protocolo do Articles:","02/25/2026")
r=teamrow(r,"EIN","EIN (se já emitido):","")
r=teamrow(r,"AUTHORITY_MODE","Autoridade para assinar:","SINGLE",'"SINGLE,DUAL"')
r=teamrow(r,"DUAL_THRESHOLD_USD","Limite p/ dupla assinatura US$ (se DUAL):","10000")
r=teamrow(r,"MAILBOX_FEE_USD","Mailbox — valor anual US$:","380")
r=teamrow(r,"MAILBOX_PERIOD","Mailbox — período coberto:","JANEIRO A DEZEMBRO DE 2026")
r=teamrow(r,"MAILBOX_VALID_UNTIL","Mailbox — validade final:","31/12/2026")
r+=1

# ---------- TERMO / INFO / AVISO ----------
bar(r,"TERMO DE RESPONSABILIDADE"); r+=1
ws.merge_cells(f"B{r}:{LASTCOL}{r+2}")
t=ws[f"B{r}"]; t.value=("O CLIENTE autoriza a Athena Business and Tax Advisors a efetuar a abertura da empresa no Estado da "
 "Flórida e, caso queira, a designar a Athena como agente registrador. O prazo de abertura é de até 15 dias úteis; "
 "assim que a empresa estiver ativa, enviaremos todos os documentos. Aceito os termos sob pena de perjúrio.")
t.font=F(size=8.5,color=INK); t.alignment=Alignment(vertical="top",wrap_text=True,indent=1)
ws.row_dimensions[r].height=16; r+=3
label(r,2,"Assinatura:"); inp(r,4,9,"CLIENT_SIGNATURE",""); r+=2
bar(r,"INFORMAÇÕES ADICIONAIS"); r+=1
label(r,2,"Atendido por:"); cc=inp(r,4,9,"SERVICED_BY",""); cc.fill=PatternFill("solid",fgColor="DCE6F2"); r+=1
label(r,2,"Observações:"); cc=inp(r,4,11,"NOTES",""); cc.fill=PatternFill("solid",fgColor="DCE6F2"); r+=2
bar(r,"AVISO LEGAL"); r+=1
ws.merge_cells(f"B{r}:{LASTCOL}{r+1}")
t=ws[f"B{r}"]; t.value=("A Athena Business and Tax Advisors não é um escritório de advocacia; não prestamos consultoria jurídica "
 "nem nos apresentamos como advogados. Para revisões legais, recomendamos aconselhamento profissional.")
t.font=F(size=8,italic=True,color="6B7785"); t.alignment=Alignment(vertical="top",wrap_text=True,indent=1)
ws.row_dimensions[r].height=14

# SIM/NAO not used now (checkboxes are X). Offshore dropdown:
for key in ["OFFSHORE"]:
    pass

# ================= HIDDEN _KEYS =================
wk=wb.create_sheet("_KEYS"); wk.sheet_state="hidden"
wk["A1"]="KEY"; wk["B1"]="COORD"
for i,(k,co) in enumerate(KV,start=2):
    wk.cell(row=i,column=1,value=k); wk.cell(row=i,column=2,value=co)

# ================= 0. CONFERENCIA =================
def slatehdr(wsx,rng,text,h=26):
    wsx.merge_cells(rng); c=wsx[rng.split(":")[0]]; c.value=text; c.fill=slate_fill
    c.font=F(size=13,bold=True,color=WHITE); c.alignment=Alignment(vertical="center",indent=1)
    wsx.row_dimensions[int(''.join(filter(str.isdigit,rng.split(":")[0])))].height=h

cref={k:f"'1. ABERTURA'!{co}" for k,co in KV}
def joinsum(cells): return "+".join(f"N({c})" if False else c for c in cells)
pct_sum="+".join(cref_ for cref_ in [f"'1. ABERTURA'!{c.split('!')[-1] if '!' in c else c}" for c in []]) # placeholder
# build direct cell refs on the ABERTURA sheet
pct_refs=[f"'1. ABERTURA'!{c}" for c in socio_pct]
name_refs=[f"'1. ABERTURA'!{c}" for c in socio_name]
ger_refs=[f"'1. ABERTURA'!{c}" for c in socio_ger]

wsc=wb.create_sheet("0. CONFERENCIA",0); wsc.sheet_view.showGridLines=False
for i,w in enumerate([2,50,14,42],start=1): wsc.column_dimensions[get_column_letter(i)].width=w
slatehdr(wsc,"B2:D2","CONFERÊNCIA — a equipe revisa antes de gerar o pacote")
c=wsc["B3"]; wsc.merge_cells("B3:D3"); c.value="Corrija na aba 1. ABERTURA o que aparecer como ERRO/REVISAR."
c.font=F(size=9,italic=True,color="6B7785")
for i,h in enumerate(["","Verificação","Status","Detalhe"],start=1):
    if i==1: continue
    cc=wsc.cell(row=5,column=i,value=h); cc.font=F(size=10,bold=True,color=WHITE); cc.fill=slate_fill; cc.border=box
sum_pct="+".join(f"VALUE(IF({r}=\"\",0,{r}))" for r in pct_refs)
cnt_name="+".join(f"IF(TRIM({r})=\"\",0,1)" for r in name_refs)
cnt_ger="+".join(f"IF(OR(UPPER(TRIM({r}))=\"X\",UPPER(TRIM({r}))=\"SIM\"),1,0)" for r in ger_refs)
checks=[
 ("Nome da empresa preenchido", f'=IF(TRIM({cref["LLC_NAME"]})<>"","OK","ERRO")', f'={cref["LLC_NAME"]}'),
 ("Estado preenchido", f'=IF(TRIM({cref["STATE"]})<>"","OK","ERRO")', f'={cref["STATE"]}'),
 ("Data de abertura preenchida", f'=IF(TRIM({cref["ABERTURA_DATA"]})<>"","OK","ERRO")', f'={cref["ABERTURA_DATA"]}'),
 ("Agente registrador preenchido", f'=IF(TRIM({cref["REGISTERED_AGENT"]})<>"","OK","ERRO")', f'={cref["REGISTERED_AGENT"]}'),
 ("Nº de sócios preenchidos", f'=IF(({cnt_name})>0,"OK","ERRO")', f'=({cnt_name})&" sócio(s)"'),
 ("Soma das participações = 100%", f'=IF(ABS(({sum_pct})-100)<0.01,"OK","ERRO")', f'="soma = "&({sum_pct})&"%"'),
 ("Pelo menos 1 sócio que assina (X)", f'=IF(({cnt_ger})>=1,"OK","ERRO")', f'=({cnt_ger})&" gerente(s)"'),
 ("Classificação x nº de sócios",
   f'=IF(AND(({cnt_name})=1,UPPER({cref["TAX_CLASSIFICATION"]})="PARTNERSHIP"),"REVISAR",IF(AND(({cnt_name})>1,UPPER({cref["TAX_CLASSIFICATION"]})="DISREGARDED ENTITY"),"REVISAR","OK"))',
   f'="1→Disregarded · 2+→Partnership. Atual: "&{cref["TAX_CLASSIFICATION"]}'),
 ("EIN", f'=IF(TRIM({cref["EIN"]})<>"","OK","PENDENTE")', f'=IF(TRIM({cref["EIN"]})<>"",{cref["EIN"]},"emitir/anexar depois")'),
 ("Mailbox: período = validade", '="CONFERIR"', f'={cref["MAILBOX_PERIOD"]}&"  ×  "&{cref["MAILBOX_VALID_UNTIL"]}'),
]
rr=6
for lb,st,dt in checks:
    a=wsc.cell(row=rr,column=2,value=lb); a.font=F(size=10); a.border=box; a.alignment=Alignment(vertical="center",indent=1,wrap_text=True)
    s=wsc.cell(row=rr,column=3,value=st); s.font=F(size=10,bold=True); s.border=box; s.alignment=Alignment(horizontal="center",vertical="center")
    d=wsc.cell(row=rr,column=4,value=dt); d.font=F(size=9,color="6B7785"); d.border=box; d.alignment=Alignment(vertical="center",indent=1,wrap_text=True)
    wsc.row_dimensions[rr].height=24; rr+=1
green=PatternFill("solid",fgColor="C6EFCE"); red=PatternFill("solid",fgColor="FFC7CE"); amber=PatternFill("solid",fgColor="FFEB9C")
rng=f"C6:C{rr-1}"
for val,fill in [("OK",green),("ERRO",red),("REVISAR",amber),("PENDENTE",amber),("CONFERIR",amber)]:
    wsc.conditional_formatting.add(rng,CellIsRule(operator="equal",formula=[f'"{val}"'],fill=fill))

# ================= 3. MAPA =================
wsm=wb.create_sheet("3. MAPA")
wsm.sheet_view.showGridLines=False
for i,w in enumerate([2,32,16,58],start=1): wsm.column_dimensions[get_column_letter(i)].width=w
slatehdr(wsm,"B2:D2","MAPA DE REVERBERAÇÃO — do atendimento ao documento final")
for i,h in enumerate(["","Campo no atendimento","Chave","Onde reverbera"],start=1):
    if i==1: continue
    cc=wsm.cell(row=4,column=i,value=h); cc.font=F(size=10,bold=True,color=WHITE); cc.fill=slate_fill; cc.border=box
mrows=[
 ("Nome da Empresa","LLC_NAME","Capa · Operating Agreement · Statement of Authority · Ledger · Certificados · Mailbox · SunBiz"),
 ("Sócio — % (Percentual)","S#_PERCENT","Operating Agreement IV.1 (FIXO) · votação · distribuições · Ledger · Certificado (valor+extenso)"),
 ("Sócio — autorizado a gerenciar (X)","S#_GERENTE","→ ROLE. X = AUTHORIZED MEMBER (assina) no Operating Agreement, Statement of Authority, Ledger e Certificado; vazio = MEMBER ONLY"),
 ("Autoridade (SINGLE/DUAL)","AUTHORITY_MODE","Operating Agreement VII · Statement of Authority — troca todo o texto de assinatura/banco/imóveis"),
 ("Classificação tributária","TAX_CLASSIFICATION","Operating Agreement III.1 · Capa (obrigações fiscais)"),
 ("Endereço / agente","PRINCIPAL_* / REGISTERED_AGENT","Operating Agreement I.3–I.4 · Capa · Mailbox · SunBiz"),
 ("Mailbox período/valor","MAILBOX_*","Mailbox Agreement — período pago = vigência"),
]
rr=5
for a,b,c in mrows:
    for col,val,fs in [(2,a,9.5),(3,b,9),(4,c,9.5)]:
        cc=wsm.cell(row=rr,column=col,value=val); cc.border=box
        cc.font=F(size=fs,bold=(col==2),color=(SLATE if col==2 else ("8A6D1A" if col==3 else INK)))
        cc.alignment=Alignment(wrap_text=True,vertical="top",indent=1)
    wsm.row_dimensions[rr].height=34; rr+=1

# =====================================================================
# DOCUMENTOS COMO ABAS (fórmulas puxam da aba 1. ABERTURA) — self-contained
# =====================================================================
import re as _re
from openpyxl.utils import get_column_letter as _gl
keycoord={k:co for k,co in KV}

# número por extenso (0..100) em tabela oculta _N2W para os certificados
_ONES=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN",
 "TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINETEEN"]
_TENS=["","","TWENTY","THIRTY","FORTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINETY"]
def _w(n):
    n=int(n)
    if n==100: return "ONE HUNDRED"
    if n<20: return _ONES[n]
    t,o=divmod(n,10); return _TENS[t]+("" if o==0 else "-"+_ONES[o])
wn=wb.create_sheet("_N2W"); wn.sheet_state="hidden"
for i in range(0,101):
    wn.cell(row=i+1,column=1,value=i); wn.cell(row=i+1,column=2,value=_w(i)+" PERCENT")
N2W="_N2W!$A$1:$B$101"

AMC=f"'1. ABERTURA'!{keycoord['AUTHORITY_MODE']}"
THR=f"'1. ABERTURA'!{keycoord['DUAL_THRESHOLD_USD']}"

def frag(tok):
    m=_re.match(r'S(\d+)_ROLE$',tok)
    if m:
        g=f"'1. ABERTURA'!{socio_ger[int(m.group(1))-1]}"
        return f'IF(OR(UPPER(TRIM({g}))="X",UPPER(TRIM({g}))="SIM"),"AUTHORIZED MEMBER","MEMBER ONLY")'
    m=_re.match(r'S(\d+)_PCTW$',tok)
    if m:
        p=f"'1. ABERTURA'!{socio_pct[int(m.group(1))-1]}"
        return f'IFERROR(VLOOKUP(VALUE({p}),{N2W},2,FALSE),"")'
    if tok=="AUTH_SIGN":
        return (f'IF({AMC}="DUAL",'
          f'"2. Signing Authority (DUAL-CONTROL). Any one Authorized Member may sign in the ordinary course up to US$ "&{THR}&". '
          f'Any transaction at or above US$ "&{THR}&" — including opening or closing bank accounts, borrowing, and any purchase, sale, mortgage, or encumbrance of Company real estate — requires the signatures of TWO Authorized Members.",'
          f'"2. Signing Authority (SINGLE). Any one Authorized Member may sign for the Company, including opening and operating bank accounts and signing checks, contracts, and other documents in the ordinary course. Presence of all members is not required.")')
    if tok=="AUTH_RE":
        return (f'IF({AMC}="DUAL",'
          f'"3. Disposition of Real Estate. Any sale, mortgage, or encumbrance of Company real estate requires the approval of a majority of Percentage Interests AND the signatures of two Authorized Members, recorded in a Minute of Meeting.",'
          f'"3. Disposition of Real Estate. Any sale, mortgage, or encumbrance of Company real estate must first be APPROVED by a majority of Percentage Interests, and recorded in a Minute of Meeting designating the Authorized Member who signs for the Company.")')
    if tok=="AUTH_STMT":
        return (f'IF({AMC}="DUAL",'
          f'"AUTHORITY (DUAL-CONTROL): Each Authorized Member may sign in the ordinary course up to US$ "&{THR}&". Transactions at or above US$ "&{THR}&", including borrowing and any purchase, sale, or encumbrance of real property, require TWO Authorized Members.",'
          f'"AUTHORITY (SINGLE-SIGNER): Each Authorized Member is authorized to open bank accounts, buy and sell property, and sign checks, withdrawals, contracts, and any other document on behalf of the Company. The signature of one Authorized Member is sufficient.")')
    if tok in keycoord: return f"'1. ABERTURA'!{keycoord[tok]}"
    return '""'

def xf(template):
    out=[]; last=0
    for m in _re.finditer(r'\{([A-Z0-9_]+)\}',template):
        lit=template[last:m.start()]
        if lit: out.append('"'+lit.replace('"','""')+'"')
        out.append(frag(m.group(1))); last=m.end()
    lit=template[last:]
    if lit: out.append('"'+lit.replace('"','""')+'"')
    return "="+"&".join(out or ['""'])

def gate(nametok,template):
    """paragraph shown only if that member's name is filled"""
    n=_re.match(r'S(\d+)_',nametok).group(1)
    nc=f"'1. ABERTURA'!{socio_name[int(n)-1]}"
    body=xf(template)[1:]  # drop '='
    return f'=IF(TRIM({nc})="","",{body})'

def docsheet(name):
    d=wb.create_sheet(name); d.sheet_view.showGridLines=False
    d.column_dimensions["A"].width=2; d.column_dimensions["B"].width=112
    d.page_setup.orientation="portrait"; d.page_setup.fitToWidth=1; d.page_setup.fitToHeight=0
    d.sheet_properties.pageSetUpPr=openpyxl.worksheet.properties.PageSetupProperties(fitToPage=True)
    return d

def dtitle(d,r,text,size=15):
    c=d.cell(row=r,column=2,value=text); c.font=F(size=size,bold=True,color=SLATE)
    c.alignment=Alignment(horizontal="center"); d.row_dimensions[r].height=size+8
def dbar(d,r,text):
    c=d.cell(row=r,column=2,value=text); c.fill=slate_fill; c.font=F(size=11,bold=True,color=WHITE)
    c.alignment=Alignment(horizontal="left",indent=1); d.row_dimensions[r].height=18
def dp(d,r,template,size=9.5,bold=False,italic=False,color=INK,center=False,gatetok=None,plain=None):
    val = plain if plain is not None else (gate(gatetok,template) if gatetok else xf(template))
    c=d.cell(row=r,column=2,value=val); c.font=F(size=size,bold=bold,italic=italic,color=color)
    c.alignment=Alignment(horizontal="center" if center else "left",vertical="top",wrap_text=True,indent=0 if center else 1)
    est=max(1,int(len(template)/95)+1); d.row_dimensions[r].height=est*(size+4.5)
    return r+1
def dnote(d,r,template):
    return dp(d,r,template,size=8.5,italic=True,color="B08900")

# ---------------- CAPA ----------------
d=docsheet("DOC · Capa")
r=2
# logo block
for rr in range(2,5):
    d.cell(row=rr,column=2).fill=slate_fill
d.merge_cells("B2:B4")
try:
    im2=XLImage("athena_logo.png"); im2.width=250; im2.height=32; d.add_image(im2,"B3")
except: pass
for rr in range(2,5): d.row_dimensions[rr].height=17
r=6
r=dp(d,r,"BUSINESS PACKAGE",size=12,bold=True,color=GOLD if False else "8A6D1A",center=True)
r=dp(d,r,"DOCUMENTS OF",size=12,color="6B7785",center=True)
r=dp(d,r,"{LLC_NAME}",size=22,bold=True,color=SLATE,center=True)
r=dp(d,r,"A {STATE} Limited Liability Company",size=10,italic=True,color="6B7785",center=True); r+=1
dbar(d,r,"CONTEÚDO DO PACOTE"); r+=1
for t in ["EIN (CP-575) · SunBiz · Certificate of Status · Articles of Organization",
          "Operating Agreement · Statement of Authority",
          "Membership Ledger · Membership Certificates",
          "Mailbox Agreement · Checklist de abertura"]:
    r=dp(d,r,"•  "+t)
r+=1
dbar(d,r,"OBRIGAÇÕES APÓS A ABERTURA"); r+=1
r=dp(d,r,"Annual Report: 1º jan – 1º maio (multa US$ 400).  Imposto federal: prazo/multa conforme classificação e ano (Form 1065, IRC §6698 — confirmar valor vigente).")
r+=1
r=dp(d,r,"A Athena Business & Tax Advisors é contabilidade e não presta serviços jurídicos. Contato: manager@athenataxadvisors.com · (407) 777-2501",size=8.5,italic=True,color="6B7785")

# ---------------- OPERATING AGREEMENT ----------------
d=docsheet("DOC · Operating Agr")
r=2
r=dp(d,r,"{LLC_NAME}",size=15,bold=True,color=SLATE,center=True)
r=dp(d,r,"OPERATING AGREEMENT",size=12,bold=True,color="8A6D1A",center=True)
r=dp(d,r,"For a Member-Managed Limited Liability Company",size=9.5,italic=True,color="6B7785",center=True); r+=1
dbar(d,r,"I. Preliminary Provisions"); r+=1
r=dp(d,r,"1. FORMATION. The members form a limited liability company (“Company”) under the Florida Revised LLC Act (Ch. 605, Fla. Stat.). The Articles of Organization were filed on {ARTICLES_FILED_DATE}.")
r=dp(d,r,"2. NAME. The name of the Company is {LLC_NAME}.")
r=dp(d,r,"3. PRINCIPAL PLACE OF BUSINESS. {PRINCIPAL_ADDRESS}, {PRINCIPAL_CITY}, {PRINCIPAL_STATE} {PRINCIPAL_ZIP}.")
r=dp(d,r,"4. REGISTERED AGENT. {REGISTERED_AGENT}, {REGISTERED_AGENT_ADDRESS}, {AGENT_CITY}, {AGENT_STATE} {AGENT_ZIP}.")
r=dp(d,r,"5. BUSINESS PURPOSE. {BUSINESS_PURPOSE}. This shall not limit any lawful activity.")
r=dp(d,r,"6. DURATION. Perpetual, until dissolved as provided herein or by law.")
r=dp(d,r,"7. MANAGEMENT. The Company is MEMBER-MANAGED; it has no separate managers unless the members amend this Agreement.")
dbar(d,r,"II. Membership Provisions"); r+=1
r=dp(d,r,"1. Nonliability. No member is personally liable for Company debts or obligations.")
r=dp(d,r,"2. The members of the Company are:")
for n in range(1,5):
    r=dp(d,r,f"   • {{S{n}_NOME}}  ·  {{S{n}_ENDERECO}}, {{S{n}_CIDADE}}, {{S{n}_ESTADO}} {{S{n}_CEP}}  ·  {{S{n}_ROLE}}",gatetok=f"S{n}_NOME")
r=dp(d,r,"3. Percentage Interests are FIXED as set forth in Article IV and the Membership Ledger; they do NOT fluctuate with capital-account balances and change only by written amendment or an admission/withdrawal/transfer under this Agreement.")
r=dnote(d,r,"Correção: percentual fixo — removida a regra que recalculava pelo saldo da conta de capital.")
r=dp(d,r,"4. Voting is in proportion to Percentage Interest; “majority” means more than 50% of interests.")
r=dp(d,r,"5. Members are paid only for services in another capacity (officer/employee/contractor), as a majority approves.")
dbar(d,r,"III. Tax and Financial Provisions"); r+=1
r=dp(d,r,"1. Tax Classification. The Company is classified as {TAX_CLASSIFICATION} for income-tax purposes; the members may change the election as permitted by law.")
r=dp(d,r,"2. Tax Year / Method: {TAX_YEAR} · {ACCOUNTING_METHOD}.")
r=dp(d,r,"3. Partnership Representative. If subject to the BBA centralized audit regime (IRC §6223), the members designate a Partnership Representative; where eligible, the Company may elect out under §6221(b).")
r=dnote(d,r,"Correção: substitui o obsoleto “Tax Matters Partner” (§6231(a)(7), TEFRA revogado).")
r=dp(d,r,"4. Within 75 days after year end, each member receives the information (Schedule K-1, if a partnership) and a financial report.")
dbar(d,r,"IV. Capital Provisions"); r+=1
r=dp(d,r,"1. Capital Contributions are due on or before {CONTRIBUTION_DUE_DATE}. Members and Percentage Interests:")
for n in range(1,5):
    r=dp(d,r,f"   • {{S{n}_NOME}} — {{S{n}_PERCENT}}%",gatetok=f"S{n}_NOME")
r=dp(d,r,"2. Additional contributions only by unanimous vote. 3. No interest on capital.")
r=dp(d,r,"4. Distributions are made in proportion to Percentage Interests, when approved by a MAJORITY of members; none if it would render the Company insolvent (§605.0405).")
r=dnote(d,r,"Correção: removido o “ACCOUNTING RECORDS OF THE COMPANY”; distribuição por voto da maioria.")
r=dp(d,r,"5. Tax Distributions. Subject to available cash and §605.0405, the Company shall endeavor to distribute, by each estimated-tax due date, an amount sufficient to cover each member’s tax on income allocated to them, pro rata.")
r=dnote(d,r,"Cláusula nova: distribuição para cobrir o imposto do K-1.")
dbar(d,r,"V. Transfer / Death"); r+=1
r=dp(d,r,"1. No transfer, pledge, or encumbrance without the written approval of all other members; a transferee is admitted only by unanimous consent.")
r=dp(d,r,"2. Death/Incapacity — Buy-Sell (controls over dissolution). For 90 days the surviving members may, by unanimous consent, purchase the interest at Fair Value; to the extent not purchased, the Company purchases it. The Company does NOT dissolve on such event.")
r=dnote(d,r,"Correção: morte segue UMA sequência (buy-sell 90 dias) e não dispara dissolução.")
dbar(d,r,"VI. Dissolution"); r+=1
r=dp(d,r,"The Company dissolves only by (a) written agreement of all members, (b) judicial decree, or (c) an event making continuation unlawful. Dissociation of a member does NOT dissolve the Company.")
dbar(d,r,"VII. Authority & General"); r+=1
r=dp(d,r,"1. Approval vs. signing authority are addressed separately (Florida law distinguishes them).")
r=dp(d,r,"{AUTH_SIGN}")
r=dp(d,r,"{AUTH_RE}")
r=dnote(d,r,"Autoridade conforme a ficha (SINGLE/DUAL) — muda sozinho aqui.")
r=dp(d,r,"4. Governing Law & Venue: State of {STATE}; venue in Orange County, Florida. 5. Disputes: mediation then BINDING arbitration (AAA, Orange County, FL); prevailing party may recover fees.")
r=dp(d,r,"6. Entire Agreement; amended only by a writing signed by all current members. 7. Severability applies.")
dbar(d,r,"VIII. Signatures"); r+=1
r=dp(d,r,"IN WITNESS WHEREOF, the members adopt this Operating Agreement of {LLC_NAME}.  Date: {AGREEMENT_DATE}"); r+=1
for n in range(1,5):
    r=dp(d,r,f"Signature: __________________________     Printed Name: {{S{n}_NOME}}  ({{S{n}_ROLE}})",gatetok=f"S{n}_NOME")
r+=1
r=dp(d,r,"Template para a Athena Business & Tax Advisors (contabilidade, não jurídico). O template mestre deve ser validado por advogado da Flórida.",size=8,italic=True,color="6B7785")

# ---------------- STATEMENT OF AUTHORITY ----------------
d=docsheet("DOC · Statement Auth")
r=2
r=dp(d,r,"STATEMENT OF AUTHORITY",size=15,bold=True,color=SLATE,center=True)
r=dp(d,r,"of {LLC_NAME}",size=12,bold=True,color="8A6D1A",center=True)
r=dp(d,r,"(Autorização interna de signatários — NÃO é o Certificate of Authority de LLC estrangeira, §605.0902)",size=8.5,italic=True,color="6B7785",center=True); r+=1
r=dp(d,r,"The members state the authority of the following persons to act for the Company:")
for n in range(1,5):
    r=dp(d,r,f"   • {{S{n}_NOME}}  —  {{S{n}_ENDERECO}}, {{S{n}_CIDADE}}, {{S{n}_ESTADO}}  —  {{S{n}_ROLE}}",gatetok=f"S{n}_NOME")
r+=1
r=dp(d,r,"{AUTH_STMT}")
r=dp(d,r,"This Statement is consistent with, and subject to, the Operating Agreement. Third parties may rely on it until superseded.  Date: {ABERTURA_DATA}",size=9.5,italic=True); r+=1
for n in range(1,5):
    r=dp(d,r,f"Signature: __________________________     Printed Name: {{S{n}_NOME}}  ({{S{n}_ROLE}})",gatetok=f"S{n}_NOME")

# ---------------- MEMBERSHIP LEDGER ----------------
d=docsheet("DOC · Ledger")
# widen for a small table: use columns B..F
d.column_dimensions["B"].width=6; d.column_dimensions["C"].width=42; d.column_dimensions["D"].width=16
d.column_dimensions["E"].width=16; d.column_dimensions["F"].width=14
r=2
c=d.cell(row=r,column=2,value=xf("INTEREST CERTIFICATE LEDGER — {LLC_NAME}")); c.font=F(size=14,bold=True,color=SLATE)
d.merge_cells(f"B{r}:F{r}"); c.alignment=Alignment(horizontal="center"); r+=2
heads=["No.","Name of Member","Effective Date","Date of Cert.","Interests"]
for i,h in enumerate(heads):
    cc=d.cell(row=r,column=2+i,value=h); cc.fill=slate_fill; cc.font=F(size=9,bold=True,color=WHITE); cc.border=box
    cc.alignment=Alignment(horizontal="center")
r+=1
for n in range(1,5):
    nc=f"'1. ABERTURA'!{socio_name[n-1]}"
    d.cell(row=r,column=2,value=f'=IF(TRIM({nc})="","",{n})').border=box
    d.cell(row=r,column=3,value=gate(f"S{n}_NOME","{S%d_NOME}"%n)).border=box
    d.cell(row=r,column=4,value=gate(f"S{n}_NOME","{ABERTURA_DATA}")).border=box
    d.cell(row=r,column=5,value=gate(f"S{n}_NOME","{ABERTURA_DATA}")).border=box
    d.cell(row=r,column=6,value=gate(f"S{n}_NOME","{S%d_PERCENT}%%"%n)).border=box
    for cc in range(2,7):
        d.cell(row=r,column=cc).font=F(size=9); d.cell(row=r,column=cc).alignment=Alignment(horizontal="center")
    r+=1

# ---------------- MEMBERSHIP CERTIFICATES ----------------
d=docsheet("DOC · Certificates")
r=2
for n in range(1,5):
    nc=f"'1. ABERTURA'!{socio_name[n-1]}"
    r=dp(d,r,f"CERTIFICATE No. 0{n}",size=10,bold=True,color="8A6D1A",center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,"MEMBERSHIP CERTIFICATE",size=14,bold=True,color=SLATE,center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,"{LLC_NAME}",size=16,bold=True,color=SLATE,center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,"This certifies that",size=10,center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,f"{{S{n}_NOME}}",size=15,bold=True,color=SLATE,center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,f"holds a membership interest of {{S{n}_PERCENT}}%  ({{S{n}_PCTW}})",size=12,bold=True,color="8A6D1A",center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,"subject to the Operating Agreement.  Issued on {ABERTURA_DATA}, Orlando, Florida.",size=9.5,center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,"_____________________________          _____________________________",size=9.5,center=True,gatetok=f"S{n}_NOME")
    r=dp(d,r,"Authorized Member                                 Authorized Member",size=8.5,color="6B7785",center=True,gatetok=f"S{n}_NOME")
    r+=1

# ---------------- MAILBOX AGREEMENT ----------------
d=docsheet("DOC · Mailbox")
r=2
r=dp(d,r,"CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE CAIXA POSTAL",size=13,bold=True,color=SLATE,center=True); r+=1
r=dp(d,r,"Empresa: {LLC_NAME}   ·   E-mail: {CLIENT_EMAIL}   ·   Telefone: {CONTACT_PHONE}")
r=dp(d,r,"Endereço: {PRINCIPAL_ADDRESS}, {PRINCIPAL_CITY}, {PRINCIPAL_STATE} {PRINCIPAL_ZIP}"); r+=1
r=dp(d,r,"CLÁUSULA I — Prestação de serviços de Caixa Postal pela Athena Business and Tax Advisors ao cliente acima, para recebimento e gerenciamento de correspondências.")
r=dp(d,r,"CLÁUSULA II — O Cliente não utilizará os serviços para fins ilegais ou proibidos pelas normas postais dos EUA.")
r=dp(d,r,"CLÁUSULA III — Valor de US$ {MAILBOX_FEE_USD},00, referente ao período de {MAILBOX_PERIOD}, pago no ato da assinatura.")
r=dp(d,r,"CLÁUSULA IV — Vigência por {MAILBOX_PERIOD}, válido até {MAILBOX_VALID_UNTIL} (coincide com o período pago). Renovação por novo acordo e pagamento.")
r=dnote(d,r,"Correção: período pago = vigência (vindos da ficha).")
r=dp(d,r,"CLÁUSULA V — O Cliente autoriza a Athena a abrir correspondências e descartar propaganda/spam.")
r=dp(d,r,"CLÁUSULA VI — Não é permitido encomendas volumosas; o serviço restringe-se a cartas e documentos, sem armazenamento físico.")
r=dp(d,r,"CLÁUSULA VII — Correspondência digitalizada e enviada ao e-mail do Cliente; mediante solicitação, encaminhamento físico (correio) ao endereço registrado em até 24h.")
r=dnote(d,r,"Correção: separado digitalização (e-mail) de encaminhamento físico (correio).")
r+=1
r=dp(d,r,"Assinatura: __________________________     Data: ____/____/______",bold=True)

wb.save("FICHA_ABERTURA_ATHENA.xlsx")
print("Saved FICHA_ABERTURA_ATHENA.xlsx | keys:",len(KV),"| abas:",wb.sheetnames)
