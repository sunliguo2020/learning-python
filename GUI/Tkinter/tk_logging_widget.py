# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-24 20:07
"""

import logging
import threading
import tkinter as tk
from time import sleep
from tkinter.scrolledtext import ScrolledText


# Define a helper thread to add messages to the log
def helperThread():
    # Sleep for 1s to allow the GUI to initialize before sending log messages
    sleep(1)
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        logging.debug("Log message")
        sleep(5)


# Define a new logging handler class which inherits the logging.Handler class

class widgetLogger(logging.Handler):
    # The init function needs the widget which will hold the log messages passed to it as
    # well as other basic information (log level, format, etc.)

    def __init__(self, widget, logLevel, format):
        logging.Handler.__init__(self)

        # Basic logging configuration
        self.setLevel(logLevel)
        self.setFormatter(logging.Formatter(format))
        self.widget = widget

        # The ScrolledText box must be disabled so users can't enter their own text
        self.widget.config(state='disabled')

    # This function is called when a log message is to be handled
    def emit(self, record):
        # Enable the widget to allow new text to be inserted
        self.widget.config(state='normal')

        # Append log message to the widget
        self.widget.insert('insert', str(self.format(record) + '\n'))

        # Scroll down to the bottom of the ScrolledText box to ensure the latest log message
        # is visible
        self.widget.see("end")

        # Re-disable the widget to prevent users from entering text
        self.widget.config(state='disabled')


class mainGui:
    def __init__(self, geometry="1000x500", title="Logging GUI"):
        # GUI Setup
        self.root = tk.Tk()

        # Set window size
        self.root.geometry(geometry)

        # Set window title
        self.root.title(title)

        # Generate a ScrolledText widget to display the log
        self.logWidget = ScrolledText(self.root)
        self.logWidget.pack()


# Logging configuration
logFormatStr = '%(asctime)s - %(threadName)s - %(funcName)s  - %(levelname)-8s %(message)s'
logging.basicConfig(format=logFormatStr, level=logging.DEBUG)

# Instantiate the main GUI window
root = mainGui()

# Instantiate a new GUI logging handler
guiLogger = widgetLogger(root.logWidget, logging.DEBUG, format=logFormatStr)
logging.getLogger().addHandler(guiLogger)

threadHandle = threading.Thread(target=helperThread, args=())
threadHandle.start()

try:
    root.root.mainloop()
except KeyboardInterrupt:
    pass
# Remove the GUI logging handler before any more logging calls try to access the GUI
logging.getLogger().removeHandler(guiLogger)

threadHandle.do_run = False
threadHandle.join()
