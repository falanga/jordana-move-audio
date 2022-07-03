import time
import torch


def test(device):
	matrix_size = 32*512

	x = torch.randn(matrix_size, matrix_size)
	y = torch.randn(matrix_size, matrix_size)

	print("*******CPU*********")
	start = time.time()
	result = torch.matmul(x,y)
	print(time.time() - start)
	print("Verify device = ", result.device)


	x_gpu = x.to(device)
	y_gpu = y.to(device)
	torch.cuda.synchronize()

	for i in range(3):
		print("*******GPU*********")
		result_gpu = []
		start = time.time()
		result_gpu = torch.matmul(x_gpu,y_gpu)
		torch.cuda.synchronize()

		print(time.time() - start)
		print("Verify device = ", result_gpu.device)

