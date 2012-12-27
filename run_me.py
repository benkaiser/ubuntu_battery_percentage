#! /usr/bin/env python
import sys
import gtk
import appindicator
import gobject
import os

# change this to edit the applets name
app_name = "Loading..."

class BatPercentageApplet:
    def __init__(self):
        self.ind = appindicator.Indicator("BatteryStatus",
                                           "BatteryStatus",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_label(app_name)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")

        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()
        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        gobject.timeout_add(100, self.check_battery)
        gtk.main()

    def check_battery(self):
        print "Updating Battery..."
        percentage = os.popen("acpi -V | awk 'NR==1{print $4 }' | sed s/,//").read().rstrip()
        self.ind.set_label(percentage)
        gobject.timeout_add(60000, self.check_battery)


    def quit(self, widget):
        sys.exit(0)


if __name__ == "__main__":
    indicator = BatPercentageApplet()
    indicator.main()
