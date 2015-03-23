#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]){

	std::vector<int> dynamicArray;
	cout<<"capacity "<<dynamicArray.capacity()<<endl;
	cout<<"size "<<dynamicArray.size()<<endl;
	for(int i = 0; i <100; i++){
		dynamicArray.push_back(253);
		cout<<"capacity "<<dynamicArray.capacity();
		cout<<"     size "<<dynamicArray.size()<<endl;

	}
	
	system("PAUSE");
}