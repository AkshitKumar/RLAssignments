import plotterclasses as pc

def main():
  gamma = [0.3, 0.5, 0.7, 0.9]

  types = ['policy_', 'value_']
  for i in types:
    curves = list()
    for j in gamma:
      yaxis = list()
      with open('../outfile/'+str(i)+str(j)) as infile:
        for f in infile:
          yaxis.append(float(f.strip()))
      curves.append(yaxis)
    if i == 'policy_':
      pc.policy_plotter(curves).plotMethod()
    else:
      pc.value_plotter(curves).plotMethod()

  sweep = ['_1', '_10', '']
  for k in types:
    for i in gamma[2:]:
      curves = list()
      for j in sweep:
        yaxis = list()
        with open('../outfile/'+str(k)+str(i)+str(j)) as infile:
          for f in infile:
            yaxis.append(float(f.strip()))
        curves.append(yaxis)
      pc.sweep_plotter(curves, i, k[:-1].capitalize()).plotMethod()
  
if __name__ == '__main__':
  main()
