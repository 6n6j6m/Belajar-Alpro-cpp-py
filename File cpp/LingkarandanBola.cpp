#include <iostream>
#include <math.h>
using namespace std;

int main(){
    float jari, k, l, lpb, v;
    const float phi = 3.14;

    cout<<"Masukkan Jari jari : "; cin >> jari;
    
    k = 2*phi*jari;
    l = phi*(pow(jari, 2));
    lpb = (4*phi)*(pow(jari, 2));
    v = (4*phi*pow(jari, 3))/3;

    cout<<"Kelilingnya : "<< k << endl;
    cout<<"Luasnya : "<< l << endl;
    cout<<"Luas Permukaan bola : "<< lpb << endl;
    cout<<"Volumenya : "<< v << endl;

    return 0;
}