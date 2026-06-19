import streamlit as st
import math  # Library bawaan Python

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Identifikasi Aldehid & Keton - Kelompok 6", 
    page_icon="🧪", 
    layout="wide"
)

# Custom CSS Premium: Efek Lab Gelap, Glassmorphic Cards, & Glowing Effects
st.markdown("""
<style>
/* Background gradasi lab gelap */
.stApp {
    background: linear-gradient(135deg, #090d16 0%, #0f172a 50%, #1e293b 100%);
}
section[data-testid="stSidebar"] {
    background-color: #090d16 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}
h1, h2, h3, h4, label, .stMarkdown, p, li {
    color: #f8fafc !important;
}
/* Efek Glassmorphism Premium untuk Kontainer */
.card {
    background: rgba(30, 41, 59, 0.45);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
}
/* Kartu Identitas */
.identity-card {
    background: rgba(15, 23, 42, 0.7);
    padding: 25px;
    border-radius: 16px;
    border-left: 6px solid #3b82f6;
    margin-top: 15px;
}
/* Indikator Tabung Reaksi Virtual */
.tube-card {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}
.pos-tollens { background: linear-gradient(135deg, #868e96, #212529); color: #fff !important; border-top: 5px solid #dee2e6; }
.pos-fehling { background: linear-gradient(135deg, #b91c1c, #7f1d1d); color: #fff !important; border-top: 5px solid #f87171; }
.pos-schiff { background: linear-gradient(135deg, #be185d, #701a75); color: #fff !important; border-top: 5px solid #f472b6; }
.neg-tube { background: linear-gradient(135deg, #1e3a8a, #172554); color: #93c5fd !important; border-top: 5px solid #3b82f6; }

th, td {
    color: #e2e8f0 !important;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Menu Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #3b82f6;'>🧪 MENU UTAMA</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Navigasi Halaman:", [
        "🏠 Beranda",
        "📖 Teori Dasar",
        "⚗️ Pereaksi Identifikasi",
        "🧪 Simulasi & Lab Kuantitatif",
        "🧬 Hemiasetal & Asetal",
        "📝 Kesimpulan"
    ])
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 0.85em; color: #94a3b8;'>Politeknik AKA Bogor<br><b>D3 Analisis Kimia 2026</b></p>", unsafe_allow_html=True)

# ==================== 1. BERANDA ====================
if menu == "🏠 Beranda":
    st.title("🧪 IDENTIFIKASI ALDEHID DAN KETON")
    st.subheader("Aplikasi Edukasi & Simulasi Laboratorium Kimia Organik")
    
    st.markdown("""
    <div class="card">
    <h3 style="color: #3b82f6;">👋 Selamat Datang!</h3>
    Aplikasi ini dirancang sebagai media pembelajaran interaktif mengenai analisis kualitatif senyawa golongan 
    <b>Aldehid (Alkanal)</b> dan <b>Keton (Alkanon)</b>. Di sini, Anda dapat mempelajari teori dasar, 
    memahami prinsip kerja pereaksi spesifik, melihat persamaan reaksi kimia, hingga melakukan simulasi praktikum virtual.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👥 Identitas Pengembang")
    st.markdown("""
    <div class="identity-card">
    <h4 style="color: #60a5fa; margin-bottom: 5px;"><b>Kelompok 6 - Kelas 1D</b></h4>
    <p style="margin: 2px 0;"><b>Program Studi:</b> D3 Analisis Kimia</p>
    <p style="margin: 2px 0;"><b>Institusi:</b> Politeknik AKA Bogor</p>
    <hr style='border-color: rgba(255,255,255,0.15); margin: 15px 0;'>
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="border-bottom: 2px solid rgba(255,255,255,0.2);"><th>No.</th><th>Nama Anggota</th><th>NIM</th></tr>
        <tr><td>1.</td><td>Arrobbia Ainnur Kalam</td><td>2560582</td></tr>
        <tr style="background: rgba(255,255,255,0.03);"><td>2.</td><td>Rafi Nanda Satria</td><td>2560740</td></tr>
        <tr><td>3.</td><td>Syaila Annisa Putri</td><td>2560791</td></tr>
        <tr style="background: rgba(255,255,255,0.03);"><td>4.</td><td>Syifa Mawardini</td><td>2560793</td></tr>
        <tr><td>5.</td><td>Yusela Tsalsa Siwi</td><td>2560808</td></tr>
    </table>
    </div>
    """, unsafe_allow_html=True)

# ==================== 2. TEORI DASAR ====================
elif menu == "📖 Teori Dasar":
    st.title("📖 Teori Dasar: Gugus Karbonil")
    
    st.markdown("""
    <div class="card">
    Aldehid dan keton adalah dua kelas senyawa organik yang sama-sama mengandung <b>gugus fungsi karbonil (C=O)</b>. 
    Perbedaan utama di antara keduanya terletak pada posisi gugus karbonil tersebut pada rantai karbon, yang 
    secara drastis memengaruhi reaktivitas kimianya, terutama terhadap agen pengoksidasi (oksidator).
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card" style="border-top: 4px solid #3b82f6;">
        <h3 style="color: #3b82f6;">🧪 Aldehid (Alkanal)</h3>
        <ul>
            <li><b>Rumus Struktur:</b> $R-CHO$ (Gugus karbonil di ujung rantai).</li>
            <li><b>Rumus Molekul:</b> $C_nH_{2n}O$</li>
            <li><b>Sifat Khas:</b> Sangat reaktif dan mudah teroksidasi menjadi asam karboksilat karena adanya atom hidrogen bebas pada karbon karbonil.</li>
            <li><b>Kelarutan:</b> Suku rendah sangat larut dalam air akibat kemampuan membentuk ikatan hidrogen.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card" style="border-top: 4px solid #ef4444;">
        <h3 style="color: #ef4444;">🧪 Keton (Alkanon)</h3>
        <ul>
            <li><b>Rumus Struktur:</b> $R-CO-R'$ (Gugus karbonil diapit dua gugus alkil).</li>
            <li><b>Rumus Molekul:</b> $C_nH_{2n}O$ (Isomer fungsional aldehid).</li>
            <li><b>Sifat Khas:</b> Stabil dan sulit dioksidasi karena tidak memiliki atom hidrogen yang terikat langsung pada gugus karbonil.</li>
            <li><b>Kelarutan:</b> Menurun seiring bertambahnya panjang rantai karbon (gugus hidrofobik).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== 3. PEREAKSI IDENTIFIKASI ====================
elif menu == "⚗️ Pereaksi Identifikasi":
    st.title("⚗️ Pereaksi Identifikasi Kualitatif")
    st.write("Berikut adalah prinsip kimia analitik di balik metode identifikasi pembeda aldehid dan keton:")
    
    with st.expander("🌟 1. Pereaksi Tollens (Uji Cerminan Perak)"):
        st.markdown("""
        - **Prinsip:** Menggunakan larutan perak nitrat ($AgNO_3$) dalam amonia berlebih membentuk ion kompleks $[Ag(NH_3)_2]^+$. 
        - **Mekanisme:** Aldehid mereduksi ion $Ag^+$ menjadi logam perak ($Ag^0$) yang mengendap membentuk cermin perak pada dinding tabung. Keton tidak bereaksi.
        - **Persamaan Reaksi:**
        """)
        st.latex(r"R-CHO + 2[Ag(NH_3)_2]^+ + 3OH^- \rightarrow R-COO^- + 2Ag_{(s)} \downarrow + 4NH_3 + 2H_2O")

    with st.expander("🔴 2. Pereaksi Fehling"):
        st.markdown("""
        - **Prinsip:** Campuran Fehling A ($CuSO_4$) dan Fehling B (Kalium Natrium Tartrat + $NaOH$).
        - **Mekanisme:** Aldehid mereduksi ion $Cu^{2+}$ (biru tua) menjadi endapan tembaga(I) oksida ($Cu_2O$) berwarna **merah bata**. Keton memberikan hasil negatif.
        - **Persamaan Reaksi:**
        """)
        st.latex(r"R-CHO + 2Cu^{2+} + 5OH^- \rightarrow R-COO^- + Cu_2O_{(s)} \downarrow + 3H_2O")

    with st.expander("🔮 3. Pereaksi Schiff"):
        st.markdown("""
        - **Prinsip:** Zat warna *fuchsine* yang didekolorisasi dengan belerang dioksida ($SO_2$).
        - **Mekanisme:** Bereaksi spesifik dengan aldehid untuk mengembalikan struktur kromofor asli, menghasilkan warna **magenta/ungu pekat**. Keton tidak mengubah warna larutan secara signifikan.
        """)

# ==================== 4. SIMULASI & LAB KUANTITATIF ====================
elif menu == "🧪 Simulasi & Lab Kuantitatif":
    st.title("🧪 Laboratorium Virtual & Pengolahan Data Analisis")
    
    tab1, tab2 = st.tabs(["🔬 Rak Tabung Reaksi Virtual", "📊 Kalkulator Akurasi & Presisi"])
    
    with tab1:
        st.write("Silakan pilih sampel senyawa kimia di bawah ini untuk memulai pengujian kualitatif visual:")

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
            
            # FITUR BARU: Visualisasi Rak Tabung Reaksi Berbasis Kartu Berwarna Realistis
            col1, col2, col3 = st.columns(3)
            
            if is_aldehid:
                with col1:
                    st.markdown("""
                    <div class="tube-card pos-tollens">
                        <p style="font-size: 1.5em; margin: 0;">🌟 TOLLENS</p>
                        <p style="font-size: 1.1em; color: #e2e8f0 !important; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Terbentuk lapisan cermin perak mengkilap mendinding.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown("""
                    <div class="tube-card pos-fehling">
                        <p style="font-size: 1.5em; margin: 0;">🔴 FEHLING</p>
                        <p style="font-size: 1.1em; color: #e2e8f0 !important; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Larutan biru berubah total menjadi endapan merah bata Cu₂O.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown("""
                    <div class="tube-card pos-schiff">
                        <p style="font-size: 1.5em; margin: 0;">🔮 SCHIFF</p>
                        <p style="font-size: 1.1em; color: #e2e8f0 !important; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Larutan jernih berubah seketika menjadi ungu/magenta tajam.</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                with col1:
                    st.markdown("""
                    <div class="tube-card neg-tube">
                        <p style="font-size: 1.5em; margin: 0;">🌟 TOLLENS</p>
                        <p style="font-size: 1.1em; margin: 5px 0;">NEGATIF (-)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Larutan tetap jernih transparan, tidak ada cermin perak.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown("""
                    <div class="tube-card neg-tube">
                        <p style="font-size: 1.5em; margin: 0;">🔴 FEHLING</p>
                        <p style="font-size: 1.1em; margin: 5px 0;">NEGATIF (-)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Larutan konstan berwarna biru tua jernih, tanpa endapan.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown("""
                    <div class="tube-card neg-tube">
                        <p style="font-size: 1.5em; margin: 0;">🔮 SCHIFF</p>
                        <p style="font-size: 1.1em; margin: 5px 0;">NEGATIF (-)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Tidak terjadi perubahan warna menjadi magenta (tetap bening).</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.write("")
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<h4 style='color: #60a5fa;'>🧠 Justifikasi Kimia Analitis:</h4>", unsafe_allow_html=True)
            if is_aldehid:
                st.markdown("Sampel yang diuji terbukti kuat memiliki gugus fungsi <b>Aldehid (-CHO)</b>. Elektron dari hidrogen labil karbonil dengan mudah mereduksi spesi pengoksidasi lemah dalam suasana uji kualitatif.")
            else:
                st.markdown("Sampel terbukti merupakan golongan <b>Keton (R-CO-R')</b>. Kandungan gugus alkil yang mengapit karbonil memproteksi senyawa dari agen oksidator kualitatif, menghasilkan respon negatif visual.")
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
            
        # Perhitungan data statistik
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

# ==================== 5. HEMIASETAL & ASETAL ====================
elif menu == "🧬 Hemiasetal & Asetal":
    st.title("🧬 Konsep Lanjut: Hemiasetal dan Asetal")
    
    st.markdown("""
    <div class="card">
    <h3 style="color: #60a5fa;">💡 Mengapa Konsep ini Penting bagi Analis Kimia?</h3>
    Dalam sampel nyata, aldehid atau keton sering kali tidak berdiri sendiri. Jika terdapat molekul alkohol dalam lingkungan larutan, 
    gugus karbonil dapat mengalami reaksi adisi nukleofilik membentuk struktur <b>Hemiasetal</b> atau <b>Asetal</b>. 
    Hal ini krusial dipahami karena pembentukan senyawa ini dapat "menyembunyikan" gugus fungsi asli yang ingin kita identifikasi.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🔄 Proses Pembentukan
    1. **Hemiasetal / Hemiketal:** Terbentuk dari reaksi reversibel antara 1 molekul aldehid/keton dengan **1 molekul alkohol**. Memiliki gugus $-OH$ (eter) dan $-OR$ (alkoksi) pada atom karbon yang sama.
    2. **Asetal / Ketal:** Terbentuk ketika hemiasetal bereaksi lebih lanjut dengan **molekul alkohol kedua** dengan bantuan katalis asam ($H^+$), melepaskan molekul air ($H_2O$).
    
    ### ⚠️ Dampak Terhadap Analisis Kualitatif di Laboratorium:
    - **Masking Effect (Penyamaran):** Ketika aldehid berubah menjadi asetal, gugus karbonil ($C=O$) yang reaktif berubah menjadi ikatan tunggal eter ($-C-O-C-$) yang jauh lebih stabil.
    - **Hasil Negatif Palsu (False Negative):** Karena asetal bersifat stabil terhadap basa, pereaksi seperti **Fehling** dan **Tollens** (yang lingkungannya basa) tidak akan mampu memutuskan ikatan asetal tersebut. Akibatnya, aldehid yang telah berubah menjadi asetal akan memberikan hasil **negatif**, padahal sampel aselinya mengandung aldehid.
    - **Solusi Analisis:** Untuk mengidentifikasinya dengan benar, sampel asetal harus dihidrolisis terlebih dahulu menggunakan **asam encer** agar gugus aldehid bebasnya kembali lepas sebelum diuji dengan pereaksi identifikasi.
    """)

# ==================== 6. KESIMPULAN ====================
elif menu == "📝 Kesimpulan":
    st.title("📝 Kesimpulan Analisis")
    
    st.markdown("""
    <div class="card">
    Berdasarkan kajian teori dan simulasi praktikum identifikasi senyawa aldehid dan keton, dapat disimpulkan bahwa:
    <br><br>
    1. <b>Diferensiasi Reaktivitas:</b> Aldehid sangat mudah dioksidasi karena memiliki atom hidrogen bebas pada karbon karbonilnya, sedangkan keton relatif inert terhadap oksidator lemah.
    <br><br>
    2. <b>Spesifisitas Pereaksi:</b> 
    <ul>
        <li>Pereaksi <b>Tollens</b> mengidentifikasi aldehid melalui pembentukan cermin perak ($Ag$).</li>
        <li>Pereaksi <b>Fehling</b> mengidentifikasi aldehid melalui pembentukan endapan merah bata ($Cu_2O$).</li>
        <li>Pereaksi <b>Schiff</b> mendeteksi gugus aldehid lewat restorasi warna magenta.</li>
    </ul>
    3. <b>Faktor Pengganggu (Interferensi):</b> Reaksi pembentukan hemiasetal dan asetal dapat memproteksi gugus karbonil dari reaksi oksidasi dalam suasana basa, sehingga pemahaman mekanismenya penting untuk menghindari kesalahan interpretasi (negatif palsu) di laboratorium kimia.
    </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
