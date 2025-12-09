# 🏗️ Arquitetura do Projeto - Hydrogen Atom

## 📐 Visão Geral da Estrutura

```mermaid
flowchart TB
    subgraph User["👤 Usuário"]
        CLI["🖥️ Command Line Interface"]
        Make["⚙️ Makefile Commands"]
        Python["🐍 Python Scripts"]
    end
    
    subgraph Project["📦 Projeto Hydrogen Atom"]
        direction TB
        
        subgraph Src["📁 src/ - Código Fonte"]
            Init["__init__.py<br/>v1.0.2"]
            Radial["radial_wavefunction.py<br/>Funções Radiais"]
            Cloud["electron_cloud_3d.py<br/>Nuvens 3D"]
            Slicing["orbital_slicing.py<br/>Animações"]
        end
        
        subgraph Tests["🧪 tests/ - Testes"]
            TestRadial["test_radial_wavefunction.py<br/>6 testes"]
            TestCloud["test_electron_cloud.py<br/>4 testes"]
        end
        
        subgraph Output["📊 output/ - Saídas"]
            RadialPNG["radial_density.png"]
            CloudPNG["electron_cloud_*.png"]
            SlicingGIF["orbital_slicing_3d.gif"]
        end
        
        subgraph Config["⚙️ Configuração"]
            Req["requirements.txt"]
            Git[".gitignore"]
            Setup["setup.cfg"]
            MakeFile["Makefile"]
        end
        
        subgraph Docs["📚 docs/ - Documentação"]
            Theory["hidrogen-atom.md<br/>Teoria Física"]
            Report["RELATORIO_REORGANIZACAO.md"]
            Summary["RESUMO_EXECUTIVO.md"]
        end
    end
    
    subgraph Deps["📚 Dependências Externas"]
        NumPy["NumPy<br/>Computação Numérica"]
        SciPy["SciPy<br/>Funções Especiais"]
        MatPlot["Matplotlib<br/>Visualização"]
        Pillow["Pillow<br/>Exportar GIF"]
    end
    
    CLI --> Make
    Make --> Python
    Python --> Src
    
    Radial --> Output
    Cloud --> Output
    Slicing --> Output
    
    Radial --> NumPy
    Radial --> SciPy
    Radial --> MatPlot
    
    Cloud --> NumPy
    Cloud --> SciPy
    Cloud --> MatPlot
    
    Slicing --> NumPy
    Slicing --> SciPy
    Slicing --> MatPlot
    Slicing --> Pillow
    
    Tests -.->|testa| Src
    
    style User fill:#e1f5ff,stroke:#0066cc,stroke-width:2px
    style Project fill:#f0f0f0,stroke:#333,stroke-width:3px
    style Deps fill:#fff5e1,stroke:#ff9900,stroke-width:2px
    style Output fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

## 🔄 Fluxo de Execução

```mermaid
flowchart LR
    Start(("🚀 Início")) --> Setup{"Setup<br/>Executado?"}
    
    Setup -->|Não| MakeSetup["make setup"]
    MakeSetup --> CreateVenv["Criar venv/"]
    CreateVenv --> InstallDeps["Instalar<br/>Dependências"]
    InstallDeps --> Ready["✅ Pronto"]
    
    Setup -->|Sim| Ready
    
    Ready --> Choice{"Escolher<br/>Visualização"}
    
    Choice -->|Radial| RunRadial["make run-radial"]
    Choice -->|Nuvem 3D| RunCloud["make run-cloud"]
    Choice -->|Animação| RunSlicing["make run-slicing"]
    
    RunRadial --> ImportRadial["Importar<br/>radial_wavefunction.py"]
    RunCloud --> ImportCloud["Importar<br/>electron_cloud_3d.py"]
    RunSlicing --> ImportSlicing["Importar<br/>orbital_slicing.py"]
    
    ImportRadial --> CalcRadial["Calcular R_nl(r)"]
    ImportCloud --> CalcCloud["Calcular ψ(r,θ,φ)"]
    ImportSlicing --> CalcSlicing["Calcular ψ(r,θ,φ)"]
    
    CalcRadial --> PlotRadial["Plotar P(r) = r²|R|²"]
    CalcCloud --> MonteCarlo["Monte Carlo<br/>Rejection Sampling"]
    CalcSlicing --> CreateSlices["Criar Fatias Z"]
    
    MonteCarlo --> Plot3D["Plotar<br/>Nuvem 3D"]
    CreateSlices --> Animate["Gerar<br/>Animação"]
    
    PlotRadial --> SaveRadial["💾 output/<br/>radial_density.png"]
    Plot3D --> SaveCloud["💾 output/<br/>electron_cloud_*.png"]
    Animate --> SaveSlicing["💾 output/<br/>orbital_slicing_3d.gif"]
    
    SaveRadial --> End(("✅ Fim"))
    SaveCloud --> End
    SaveSlicing --> End
    
    style Start fill:#4caf50,stroke:#2e7d32,stroke-width:3px,color:#fff
    style End fill:#4caf50,stroke:#2e7d32,stroke-width:3px,color:#fff
    style Setup fill:#ff9800,stroke:#e65100,stroke-width:2px
    style Choice fill:#2196f3,stroke:#0d47a1,stroke-width:2px
