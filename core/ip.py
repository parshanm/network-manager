class Ip:
    def __init__(self, ip, range_):
        self.range = range_
        self.ip = ip

    def __eq__(self, other):
        return self.ip == other.ip

    def next(self, first:str='100'):
        """
        this func get an ip and returns the next one
        """
        old = self.ip.split('.')
        if int(old[-1]) == self.range:
            last_part = first
            mid_part = str(int(old[2]) + 1)
            return self.__class__(f'192.168.{mid_part}.{last_part}', self.range)
        elif int(old[-1]) < self.range:
            mid_part = old[2]
            last_part = str(int(old[-1]) + 1)

            return self.__class__(f'192.168.{mid_part}.{last_part}', self.range)

