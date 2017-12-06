




import random

import itertools


# p = itertools.count(0,10)

# for i in p: print(i)

# list = [i for i in random.randrange(20,100)]
#
# print(list)


class Card:
    card_view = []

    def __init__(self):
        self.list = self._get_random_list()

    @staticmethod
    def _get_random_list():
        result = []
        while True:
            i = random.randrange(1, 91)
            if i not in result:
                result.append(i)
            if len(result) >= 15:
                return result

    def _get_card_view(self):
        if self.card_view:
            return self.card_view
        list_splitters = [' ' for i in range(0, 4)]
        result_list = []
        start_index = 0
        end_index = 5
        for i in range(0, 3):
            line = list_splitters + self.list[start_index:end_index]
            random.shuffle(line)
            result_list.append(line)
            start_index += 5
            end_index += 5
        self.card_view = result_list
        return self.card_view

    def __str__(self):
        raw = self._get_card_view()
        result = ""
        for line in raw:
            result += ' '.join(['{0:<2}'.format(str(e)) for e in line]) + '\n'
        return result

    def del_number(self, number):
        if number not in self.list:
            return
        del self.list[self.list.index(number)]
        # self.list.pop(self.list.index(number))
        for line in self.card_view:
            if number in line:
                line[line.index(number)] = '-'
                break

    @property
    def is_win(self):
        """
        is win
        """
        return len(self.list) == 0


bag = list(range(1, 91))
random.shuffle(bag)
print(bag)
card1 = Card()
card2 = Card()
while len(bag) != 0:
    current = bag.pop(0)
    card1.del_number(current)
    card2.del_number(current)
    print('Выпало число ', current)
    print('card1:')
    print(card1)
    print('card2:')
    print(card2)
    if card1.is_win:
        print('card1 is win')
        break
    if card2.is_win:
        print('card2 is win')
        break
