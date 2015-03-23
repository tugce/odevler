#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]){

	std::vector<int> dynamicArray;
	int *p1,*p2;
	cout<<"capacity "<<dynamicArray.capacity()<<endl;
	cout<<"size "<<dynamicArray.size()<<endl;
	dynamicArray.push_back(5);
	p1 = &dynamicArray[0];
	for(int i = 0; i <100; i++){
		dynamicArray.push_back(253);
		cout<<"capacity "<<dynamicArray.capacity();
		cout<<"     size "<<dynamicArray.size()<<endl;

	}
	p2 = dynamicArray[0];
	
	system("PAUSE");
}