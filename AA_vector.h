#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]){
	std::vector<int> array;
	std::vector<int> *arrayP_old_1, *arrayP_old_2;
	int *p1, *p2;
	
	array.push_back(100);
	p1 = &array[0];
	cout<<"dizinin birinci elemanının adresi:"<<endl;
	arrayP_old_1 = array;
	cout<<arrayP_old_1<<endl;
	int c = 190;
	
	cout<<array.capacity()<<endl;
	for(int ss =0; ss<100000;ss++){
		array.push_back(c);
	}
	cout<<array.capacity()<<endl;
	
	arrayP_old_2 = &array;
	cout<<arrayP_old_2<<endl;
	system("PAUSE");
}