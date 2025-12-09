## Equação de Schrödinger para o átomo de Hidrogênio em 3D

<b>1. A Equação Mestra</b>

O átomo de Hidrogênio consiste em um elétron orbitando um próton. 

O potencial é Coulombiano: 

$$V(r) = - \frac{e^2}{4\pi\epsilon_0 r}$$.

A equação de Schrödinger independente do tempo é:

$$\hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r})$$

Expandindo o Laplaciano em coordenadas esféricas $(r, \theta, \phi)$, a função de onda $\psi$ pode ser separada em duas partes: 
- uma radial e
- uma angular.

$$\psi_{n,l,m}(r, \theta, \phi) = \underbrace{R_{nl}(r)}_{\text{Radial}} \cdot \underbrace{Y_{lm}(\theta, \phi)}_{\text{Angular}}$$

Onde os números quânticos definem o estado: 

- $n$ (Principal): Energia e tamanho do orbital ($1, 2, 3...$).
- $l$ (Azimutal): Forma do orbital ($0$ a $n-1$). ($l=0 \to s$, $l=1 \to p$, $l=2 \to d$).
- $m$ (Magnético): Orientação espacial ($-l$ a $+l$).

![alt text](pics/hidrogen-licensed-image.jpeg)

<b>2. A Matemática das Partes</b>

<b>A. Parte Radial ($R_{nl}$)</b>
Descreve a probabilidade de encontrar o elétron a uma certa distância do núcleo. Envolve os Polinômios Associados de Laguerre. A densidade de probabilidade radial não é apenas $R^2$, mas sim 

$P(r) = r^2 |R_{nl}(r)|^2$ 

(devido ao volume da casca esférica).

<b>B. Parte Angular ($Y_{lm}$)</b>
Descreve a forma geométrica. São as famosas <i>Harmônicas Esféricas</i>.

<b>3. Visualização Computacional (Python & VS Code)</b>

Para visualizar isso de forma "impactante" e elegante, não usaremos apenas linhas. Vamos criar uma Nuvem de Probabilidade de Monte Carlo.

<b>4. Insights Físicos e O Que Observar</b>

Ao rodar os scripts acima, preste atenção nestes detalhes fundamentais:

- A Natureza Probabilística: O gráfico 3D não mostra uma "casca" sólida. Ele mostra onde é mais provável que o elétron interaja. As regiões mais densas e brilhantes (cores quentes no script) são as de maior probabilidade.
- Nós Radiais (Radial Nodes): No primeiro script (gráfico 2D), note que para orbitais maiores (ex: 2s, 3s), a probabilidade toca o zero em certos raios antes de subir novamente. Esses são os "nós", regiões onde a probabilidade de encontrar o elétron é nula.
    - Regra de Ouro: Número de nós radiais = $n - l - 1$.

- Forma (Angular):
    - Mude l=0 no script 3D: Você verá uma esfera perfeita ($s$).
    - Mude l=1: Você verá o formato de "halteres" ($p$).
    - Mude l=2: Você verá formatos complexos de trevos ou halteres com anéis (como o $3d_{z^2}$).

<b>5. Por que isso é elegante?</b>

A elegância reside no fato de que toda essa complexidade visual — lóbulos, anéis, nuvens — emerge de uma única equação diferencial linear. 
Não desenhamos essas formas manualmente; a natureza as dita através das condições de contorno da matemática.

---

# ⚛️ Hydrogen Atom Wavefunction Visualization

Visualização computacional das soluções da Equação de Schrödinger para o átomo de Hidrogênio em 3D, utilizando Python, Métodos de Monte Carlo e Fatiamento de Densidade de Probabilidade.

![Hydrogen Orbital Animation](fatiamento_orbital_3d.gif)
*(Certifique-se de que o gif gerado esteja na raiz do repo ou em uma pasta /assets)*

## 📋 Sobre o Projeto

Este projeto resolve a parte radial e angular da função de onda do Hidrogênio $\psi_{n,l,m}(r, \theta, \phi)$ e utiliza técnicas de visualização científica para renderizar:

1.  **Densidade Radial:** A probabilidade de encontrar o elétron a uma distância $r$ do núcleo.
2.  **Nuvem de Pontos 3D:** Utilizando amostragem por rejeição (Monte Carlo) para simular a natureza probabilística do orbital.
3.  **Fatiamento Interno (Slicing):** Animação de corte transversal para visualização dos nós radiais e angulares internos.

## 🚀 Tecnologias

* **Python 3.x**
* **NumPy:** Álgebra linear e grids.
* **SciPy:** Polinômios de Laguerre e Harmônicas Esféricas (`scipy.special`).
* **Matplotlib:** Plotagem 3D, Heatmaps e Animação.

## 🧠 Física

A solução baseia-se na separação de variáveis em coordenadas esféricas:

$$\psi_{n,l,m}(r, \theta, \phi) = R_{nl}(r) Y_{lm}(\theta, \phi)$$

Onde $n, l, m$ são os números quânticos principais, azimutais e magnéticos.

## 📦 Como Rodar

1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install numpy matplotlib scipy pillow