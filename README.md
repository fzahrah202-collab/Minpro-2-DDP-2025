# Minpro-2-DDP-2025
Nama : Fatimatuzzahrah NIM : 2509116020 Sistem Informasi A'2025

🐾 Sistem Manajemen Jasa Penitipan Hewan

📖 Deskripsi Singkat

Program ini adalah sistem sederhana untuk mengelola data penitipan hewan peliharaan.
Fitur yang tersedia:

Login sistem dengan dua role: Admin & User

Input data hewan (nama, jenis, lama penitipan)

Simpan data hingga maksimal 3 hewan

Lihat daftar hewan dalam bentuk tabel

Edit data hewan berdasarkan nama (khusus Admin)

Hapus data hewan berdasarkan nama (khusus Admin)

Menu berulang (looping) sampai pengguna memilih keluar



_____________________________________________________________________________________________________________________________________________________________________________________________________________________

🔄 Alur Program

Mulai 

1. Tampilkan judul program


2. Login (Max 3x percobaan)

Input username & password

Jika benar -> masuk ke menu sesuai role

Jika salah -> ulangi sampai 3 kali

Jika salah 3x -> program berhenti

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

👤 Menu Admin

1. Lihat Daftar Hewan
Menampilkan tabel daftar hewan yang sedang dititipkan.

2. Tambah Hewan
Input nama, jenis, lama penitipan -> data disimpan ke list.

3. Edit Hewan
input nama hewan yang ingin diganti -> ubah data -> simpan.

4. Hapus Hewan
input nama hewan yang ingin dihapus -> hapus dari list.

5. Keluar
Menghentikan menu admin & keluar dari program.


_____________________________________________________________________________________________________________________________________________________________________________________________________________________

👥 Menu User

1. Lihat Daftar Hewan
Menampilkan tabel daftar hewan.

2. Tambah Hewan
Input nama, jenis, lama penitipan -> data disimpan ke list.

3. Keluar
Menghentikan menu user & keluar dari program.


_____________________________________________________________________________________________________________________________________________________________________________________________________________________

Akhir Program -> Selesai ✅

_____________________________________________________________________________________________________________________________________________________________________________________________________________________

FLOWCHART

<img width="1469" height="1450" alt="flowchart minpro2 revisi drawio" src="https://github.com/user-attachments/assets/a262d456-3b36-419c-b2d5-e8ab32722550" />



_____________________________________________________________________________________________________________________________________________________________________________________________________________________

OUTPUT

kondisi login ketika username dan password admin benar
<img width="459" height="416" alt="Screenshot 2025-09-28 182431" src="https://github.com/user-attachments/assets/3d2db97e-d38d-4604-8bc5-158077c35f66" />

kondisi login ketika username admin benar dan password salah -> (saat salah 3 kali program berhenti)
<img width="488" height="398" alt="Screenshot 2025-09-28 182649" src="https://github.com/user-attachments/assets/7f0c1067-e3cd-41a7-b944-e86515132d61" />

kondisi login ketika username dan password user benar
<img width="512" height="363" alt="Screenshot 2025-09-28 182730" src="https://github.com/user-attachments/assets/2c3428dc-c95e-44d1-aef5-d3dee3188335" />

kondisi login ketika username user benar dan password salah -> (saat salah 3 kali program berhenti)
<img width="530" height="400" alt="Screenshot 2025-09-28 182856" src="https://github.com/user-attachments/assets/58a2d55a-cb78-4f66-84d2-eac6180335a9" />

kondisi login ketika username tidak ada
<img width="585" height="379" alt="Screenshot 2025-09-28 183100" src="https://github.com/user-attachments/assets/39ca5fec-de3d-4d0a-a2be-d489e48dcd55" />

kondisi lihat daftar hewan saat list kosong
<img width="561" height="635" alt="Screenshot 2025-09-28 183236" src="https://github.com/user-attachments/assets/64474c72-8760-4ce4-8e60-00cc9335e00e" />

konisi lihat daftar hewan ketika sudah ada data
<img width="570" height="529" alt="Screenshot 2025-09-28 183411" src="https://github.com/user-attachments/assets/e06e4cec-94f2-4e4f-a127-321c5ddcca51" />

