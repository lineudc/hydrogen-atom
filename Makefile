# Makefile para o projeto Hydrogen Atom
# =======================================
# Automatiza setup, execução e testes do projeto

.PHONY: help setup venv install clean test run-radial run-cloud run-slicing format lint all

# Configurações
PYTHON := python3
VENV := venv
VENV_BIN := $(VENV)/bin
PIP := $(VENV_BIN)/pip
PYTHON_VENV := $(VENV_BIN)/python

# Cores para output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

# Target padrão
help:
	@echo "$(BLUE)Hydrogen Atom - Sistema de Build$(NC)"
	@echo ""
	@echo "$(GREEN)Comandos disponíveis:$(NC)"
	@echo "  $(YELLOW)make setup$(NC)        - Configura todo o ambiente (venv + dependências)"
	@echo "  $(YELLOW)make venv$(NC)         - Cria apenas o ambiente virtual"
	@echo "  $(YELLOW)make install$(NC)      - Instala apenas as dependências"
	@echo "  $(YELLOW)make test$(NC)         - Executa os testes"
	@echo "  $(YELLOW)make run-radial$(NC)   - Executa visualização de função de onda radial"
	@echo "  $(YELLOW)make run-cloud$(NC)    - Executa visualização de nuvem eletrônica 3D"
	@echo "  $(YELLOW)make run-slicing$(NC)  - Executa animação de fatiamento orbital"
	@echo "  $(YELLOW)make format$(NC)       - Formata o código com black"
	@echo "  $(YELLOW)make lint$(NC)         - Verifica código com flake8"
	@echo "  $(YELLOW)make clean$(NC)        - Remove arquivos temporários e cache"
	@echo "  $(YELLOW)make all$(NC)          - Setup completo + testes"

# Setup completo
setup: venv install
	@echo "$(GREEN)✓ Setup completo!$(NC)"
	@echo "$(BLUE)Para ativar o ambiente virtual, execute:$(NC)"
	@echo "  source $(VENV)/bin/activate"

# Criar ambiente virtual
venv:
	@echo "$(BLUE)Criando ambiente virtual...$(NC)"
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✓ Ambiente virtual criado em $(VENV)$(NC)"

# Instalar dependências
install: venv
	@echo "$(BLUE)Instalando dependências...$(NC)"
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@echo "$(GREEN)✓ Dependências instaladas$(NC)"

# Executar testes
test: venv
	@echo "$(BLUE)Executando testes...$(NC)"
	@$(PYTHON_VENV) -m pytest tests/ -v --cov=src --cov-report=term-missing
	@echo "$(GREEN)✓ Testes concluídos$(NC)"

# Executar scripts individuais
run-radial: venv
	@echo "$(BLUE)Executando visualização de função de onda radial...$(NC)"
	@$(PYTHON_VENV) src/radial_wavefunction.py

run-cloud: venv
	@echo "$(BLUE)Executando visualização de nuvem eletrônica 3D...$(NC)"
	@$(PYTHON_VENV) src/electron_cloud_3d.py

run-slicing: venv
	@echo "$(BLUE)Executando animação de fatiamento orbital...$(NC)"
	@$(PYTHON_VENV) src/orbital_slicing.py

# Formatação de código
format: venv
	@echo "$(BLUE)Formatando código com black...$(NC)"
	@$(PYTHON_VENV) -m black src/ tests/
	@echo "$(GREEN)✓ Código formatado$(NC)"

# Verificação de estilo
lint: venv
	@echo "$(BLUE)Verificando código com flake8...$(NC)"
	@$(PYTHON_VENV) -m flake8 src/ tests/ --max-line-length=100 --extend-ignore=E203,W503
	@echo "$(GREEN)✓ Verificação concluída$(NC)"

# Limpeza
clean:
	@echo "$(BLUE)Limpando arquivos temporários...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@rm -f .coverage
	@rm -f *.gif
	@echo "$(GREEN)✓ Limpeza concluída$(NC)"

# Setup completo + testes
all: setup test
	@echo "$(GREEN)✓ Projeto pronto para uso!$(NC)"
