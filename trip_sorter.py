class TripSorter(object):
    def __init__(self, bcardsin=None):
        if bcardsin:
            self.bcards = bcardsin
        else:
            self.bcards = {
                0: {"from": "berlin", "to": "rome", "type": "flight", "no": "33A", "seatno": "seat no 69",
                    "addinfo": "(Gate no 44)"},
                1: {"from": "krakow", "to": "bydgoszcz", "type": "bus", "no": "123B", "seatno": "", "addinfo": ""},
                2: {"from": "warsaw", "to": "poznan", "type": "train", "no": "777", "seatno": "",
                    "addinfo": "(Track no 1)"},
                3: {"from": "barcelona", "to": "warsaw", "type": "flight", "no": "66", "seatno": "seat no 69",
                    "addinfo": "(Gate no 55)"},
                4: {"from": "poznan", "to": "berlin", "type": "train", "no": "9", "seatno": "seat no 69",
                    "addinfo": "(Track no 13)"},
                5: {"from": "rome", "to": "krakow", "type": "flight", "no": "111", "seatno": "seat no 69",
                    "addinfo": "(Gate no 66)"},
            }

    @staticmethod
    def bubbleit(bcards):
        """the main sorting algorithm, using plain bubble sort method"""

        iterations = len(bcards) - 1

        for iteration in range(iterations, 0, -1):
            for i in range(iterations):
                if bcards[i]["to"] != bcards[i + 1]["from"]:
                    tmp = bcards[i]
                    bcards[i] = bcards[i + 1]
                    bcards[i + 1] = tmp

        return bcards

    def composeit(self):
        """simple function to print sorted items, without any particular fireworks used :)"""

        bcardsout = self.bubbleit(self.bcards)
        for key, bcout in bcardsout.items():
            if key % 2 == 0:
                print('Take {} number {} from {} to {}{}. {}'.format(bcout["type"], bcout["no"], bcout["from"],
                                                                     bcout["to"], bcout["addinfo"] if bcout["addinfo"]
                                                                     else '', bcout["seatno"] if bcout["seatno"]
                                                                     else 'No seat assignment.'))
            else:
                print('From {} take {} number {} to {}{}. {}'.format(bcout["from"], bcout["type"], bcout["no"],
                                                                     bcout["to"], bcout["addinfo"] if bcout["addinfo"]
                                                                     else '', bcout["seatno"] if bcout["seatno"] else
                                                                     'No seat assignment.'))


if __name__ == '__main__':
    ts = TripSorter()
    ts.composeit()
