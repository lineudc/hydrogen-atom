"""
Módulo para geração e visualização de nuvens eletrônicas 3D do átomo de Hidrogênio.

Este módulo implementa:
- Cálculo completo da função de onda ψ(r,θ,φ) = R_nl(r) * Y_lm(θ,φ)
- Geração de nuvens de pontos usando Monte Carlo (rejection sampling)
- Visualização 3D interativa dos orbitais
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm, genlaguerre
from math import factorial
from typing import Tuple


def hydrogen_wavefunction(
    n: int, 
    l: int, 
    m: int, 
    r: np.ndarray, 
    theta: np.ndarray, 
    phi: np.ndarray
) -> np.ndarray:
    """
    Calcula a função de onda completa do átomo de Hidrogênio.
    
    ψ(r,θ,φ) = R_nl(r) * Y_lm(θ,φ)
    
    Parameters
    ----------
    n : int
        Número quântico principal (n ≥ 1)
    l : int
        Número quântico azimutal (0 ≤ l < n)
    m : int
        Número quântico magnético (-l ≤ m ≤ l)
    r : np.ndarray
        Coordenada radial
    theta : np.ndarray
        Ângulo polar (0 a π)
    phi : np.ndarray
        Ângulo azimutal (0 a 2π)
    
    Returns
    -------
    np.ndarray
        Valores complexos da função de onda
    """
    # Parte Radial
    rho = (2.0 * r) / n
    prefactor_r = np.sqrt(
        ((2.0/n)**3 * factorial(n-l-1)) / (2.0*n*factorial(n+l))
    )
    L = genlaguerre(n-l-1, 2*l+1)(rho)
    R_nl = prefactor_r * np.exp(-rho/2) * (rho**l) * L
    
    # Parte Angular (Harmônicas Esféricas)
    Y_lm = sph_harm(m, l, phi, theta)
    
    return R_nl * Y_lm


def generate_electron_cloud(
    n: int, 
    l: int, 
    m: int, 
    num_points: int = 50000,
    max_attempts_multiplier: int = 200,
    verbose: bool = True
) -> np.ndarray:
    """
    Gera uma nuvem de pontos usando o método de Monte Carlo (Rejection Sampling).
    
    Parameters
    ----------
    n : int
        Número quântico principal
    l : int
        Número quântico azimutal
    m : int
        Número quântico magnético
    num_points : int, optional
        Número de pontos desejado. Default: 50000
    max_attempts_multiplier : int, optional
        Multiplicador para tentativas máximas. Default: 200
    verbose : bool, optional
        Se True, imprime mensagens de progresso. Default: True
    
    Returns
    -------
    np.ndarray
        Array (N, 3) com coordenadas (x, y, z) dos pontos
    """
    if verbose:
        print(f"Gerando nuvem para Orbital ({n},{l},{m})... Aguarde.")
    
    points = []
    max_val = 0.2  # Valor estimado para normalização da rejeição
    box_size = n * 5 + 5  # Tamanho da caixa depende de n
    
    count = 0
    max_attempts = num_points * max_attempts_multiplier
    
    while len(points) < num_points and count < max_attempts:
        # 1. Escolher ponto aleatório no espaço 3D
        x, y, z = np.random.uniform(-box_size, box_size, 3)
        
        # 2. Converter para coordenadas esféricas
        r = np.sqrt(x**2 + y**2 + z**2)
        if r == 0:
            continue
            
        theta = np.arccos(z/r)
        phi = np.arctan2(y, x)
        
        # 3. Calcular densidade de probabilidade |ψ|²
        psi = hydrogen_wavefunction(n, l, m, r, theta, phi)
        prob_density = np.abs(psi)**2
        
        # 4. Método de Rejeição
        if np.random.uniform(0, max_val) < prob_density:
            points.append((x, y, z))
        
        count += 1
    
    if verbose:
        efficiency = len(points) / count * 100 if count > 0 else 0
        print(f"Gerados {len(points)} pontos em {count} tentativas ({efficiency:.1f}% de eficiência)")
    
    return np.array(points)


def plot_electron_cloud(
    n: int, 
    l: int, 
    m: int, 
    num_points: int = 50000,
    save_path: str = None,
    figsize: Tuple[int, int] = (10, 10)
) -> None:
    """
    Plota a nuvem eletrônica 3D para um orbital específico.
    
    Parameters
    ----------
    n : int
        Número quântico principal
    l : int
        Número quântico azimutal
    m : int
        Número quântico magnético
    num_points : int, optional
        Número de pontos na nuvem. Default: 50000
    save_path : str, optional
        Caminho para salvar a figura. Se None, apenas exibe.
    figsize : tuple, optional
        Tamanho da figura. Default: (10, 10)
    """
    cloud = generate_electron_cloud(n, l, m, num_points)
    
    if len(cloud) == 0:
        print("Erro: Nenhum ponto foi gerado!")
        return
    
    x, y, z = cloud[:, 0], cloud[:, 1], cloud[:, 2]
    
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    
    # Estética escura e elegante
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    # Plot da nuvem com transparência para efeito de volume
    scatter = ax.scatter(x, y, z, s=0.5, c=z, cmap='inferno', alpha=0.3)
    
    # Adiciona colorbar
    plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8, label='Altura Z')
    
    # Remover eixos para visual limpo
    ax.set_axis_off()
    
    # Título
    orbital_names = {0: 's', 1: 'p', 2: 'd', 3: 'f'}
    orbital_name = orbital_names.get(l, f'l={l}')
    plt.title(
        f'Orbital de Hidrogênio: {n}{orbital_name} (m={m})', 
        color='white', 
        size=20
    )
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='black')
        print(f"Figura salva em: {save_path}")
    else:
        plt.show()


def main():
    """Função principal para execução standalone do módulo."""
    # Configuração padrão: orbital 3d (m=0)
    n, l, m = 3, 2, 0
    plot_electron_cloud(n, l, m)


if __name__ == "__main__":
    main()
