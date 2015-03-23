#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]){

	std::vector<int> dynamicArray;
	int *p1,*p2;
	
	dynamicArray.push_back(5);
	p1 = &dynamicArray[0];
	
	cout<<"capacity "<<dynamicArray.capacity();
	cout<<"     size "<<dynamicArray.size()<<endl;
	//for u 1000, 10000, 100000 için dene
	for(int i = 0; i <3000; i++){
		dynamicArray.push_back(253);
		cout<<"capacity "<<dynamicArray.capacity();
		cout<<"     size "<<dynamicArray.size()<<endl;
		p2 = &dynamicArray[0];
		if(p1 != p2){
			cout<<"    dizi yer degistirildi"<<endl;
			p1=p2;
			cin>>temp;
		}

	}
	p2 = dynamicArray[0];
	cout<<"ilk eleman adresi:  "<<p1<<endl<<"    ilk eleman adresi   :   "<<p2<<endl;
	
	system("PAUSE");
}