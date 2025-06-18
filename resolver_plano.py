from PrimoPobre import PrimoPobre

def main():
    # Criar uma instância do PrimoPobre
    pp = PrimoPobre()
    
    # Carregar o plano do arquivo
    pp.load_plan_txt("meu_plano")
    
    # Resolver o plano
    pp.solve_plan("MeuPlanoFinanceiro")
    
    # Imprimir a solução usando o método público
    pp.print_plan_solution("MeuPlanoFinanceiro")

if __name__ == "__main__":
    main()