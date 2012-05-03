udprr
-----
udprr is a simple udp load balancer using twisted. 

Installation
------------
Basic Python installation::

    # on most linux distributions...
    git clone git://github.com/kmcminn/udprr.git
    cd udprr/
    python setup.py install
    cp contrib/udprr.init /etc/rc.d/init.d/udprr
    cp contrib/udprr.logrotate /etc/logrotate.d/udprr
    cp conf/udprr.conf /etc/udprr.conf

    # edit udprr.conf for your setup, then...

    chkconfig add udprr
    chkconfig udprr on
    service udprr start
    


Configuration
----------------------
See the config file for basic options. On the command line::


    $ udprr -h
    Usage: udprr [options]

    Options:
      -h, --help            show this help message and exit
      -l LOGGING_LEVEL, --logging-level=LOGGING_LEVEL
                            debug level default is warning
      -o LOG_FILE, --log-file=LOG_FILE
                            log to file instead of stdout
      -c CONFIG_FILE, --config-file=CONFIG_FILE
                            path to config file


About
--------------------
Why on earth wasnt there a good udp load balancer?
