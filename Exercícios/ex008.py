medida = float(input('Digite uma medida em metros: '))

km = medida * 0.001

hm = medida * 0.01

dam = medida * 0.1

dm = medida * 10

cm = medida * 100

mm = medida * 1000

print('A medida de {} m tem {:.3} km, {:.2} hm, {:0.1} dam, {:.0f} dm, {:.0f} cm e {:.0f} mm'.format(medida, km, hm, dam, dm, cm, mm))
