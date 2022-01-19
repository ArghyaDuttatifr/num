
#include<iostream>
using namespace std;
int main()
{
	int arr[100], tot , larg, i;
	cout<< " Enter the size (max. 100 ): ";
	cin >>tot;
	cout<< " enter " << tot << " Array Element : ";
	for ( i = 0 ; i < tot ; i++ )
		cin >> arr[i];
	larg = arr[0];
	for ( i=1; i< tot ; i++){
		if ( larg< arr[i])
			larg = arr[i];
	}
	cout<<"\nLargest Number = "<<larg;
	cout<<endl;
	return 0;
}
		

