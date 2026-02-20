import colorama
from colorama import Fore, Back, Style, init

init()

print("=== dir(colorama) ===")
print(dir(colorama))

print("\n=== Атрибуты Fore ===")
print([x for x in dir(Fore) if x.isupper()])

print("\n=== Атрибуты Back ===")
print([x for x in dir(Back) if x.isupper()])

print("\n=== Атрибуты Style ===")
print([x for x in dir(Style) if x.isupper()])
