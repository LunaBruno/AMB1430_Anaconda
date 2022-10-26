from ufersa import Ufersa


def main():
    # Criar o objeto ufersa
    ufersa = Ufersa()

    # Criar predios
    ufersa.cadastrar_predio('Reitoria')
    ufersa.cadastrar_predio('Centro de Engenharias')
    ufersa.cadastrar_predio('Central de Aulas VI')

    # Criar salas no predio
    ufersa.cadastrar_sala('Reitoria', 'Gabinete', 10.0, 1.0)
    ufersa.cadastrar_sala('Reitoria', 'Secretaria', 10.0, 10.0)
    ufersa.cadastrar_sala('Central de Aulas VI', 'Sala secreta', 10.0, 10.0)

    # Gerar lista de caracteristicas da sala
    print(f'Predios:      {ufersa.id_predios()}')
    print(f'Salas:        {ufersa.id_salas()}')
    print(f'Larguras:     {ufersa.larguras()}')
    print(f'Comprimentos: {ufersa.comprimentos()}')
    print(f'Temperaturas: {ufersa.temperaturas()}')
    print(f'Umidades:     {ufersa.umidades()}')


if __name__ == '__main__':
    main()