```

## 🧮 Fluxo de Cálculos Físicos

```mermaid
flowchart TB
    subgraph Input["⚙️ Parâmetros de Entrada"]
        NQN["n: Número Quântico Principal"]
        LQN["l: Número Quântico Azimutal"]
        MQN["m: Número Quântico Magnético"]
    end
    
    subgraph Radial["📊 Parte Radial R_nl(r)"]
        Rho["ρ = 2r/n"]
        Prefactor["Prefator de<br/>Normalização"]
        Laguerre["Polinômios de<br/>Laguerre L_n^l(ρ)"]
        Rnl["R_nl(r) = C × e^(-ρ/2) × ρ^l × L(ρ)"]
    end
    
    subgraph Angular["🌐 Parte Angular Y_lm(θ,φ)"]
        Theta["θ: Ângulo Polar"]
        Phi["φ: Ângulo Azimutal"]
        SphHarm["Harmônicas<br/>Esféricas Y_lm"]
    end
    
    subgraph Complete["✨ Função de Onda Completa"]
        Psi["ψ(r,θ,φ) = R_nl(r) × Y_lm(θ,φ)"]
        Prob["Probabilidade = |ψ|²"]
    end
    
    subgraph Visualizations["📈 Visualizações"]
        ProbRadial["P(r) = r² |R_nl(r)|²<br/>Densidade Radial"]
        Cloud3D["Nuvem 3D<br/>Monte Carlo"]
        Slices["Fatias 2D<br/>Animação"]
    end
    
    NQN --> Rho
    LQN --> Prefactor
    LQN --> Laguerre
    
    Rho --> Rnl
    Prefactor --> Rnl
    Laguerre --> Rnl
    
    LQN --> SphHarm
    MQN --> SphHarm
    Theta --> SphHarm
    Phi --> SphHarm
    
    Rnl --> Psi
    SphHarm --> Psi
    
    Psi --> Prob
    
    Rnl --> ProbRadial
    Prob --> Cloud3D
    Prob --> Slices
    
    style Input fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style Radial fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style Angular fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Complete fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style Visualizations fill:#fce4ec,stroke:#c2185b,stroke-width:2px
