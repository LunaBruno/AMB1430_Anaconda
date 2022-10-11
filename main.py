from ufersa import Ufersa


def main():
    # Criar o objeto ufersa
    ufersa = Ufersa()

    # Criar predio
    ufersa.cadastrar_predio(0)

    # Criar salas no predio
    ufersa.cadastrar_sala(0, 0, 5.0, 6.0)
    ufersa.cadastrar_sala(0, 1, 4.5, 5.5)
    ufersa.cadastrar_sala(0, 2, 6.0, 5.0)

    # Selecionar predio e sala para consulta da temperatura
    id_predio = 0
    id_sala = 1

    # Consultar temperatura
    temperatura_sala = ufersa.temperatura_sala(id_predio, id_sala)
    print(f'Prédio {id_predio} | Sala {id_sala} | Temperatura: {temperatura_sala:.2f} graus')


if __name__ == '__main__':
    main()
