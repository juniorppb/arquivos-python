dist = float(input('Digite uma distância em metros: '))
mm = dist * 1000
cm = dist * 100
dm = dist * 10
dam = dist / 10
hm = dist / 100
km = dist / 1000
print('A distância de {}m, equivale há {:.0f}mm, {:.0f}cm, {:.0f}dm.\nQue é igual há {}dam, {}hm, {}km.'.format(dist, mm, cm, dm, dam,hm, km))
