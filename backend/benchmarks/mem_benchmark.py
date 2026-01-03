import numpy as np

# NES RAM simulation benchmarks
def test_nes_ram_write_list(benchmark):
	# NES RAM is 2KB (2048 bytes)
	ram = [0] * 2048
	def write():
		for i in range(2048):
			ram[i] = (i * 3) % 256
	benchmark(write)

def test_nes_ram_read_list(benchmark):
	ram = [(i * 3) % 256 for i in range(2048)]
	def read():
		for i in range(2048):
			x = ram[i]
	benchmark(read)

def test_nes_ram_write_numpy(benchmark):
	ram = np.zeros(2048, dtype=np.uint8)
	def write():
		ram[:] = (np.arange(2048, dtype=np.uint16) * 3) % 256
	benchmark(write)

def test_nes_ram_read_numpy(benchmark):
	ram = (np.arange(2048, dtype=np.uint16) * 3) % 256
	ram = ram.astype(np.uint8)
	def read():
		x = ram[:].sum()
	benchmark(read)