kondisi tambah hewan ketika input benar (lama penitipan berupa angka)
<img width="467" height="533" alt="Screenshot 2025-09-28 183532" src="https://github.com/user-attachments/assets/06cb4eb4-adea-4d04-835d-6af46ddea558" />

kondisi tambah hewan ketika input salah ( lama penitipan bukan angka )
<img width="629" height="632" alt="Screenshot 2025-09-28 184017" src="https://github.com/user-attachments/assets/a6022833-e9a8-4e6e-9147-423a778910d4" />

kondisi edit hewan ketika list kosong
<img width="442" height="426" alt="Screenshot 2025-09-28 184427" src="https://github.com/user-attachments/assets/2b27337a-3a84-484a-9c3f-31b2b1b5ce91" />

kondisi edit hewan ketika data hewan ada
<img width="592" height="795" alt="Screenshot 2025-09-28 184839" src="https://github.com/user-attachments/assets/405d57fc-4546-4420-bc90-42e831ac156b" />

kondisi edit hewan ketika nama hewan yang ingin diganti tidak ada
<img width="635" height="576" alt="Screenshot 2025-09-28 190714" src="https://github.com/user-attachments/assets/d4e4aefe-72e4-49a4-b90a-62cd4619a82b" />

kondisi edit hewan ketika input lama penitipan bukan angka
<img width="784" height="815" alt="Screenshot 2025-09-28 190953" src="https://github.com/user-attachments/assets/c387acdf-0394-4308-8fbc-286707e2d057" />

kondisi ketika ingin menghapus data hewan tapi list kosong
<img width="534" height="606" alt="Screenshot 2025-09-28 191058" src="https://github.com/user-attachments/assets/a9357849-be43-4abc-9a59-27ab3961564e" />

kondisi ketika ingin menghapus data hewan dan data hewannya ada
<img width="788" height="784" alt="Screenshot 2025-09-28 191237" src="https://github.com/user-attachments/assets/c61a94a4-5279-4149-93e1-135b9bd60538" />

kondisi ketika ingin menghapus data hewan tapi nama hewan yang ingin dihapus tidak ada dalam daftar
<img width="609" height="746" alt="Screenshot 2025-09-28 191317" src="https://github.com/user-attachments/assets/38a9a911-48eb-48f6-8e73-8ea07310d62a" />

kondisi keluar dari menu admin
<img width="587" height="213" alt="Screenshot 2025-09-28 191350" src="https://github.com/user-attachments/assets/4baeb814-7e53-4947-90c7-824a50e24046" />

kondisi ketika menginput menu admin selain 1-5
<img width="514" height="577" alt="Screenshot 2025-09-28 191432" src="https://github.com/user-attachments/assets/b7d15a0c-e319-4103-b847-bb8f861d38a9" />

kondisi ketika input menu bukan berupa angka
<img width="398" height="397" alt="Screenshot 2025-09-28 191510" src="https://github.com/user-attachments/assets/821fe856-f83a-4305-96a5-fbb8c619913c" />

kondisi lihat hewan di menu user 
<img width="460" height="543" alt="Screenshot 2025-09-28 191629" src="https://github.com/user-attachments/assets/da375880-02a6-4be1-bdd0-93b4c4c5b1b9" />
<img width="561" height="728" alt="Screenshot 2025-09-28 191842" src="https://github.com/user-attachments/assets/c2a70d7a-2539-4aaa-944c-de322ff7d0b6" />

kondisi tambah hewan di menu user
<img width="561" height="728" alt="Screenshot 2025-09-28 191842" src="https://github.com/user-attachments/assets/c90cc18c-2597-4150-a9d2-8eb35d85b96f" />

konisi keluar dari menu user
<img width="644" height="192" alt="Screenshot 2025-09-28 192041" src="https://github.com/user-attachments/assets/c0a465f2-6673-464e-8475-6e39da019c82" />

kondisi input  selain 1-3 di menu user 
<img width="450" height="413" alt="Screenshot 2025-09-28 191948" src="https://github.com/user-attachments/assets/7f315598-b9ab-4c2c-9320-b6743cd60e92" />

kondisi input bukan angka di menu user
<img width="318" height="169" alt="Screenshot 2025-09-28 192027" src="https://github.com/user-attachments/assets/8f55043c-1fa2-43f1-bca8-ad669dba7667" />





