```

## 🧪 Fluxo de Testes

```mermaid
flowchart LR
    Start(("▶️ make test")) --> Pytest["🧪 pytest"]
    
    Pytest --> TestRadial["test_radial_wavefunction.py"]
    Pytest --> TestCloud["test_electron_cloud.py"]
    
    TestRadial --> T1["✓ test_radial_wavefunction_1s"]
    TestRadial --> T2["✓ test_invalid_n"]
    TestRadial --> T3["✓ test_invalid_l"]
    TestRadial --> T4["✓ test_negative_l"]
    TestRadial --> T5["✓ test_normalization"]
    TestRadial --> T6["✓ test_nonnegative"]
    
    TestCloud --> T7["✓ test_wavefunction_shape"]
    TestCloud --> T8["✓ test_wavefunction_complex"]
    TestCloud --> T9["✓ test_cloud_generation"]
    TestCloud --> T10["✓ test_cloud_minimum_points"]
    
    T1 --> Coverage["📊 Coverage Report"]
    T2 --> Coverage
    T3 --> Coverage
    T4 --> Coverage
    T5 --> Coverage
    T6 --> Coverage
    T7 --> Coverage
    T8 --> Coverage
    T9 --> Coverage
    T10 --> Coverage
    
    Coverage --> Result{"Todos<br/>Passaram?"}
    
    Result -->|Sim| Success(("✅ 10/10<br/>Sucesso"))
    Result -->|Não| Fail(("❌ Falha"))
    
    style Start fill:#2196f3,stroke:#0d47a1,stroke-width:2px,color:#fff
    style Success fill:#4caf50,stroke:#2e7d32,stroke-width:3px,color:#fff
    style Fail fill:#f44336,stroke:#c62828,stroke-width:3px,color:#fff
    style Pytest fill:#9c27b0,stroke:#4a148c,stroke-width:2px,color:#fff
```

## 📦 Estrutura de Módulos

```mermaid
flowchart TB
    subgraph Package["📦 hydrogen-atom"]
        direction TB
        
        Init["__init__.py<br/>__version__ = '1.0.2'"]
        
        subgraph Modules["🔧 Módulos Principais"]
            Radial["radial_wavefunction.py"]
            Cloud["electron_cloud_3d.py"]
            Slicing["orbital_slicing.py"]
        end
        
        subgraph Functions["⚙️ Funções Exportadas"]
            F1["radial_wavefunction(n, l, r)"]
            F2["radial_probability_density(n, l, r)"]
            F3["plot_radial_density(...)"]
            F4["hydrogen_wavefunction(n, l, m, r, θ, φ)"]
            F5["generate_electron_cloud(n, l, m, ...)"]
            F6["plot_electron_cloud(n, l, m, ...)"]
            F7["hydrogen_wavefunction_slice(...)"]
            F8["create_orbital_slicing_animation(...)"]
        end
    end
    
    Init -.-> Modules
    
    Radial --> F1
    Radial --> F2
    Radial --> F3
    
    Cloud --> F4
    Cloud --> F5
    Cloud --> F6
    
    Slicing --> F7
    Slicing --> F8
    
    F1 --> scipy["scipy.special.genlaguerre"]
    F4 --> scipy2["scipy.special.sph_harm_y"]
    F7 --> scipy3["scipy.special.sph_harm_y"]
    
    F3 --> mpl["matplotlib.pyplot"]
    F6 --> mpl2["matplotlib.pyplot"]
    F8 --> mpl3["matplotlib.animation"]
    
    style Package fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px
    style Modules fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    style Functions fill:#e0f2f1,stroke:#00695c,stroke-width:2px
```

## 🎨 Diagrama de Classes Simplificado

```mermaid
classDiagram
    class RadialWavefunction {
        +radial_wavefunction(n, l, r) ndarray
        +radial_probability_density(n, l, r) ndarray
        +plot_radial_density(states, r_max, num_points, save_path)
        +main()
    }
    
    class ElectronCloud3D {
        +hydrogen_wavefunction(n, l, m, r, θ, φ) ndarray
        +generate_electron_cloud(n, l, m, num_points) ndarray
        +plot_electron_cloud(n, l, m, num_points, save_path)
        +main()
    }
    
    class OrbitalSlicing {
        +hydrogen_wavefunction_slice(n, l, m, r, θ, φ) ndarray
        +create_orbital_slicing_animation(n, l, m, grid_limit, ...)
        +main()
    }
    
    class QuantumNumbers {
        <<dataclass>>
        +int n
        +int l
        +int m
    }
    
    RadialWavefunction ..> QuantumNumbers : usa
    ElectronCloud3D ..> QuantumNumbers : usa
    OrbitalSlicing ..> QuantumNumbers : usa
    
    ElectronCloud3D --|> RadialWavefunction : estende conceito
    OrbitalSlicing --|> ElectronCloud3D : estende conceito
