import uhd
import numpy as np

fs = 1e8
freq = 2.45e9
gain = 40
samples = np.fromfile("output.sigmf-data", dtype=np.complex64)
usrp = uhd.usrp.MultiUSRP("addr=192.168.2.21,type=x300,send_buff_size=1048576")
usrp.set_tx_subdev_spec(uhd.usrp.SubdevSpec('B:0'))
usrp.set_tx_rate(fs)
usrp.set_tx_freq(freq)
usrp.set_tx_gain(gain)
usrp.set_tx_antenna("TX/RX")
st_args = uhd.usrp.StreamArgs("fc32", "sc16")
st_args.channels = [0]
tx_streamer = usrp.get_tx_stream(st_args)
num_sent = tx_streamer.send(samples, uhd.types.TXMetadata())
print("Samples sent:", num_sent)
