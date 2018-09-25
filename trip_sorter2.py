from collections import namedtuple


class TripSorter2(object):
    def __init__(self, bacardsin=None):
        if bacardsin:
            self.bcards = bacardsin
        else:
            BoardingCard = namedtuple("BoardingCard", "cfrom cto ctype no seatno addinfo")

            bc1 = BoardingCard(cfrom="berlin", cto="rome", ctype="flight", no="137", seatno="seat no A37",
                               addinfo="(Gate no 66)")
            bc2 = BoardingCard(cfrom="krakow", cto="bydgoszcz", ctype="bus", no="223", seatno="", addinfo="")
            bc3 = BoardingCard(cfrom="warsaw", cto="poznan", ctype="train", no="55", seatno="seat no C69",
                               addinfo="(Track no 1)")
            bc4 = BoardingCard(cfrom="barcelona", cto="warsaw", ctype="flight", no="69", seatno="seat no Z123",
                               addinfo="(Gate no 1)")
            bc5 = BoardingCard(cfrom="poznan", cto="berlin", ctype="bus", no="321", seatno="", addinfo="")
            bc6 = BoardingCard(cfrom="rome", cto="krakow", ctype="flight", no="Z123", seatno="seat no G321",
                               addinfo="(Gate no 55)")

            bcards = dict()

            '''let's create new dict of namedtuples with start points as our keys'''
            bcards[bc1.cfrom] = bc1
            bcards[bc2.cfrom] = bc2
            bcards[bc3.cfrom] = bc3
            bcards[bc4.cfrom] = bc4
            bcards[bc5.cfrom] = bc5
            bcards[bc6.cfrom] = bc6
            self.bcards = bcards


    @staticmethod
    def sortit(bcards):
        """the main sorting algorithm"""

        '''we will store our final sorted items here'''
        bcsorted = dict()
        keys = [key for key, bcard in bcards.items()]
        '''now let's collect all the destinations here...'''
        dests = [bcards[key].cto for key, bcard in bcards.items()]
        '''...and find the start of our journey by looking for a start point 
        that's not a destination in the same time'''
        start_key = [key for key in keys if key not in dests][0]

        i = 0
        bcsorted[i] = bcards[start_key]
        '''since we have the very first element already found, we can pop it out from the namedtuples dict, 
        because we don't need to iterate over it again'''
        bcards.pop(start_key, None)

        for key, bcard in bcards.items():
            '''we can use newly created dict with our start point to find the second step of our journey...'''
            if i == 0:
                searchto = bcsorted[i].cto
            i += 1
            '''...and then just find next steps by looking into bcards dict for "from" keys 
            matching bcards "to" values'''
            try:
                '''easy workaround with try/except, as the last card throws KeyError 
                (since there's nowhere else to go)'''
                bcsorted[i] = bcards[searchto]
                searchto = bcards[searchto].cto
            except KeyError:
                pass

        return bcsorted

    def composeit(self):
        """simple function to print sorted items, without any particular fireworks used :)"""

        bcsorted = self.sortit(self.bcards)
        for key, bcout in bcsorted.items():
            if key % 2 == 0:
                print('Take {} number {} from {} to {}{}. {}'.format(bcout.ctype, bcout.no, bcout.cfrom, bcout.cto,
                                                                     bcout.addinfo if bcout.addinfo else '',
                                                                     bcout.seatno if bcout.seatno else
                                                                     'No seat assignment.'))
            else:
                print('From {} take {} number {} to {}{}. {}'.format(bcout.ctype, bcout.no, bcout.cfrom, bcout.cto,
                                                                     bcout.addinfo if bcout.addinfo else '',
                                                                     bcout.seatno if bcout.seatno else
                                                                     'No seat assignment.'))


if __name__ == '__main__':
    ts2 = TripSorter2()
    ts2.composeit()
