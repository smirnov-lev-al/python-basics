class OfficeEquipmentStorehous():
    def __init__(self, *equipments):
        self._numequipments = {'scanner': 0, 'printer': 0, \
                               'xerox': 0, 'unclassified': 0};
        self._equipmentlist = {'scanner': [], 'printer': [], \
                               'xerox': [], 'unclassified': []};
        if len(equipments) != 0:
            for eq in equipments:  self.oeadd(eq);
    
    @staticmethod
    def oetype(equipment):
        if type(equipment) == Scanner:
            return 'scanner';
        elif type(equipment) == Printer:
            return 'printer';
        elif type(equipment) == Xerox:
            return 'xerox';
        elif type(equipment) == OfficeEquipment:
            return 'unclassified';
        else:
            return None;
    
    def oeadd(self, equipment):
        oetype_str = self.oetype(equipment);
        if oetype_str != None:
            self._numequipments[oetype_str] += 1;
            self._equipmentlist[oetype_str].append(equipment);
    
    def oeextract(self, oetype_str, oeindex = None):
        if oetype_str in self._equipmentlist.keys():
            self._numequipments[oetype_str] -= 1;
            if oetype_str == None:
                equipment = self._equipmentlist[oetype_str].pop();
            else:
                equipment = self._equipmentlist[oetype_str].pop(oeindex);
            return equipment;
        else:
            return None;
    
    def oefilter(self, oetype_str, **oefeature):
        if oetype_str in self._equipmentlist.keys():
            equipmens = [];
            for eq in self._equipmentlist[oetype_str]:
                collect = True;
                for key, val in oefeature.items():
                    if getattr(eq, key, None) != val:
                        collect = False;
                if collect:
                    equipmens.append(eq);
            return equipmens;
        else:
            return None;

class OfficeEquipment():
    __num_equipments = 0;
    def __init__(self, size, cost, year, name, status = 'new'):
        self.size = size;
        self.cost = cost;
        self.year = year;
        self.name = name;
        self.status = status;
        OfficeEquipment.__num_equipments += 1;
        
    def __str__(self):
        return f'size: {self.size}, cost: {self.cost}, ' + \
               f'year: {self.year}, name: {self.name}, status: {self.status}';

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
        
    def __str__(self):
        return 'Scanner:\n' + super().__str__();

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
    
    def __str__(self):
        return 'Printer:\n' + super().__str__();

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
    
    def __str__(self):
        return 'Xerox:\n' + super().__str__();


if __name__ == '__main__':
    scanner1 = Scanner('42x53x10', '$650', 2018, 'HP', 2.5e+5, 0);
    scanner2 = Scanner('42x53x10', '$850', 2017, 'Dell', 2.5e+5, 0);
    printer1 = Printer('75x75x50', '$650', 2018, 'HP', 3e+5, 0, status = 'new');
    printer2 = Printer('75x75x50', '$550', 2016, 'LG', 3e+5, 0, status = 'new');
    xerox = Xerox('80x70x45', '$500', 2012, 'Samsung', 1e+5, 978, status = 'used');
    oestorehous = OfficeEquipmentStorehous(scanner1, printer1, xerox);
    oestorehous.oeadd(scanner2);
    oestorehous.oeadd(printer2);
    scaner3 = oestorehous.oeextract('scanner', 0);
    print(scaner3, '\n');
    
    equipmens = oestorehous.oefilter('printer', status = 'new');
    if equipmens != None:
        for eq in equipmens:
            print(eq);
    
    equipmens = oestorehous.oefilter('printer', status = 'new', name = 'LG');
    if equipmens != None:
        for eq in equipmens:
            print(eq);
    