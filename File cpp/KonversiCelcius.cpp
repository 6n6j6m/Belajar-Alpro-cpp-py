#include <iostream>
using namespace std;

int main() {
    int pilih;
    float suhu, hasilkonversi;
    cout << "Program Konversi Celsius ke Suhu Berbeda" << endl;
    cout << "1. Celsius ke Reamur" << endl;
    cout << "2. Celsius ke Fahrenheit" << endl;
    cout << "3. Celsius ke Kelvin" << endl;
    cout << "4. Celsius ke Rankine" << endl;
    
    cout << "Pilih jenis konversi (1, 2, 3, atau 4): "; cin >> pilih;
    cout << "Masukkan besar suhu dalam Celsius: "; cin >> suhu;

    if (pilih == 1) {
        hasilkonversi = (4.0 / 5.0) * suhu;
        cout << suhu << " Celsius = " << hasilkonversi << " Reamur" << endl;
    } else if (pilih == 2) {
        hasilkonversi = (9.0 / 5.0) * suhu + 32;
        cout << suhu << " Celsius = " << hasilkonversi << " Fahrenheit" << endl;
    } else if (pilih == 3) {
        hasilkonversi = suhu + 273.15;
        cout << suhu << " Celsius = " << hasilkonversi << " Kelvin" << endl;
    } else if (pilih == 4) {
        hasilkonversi = ((suhu + 273.15) * 9.0) / 5.0;
        cout << suhu << " Celsius = " << hasilkonversi << " Rankine" << endl;
    } else {
        cout << "tidak ada" << endl;
    }

    return 0;
}
