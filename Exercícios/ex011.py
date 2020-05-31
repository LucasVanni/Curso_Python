largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

área = largura * altura

quantidadeDeTinta = área / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, área))

print('A quantidade de tinta necessária para pintar essa mediada é de {} litros de tinta.'.format(quantidadeDeTinta))
