# Microgrid Energy Management System  
# Mikroşebeke Enerji Yönetim Sistemi

## English Description

This project presents a rule-based energy management system for a hybrid microgrid structure. The system includes photovoltaic generation, wind generation, battery energy storage, generator support, grid connection, and critical/non-critical loads.

The developed system aims to manage energy sources efficiently, reliably, and sustainably according to renewable energy generation, load demand, battery state of charge, grid status, and electricity price.

---

## Türkçe Açıklama

Bu proje, hibrit bir mikroşebeke yapısı için kural tabanlı bir enerji yönetim sistemini kapsamaktadır. Sistem; güneş enerjisi üretimi, rüzgâr enerjisi üretimi, batarya enerji depolama sistemi, jeneratör desteği, şebeke bağlantısı ve kritik/kritik olmayan yüklerden oluşmaktadır.

Geliştirilen sistemin amacı; yenilenebilir enerji üretimi, yük talebi, batarya doluluk oranı, şebeke durumu ve elektrik fiyatı gibi değişkenlere göre enerji kaynaklarını verimli, güvenilir ve sürdürülebilir şekilde yönetmektir.

---

## Project Aim / Projenin Amacı

The aim of this project is to determine the most suitable energy source in different operating conditions and to ensure energy continuity in the microgrid system.

Bu projenin amacı, farklı çalışma koşullarında en uygun enerji kaynağını belirlemek ve mikroşebeke sisteminde enerji sürekliliğini sağlamaktır.

---

## System Components / Sistem Bileşenleri

- Photovoltaic (PV) energy system / Güneş enerjisi sistemi
- Wind energy system / Rüzgâr enerjisi sistemi
- Battery energy storage system / Batarya enerji depolama sistemi
- Generator / Jeneratör
- Grid connection / Şebeke bağlantısı
- Critical and non-critical loads / Kritik ve kritik olmayan yükler
- Rule-based energy management algorithm / Kural tabanlı enerji yönetim algoritması
- MATLAB/Simulink simulation model / MATLAB/Simulink simülasyon modeli
- Python-based monitoring and decision structure / Python tabanlı izleme ve karar yapısı

---

## Energy Management Logic / Enerji Yönetim Mantığı

The system prioritizes renewable energy sources. If the total PV and wind generation is sufficient, the load demand is supplied by renewable energy. If renewable generation is not sufficient, the battery is used to support the load.

When the battery state of charge is low or the energy demand cannot be met, the system uses grid support if the grid is available. In grid outage conditions, the generator is activated. If the total available energy is still insufficient, non-critical loads can be disconnected in order to maintain the supply of critical loads.

Sistem öncelikli olarak yenilenebilir enerji kaynaklarını kullanmaktadır. PV ve rüzgâr üretimi yük talebini karşılamaya yeterliyse yükler yenilenebilir enerji ile beslenir. Yenilenebilir üretim yetersiz kaldığında batarya devreye girerek yükü destekler.

Batarya doluluk oranı düşük olduğunda veya enerji talebi karşılanamadığında, şebeke mevcutsa şebeke desteği kullanılır. Şebeke kesintisi durumunda jeneratör devreye alınır. Mevcut enerji yine de yetersiz kalırsa kritik yüklerin beslenmesini sürdürebilmek için kritik olmayan yükler devreden çıkarılabilir.

---

## Data Files / Veri Dosyaları

- `solar_power_data.xlsx` : PV generation data / Güneş enerjisi üretim verileri
- `wind_power_data.xlsx` : Wind generation data / Rüzgâr enerjisi üretim verileri
- `electricity_price_data.xlsx` : Electricity price data / Elektrik fiyat verileri

---

## Project Files / Proje Dosyaları

- `ems_algorithm.py` : Rule-based energy management algorithm / Kural tabanlı enerji yönetim algoritması
- `dashboard.py` : Monitoring and visualization code / İzleme ve görselleştirme kodu
- `microgrid_simulation.slx` : MATLAB/Simulink simulation model / MATLAB/Simulink simülasyon modeli
- `microgrid_energy_management_thesis.pdf` : Graduation project thesis / Bitirme tezi
- `solar_power_data.xlsx` : Solar power data / Güneş enerjisi verileri
- `wind_power_data.xlsx` : Wind power data / Rüzgâr enerjisi verileri
- `electricity_price_data.xlsx` : Electricity price data / Elektrik fiyat verileri

---

## Technologies Used / Kullanılan Teknolojiler

- MATLAB/Simulink
- Python
- Microsoft Excel
- Rule-based control / Kural tabanlı kontrol
- Data visualization / Veri görselleştirme
- Microgrid energy management / Mikroşebeke enerji yönetimi

---

## Project Team / Proje Ekibi

- Nil Sümeyra Kılınç
- Işıl Köse

---

## Keywords / Anahtar Kelimeler

Microgrid, Energy Management System, Renewable Energy, PV System, Wind Energy, Battery Storage, Generator, Grid Support, MATLAB/Simulink, Python

Mikroşebeke, Enerji Yönetim Sistemi, Yenilenebilir Enerji, Güneş Enerjisi, Rüzgâr Enerjisi, Batarya Depolama, Jeneratör, Şebeke Desteği, MATLAB/Simulink, Python
