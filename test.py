from colored import attr, fg

note = 'Hello, World!'


green = fg('green')
red = fg('red')
res = attr(0)

text_green = green + f'{note}' + res
text_red = red + f'{note}'
print(text_green)
print(text_red)

print(note)
