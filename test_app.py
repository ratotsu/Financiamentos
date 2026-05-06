"""
Testes básicos para a aplicação Flask
"""

def test_import():
    """Testar se os módulos podem ser importados"""
    try:
        from app import app
        print("✓ Aplicação importada com sucesso")
        return True
    except Exception as e:
        print(f"✗ Erro ao importar: {e}")
        return False

def test_app_config():
    """Testar se a aplicação está configurada para produção"""
    try:
        from app import app
        assert app.config['DEBUG'] == False, "DEBUG deve ser False"
        assert app.config['ENV'] == 'production', "ENV deve ser production"
        print("✓ Configuração de produção OK")
        return True
    except AssertionError as e:
        print(f"✗ {e}")
        return False
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

def test_routes():
    """Testar se as rotas estão registradas"""
    try:
        from app import app
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        
        required_routes = [
            '/',
            '/financiamento-carro-usado',
            '/financiamento-moto-honda',
            '/juros-financiamento-2026',
            '/simulador-sem-entrada',
            '/ads.txt',
            '/googlee9e345b2ea532dde.html',
        ]
        
        for route in required_routes:
            assert route in routes, f"Rota {route} não encontrada"
        
        print(f"✓ Todas as {len(required_routes)} rotas registradas")
        return True
    except AssertionError as e:
        print(f"✗ {e}")
        return False
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Iniciando testes básicos...\n")
    
    tests = [
        test_import,
        test_app_config,
        test_routes,
    ]
    
    results = [test() for test in tests]
    
    print(f"\n{'='*40}")
    print(f"Resultado: {sum(results)}/{len(results)} testes passaram")
    print(f"{'='*40}")
    
    if all(results):
        print("✓ Tudo OK! Pronto para produção")
    else:
        print("✗ Há problemas a resolver antes do deploy")
