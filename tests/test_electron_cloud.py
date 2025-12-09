"""
Testes para o módulo electron_cloud_3d.py
"""

import pytest
import numpy as np
from src.electron_cloud_3d import (
    hydrogen_wavefunction,
    generate_electron_cloud
)


class TestHydrogenWavefunction:
    """Testes para função de onda completa do hidrogênio."""
    
    def test_wavefunction_shape(self):
        """Testa se função retorna valores do tamanho correto."""
        n, l, m = 2, 1, 0
        r = np.array([1.0, 2.0, 3.0])
        theta = np.array([0.5, 1.0, 1.5])
        phi = np.array([0.0, 1.0, 2.0])
        
        psi = hydrogen_wavefunction(n, l, m, r, theta, phi)
        
        assert len(psi) == len(r)
    
    def test_wavefunction_complex(self):
        """Testa se função retorna valores complexos para m != 0."""
        n, l, m = 2, 1, 1
        r = np.array([1.0])
        theta = np.array([1.0])
        phi = np.array([1.0])
        
        psi = hydrogen_wavefunction(n, l, m, r, theta, phi)
        
        # Para m != 0, a função pode ter parte imaginária
        assert np.iscomplexobj(psi)


class TestElectronCloud:
    """Testes para geração de nuvem eletrônica."""
    
    def test_cloud_generation(self):
        """Testa se nuvem é gerada com sucesso."""
        n, l, m = 1, 0, 0
        cloud = generate_electron_cloud(n, l, m, num_points=100, verbose=False)
        
        # Deve retornar array 2D
        assert cloud.ndim == 2
        # Deve ter 3 coordenadas (x, y, z)
        assert cloud.shape[1] == 3
    
    def test_cloud_minimum_points(self):
        """Testa se gera pelo menos alguns pontos."""
        n, l, m = 2, 1, 0
        cloud = generate_electron_cloud(n, l, m, num_points=50, verbose=False)
        
        # Deve gerar pelo menos alguns pontos
        assert len(cloud) > 0
