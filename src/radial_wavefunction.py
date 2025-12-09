"""
Módulo para cálculo e visualização de funções de onda radiais do átomo de Hidrogênio.

Este módulo implementa:
- Cálculo da função de onda radial R_nl(r)
- Densidade de probabilidade radial P(r) = r² |R_nl(r)|²
- Visualização de diferentes orbitais
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
from math import factorial
from typing import Tuple, List


def radial_wavefunction(n: int, l: int, r: np.ndarray) -> np.ndarray:
    """
    Calcula a função de onda radial R_nl(r) normalizada para o Hidrogênio.
    
    Parameters
    ----------
    n : int
        Número quântico principal (n ≥ 1)
    l : int
        Número quântico azimutal (0 ≤ l < n)
    r : np.ndarray
        Array de distâncias radiais em unidades de raio de Bohr (a0 = 1)
    
    Returns
    -------
    np.ndarray
        Valores da função de onda radial R_nl(r)
    
    Raises
    ------
    ValueError
        Se n < 1 ou l >= n ou l < 0
    """
    if n < 1:
        raise ValueError(f"n deve ser ≥ 1, recebido: {n}")
    if l < 0:
        raise ValueError(f"l deve ser ≥ 0, recebido: {l}")
    if l >= n:
        raise ValueError(f"l deve ser < n, recebido: l={l}, n={n}")
    
    scaled_r = (2 * r) / n
    prefactor = np.sqrt(
        (2 / n)**3 * factorial(n - l - 1) / (2 * n * factorial(n + l))
    )
    laguerre = genlaguerre(n - l - 1, 2 * l + 1)
    
    return prefactor * np.exp(-scaled_r / 2) * (scaled_r ** l) * laguerre(scaled_r)


def radial_probability_density(n: int, l: int, r: np.ndarray) -> np.ndarray:
    """
    Calcula a densidade de probabilidade radial P(r) = r² |R_nl(r)|².
    
    Parameters
    ----------
    n : int
        Número quântico principal
    l : int
        Número quântico azimutal
    r : np.ndarray
        Array de distâncias radiais
    
    Returns
    -------
    np.ndarray
        Densidade de probabilidade radial
    """
    R = radial_wavefunction(n, l, r)
    return (r**2) * (R**2)


def plot_radial_density(
    states: List[Tuple[int, int, str]] = None,
    r_max: float = 25.0,
    num_points: int = 1000,
    save_path: str = None
) -> None:
    """
    Plota a densidade de probabilidade radial para diferentes estados.
    
    Parameters
    ----------
    states : list of tuple, optional
        Lista de tuplas (n, l, label) para plotar.
        Default: [(1, 0, '1s'), (2, 0, '2s'), (2, 1, '2p'), (3, 2, '3d')]
    r_max : float, optional
        Distância radial máxima (em a0). Default: 25.0
    num_points : int, optional
        Número de pontos para o grid radial. Default: 1000
    save_path : str, optional
        Caminho para salvar a figura. Se None, apenas exibe.
    """
    if states is None:
        states = [(1, 0, '1s'), (2, 0, '2s'), (2, 1, '2p'), (3, 2, '3d')]
    
    r = np.linspace(0, r_max, num_points)
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for n, l, label in states:
        P = radial_probability_density(n, l, r)
        ax.plot(r, P, label=f'Orbital {label} (n={n}, l={l})', linewidth=2)
    
    ax.set_title(
        'Densidade de Probabilidade Radial do Hidrogênio', 
        fontsize=16, 
        color='white'
    )
    ax.set_xlabel('Distância do Núcleo ($r/a_0$)', fontsize=12)
    ax.set_ylabel('Probabilidade $P(r)$', fontsize=12)
    ax.legend()
    ax.grid(alpha=0.2)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura salva em: {save_path}")
    else:
        plt.show()


def main():
    """Função principal para execução standalone do módulo."""
    plot_radial_density()


if __name__ == "__main__":
    main()
