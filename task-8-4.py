class OfficeEquipmentStorehous():
    def __init__(self, *equipments):
        self.__numequips, self.__numscans = 0, 0;
        self.__numprints, self.__numxers  = 0, 0;
        self.equipmentlist = {'scanner': [], 'printer': [], \
                              'xerox': [], 'unclassified': []};
        if len(equipments) > 0:
            for eq in equipments:
                if type(eq) == Scanner:
                    self.__numequips += 1;
                    self.__numscans  += 1;
                    self.equipmentlist['scanner'].append(eq);
                elif type(eq) == Printer:
                    self.__numequips += 1;
                    self.__numprints += 1;
                    self.equipmentlist['printer'].append(eq);
                elif type(eq) == Xerox:
                    self.__numequips += 1;
                    self.__numxers +=1
                    self.equipmentlist['xerox'].append(eq);
                elif type(eq) == OfficeEquipment:
                    self.__numequips += 1;
                    self.equipmentlist['unclassified'].append(eq);
                else:
                    pass;

class OfficeEquipment():
    __num_equipments = 0;
    def __init__(self, size, cost, year, name, status = 'new'):
        self.size = size;
        self.cost = cost;
        self.year = year;
        self.name = name;
        self.status = status;
        OfficeEquipment.__num_equipments += 1;

class Scanner(OfficeEquipment):
    __num_scanners = 0;
    def __init__(self, size, cost, year, name, duplex = False, paperf = 'a4',
                 usb = [True, 1, ['st-2']], net = (True, False), **kwargs):
        if 'status' in kwargs:
            super().__init__(size, cost, year, name, kwargs['status']);
        else:
            super().__init__(size, cost, year, name);
        self.duplex = duplex;
        self.paper_format = paperf;
        self.network_interface = {'lan': net[0], 'wifi': net[1]};
        self.usb_interface = {'presence': usb[0], 'quantity': usb[1], 'types': usb[2]};
        Scanner.__num_scanners += 1;

class Printer(OfficeEquipment):
    __num_printers = 0;
    def __init__(self, size, cost, year, name, maxnc, nc,
                 pclass = 'inkjet', dpi = 1200, duplex = True,
                 paperk = ['plain', 'photo'], paperf = ['a4'],
                 usb = [True, 1, ['st-2']], net = (True, False),
                 cartridgee_status = ['exist', 'new'], **kwargs):
        if 'status' in kwargs:
            super().__init__(size, cost, year, name, kwargs['status']);
        else:
            super().__init__(size, cost, year, name);
        self._max_num_copies = maxnc;
        self.num_copies = nc;
        self.pclass = pclass;
        self.duplex = duplex;
        self.__max_dpi = dpi;
        self.paper = {'kind': paperk, 'format': paperf};
        self.network_interface = {'lan': net[0], 'wifi': net[1]};
        self.usb_interface = {'presence': usb[0], 'quantity': usb[1], 'types': usb[2]};
        self.cartridge_status = cartridgee_status;
        Printer.__num_printers += 1;

class Xerox(OfficeEquipment):
    __num_xeroxes = 0;
    def __init__(self, size, cost, year, name,
                 maxnc, nc, dpi = 1200, duplex = True,
                 paperk = ['plain', 'photo'], paperf = ['a4'],
                 usb = [True, 1, ['st-2']], net = (True, False),
                 cartridgee_status = ['exist', 'new'], **kwargs):
        if 'status' in kwargs:
            super().__init__(size, cost, year, name, kwargs['status']);
        else:
            super().__init__(size, cost, year, name);
        self._max_num_copies = maxnc;
        self.num_copies = nc;
        self.duplex = duplex;
        self.__max_dpi = dpi;
        self.paper = {'kind': paperk, 'format': paperf};
        self.network_interface = {'lan': net[0], 'wifi': net[1]};
        self.usb_interface = {'presence': usb[0], 'quantity': usb[1], 'types': usb[2]};
        self.cartridge_status = cartridgee_status;
        Xerox.__num_xeroxes += 1;

if __name__ == '__main__':
    scanner = Scanner('42x53x10', '$650', 2018, 'HP', 2.5e+5, 0);
    printer = Printer('75x75x50', '$650', 2018, 'HP', 3e+5, 0, status = 'new');
    xerox = Xerox('80x70x45', '$500', 2012, 'Samsung', 1e+5, 978, status = 'used');
