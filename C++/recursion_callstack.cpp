#include <iostream>

void doit(){
  int a;
  std::cin >> a;
  if(a==0){
    std::cout << std::endl;
    std::cout << a << std::endl;
  }
  else{
    doit();
    std::cout << a << std::endl;
  }
}

int main(){
  doit();
  return 0;
}
