#ifndef ADD_CC
#define ADD_CC

#include <pybind11/pybind11.h>
#include <torch/torch.h>

// declarations

torch::Tensor add_tensor(torch::Tensor& a, torch::Tensor& b);
int add(int i, int j);

// definitions

torch::Tensor add_tensor(torch::Tensor& a, torch::Tensor& b) {
  torch::Tensor c = a + b;
  return c;
}

int add(int i, int j) {
  return i + j;
}

PYBIND11_MODULE(csrc, m) {
  m.doc() = "pybind11 example plugin";
  m.def("add", &add, "A function which adds two numbers.");
  m.def("add_tensor", &add_tensor, "A function which adds two tensors.");
}

#endif
