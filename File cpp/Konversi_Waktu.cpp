#include <iostream>
using namespace std;

int waktu_ke_detik(int jam, int menit, int detik) {
    int total_detik = jam * 3600 + menit * 60 + detik;
    return total_detik;
}

void detik_ke_waktu(int total_detik, int &jam, int &menit, int &detik) {
    jam = total_detik / 3600;
    int sisa_detik = total_detik % 3600; // sisa detik digunakan untuk mencari menit dan detik karna dia adalah sisa bagi dari jam
    menit = sisa_detik / 60;
    detik = sisa_detik % 60;
}

int main() {
    //waktu ke detik
    int jaminput, menitinput, detikinput,total_detik, total_detik_input;
    cout << "Masukkan jumlah jam: "; cin >> jaminput;
    cout << "Masukkan jumlah menit: "; cin >> menitinput;
    cout << "Masukkan jumlah detik: "; cin >> detikinput;

    total_detik = waktu_ke_detik(jaminput, menitinput, detikinput);
    cout << "Total detik: " << total_detik << " detik." <<endl;


    //konversi detik ke waktu
    total_detik_input;
    cout << "Masukkan total detik: "; cin >> total_detik_input;

    int jam_hasil, menit_hasil, detik_hasil;
    detik_ke_waktu(total_detik_input, jam_hasil, menit_hasil, detik_hasil);

    cout << "Waktu: " << jam_hasil << " jam, " << menit_hasil << " menit, " << detik_hasil << " detik." <<endl;
    return 0;
}
