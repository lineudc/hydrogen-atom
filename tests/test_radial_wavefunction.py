"""
Testes para o módulo radial_wavefunction.py
"""

import pytest
import numpy as np
from src.radial_wavefunction import (
    radial_wavefunction,
    radial_probability_density
)


class TestRadialWavefunction:
    """Testes para função de onda radial."""
    
    def test_radial_wavefunction_1s(self):
        """Testa função de onda para estado fundamental 1s."""
        n, l = 1, 0
        r = np.array([0.0, 1.0, 2.0])
        R = radial_wavefunction(n, l, r)
        
        # Deve retornar array do mesmo tamanho
        assert len(R) == len(r)
        # Valores devem ser reais para l=0, m=0
        assert np.all(np.isreal(R))
    
    def test_radial_wavefunction_invalid_n(self):
        """Testa se levanta exceção para n inválido."""
        with pytest.raises(ValueError):
            radial_wavefunction(0, 0, np.array([1.0]))
    
    def test_radial_wavefunction_invalid_l(self):
        """Testa se levanta exceção para l >= n."""
        with pytest.raises(ValueError):
            radial_wavefunction(2, 2, np.array([1.0]))
    
    def test_radial_wavefunction_negative_l(self):
        """Testa se levanta exceção para l negativo."""
        with pytest.raises(ValueError):
            radial_wavefunction(2, -1, np.array([1.0]))
    
    def test_probability_density_normalization(self):
        """Testa se densidade de probabilidade está razoavelmente normalizada."""
        n, l = 2, 1
        r = np.linspace(0, 50, 10000)
        P = radial_probability_density(n, l, r)
        
        # Integração numérica usando regra do trapézio
        # ∫ P(r) dr deve ser próximo de 1
        dr = r[1] - r[0]
        integral = np.trapz(P, dx=dr)
        
        # Tolerância de 1% devido à aproximação numérica
        assert abs(integral - 1.0) < 0.01
    
    def test_probability_density_nonnegative(self):
        """Testa se densidade de probabilidade é não-negativa."""
        n, l = 3, 2
        r = np.linspace(0, 30, 1000)
        P = radial_probability_density(n, l, r)
        
        assert np.all(P >= 0)
