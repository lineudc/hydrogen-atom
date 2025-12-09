# Hydrogen Atom Visualization

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Visualização computacional de orbitais do átomo de Hidrogênio usando Python. Este projeto implementa soluções da Equação de Schrödinger para o átomo de Hidrogênio, gerando visualizações elegantes e cientificamente precisas.

## 📋 Características

- **Função de Onda Radial**: Visualização 2D da densidade de probabilidade radial P(r) = r² |R_nl(r)|²
- **Nuvem Eletrônica 3D**: Geração de nuvens de pontos usando Monte Carlo (rejection sampling)
- **Animação de Fatiamento**: Visualização de fatias transversais dos orbitais em diferentes alturas
- **Código Documentado**: Docstrings completas e type hints
- **Testes Automatizados**: Suite de testes com pytest

## 🧮 Fundamentos Teóricos

O projeto implementa a solução da equação de Schrödinger independente do tempo para o átomo de Hidrogênio:

$$\\hat{H}\\psi(\\mathbf{r}) = E\\psi(\\mathbf{r})$$

A função de onda é separada em partes radial e angular:

$$\\psi_{n,l,m}(r, \\theta, \\phi) = R_{nl}(r) \\cdot Y_{lm}(\\theta, \\phi)$$

Onde:
- **n** (Principal): Energia e tamanho do orbital (1, 2, 3...)
- **l** (Azimutal): Forma do orbital (0 ≤ l < n)
- **m** (Magnético): Orientação espacial (-l ≤ m ≤ l)

## 🚀 Instalação e Setup

### Requisitos

- Python 3.13+ (compatível com versões 3.8+)
- make (opcional, mas recomendado)

### Setup Rápido com Makefile

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/hydrogen-atom.git
cd hydrogen-atom

# Setup completo (cria venv + instala dependências)
make setup

# Ative o ambiente virtual
source venv/bin/activate
```

### Setup Manual

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # macOS/Linux
# ou
venv\\Scripts\\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

## 🎯 Uso

### Usando Makefile (Recomendado)

```bash
# Ver todos os comandos disponíveis
make help

# Executar visualizações
make run-radial    # Função de onda radial
make run-cloud     # Nuvem eletrônica 3D
make run-slicing   # Animação de fatiamento

# Executar testes
make test

# Formatação e linting
make format
make lint

# Limpeza de arquivos temporários
make clean
```

### Executando Scripts Diretamente

```bash
# Ativar ambiente virtual primeiro
source venv/bin/activate

# Executar scripts individuais
python src/radial_wavefunction.py
python src/electron_cloud_3d.py
python src/orbital_slicing.py
```

### Uso Programático

```python
from src.radial_wavefunction import plot_radial_density
from src.electron_cloud_3d import plot_electron_cloud

# Visualizar densidade radial
plot_radial_density(
    states=[(1, 0, '1s'), (2, 1, '2p'), (3, 2, '3d')],
    save_path='radial_density.png'
)

# Visualizar nuvem 3D para orbital 3d
plot_electron_cloud(n=3, l=2, m=0, num_points=100000)
```

## 📁 Estrutura do Projeto

```
hydrogen-atom/
├── src/                          # Código fonte
│   ├── __init__.py              # Inicialização do pacote
│   ├── radial_wavefunction.py   # Funções de onda radiais
│   ├── electron_cloud_3d.py     # Nuvens eletrônicas 3D
│   └── orbital_slicing.py       # Animação de fatiamento
├── tests/                        # Testes automatizados
│   ├── __init__.py
│   ├── test_radial_wavefunction.py
│   └── test_electron_cloud.py
├── output/                       # Figuras e animações geradas
├── docs/                         # Documentação adicional
├── pics/                         # Imagens e recursos
├── olds/                         # Arquivos legados
├── requirements.txt              # Dependências Python
├── Makefile                      # Automação de tarefas
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Este arquivo
```

## 🧪 Testes

```bash
# Executar todos os testes
make test

# Executar testes manualmente
pytest tests/ -v --cov=src --cov-report=term-missing
```

## 📊 Exemplos de Saída

### Densidade de Probabilidade Radial
Mostra a probabilidade de encontrar o elétron em função da distância do núcleo para diferentes orbitais (1s, 2s, 2p, 3d).

### Nuvem Eletrônica 3D
Representação tridimensional da distribuição de probabilidade usando milhares de pontos gerados por Monte Carlo.

### Animação de Fatiamento
GIF animado mostrando fatias 2D do orbital em diferentes alturas, revelando a estrutura interna.

## 🛠️ Desenvolvimento

### Formatação de Código

```bash
make format  # Usa black
```

### Verificação de Estilo

```bash
make lint  # Usa flake8
```

### Adicionando Novos Recursos

1. Adicione código em `src/`
2. Adicione testes em `tests/`
3. Execute `make test` para validar
4. Execute `make format && make lint` para verificar estilo

## 📚 Documentação Adicional

Para uma explicação detalhada da teoria por trás das implementações, veja `docs/hidrogen-atom.md`.

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ✨ Autor

**Lineu Del Campo**

## 🙏 Agradecimentos

- Comunidade Python científica
- Desenvolvedores do NumPy, SciPy e Matplotlib
- Recursos educacionais de Mecânica Quântica

---

**Nota**: Este projeto foi desenvolvido com fins educacionais e de visualização científica.
