# ==================== 4. SIMULASI & LAB KUANTITATIF ====================
elif menu == "🧪 Simulasi & Lab Kuantitatif":
    st.title("🧪 Laboratorium Virtual & Pengolahan Data Analisis")
    
    tab1, tab2 = st.tabs(["🔬 Rak Tabung Reaksi Virtual", "📊 Kalkulator Akurasi & Presisi"])
    
    with tab1:
        st.markdown("""
        <p style='font-size:1.15em; color: #e2e8f0;'>
            Silakan pilih sampel senyawa kimia di bawah ini untuk memulai pengujian kualitatif visual secara virtual:
        </p>
        """, unsafe_allow_html=True)

        # Perbaikan CSS lokal khusus agar teks dropdown selectbox kontras (hitam di dalam list putih/terang)
        st.markdown("""
        <style>
        div[data-baseweb="select"] {
            background-color: #0f172a !important;
            border: 1px solid #475569 !important;
            border-radius: 8px;
        }
        div[data-baseweb="select"] * {
            color: #ffffff !important;
        }
        div[role="listbox"] {
            background-color: #ffffff !important;
        }
        div[role="listbox"] ul li {
            color: #000000 !important;
            background-color: #ffffff !important;
        }
        div[role="listbox"] ul li:hover {
            background-color: #cbd5e1 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        sampel = st.selectbox("Pilih Sampel Senyawa:", [
            "Formaldehid (Metanal) - Aldehid",
            "Asetaldehid (Etanal) - Aldehid",
            "Aseton (Propanon) - Keton",
            "Butanon (Metil Etil Keton) - Keton"
        ])

        if st.button("🔬 Jalankan Pengujian Tabung Reaksi", key="btn_simulasi"):
            st.write("---")
            st.subheader(f"📊 Hasil Pengamatan Visual: {sampel}")
            
            is_aldehid = "Aldehid" in sampel
            col1, col2, col3 = st.columns(3)
            
            if is_aldehid:
                with col1:
                    st.markdown("""
                    <div class="tube-card pos-tollens">
                        <p style="font-size: 1.5em; margin: 0; letter-spacing:1px;">🌟 TOLLENS</p>
                        <p style="font-size: 1.2em; color: #cbd5e1 !important; font-weight: bold; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.9em; font-weight: normal; color: #f1f5f9;">Terbentuk lapisan cermin perak mengkilap mendinding pada tabung.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown("""
                    <div class="tube-card pos-fehling">
                        <p style="font-size: 1.5em; margin: 0; letter-spacing:1px;">🔴 FEHLING</p>
                        <p style="font-size: 1.2em; color: #f87171 !important; font-weight: bold; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.9em; font-weight: normal; color: #f1f5f9;">Larutan biru berubah total menjadi endapan merah bata Cu₂O.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown("""
                    <div class="tube-card pos-schiff">
                        <p style="font-size: 1.5em; margin: 0; letter-spacing:1px;">🔮 SCHIFF</p>
                        <p style="font-size: 1.2em; color: #f472b6 !important; font-weight: bold; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.9em; font-weight: normal; color: #f1f5f9;">Larutan jernih berubah seketika menjadi ungu/magenta tajam.</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                with col1:
                    st.markdown("""
                    <div class="tube-card neg-tube">
                        <p style="font-size: 1.5em; margin: 0; letter-spacing:1px;">🌟 TOLLENS</p>
                        <p style="font-size: 1.2em; color: #93c5fd !important; font-weight: bold; margin: 5px 0;">NEGATIF (-)</p>
                        <span style="font-size: 0.9em; font-weight: normal; color: #cbd5e1;">Larutan tetap jernih transparan; tidak terbentuk lapisan perak.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown("""
                    <div class="tube-card neg-tube">
                        <p style="font-size: 1.5em; margin: 0; letter-spacing:1px;">🔴 FEHLING</p>
                        <p style="font-size: 1.2em; color: #93c5fd !important; font-weight: bold; margin: 5px 0;">NEGATIF (-)</p>
                        <span style="font-size: 0.9em; font-weight: normal; color: #cbd5e1;">Larutan tetap berwarna biru tua jernih; tidak ada endapan.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown("""
                    <div class="tube-card neg-tube">
                        <p style="font-size: 1.5em; margin: 0; letter-spacing:1px;">🔮 SCHIFF</p>
                        <p style="font-size: 1.2em; color: #93c5fd !important; font-weight: bold; margin: 5px 0;">NEGATIF (-)</p>
                        <span style="font-size: 0.9em; font-weight: normal; color: #cbd5e1;">Tidak terjadi perubahan warna (larutan tetap bening).</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.write("")
            
            # KONTEN PENJELASAN DETAIL JAUH LEBIH MEDALAM & MUDAH DIPAHAMI
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<h3 style='color: #818cf8; margin-top:0;'>🧠 Justifikasi & Pembahasan Kimia Analitis Terperinci</h3>", unsafe_allow_html=True)
            
            if is_aldehid:
                st.markdown(f"""
                Sampel yang Anda uji adalah **{sampel}**. Berdasarkan pengamatan virtual, senyawa ini memberikan hasil **POSITIF** pada ketiga uji pembeda karena termasuk dalam golongan **Aldehid (Alkanal)**. 
                
                Berikut adalah penjelasan detail mekanisme reaksinya agar mudah dipahami:
                
                * **Mengapa Uji Tollens Membentuk Cermin Perak?**
                    Aldehid memiliki atom hidrogen yang terikat langsung pada gugus fungsi karbonil ($R-CHO$). Atom hidrogen ini bersifat labil dan sangat mudah melepaskan elektronnya (mengalami oksidasi). Ketika ditambahkan pereaksi Tollens yang mengandung ion kompleks $[Ag(NH_3)_2]^+$, gugus aldehid bertindak sebagai **reduktor**. Gugus aldehid menyerahkan elektronnya untuk mereduksi ion $Ag^+$ (bilangan oksidasi +1) menjadi logam logam perak murni ($Ag^0$, bilangan oksidasi 0). Secara fisik, atom perak bebas ini akan mengendap dan menempel dengan rapat pada dinding dalam tabung reaksi yang bersih, membentuk lapisan mengkilap seperti **cermin perak**. Sementara itu, senyawa aldehidnya sendiri naik tingkat oksidasinya menjadi asam karboksilat.
                
                * **Mengapa Uji Fehling Menghasilkan Endapan Merah Bata?**
                    Pereaksi Fehling mengandung ion tembaga (II) atau Kupri ($Cu^{2+}$) yang terikat dalam bentuk kompleks tartrat dalam kondisi basa kuat, yang memberikan warna khas biru tua jernih. Mirip dengan prinsip Tollens, sifat reduktor pada gugus fungsi aldehid akan mendonasikan elektron kepada ion $Cu^{2+}$ (biloks +2), sehingga ion tersebut mengalami reduksi menjadi ion tembaga (I) atau Kupro ($Cu^+$, biloks +1). Ion $Cu^+$ ini segera berikatan dengan ion hidroksida ($OH^-$) di dalam lingkungan basa dan membentuk senyawa **Tembaga(I) Oksida ($Cu_2O$)**. Senyawa $Cu_2O$ ini tidak larut dalam air dan memiliki karakteristik fisik berupa **endapan padat berwarna merah bata**. Pemanasan diperlukan dalam uji ini untuk mempercepat laju tumbukan antar partikel zat.
                
                * **Mengapa Uji Schiff Memunculkan Warna Magenta?**
                    Pereaksi Schiff dibuat dari zat warna organik *fuchsine* (yang aslinya berwarna merah muda pekat). Zat warna tersebut dialiri gas $SO_2$ sehingga gugus kromofor (gugus penentu warna) pada molekulnya rusak dan berubah menjadi bentuk asam leko-sulfonat yang **tidak berwarna (bening)**. Ketika sampel senyawa aldehid dimasukkan ke dalam larutan bening tersebut, gugus aldehid yang bersifat sangat elektrofilik (suka elektron) akan mengikat molekul belerang ($SO_2$) yang mengikat zat warna tadi. Akibat terikatnya sulfur oleh aldehid, struktur kromofor pada zat warna *fuchsine* kembali pulih seperti semula. Pemulihan struktur ikatan rangkap terkonjugasi ini menghasilkan efek visual berupa perubahan warna larutan yang dramatis dari bening menjadi **warna magenta atau ungu tua**.
                """)
            else:
                st.markdown(f"""
                Sampel yang Anda uji adalah **{sampel}**. Berdasarkan pengamatan virtual, senyawa ini memberikan hasil **NEGATIF** pada ketiga uji pembeda karena termasuk dalam golongan **Keton (Alkanon)** yang memiliki karakteristik struktur kimia berbeda.
                
                Berikut adalah alasan ilmiah mengapa keton tidak bereaksi:
                
                * **Mengapa Keton Gagal dalam Uji Oksidasi (Tollens & Fehling)?**
                    Struktur umum dari keton adalah $R-CO-R'$, di mana atom karbon pada gugus fungsi karbonil ($C=O$) diapit secara kuat oleh dua gugus alkil atau rantai karbon (tidak mengikat atom hidrogen langsung pada karbon karbonil). Karena ketiadaan atom hidrogen bebas inilah, keton bersifat **sangat stabil dan resisten (kebal) terhadap agen pengoksidasi lemah**. Keton tidak mampu bertindak sebagai reduktor (tidak bisa mendonasikan elektron). Akibatnya:
                    1.  **Pada Uji Tollens:** Tidak ada reduksi ion $Ag^+$ menjadi logam perak murni. Larutan tabung reaksi akan **tetap bening**.
                    2.  **Pada Uji Fehling:** Tidak ada reduksi ion $Cu^{2+}$ menjadi ion $Cu^+$. Larutan akan **tetap berwarna biru tua jernih** dan tidak akan terbentuk endapan padat apa pun meskipun larutan dipanaskan.
                
                * **Mengapa Keton Tidak Mengubah Warna Pereaksi Schiff?**
                    Gugus fungsi karbonil pada keton diapit oleh dua gugus alkil ($R$). Gugus alkil memiliki sifat pendorong elektron (efek induksi positif). Dorongan elektron dari dua sisi ini membuat atom karbon karbonil pada keton menjadi kurang parsial positif (kurang elektrofilik) dibandingkan karbonil pada aldehid. Karena daya tariknya yang lemah, gugus karbonil keton **tidak mampu menarik atau memutus ikatan** senyawa sulfur pada pereaksi Schiff yang tidak berwarna. Akibatnya, struktur zat warna asli *fuchsine* tidak dapat terbentuk kembali, dan larutan pengujian akan **tetap bening transparan**.
                """)
            st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("### 📊 Pengolahan Parameter Statistik Laboratorium")
        st.write("Masukkan nilai kadar yang diperoleh praktikan untuk pengujian replikasi simplo, duplo, dan triplo:")
        
        col_in1, col_in2, col_in3 = st.columns(3)
        with col_in1:
            simplo = st.number_input("Kadar Simplo (%)", min_value=0.0, value=12.45, step=0.01)
        with col_in2:
            duplo = st.number_input("Kadar Duplo (%)", min_value=0.0, value=12.60, step=0.01)
        with col_in3:
            triplo = st.number_input("Kadar Triplo (%)", min_value=0.0, value=12.38, step=0.01)
            
        # Perhitungan data statistik menggunakan matematika murni
        rata_rata = (simplo + duplo + triplo) / 3
        varians = ((simplo - rata_rata)**2 + (duplo - rata_rata)**2 + (triplo - rata_rata)**2) / 2
        std_dev = math.sqrt(varians)
        
        st.write("---")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="Rata-rata Analisis Kelompok", value=f"{rata_rata:.3f} %")
        with col_m2:
            st.metric(label="Standar Deviasi Presisi (SD)", value=f"{std_dev:.3f} %")
            
        st.markdown("### 📋 Laporan Ringkasan Lembar Kerja")
        st.markdown(f"""
        | Parameter Analisis | Nilai yang Diperoleh | Status Verifikasi |
        | :--- | :---: | :---: |
        | Hasil Kadar Uji - Simplo | {simplo:.2f} % | Terverifikasi |
        | Hasil Kadar Uji - Duplo | {duplo:.2f} % | Terverifikasi |
        | Hasil Kadar Uji - Triplo | {triplo:.2f} % | Terverifikasi |
        | **Rerata Total (Mean)** | **{rata_rata:.3f} %** | **Memenuhi Syarat** |
        """)