```

## 🔗 Dependências e Integrações

```mermaid
flowchart TB
    subgraph External["🌐 Bibliotecas Externas"]
        NumPy["NumPy 1.26.4<br/>Arrays e Computação"]
        SciPy["SciPy 1.16.3<br/>Funções Especiais"]
        Matplotlib["Matplotlib 3.10.7<br/>Plotagem"]
        Pillow["Pillow 10.4.0<br/>Processamento Imagem"]
    end
    
    subgraph Internal["📦 Módulos Internos"]
        Radial["radial_wavefunction.py"]
        Cloud["electron_cloud_3d.py"]
        Slicing["orbital_slicing.py"]
    end
    
    subgraph DevTools["🛠️ Ferramentas Dev"]
        Pytest["pytest 7.4.4"]
        Black["black 23.12.1"]
        Flake8["flake8 6.1.0"]
        Coverage["pytest-cov 4.1.0"]
    end
    
    NumPy --> Radial
    NumPy --> Cloud
    NumPy --> Slicing
    
    SciPy --> Radial
    SciPy --> Cloud
    SciPy --> Slicing
    
    Matplotlib --> Radial
    Matplotlib --> Cloud
    Matplotlib --> Slicing
    
    Pillow --> Slicing
    
    Pytest -.->|testa| Internal
    Black -.->|formata| Internal
    Flake8 -.->|verifica| Internal
    Coverage -.->|analisa| Internal
    
    style External fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    style Internal fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
    style DevTools fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

## 📁 Mapeamento de Arquivos

```mermaid
graph TB
    Root["📁 hydrogen-atom/"]
    
    Root --> Src["📁 src/"]
    Root --> Tests["📁 tests/"]
    Root --> Output["📁 output/"]
    Root --> Docs["📁 docs/"]
    Root --> Olds["📁 olds/"]
    Root --> Pics["📁 pics/"]
    Root --> Venv["📁 venv/"]
    
    Src --> SrcInit["__init__.py"]
    Src --> SrcRadial["radial_wavefunction.py"]
    Src --> SrcCloud["electron_cloud_3d.py"]
    Src --> SrcSlicing["orbital_slicing.py"]
    
    Tests --> TestInit["__init__.py"]
    Tests --> TestRadial["test_radial_wavefunction.py"]
    Tests --> TestCloud["test_electron_cloud.py"]
    
    Output --> OutReadme["README.md"]
    Output --> OutRadial["radial_density.png"]
    Output --> OutCloud["electron_cloud_*.png"]
    Output --> OutSlicing["orbital_slicing_3d.gif"]
    
    Docs --> DocsTheory["hidrogen-atom.md"]
    Docs --> DocsReport["RELATORIO_REORGANIZACAO.md"]
    Docs --> DocsSummary["RESUMO_EXECUTIVO.md"]
    Docs --> DocsArch["ARCHITECTURE.md"]
    
    Root --> Makefile["Makefile"]
    Root --> Req["requirements.txt"]
    Root --> Git[".gitignore"]
    Root --> Setup["setup.cfg"]
    Root --> License["LICENSE"]
    Root --> Readme["README.md"]
    Root --> Quick["QUICKSTART.md"]
    Root --> Change["CHANGELOG.md"]
    Root --> LeiaMe["LEIA-ME.md"]
    Root --> Status["PROJECT_STATUS.md"]
    
    style Root fill:#ffeb3b,stroke:#f57f17,stroke-width:4px
    style Src fill:#4caf50,stroke:#2e7d32,stroke-width:2px
    style Tests fill:#2196f3,stroke:#0d47a1,stroke-width:2px
    style Output fill:#ff9800,stroke:#e65100,stroke-width:2px
    style Docs fill:#9c27b0,stroke:#4a148c,stroke-width:2px
```

---

**Legenda**:
- 🚀 Pontos de entrada
- 📊 Dados/Saídas
- ⚙️ Configuração
- 🧪 Testes
- 📚 Documentação
- 🔧 Processamento
- ✅ Sucesso
- ❌ Erro
