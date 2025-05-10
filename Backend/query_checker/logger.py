import logging
import psutil

def getprocdet(host,port):
    cons = psutil.net_connections()
    for i in cons:
        if i.laddr.ip == host and i.laddr.port == port:
            pid = i[-1]
            pname = psutil.Process(pid).name()
    return pid,pname

def getdatabase(og):
    return og.split(" from ")[1].split(" ")[0]

def logQuery(host,port,inp,og,stat):
    if stat:
        stat = 'safe'
    else:
        stat = 'malicious'
    logging.basicConfig(
        format="%(asctime)s\t%(message)s",
        style="%",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
        filemode='a',
        filename='logs/checker.log',
        force=True
    )
    pid,pname = getprocdet(host,port)
    database = getdatabase(og)
    try:
        logging.debug(f"{host}:{port}\t{pid}\t{pname}\t{og}\t{inp}\t{database}\t{stat}")
        return 0
    except:
        return -1
    
def logServ(msg):
    logging.basicConfig(
        format="%(asctime)s\t%(message)s",
        style="%",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
        filemode='a',
        filename='logs/service.log',
        force=True
    )
    try:
        logging.debug(msg)
        return 0
    except:
        return -1