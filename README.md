<div align="center">

# Blender Atlas 4.0

**Guia interativo de Blender — do básico à criação de projetos 3D**

Um material de estudo que funciona diretamente no navegador, com módulos de modelagem, escultura, pintura, modificadores, animação e desafios práticos.

[**Abrir apostila (HTML)**](./index.html) · [**Gerador de cenas**](./scripts_blender/gerar_cenas_atlas4.py)

</div>

---

## Começar

1. Abra o arquivo [index.html](./index.html) no navegador.
2. Escolha um módulo no menu lateral.
3. Acompanhe as aulas, marque etapas concluídas e avance nos projetos.
4. Use a área de progresso para exportar seu backup quando necessário.

O Atlas foi desenvolvido com **HTML, CSS e JavaScript puro**, reunidos em um único arquivo. Não requer Node.js, servidor, framework ou instalação para leitura. O progresso é armazenado localmente no navegador, quando disponível.

## Conteúdo

- **21 projetos completos**, com etapas orientadas;
- **20 desafios práticos** para desenvolver por conta própria;
- **20 tutoriais visuais**, cada um com cinco etapas;
- referências de atalhos, modificadores, modelagem, escultura, materiais, pintura e animação;
- visualizações e atividades interativas;
- links auxiliares para consulta externa.

As ilustrações são **diagramas didáticos**, não capturas oficiais da interface do Blender. Alguns atalhos dependem do modo de edição, da versão e da configuração de teclas.

## Cenas de exemplo (opcional)

O script [gerar_cenas_atlas4.py](./scripts_blender/gerar_cenas_atlas4.py) gera cenas iniciais para exercícios. Ele não é necessário para usar o HTML.

Para usar dentro do **Blender**:

1. Entre na área **Scripting** e abra o arquivo Python.
2. Escolha uma cena alterando a variável `CENA` no início do script.
3. Execute **Run Script**.

Opções de cena: `bau`, `espada`, `cerca`, `arvore`, `rocha`, `personagem` e `animacao`.

O script cria modelos de **estudo**, não modelos finais completos. Também pode ser executado pelo terminal com a opção `--all` do Blender. A sintaxe do Python foi conferida, mas a execução dentro do Blender **não foi validada neste ambiente**.

## Links auxiliares

| Recurso | Para que serve |
|---|---|
| [ambientCG](https://ambientcg.com/) | Biblioteca de materiais e texturas PBR para modelos e cenários 3D. |
| [PureRef](https://www.pureref.com/) | Organização de imagens de referência para modelagem, escultura e pintura. |
| [Zotero](https://www.zotero.org/) | Organização de fontes bibliográficas, PDFs, citações e pesquisas acadêmicas. |

A apostila não inclui catálogos de texturas para download. Os serviços listados acima são externos e podem exigir internet.

## Estrutura do repositório

```text
Blender-Atlas-4.0/
├── index.html
├── scripts_blender/
│   └── gerar_cenas_atlas4.py
└── README.md
```

---

> **Nota sobre autoria:** repositório de estudo e distribuição do Blender Atlas. Os materiais disponibilizados aqui não devem ser apresentados automaticamente como trabalhos autorais de quem apenas os utiliza ou publica.
