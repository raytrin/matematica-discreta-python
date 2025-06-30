# 🧠 Treinador de Lógica Proposicional

Este é um dos meus projetos semanais para reforçar o que estou estudando na faculdade na matéria de **Matemática Discreta**. Além de aprender a teoria, estou praticando Python. 🐍

## O que o programa faz

- **Treinar negação** de proposições como `p∧q`, `p->q`, `¬p`
- **Ver equivalências** de expressões lógicas (ex: `p -> q` equivale a `¬p v q`)  
- **Descobrir como escrever** essas expressões em Python (ex: `p and q`, `not p or q`)
- **Fazer um quiz** com perguntas sobre negação, equivalência e conectivos
- **Gerar tabela verdade** para as principais operações lógicas

## Como usar

Execute o programa:
```bash
python logica.py
```

Depois escolha uma das opções do menu:
- `1`: Treinar negação
- `2`: Modo programador  
- `3`: Quiz de lógica
- `4`: Tabela verdade
- `0`: Sair

### Formatos aceitos

**Para treino, modo programador e quiz:**
- `p∧q` ou `p^q` → conjunção  
- `pvq` → disjunção  
- `p->q` → implicação  
- `p<->q` → bicondicional  
- `¬p` → negação  

**Para tabela verdade:**
- `p and q` → conjunção
- `p or q` → disjunção
- `not p or q` → implicação
- `p == q` → bicondicional  

(Use exatamente esses formatos)

## Exemplo de uso

```
Proposição: p -> q
Digite a negação: p∧¬q
✓ Acertou! Parabéns!
```

---

Se quiser trocar uma ideia, sinta-se à vontade! 

---
