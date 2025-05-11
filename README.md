
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

  

## Business Understanding

Edutech merupakan bidang yang menggabungkan teknologi dengan pendidikan untuk meningkatkan proses belajar-mengajar, memperluas akses pendidikan dan memudahkan administrasi pendidikan.

### Permasalahan Bisnis
Jaya Jaya Institut adalah salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias _dropout_.
Tingginya angka _dropout_ yang berdampak pada reputasi, pendapatan dan efisiensi operasional, sehingga memerulukan deteksi dini berbasis data dan program interverensi yang tepat.
  
### Cakupan Proyek

1. Data Understanding 
- Melakukan eksplorasi data dari dataset data.csv guna mempelajari karakteristik dataset
2. Data Preparation 
- Melakukan persiapan data untuk digunakan analisis seperti menghapus row dengan status Enrolled 
3. Modeling 
- Membuat model prediktif menggunakan beberapa model dengan rasio training dan test sebanyak 80/20 dan bantuan Gridsearch untuk mendapatkan parameter terbaik
4. Evaluation 
- Melakukan evaluasi model menggunakan data test dan menampilkan hasil evaluasi
5. Deployment 
- Melakukan deployment model terbaik yaitu GradientBoost dengan bantuan Streamlit
6. Membuat bussiness dashboard untuk membantu memantau performance metrik dari siswa
7. Memberikan kesimpulan dan rekomendasi

### Persiapan

Sumber data: 
```
https://doi.org/10.24432/C5MC89
```

Setup environment:
```
mkdir students_performance
cd students_performance
pip install -r requirement.txt
```
 

## Business Dashboard

Dashboard dibuat menggunakan Metabase untuk menampilkan informasi terkait performa mahasiswa dengan fokus pada tingkat dropout dan faktor faktor yang mempengaruhinya.
Untuk menjalankan Dashboard gunakan Docker untuk menjalankan Metabase
```
docker pull metabase/metabase:latest
```
Kemudian jalankan Metabase dengan perintah
```
docker run -p 3000:3000 --name metabase metabase/metabase
```
Copy file metabase.db.mv.db kedalam container dengan menggunakan perintah
```
docker cp .\metabase.db.mv.db metabase:/metabase.db/metabase.db.mv.db
```
Login ke Metabase menggunakan username dan password berikut ini
```
username: root@mail.com
password: root123
```
  

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototype isi data sesuai form, kemudian klik pada tombol predict, prediksi akan muncul setelahnya.  Prototype dapat diakses melalui link berikut ini

```
https://students-performances.streamlit.app/
```

  

## Conclusion
1. __Tingkat Dropout yang TInggi__: sebanyak 39.15% siswa tidak menyelesaikan pendidikan
2. __Tingkat Dropout Penerima Beasiswa Relatif Rendah__ : hanya 134 siswa atau 13.83% yang tidak menyelesaikan pendidikan, angka ini jauh lebih rendah dibandingkan dengan tingkat dropout secara keseluruhan
3. Tidak ada perbedaan yang signifikan antara gender terhadap dropout
4. Faktor yang paling berpengaruh diambil dari Importance Feature model __Gradient Boosting__ adalah `Curricular_units_1st_sem_approved`, `Curricular_units_2nd_sem_grade`, `Tuition_fees_up_to_date`, `Scholarship_holder`, `Admission_grade`, `Application_mode`

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Fokus pada dukungan belajar pada semester awal, seperti bimbingan tambahan
- Beasiswa terbukti menurunkan dropout, pertimbangkan untuk memperluas cakupan beasiswa
- Gunakan dahsboard dan model prediktif untuk memantau dan mendeteksi dini resiko dropout