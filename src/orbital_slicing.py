"""
Módulo para animação de fatiamento de orbitais do átomo de Hidrogênio.

Este módulo cria animações 2D mostrando fatias transversais dos orbitais
em diferentes alturas, revelando a estrutura interna da distribuição de probabilidade.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.special import sph_harm, genlaguerre
from math import factorial
from typing import Optional


def hydrogen_wavefunction_slice(
    n: int, 
    l: int, 
    m: int, 
    r: np.ndarray, 
    theta: np.ndarray, 
    phi: np.ndarray
) -> np.ndarray:
    """
    Calcula a função de onda do átomo de Hidrogênio com tratamento de singularidades.
    
    Parameters
    ----------
    n : int
        Número quântico principal
    l : int
        Número quântico azimutal
    m : int
        Número quântico magnético
    r : np.ndarray
        Coordenada radial
    theta : np.ndarray
        Ângulo polar
    phi : np.ndarray
        Ângulo azimutal
    
    Returns
    -------
    np.ndarray
        Valores da função de onda (com NaNs substituídos por zero)
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        rho = (2.0 * r) / n
        prefactor_r = np.sqrt(
            ((2.0/n)**3 * factorial(n-l-1)) / (2.0*n*factorial(n+l))
        )
        L = genlaguerre(n-l-1, 2*l+1)(rho)
        R_nl = prefactor_r * np.exp(-rho/2) * (rho**l) * L
        Y_lm = sph_harm(m, l, phi, theta)
        psi = R_nl * Y_lm
        # Corrige NaNs que podem ocorrer na origem (r=0)
        psi[np.isnan(psi)] = 0
    
    return psi


def create_orbital_slicing_animation(
    n: int = 3,
    l: int = 2,
    m: int = 0,
    grid_limit: float = 18.0,
    resolution: int = 250,
    frames: int = 60,
    output_file: str = "orbital_slicing.gif",
    fps: int = 15,
    cmap: str = 'magma',
    verbose: bool = True
) -> None:
    """
    Cria uma animação de fatiamento de orbital.
    
    Parameters
    ----------
    n : int, optional
        Número quântico principal. Default: 3
    l : int, optional
        Número quântico azimutal. Default: 2
    m : int, optional
        Número quântico magnético. Default: 0
    grid_limit : float, optional
        Tamanho da caixa em raios de Bohr. Default: 18.0
    resolution : int, optional
        Resolução da imagem 2D. Default: 250
    frames : int, optional
        Número de fatias na animação. Default: 60
    output_file : str, optional
        Nome do arquivo de saída. Default: "orbital_slicing.gif"
    fps : int, optional
        Frames por segundo. Default: 15
    cmap : str, optional
        Colormap do matplotlib. Default: 'magma'
    verbose : bool, optional
        Se True, imprime mensagens de progresso. Default: True
    """
    if verbose:
        print(f"Configurando animação para orbital ({n},{l},{m})...")
    
    # Preparação da Grade 2D
    x_1d = np.linspace(-grid_limit, grid_limit, resolution)
    y_1d = np.linspace(-grid_limit, grid_limit, resolution)
    X_grid, Y_grid = np.meshgrid(x_1d, y_1d)
    
    # Definindo os planos Z que vamos fatiar
    z_slices = np.linspace(-grid_limit, grid_limit, frames)
    
    # Configuração do Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('black')
    
    # Encontrar densidade máxima global para fixar escala de cores
    if verbose:
        print("Calculando escala global de cores... Aguarde.")
    
    max_density_global = 0
    test_z = [0, grid_limit/2, -grid_limit/2]
    
    for tz in test_z:
        R_test = np.sqrt(X_grid**2 + Y_grid**2 + tz**2)
        with np.errstate(divide='ignore', invalid='ignore'):
            T_test = np.arccos(tz / R_test)
        P_test = np.arctan2(Y_grid, X_grid)
        psi_test = hydrogen_wavefunction_slice(n, l, m, R_test, T_test, P_test)
        max_density_global = max(max_density_global, np.max(np.abs(psi_test)**2))
    
    # Configuração inicial da imagem
    im = ax.imshow(
        np.zeros_like(X_grid),
        extent=[-grid_limit, grid_limit, -grid_limit, grid_limit],
        cmap=cmap,
        origin='lower',
        vmin=0,
        vmax=max_density_global * 0.8
    )
    
    colorbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    colorbar.set_label('Densidade de Probabilidade $|\\psi|^2$')
    ax.set_xlabel('X ($a_0$)')
    ax.set_ylabel('Y ($a_0$)')
    title_text = ax.set_title('', color='white', fontsize=14)
    
    # Função de atualização da animação
    def update(frame_idx):
        current_z = z_slices[frame_idx]
        
        Z_grid = np.full_like(X_grid, current_z)
        R_grid = np.sqrt(X_grid**2 + Y_grid**2 + Z_grid**2)
        
        with np.errstate(divide='ignore', invalid='ignore'):
            Theta_grid = np.arccos(Z_grid / R_grid)
        
        Phi_grid = np.arctan2(Y_grid, X_grid)
        
        psi = hydrogen_wavefunction_slice(n, l, m, R_grid, Theta_grid, Phi_grid)
        prob_density_slice = np.abs(psi)**2
        
        im.set_data(prob_density_slice)
        
        orbital_names = {0: 's', 1: 'p', 2: 'd', 3: 'f'}
        orbital_name = orbital_names.get(l, f'l={l}')
        title_text.set_text(
            f'Fatiando Orbital {n}{orbital_name} (m={m})\\n'
            f'Altura Z = {current_z:.2f} $a_0$'
        )
        
        return im, title_text
    
    # Gerar e salvar animação
    if verbose:
        print(f"Gerando animação de {frames} quadros. Isso pode levar um minuto...")
    
    anim = FuncAnimation(fig, update, frames=frames, interval=1000//fps, blit=True)
    
    # Salva como GIF
    anim.save(output_file, writer='pillow', fps=fps)
    
    if verbose:
        print(f"Concluído! Animação salva como: {output_file}")
    
    plt.close()


def main():
    """Função principal para execução standalone do módulo."""
    create_orbital_slicing_animation(
        n=3,
        l=2,
        m=0,
        output_file='orbital_slicing_3d.gif'
    )


if __name__ == "__main__":
    main()
