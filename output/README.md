# 📊 Output - Visualizações Geradas

Este diretório contém as figuras e animações geradas pelos scripts.

## 📁 Arquivos Gerados

### Densidade de Probabilidade Radial
- **`radial_density.png`** - Gráfico 2D mostrando P(r) = r² |R_nl(r)|²
- Gerado por: `python src/radial_wavefunction.py` ou `make run-radial`

### Nuvem Eletrônica 3D
- **`electron_cloud_3d_0.png`** - Visualização 3D do orbital 3d (m=0)
- Gerado por: `python src/electron_cloud_3d.py` ou `make run-cloud`
- Formato de nome: `electron_cloud_{n}{orbital}_{m}.png`
  - Exemplo: `electron_cloud_3d_0.png` = orbital 3d com m=0

### Animação de Fatiamento
- **`orbital_slicing_3d.gif`** - Animação mostrando fatias 2D do orbital
- Gerado por: `python src/orbital_slicing.py` ou `make run-slicing`

## 🎨 Como Gerar

### Opção 1: Comandos Make (Recomendado)
```bash
make run-radial    # Gera radial_density.png
make run-cloud     # Gera electron_cloud_3d_0.png
make run-slicing   # Gera orbital_slicing_3d.gif
```

### Opção 2: Scripts Diretos
```bash
python src/radial_wavefunction.py
python src/electron_cloud_3d.py
python src/orbital_slicing.py
```

### Opção 3: Programático
```python
from src.radial_wavefunction import plot_radial_density
from src.electron_cloud_3d import plot_electron_cloud

# Customizar e salvar
plot_radial_density(
    states=[(1, 0, '1s'), (2, 1, '2p')],
    save_path='output/custom_radial.png'
)

plot_electron_cloud(
    n=2, l=1, m=0,
    save_path='output/orbital_2p.png'
)
```

## 🗑️ Limpeza

Para remover todos os arquivos gerados:
```bash
rm output/*.png output/*.gif
```

Ou use o Makefile (limpa apenas temporários, preserva output):
```bash
make clean
```

## 📝 Notas

- ✅ Arquivos aqui são **versionados no Git** (não estão no .gitignore)
- ✅ Diretório criado automaticamente pelos scripts se não existir
- ✅ Nomes de arquivo seguem padrão consistente
- ✅ Figuras salvas em alta resolução (300 DPI)

---

**Dica**: Execute os scripts para popular este diretório com visualizações!
