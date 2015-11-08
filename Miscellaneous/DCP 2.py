import inflect

print(sum([len(inflect.engine().number_to_words(i).replace(' ', '').replace('-', '')) for i in range(1,1001)]))

