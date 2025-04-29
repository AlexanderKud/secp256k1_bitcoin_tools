#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>

int main() {
  using namespace boost::multiprecision;
  int128_t mybignum = 18446744073709551615ull;
  std::cout << mybignum * mybignum << std::endl;
}
