
zaehler = {}

while True:
    try:
      item = (input().strip().upper())
    except EOFError:
      break
  
    if  item in zaehler:
        zaehler[item] += 1
    else:
        zaehler[item] = 1

for name in sorted(zaehler):
  print(f"{zaehler[name]} {name}")