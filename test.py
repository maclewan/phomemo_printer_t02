from phomemo_printer.ESCPOS_printer import Printer

printer = Printer(bluetooth_address="0F:1A:C6:62:A8:55", channel=1)
printer.print_image("img.png")
printer.close()