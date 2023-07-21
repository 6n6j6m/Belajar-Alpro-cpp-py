#include <iostream>
#include <string>

using namespace std;

int main(){
    float a,b,hasil;
    int pilih;

    cout<<"Program Kalkulator"<<endl;

    cout<<"1. Tambah"<<endl;
    cout<<"2. Kurang"<<endl;
    cout<<"3. Kali"<<endl;
    cout<<"4. Bagi"<<endl;

    cout<<"Masukkan Bilangan Pertama : "; cin>>a;
    cout<<"Masukkan Bilangan Kedua : "; cin>>b;
    cout<<"Pilih Operasi aritmatika yang akan digunakan : "; cin>>pilih;

    switch(pilih){
        case 1:
            hasil= a + b;
            break;
        case 2:
            hasil = a - b;
            break;
        case 3:
            hasil = a * b;
            break;
        case 4: 
            hasil = a / b;
            break;
}

    cout<<"Hasilnya adalah : "<<hasil<<endl;

    system("pause");
    return 0;
}