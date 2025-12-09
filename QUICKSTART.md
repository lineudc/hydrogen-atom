# 🚀 Guia Rápido - Hydrogen Atom

## 📦 Setup Inicial (Apenas uma vez)

```bash
# Navegar até o projeto
cd /Users/lineufdelciampo/projetos/hydrogen-atom

# Setup automático (cria venv + instala tudo)
make setup

# Ativar ambiente virtual
source venv/bin/activate
```

## ⚡ Comandos Principais

### Executar Visualizações

```bash
# Densidade de probabilidade radial (gráfico 2D)
make run-radial

# Nuvem eletrônica 3D
make run-cloud

# Animação de fatiamento (gera GIF)
make run-slicing
```

### Desenvolvimento

```bash
# Ver todos os comandos
make help

# Rodar testes
make test

# Formatar código
make format

# Verificar estilo
make lint

# Limpar temporários
make clean
```

## 🐍 Uso Programático

### Ativar ambiente primeiro

```bash
source venv/bin/activate
```

### Executar scripts diretamente

```bash
python src/radial_wavefunction.py
python src/electron_cloud_3d.py
python src/orbital_slicing.py
```

### Usar como biblioteca

```python
from src.radial_wavefunction import plot_radial_density
from src.electron_cloud_3d import plot_electron_cloud

# Customizar visualizações
plot_radial_density(
    states=[(1, 0, '1s'), (2, 1, '2p')],
    save_path='meu_grafico.png'
)

plot_electron_cloud(
    n=3, l=2, m=0,
    num_points=100000,
    save_path='nuvem_3d.png'
)
```

## 🔧 Comandos Git (Para publicar)

```bash
# Inicializar (se ainda não tiver)
git init

# Adicionar arquivos
git add .

# Commit
git commit -m "Projeto reorganizado e documentado"

# Adicionar remote (substitua com seu repo)
git remote add origin https://github.com/lineudc/hydrogen-atom.git

# Push
git push -u origin main
```

## 📝 Estrutura de Arquivos

```
Arquivos importantes:
- src/                 → Código fonte
- tests/              → Testes
- olds/               → Scripts originais
- docs/               → Documentação
- Makefile            → Comandos automatizados
- requirements.txt    → Dependências
- README.md           → Documentação completa
```

## 🎯 Atalhos Úteis

```bash
# Tudo de uma vez (setup + test)
make all

# Reinstalar dependências
make install

# Ver status dos testes
make test

# Preparar para commit (format + lint + test)
make format && make lint && make test
```

## 🆘 Problemas Comuns

### Ambiente virtual não ativo
```bash
# Solução: Ativar sempre antes de usar
source venv/bin/activate
```

### Dependências faltando
```bash
# Solução: Reinstalar
make install
```

### Cache causando problemas
```bash
# Solução: Limpar tudo
make clean
```

## 📚 Documentação Completa

- `README.md` - Documentação técnica (inglês)
- `docs/RESUMO_EXECUTIVO.md` - Resumo em português
- `docs/RELATORIO_REORGANIZACAO.md` - Relatório detalhado
- `docs/hidrogen-atom.md` - Teoria física

## 🎨 Personalização

Edite os arquivos em `src/` para mudar:
- Números quânticos (n, l, m)
- Número de pontos
- Colormaps
- Tamanhos de figura
- Etc.

---

**Dica**: Execute `make help` a qualquer momento para ver todos os comandos!
