import matplotlib.pyplot as plt
import numpy as np
import keyboard


keyboard.press_and_release('shift+s, space')

keyboard.write('The quick brown fox jumps over the lazy dog.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))
print(help(keyboard))
# keyboard.press_and_release('ctrl+t')

# keyboard.write('hashtagtreinamentos.com')

# keyboard.press_and_release('enter')


# vendas = np.random.randint(1000, 3000, 50)
# meses = np.arange(1, 51)

# plt.plot(meses, vendas)
# plt.axis([0, 50, 0, max(vendas) + 200])
# plt.xlabel('Meses')
# plt.ylabel('Vendas')
# plt.show()

