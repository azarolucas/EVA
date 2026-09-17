# Athena — Business Package

App de arquivo único para o time da **Athena Business & Tax Advisors** captar as
informações da abertura de empresa e **gerar o Business Package completo** (com a
marca da Athena), tudo a partir dos mesmos dados.

## Como usar (dia a dia)

1. Abra **`Athena_Business_Package.html`** em qualquer navegador (Chrome/Edge/Safari).
   Não precisa de internet nem instalar nada.
2. **Aba 1 · Dados do Cliente** — pode entregar ao cliente para preencher, ou preencher
   internamente. Tem o checkbox de **Confirmação do cliente**.
3. **Aba 2 · Decisões da Empresa** — o time define: administração (member/manager-managed),
   autoridade (SINGLE/DUAL), disposição de imóveis, classificação tributária, mailbox,
   nº SunBiz, EIN emitido?, Certificate of Status?, etc.
4. **Conferência** — checagem automática (soma dos %, ao menos 1 gerente, etc.).
5. **Gerar Business Package** — monta todos os documentos.
6. **Imprimir / Salvar PDF** — exporta (cada documento em sua página).

Persistência: **Salvar** (localStorage do navegador) · **Exportar/Importar** (.json).
O app abre pré-preenchido com a **VIVELLE LLC** como exemplo.

## O que o pacote gera

Na ordem: **Ficha de Conferência do Cliente → Capa → Operating Agreement →
Statement of Authority → Membership Ledger → STOCK / Interest Certificate (1 por sócio)
→ Mailbox Agreement (se contratado)**.

## Reverberação (fonte única)

Preencheu uma vez → propaga para todos os documentos, batendo entre si:

- **"autorizado a gerenciar (assina)"** → `AUTHORIZED MEMBER` no acordo, Statement of
  Authority, ledger e certificado; sem marca → `MEMBER ONLY`.
- **Autoridade SINGLE/DUAL** → muda o texto de assinatura/banco/imóveis.
- **% de participação (fixo)** → Art. IV, votação, distribuições, ledger, STOCK.
- **Administração member/manager-managed** → cláusula de gestão.
- **Disposição de imóveis** → marca só a opção escolhida (não mais "any member").
- **Mailbox** → só entra se contratado.

## Operating Agreement — texto integral

O Operating Agreement reproduz o **texto original completo** (nada removido). Foram
corrigidas apenas as **inconsistências**:

1. Percentual **fixo** (Art. IV), não recalculado pelo saldo da conta de capital.
2. **Partnership Representative** (IRC §6223) no lugar do obsoleto "Tax Matters Partner".
3. Distribuições por **maioria** (removido o "ACCOUNTING RECORDS OF THE COMPANY").
4. Morte/saída em **uma sequência única** (buy-sell), sem dissolver a LLC.
5. **VII.3 Disposition of Real Estate** com **uma opção marcada** (escolhida na aba 2).
6. Correção do typo "member **of** the company".

> A Athena é contabilidade, não jurídico. O template mestre do Operating Agreement
> deve ser validado uma vez por um advogado da Flórida.

## Estrutura

```
athena-business-package/
├── Athena_Business_Package.html   # o app (abrir no navegador)
├── build_html.py                  # gera o HTML acima (ajustar textos/campos/visual aqui)
├── assets/
│   └── athena_logo.png            # logo (extraído do formulário; trocar pelo oficial se houver)
└── extras/
    ├── build_master.py            # gerador alternativo: planilha-ficha .xlsx
    ├── gerar_pacote.py            # gerador alternativo: documentos .docx
    └── OA_original_full.txt       # texto integral original do Operating Agreement (referência)
```

## Rebuild

```
python3 build_html.py    # reescreve Athena_Business_Package.html (embute o logo em base64)
```

## Pendências / próximos passos

- Trocar `assets/athena_logo.png` pelo **logo oficial em alta** (PNG/SVG), se houver.
- **Versão em inglês** (Company Formation) no mesmo app (toggle PT/EN).
