class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def make_computations(self):
        if self.__cpu >= 560:
            print(f'\nCpu is very good {self.__cpu}')
        else:
            print(f'\nCpu is bad {self.__cpu}')
        if self.__memory == 'Intel Core I7':
            print(f'Nice memory {self.__memory}')
        else:
            print(f'fuuuuu memory {self.__memory}')

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        print(f"\nComputer\nCpu: {self.cpu} Memory: {self.memory}")


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            if str(call_to_number).startswith('+996 70'):
                print(f'Идет звонок на номер {call_to_number} с сим-карты 1 - {self.__sim_cards_list[0]}')
            else:
                print('Не верный номер телефона для данной sim card! ')
        if sim_card_number == 2:
            if str(call_to_number).startswith('+996 55'):
                print(f'Идет звонок на номер {call_to_number} с сим-карты 2 - {self.__sim_cards_list[1]}')
            else:
                print('Не верный номер телефона для данной sim card!')
        if sim_card_number == 3:
            if str(call_to_number).startswith('+996 77'):
                print(f'Идет звонок на номер {call_to_number} с сим-карты 3 - {self.__sim_cards_list[2]}')
            else:
                print('Не верный номер телефона для данной sim card!')

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self):
        location = 'School - Park - Market - Football field - Home'
        print('\nMy location: ', location)

    def __str__(self):
        print(f"\nSmartPhone\nCpu: {self.cpu} Memory: {self.memory}")


com = Computer(1000, 'Intel Core I7')

ph = Phone(['O!', "MegaCom", 'Beeline'])
ph.call(int(input('\nPhone\nSim cards 1) O!, 2) MegaCom or 3) Beeline: ')), input('Call to number (+996 *** ** ** **): '))

sm = SmartPhone(420, 'Android', ['O!', "MegaCom", 'Beeline'])
sm.use_gps()
sm.call(int(input('\nSmartPhone\nSim cards 1) O!, 2) MegaCom or 3) Beeline: ')), input('Call to number (+996 *** ** ** **): '))

lst = [com, ph, sm]
for i in lst:
    i.__str__()