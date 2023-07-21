#include <stdio.h>
#include <iostream>
#include <string.h>
#include <conio.h>

using namespace std;

struct mdata {
    string nama;
    string nim;
    float IPK;
};

int main(){
	int i,N;
    mdata mahasiswa[100];
	float nmax=-1,nmin=5.0,nlulus=0;
	string cari;
	bool hasilcari = false;
	cout<<"input N : "; cin>>N;
	
	for(i=0;i<N;i++){
		cout<<"Input NIM :"; cin>>mahasiswa[i].nim;
		cin.ignore();
		cout<<"Input Nama :"; getline(cin, mahasiswa[i].nama);
		cout<<"Input IPK :"; cin>>mahasiswa[i].IPK;
		if(mahasiswa[i].IPK>=2.0){
			nlulus +=1;
		}
		if(mahasiswa[i].IPK>nmax){
			nmax=mahasiswa[i].IPK; 
		}
		if(mahasiswa[i].IPK<nmin){
			nmin=mahasiswa[i].IPK;
		}cout<<endl;	
	}
	
	cout<<"Nilai Maksimumnya : "<<nmax<<endl;
	cout<<"Nilai Minimumnya : "<<nmin<<endl;	
	cout<<"Nilai yang lulus : ";
	for(i=0;i<N;i++){
		if(mahasiswa[i].IPK>=2.0)
			cout<<mahasiswa[i].IPK<<"--";
	}	
	cout<<endl<<"Banyak yang lulus : "<<nlulus<<endl;
	
    cout<<endl<<"Cari NIM : "; cin>>cari;
    for(i=0;i<N;i++){
    	if(mahasiswa[i].nim==cari){
    		cout<<"Nama : "<<mahasiswa[i].nama<<endl;
    		cout<<"IPK : "<<mahasiswa[i].IPK;
    		hasilcari=true;
    		break;
		}
	}
	
	if(hasilcari==false){
		cout<<"mhs tsb tak ditemukan";
	}
return 0;
}


