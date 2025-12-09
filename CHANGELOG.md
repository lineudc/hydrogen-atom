# 🔧 Changelog - Hydrogen Atom

## [1.0.2] - 2025-12-09

### ✨ Novos Recursos

#### Diretório de Output
- **Adicionado**: Diretório `output/` para armazenar figuras geradas
- **Modificado**: Todos os scripts agora salvam automaticamente em `output/`
  - `radial_density.png` - Densidade radial
  - `electron_cloud_{n}{orbital}_{m}.png` - Nuvens 3D
  - `orbital_slicing_3d.gif` - Animações

- **Arquivos modificados**:
  - `src/radial_wavefunction.py` - Salva em `output/radial_density.png`
  - `src/electron_cloud_3d.py` - Salva em `output/electron_cloud_*.png`
  - `src/orbital_slicing.py` - Salva em `output/orbital_slicing_3d.gif`
  - `.gitignore` - Permite versionamento de arquivos em `output/`

- **Benefícios**:
  - ✅ Organização centralizada das visualizações
  - ✅ Nomes de arquivo padronizados
  - ✅ Diretório criado automaticamente se não existir
  - ✅ Figuras versionadas no Git

### 📝 Documentação
- Criado `output/README.md` explicando estrutura de saída

---

## [1.0.1] - 2025-12-09

### 🐛 Correções

#### Atualização da API do SciPy
- **Problema**: DeprecationWarning ao usar `scipy.special.sph_harm`
  ```
  DeprecationWarning: `scipy.special.sph_harm` is deprecated as of SciPy 1.15.0 
  and will be removed in SciPy 1.17.0. Please use `scipy.special.sph_harm_y` instead.
  ```

- **Solução**: Migração para `sph_harm_y` (nova API do SciPy)
  
- **Arquivos modificados**:
  - `src/electron_cloud_3d.py`
  - `src/orbital_slicing.py`

- **Mudanças técnicas**:
  ```python
  # ANTES (API antiga - deprecada)
  from scipy.special import sph_harm
  Y_lm = sph_harm(m, l, phi, theta)  # ordem: (m, l, phi, theta)
  
  # DEPOIS (API nova)
  from scipy.special import sph_harm_y
  Y_lm = sph_harm_y(l, m, theta, phi)  # ordem: (l, m, theta, phi)
  ```

- **Nota importante**: A nova função `sph_harm_y` tem **ordem de parâmetros diferente**:
  - **Antiga**: `sph_harm(m, l, phi, theta)`
  - **Nova**: `sph_harm_y(l, m, theta, phi)`

- **Impacto**: Nenhum - Resultados idênticos, apenas API atualizada

- **Testes**: ✅ Todos os 10 testes continuam passando

### ✅ Validação

```bash
# Executar testes
make test
# Resultado: 10 passed in 1.80s (SEM warnings!)

# Testar nuvem eletrônica
python src/electron_cloud_3d.py
# Resultado: Executa sem DeprecationWarnings
```

---

## [1.0.0] - 2025-12-09

### 🎉 Lançamento Inicial

- Reorganização completa do projeto
- Estrutura profissional (src/, tests/, docs/)
- 10 testes automatizados
- Makefile com 11 comandos
- Documentação completa
- Ambiente virtual configurado
- Código refatorado com docstrings e type hints

---

**Compatibilidade**:
- SciPy >= 1.15.0 (usa `sph_harm_y`)
- SciPy < 1.15.0 (compatível com `sph_harm` - necessita reverter)

**Versionamento**: Seguindo [Semantic Versioning](https://semver.org/)
