# mini-project-2
nama: Zahra Aurellya Herdiansyah nim:062 
nim: 2409116062
kelas: SI B'24


# kode program dan input
![Screenshot 2024-10-14 194220](https://github.com/user-attachments/assets/6d411a8c-a612-41bd-88b4-1e3a2f230502)
#fungsinya untuk membuat dan menampilkan tabel dengan rapih

![Screenshot 2024-10-14 194231](https://github.com/user-attachments/assets/bab67fa9-ebca-49de-8a4a-5fc1cacf147b)
#disini saya menggunakan dictionary untuk digunakan dalam login nanti

![Screenshot 2024-10-14 225358](https://github.com/user-attachments/assets/e59c2cc8-a333-4e58-a11c-cc969eb7c61d)
#disini reward merupakan list yang berisi dictionary, setiap dictionary mewakili item yang dapat ditukarkan dengan poin reward
#'NO': nomor urut item, 'ITEM': nama item(hadiah), 'POIN': jumlah poin yang perlu ditukarkan untuk mendapatkan item tersebut

![Screenshot 2024-10-14 225439](https://github.com/user-attachments/assets/a8487966-3656-42ab-bfdb-a24a06fb22cb)
#line 22 digunakan untuk memasukkan username melalui input
#line 23 digunakan untuk memasukkan password melalui input
#line 25 berfungsi memeriksa apakah username ada dalam dictionary pengguna, jika ada fungsi akan memeriksa apakah password yang dimasukkan sesuai dengan nilai yang terdaftar untuk username tersebut
#pada line 26 jika kedua kondisi terpenuhi, maka akan mencetak pesan selamat datang dan mengembalikan username
#pada line 29 jika tidak maka akan mencetak pesan bahwa username tidak valid

![Screenshot 2024-10-14 230848](https://github.com/user-attachments/assets/49d2e51b-1b96-4db4-a3e4-052c6c68e5d2)
#pada fungsi menu_admin dibuat untuk antarmuka untuk menu admin yang memberikan beberapa opsi
#line 34 menggunakan while True untuk looping(perulangan) yang terus berjalan, dan memungkinkan admin untuk memilih opsi berulang kali sampai mereka memilih untuk  logout
#line35-41 berfungsi untuk menampilkan menu admin setiap loop berjalan, dengan daftar opsi yang ada
#line 43  admin diminta untuk memilih opsi dengan memasukkan angka yang sesuai
#line 45 apabila menginput '1' maka akan memanggil fungsi lihat_transaksi() untuk menampilkan daftar transaksi
#line 47 apabila menginput '2' maka akan memanggil fungsi tambah_transaksi() untuk menambahkan transaksi baru
#line 49 apabila menginput '3' maka akan memanggil fungsi ubah_transaksi() untuk mengubah transaksi yang sudah ada
#line 51 apabila menginput '4' maka akan memanggil fungsi hapus_transaksi() untuk menghapus transaksi yang sudah ada
#line 53 apabila menginput '5' untuk mencetak pesan logout dan menghentikan loop pada line 55
#line 57 jika pilihan tidak valid, admin diberi tahu dan diminta mencoba kembali

![Screenshot 2024-10-14 232106](https://github.com/user-attachments/assets/5c130d99-31e2-4e7b-8405-d428ba8a33fb)
#fungsi menu_pembeli dibuat untuk antarmuka untuk menu yang ditawarkan kepada pembeli, mirip dengan menu admin tetapi dengan opsi yang berbeda
#line 60 menggunakan while True untuk looping(perulangan) yang terus berjalan, dan memungkinkan admin untuk memilih opsi berulang kali sampai mereka memilih untuk  logout
#line 69 admin diminta untuk memilih opsi dengan memasukkan angka yang sesuai
#line 71 apabila menginput '1' maka akan memanggil fungsi lihat_transaksi() untuk menampilkan daftar transaksi
#line 73 apabila menginput '2' maka akan memanggil fungsi tambah_transaksi() untuk menambahkan transaksi baru
#line 75 apabila menginput '3'  maka akan memanggil fungsi lihat_poin_reward() untuk menampilkan poin reward yang dimiliki
#line 77 apabila menginput '4' maka akan memanggil fungsi tukar_poin_reward() untuk menukarkan poin reward dengan item
#line 79 apabila meninput '5' maka akan mencetak pesan logout dan menghitamkan loop dengan break pada line 81
#line 83 diberitahukan jika pilihan tidak valid, pemebeli diberi tahu dan diminta mencoba lagi

![Screenshot 2024-10-14 233555](https://github.com/user-attachments/assets/3261e6a0-8fca-4401-8346-875952bcc1d7)
#line 85 fungsi tabel_poin_reward dibuat menggunakan PrettyTable untuk menampilkan item dan jumlah poin yang diperlukan dalam format tabel yang rapi
#line 86 membuat PrettyTable dengan kolom "NO", "ITEM", dan "POIN" ini akan menjadi header dari table yang akan ditampilkan
#line 88 untuk setiap item, fungsi menambahkan baris baru ke tabel menggunakan add_row yang mengisi kolom dengan no, item, dan poin yang diperlukan

![Screenshot 2024-10-14 233603](https://github.com/user-attachments/assets/8e0e7d1d-133e-4096-99bd-bf180e7bcc94)
#jadi pada item_poin ini merupakan sebuah dictionary yang menyimpan jumlah poin yang diperlukan untuk menukarkan setiap item reward berdasarkan nomor item

![Screenshot 2024-10-14 234504](https://github.com/user-attachments/assets/94e6b75d-7850-413f-b6ec-c074925f3c32)
#line 100 fungsi lihat_transaksi berfungsi menampilkan daftar transaksi yang telah dilakukan
#line 101 memastikan bahwa ada tranksaksi yang perlu ditampilkan
#line 102 mencetak header "Daftar Transaksi"
#line 103 menggunakan enumerate(transaksi, 1), fungsi melakukann iterasi melalui list transaksi, dimana i adalah nomor urut yang dimulai dari 1 dan t adalah item  transaksi dan juga setiap transaksi  dicetak dengan format yang rapi sesuai nomor urut
#line 106 jika list transaksi kosong, akan memberi tahu pengguna bahwa belum ada transaksi yang dilakukan

![Screenshot 2024-10-14 234517](https://github.com/user-attachments/assets/07f6d52e-559f-4598-b668-fea2054dbb4c)
#line 109 fungsi tambah_transaksi bertujuan untuk menambahkan detail transaksi ke dalam list  transaksi dan juga menambahkan poin reward untuk pembeli
#line 110 meminta pembeli memasukkan detail transaksi melalui input()
#line 111 memasukkan detail transaksi yang ditambahkan ke list transaksi
#line 112 poin reward untuk pembeli ditambahkan sebanyak 10 poin setiap kali transaksi baru ditambahkan
#line 113 mencetak pesan konfirmasi bahwa transaksi telat berhasil ditambahkan

![Screenshot 2024-10-15 000125](https://github.com/user-attachments/assets/570f0f90-fd7f-4e74-ba40-6da3ed019cd2)
#line 115 fungsi lihat_poin_reward berfungsi untuk menampilkan jumlah poin reward yang dimiliki oleh pembeli
#line 116 dengan menggunakan f-string, fungsi mengambil nilai dari dictionary poin_reward untuk kunci "Pembeli" dan menampilkannya dalam bentuk format yang rapi

![Screenshot 2024-10-15 000155](https://github.com/user-attachments/assets/adb42c5b-5834-4d1a-9422-c96edabe8726)
#line 118 fungsi tukar_poin_reward berfungsu untuk pembeli menukarkan poin reward mereka dengan item(hadiah)
#line 119 menampilkan daftar item(hadiah) beserta poin yang diperlukan untuk menukarnya
#line 120 menampilkan jumlah poin reward yang dimiliki saat ini oleh pembeli
#line 121 pembeli diminta untuk memasukkan nomor item yang ingin ditukar melalui input()
#line 123 fungsi memeriksa apakah pilihan pembeli ada di item_poin
#line 124 jika pilihan valid, maka fungsi akan mengambil nilai poin yang diperlukan untuk item tersebut
#line 125 fungsi akan memeriksa apakah poin reward yang dimiliki pembeli cukup untuk menukarkan item
#line 126 jika cukup, poin milik pembeli akan dikurangi poin reward yang ditukarkan
#line 127 pembeli akan mendapatkan konfirmasi bahwa mereka berhasil mendapatkan item tersebut
#line 129 jika pilihan item tidak valid, fungsi akan mencetak pesan untuk mencoba lagi

![Screenshot 2024-10-15 001753](https://github.com/user-attachments/assets/e35a53fd-b540-4ae5-9d2f-5c619440dbaf)
#line 134 fungsi ubah_transaksi berfungsi untuk mengubah detail transaksi yang telah ada
#line 135 menampilkan daftar transaksi yang ada, ini akan membantu admin memilih transaksi yang ingin diubah
#line 136 admin diminta untuk memasukkan nomor transaksi yang ingin diubah, input ini kemudian dikurangi 1 untuk mendapatkan indeks yang sesuai dalam list(karena indeks di python dimulai dari 0)
#line 137 fungsi memeriksa apakah indeks yang dimasukkan valid, dalam rentang list transaksi
#line 138  jika valid admin diminta untuk memasukkan detail baru untuk transaksi tersebut
#line 139 detail baru yang dimasukkan admin akan menggantikan detail lama pada indeks yang sesuai dalam list transaksi
#line 140 mencetak pesan konfirmasi bahwa transaksi telah berhasil diubah
#line 142 jika nomor transaksi tidak valid fungsi akan mencetak pesan bahwa nomor transaksi tidak valid

![Screenshot 2024-10-15 001808](https://github.com/user-attachments/assets/95350300-15b6-4f93-81a3-166f2f777563)
#line 145 fungsi hapus_transaksi bertujuan menghapus transaksi dari daftar yang ada
#line 146 menampilkan daftar transaksi yang ada
#line 147 admin diminta untuk memasukkan nomor transaksi yang ingin dihapus, input ini kemudian dikurangi 1 untuk mendapatkan indeks yang sesuai dalam list
#line 148 fungsi akan memeriksa apakah indeks yang dimasukkan valid
#line 149 jika valid fungsi menggunakan del untuk menghapus item pada indeks yang sesuai dalam list transaksi
#line 150 mencetak pesan konfirmasi bahwa transaksi telah berhasil dihapus
#line 152 jika nomor transaksi tidak valid fungsi akan mencetak pesan bahwa nomor transaksi tidak valid

![Screenshot 2024-10-15 003524](https://github.com/user-attachments/assets/9811f580-9e6a-4bf8-8e4c-ae2fe762f1d2)
#line 155 fungsi main berfungsi sebagai titik awal program, mengatur alur login dan navigasi menu berdasarkan jenis pengguna
#line 156  menggunakan loop yang terus berjalan, memungkinkan pengguna untuk login kembali sampai program dihentikan secara manual\
#line 157 setiap iterasi loop menampilkan header "Login" dan memanggil fungsi login() untuk  meminta pengguna memasukkan kredensial mereka
#line 158 setelah login fungsi memeriksa hasil dari login()
#line 159 jika pengguan "Admin", fungsi menu_admin() dipanggil untuk mengarahkan admin ke menu admin
#line 160 jika pengguna "Pembeli, fungsi menu_pembeli() dipanggil untukmengrahkan pembeli ke menu  pembeli

![Screenshot 2024-10-15 004409](https://github.com/user-attachments/assets/9179ea60-89a6-4f65-bf83-37cd1fb9adb9)
#line 166  memastikan bahwa fungsi main() hanya akan dipanggil jika file dijalankan langsung dan tidak  akan dipanggil jika file diimpor sebagai modul


# output pembeli
![Screenshot 2024-10-15 005642](https://github.com/user-attachments/assets/4bf87b8d-1f04-41c7-9f91-61590e3428a5)
#apabila login salah password/username

![Screenshot 2024-10-15 005724](https://github.com/user-attachments/assets/0126c8a1-8850-455a-be81-3227fecee893)
#apabila login benar

![Screenshot 2024-10-15 005735](https://github.com/user-attachments/assets/5aec7c2a-173c-4bcd-b24c-8e7114092eca)
#daftar menu pembeli

![Screenshot 2024-10-15 005743](https://github.com/user-attachments/assets/9900b540-9821-43ec-8f2c-6033bc763626)
#opsi 1 melihat transaksi saat belum melakukan transaksi

![Screenshot 2024-10-15 005806](https://github.com/user-attachments/assets/8a5e510f-8294-47b8-9899-a1cad103a503)
#opsi 2 menambahkan transaksi dan berhasil

![Screenshot 2024-10-15 005820](https://github.com/user-attachments/assets/8bcb307c-8a71-421f-970b-e03397749f72)
#opsi 1 melihat transaksi saat sudah melakukan transaksi

![Screenshot 2024-10-15 005843](https://github.com/user-attachments/assets/e6ec3a3a-ead6-4925-bc24-74b5020e593e)
#opsi 2 menambahkan kembali transaksi dan berhasil

![Screenshot 2024-10-15 005910](https://github.com/user-attachments/assets/9b670790-7d57-4cc1-9fd7-fe4780788b6a)
#opsi  1 melihat transaksi saat sudah melakukan 2 kali transaksi

![Screenshot 2024-10-15 005923](https://github.com/user-attachments/assets/cdefde1b-9dfb-42e2-8390-f4d5a406bd1c)
#opsi 3 melihat poin reward yang didapatkan setelah melakukan transaksi

![Screenshot 2024-10-15 005947](https://github.com/user-attachments/assets/823b49e8-5988-4805-9171-227b73523a28)
#opsi 4 untuk menukar poin reward dan daftar itemnya, poin item yang ingin ditukar lebih dari poin yang dimiliki

![Screenshot 2024-10-15 010006](https://github.com/user-attachments/assets/1a9f8522-745e-4beb-ac9e-4d3f52f721f3)
#opsi 4 untuk menukar poin reward dan daftar itemnya, poin yang dimiliki mencukupi 

![Screenshot 2024-10-15 010023](https://github.com/user-attachments/assets/a4ca3256-c986-4d80-a82d-4ea05ca222e3)
#opsi 3 lihat poin yang dimiliki setelah ditukar dengan item

![Screenshot 2024-10-15 010038](https://github.com/user-attachments/assets/2eb6f7bb-06b3-4fdb-8a0a-b1da8fb1f718)
#opsi 5 logout dari menu pembeli

# output admin
![Screenshot 2024-10-15 011303](https://github.com/user-attachments/assets/4f1a0e87-1077-4135-8861-0555733bfff3)
#apabila login salah

![Screenshot 2024-10-15 011308](https://github.com/user-attachments/assets/234ae651-d0d7-4571-86d2-73a5f0ef53ab)
#apabila login benar

![Screenshot 2024-10-15 011321](https://github.com/user-attachments/assets/3679e746-2598-4cbc-b334-9665efa8afdf)
#daftar menu admin

![Screenshot 2024-10-15 011329](https://github.com/user-attachments/assets/b320a2c5-0daf-4e5f-b5f3-c4dd6698e406)
#opsi  1 melihat transaksi, sebelumnya sudah melakukan transaksi di output pembeli

![Screenshot 2024-10-15 011353](https://github.com/user-attachments/assets/8629dffb-18c2-4e00-83e8-a4c092f34fc6)
#opsi 2 menambahkan transaksi

![Screenshot 2024-10-15 011409](https://github.com/user-attachments/assets/9f8eaf79-5ec2-45b8-93f6-0d2425f29c0e)
#opsi 1 melihat kembali transaksi setelah melakukan penambahan transaksi

![Screenshot 2024-10-15 011447](https://github.com/user-attachments/assets/1dba6b8b-6966-485a-92b3-9026c359c707)
#opsi 3 melakukan perubahan transaksi

![Screenshot 2024-10-15 011458](https://github.com/user-attachments/assets/99db2788-796a-4277-8561-fcd537078c60)
#opsi 1 melihat kembali hasil transaksi setelah dilakukan perubahan transaksi

![Screenshot 2024-10-15 011518](https://github.com/user-attachments/assets/82298ff1-5958-4bae-bc35-f2e3fe64fb15)
#opsi 4 melakukan penghapusan transaksi 

![Screenshot 2024-10-15 011528](https://github.com/user-attachments/assets/633ea2ab-f87f-4c4d-802a-fdfb01562014)
#opsi 1 melihat hasil transaksi setelah penghapusan transaksi

![Screenshot 2024-10-15 011546](https://github.com/user-attachments/assets/773a846b-750c-447f-8014-069f4d35acea)
#opsi 5 melakukan logout dari menu admin



