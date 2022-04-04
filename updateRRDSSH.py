import time
import rrdtool
from getSNMP_1 import consultaSNMP


while 1:
    tcp_in_segs = int(
        consultaSNMP('comunidadGVL','192.168.100.13',
                     '1.3.6.1.2.1.6.10.0'))
    tcp_out_segs = int(
        consultaSNMP('comunidadGVL','192.168.100.13',
                     '1.3.6.1.2.1.6.11.0'))
    tcp_in_errs = int(
        consultaSNMP('comunidadGVL','192.168.100.13',
                     '1.3.6.1.2.1.6.14.0'))

    valorSSH = "N:" + str(tcp_in_segs) + ':' + str(tcp_out_segs) + ':' + str(tcp_in_errs)
    print (valorSSH)
    rrdtool.update("reporteSSH.rrd", valorSSH)
    rrdtool.dump("reporteSSH.rrd","reporteSSH.xml")
    time.sleep(1)