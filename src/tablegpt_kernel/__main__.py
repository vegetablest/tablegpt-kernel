from ipykernel.kernelapp import IPKernelApp

from tablegpt_kernel.kernel import TablegptKernel

IPKernelApp.launch_instance(kernel_class=TablegptKernel)
