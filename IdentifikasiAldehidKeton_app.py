import streamlit as st
import math  # Library bawaan Python

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Identifikasi Aldehid & Keton - Kelompok 6", 
    page_icon="🧪", 
    layout="wide"
)

# Custom CSS Premium: Efek Lab Futuristik, Grid Pattern, & Solusi Selectbox Kontras
st.markdown("""
<style>
/* Background gradasi lab ultra modern dengan tekstur grid */
.stApp {
    background-color: #020617;
    background-image: 
        radial-gradient(at 0% 0%, rgba(30, 27, 75, 0.4) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(49, 16, 66, 0.5) 0px, transparent 50%),
        linear-gradient(rgba(255, 255, 255, 0.007) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.007) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px;
}
section[data-testid="stSidebar"] {
    background-color: #020617 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}
h1, h2, h3, h4, label, .stMarkdown, p, li {
    color: #f8fafc !important;
}
/* Efek Glassmorphism Premium dengan Pendaran Glow Lembut */
.card {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    border: 1px solid rgba(99, 102, 241, 0.15);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
}
/* Kartu Identitas */
.identity-card {
    background: rgba(2, 6, 23, 0.8);
    padding: 25px;
    border-radius: 16px;
    border-left: 6px solid #6366f1;
    margin-top: 15px;
    box-shadow: inset 0 0 20px rgba(99, 102, 241, 0.05);
}
/* Indikator Tabung Reaksi Virtual */
.tube-card {
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    font-weight: bold;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 12px 24px rgba(0,0,0,0.3);
    transition: transform 0.3s;
}
.pos-tollens { background: linear-gradient(135deg, #64748b, #0f172a); color: #fff !important; border-top: 5px solid #cbd5e1; }
.pos-fehling { background: linear-gradient(135deg, #dc2626, #450a0a); color: #fff !important; border-top: 5px solid #f87171; }
.pos-schiff { background: linear-gradient(135deg, #db2777, #4c0519); color: #fff !important; border-top: 5px solid #f472b6; }
.neg-tube { background: linear-gradient(135deg, #1e40af, #030712); color: #93c5fd !important; border-top: 5px solid #3b82f6; }

th, td {
    color: #e2e8f0 !important;
    padding: 12px;
}

/* PERBAIKAN STYLES DROP-DOWN (SELECTBOX) AGAR JELAS TERBACA */
div[data-baseweb="select"] {
    background-color: #0f172a !important;
    border-radius: 8px;
    border: 1px solid #475569 !important;
}
div[data-baseweb="select"] * {
    color: #ffffff !important;
}
ul[role="listbox"] {
    background-color: #0f172a !important;
}
ul[role="listbox"] li {
    color: #ffffff !important;
    background-color: #0f172a !important;
}
ul[role="listbox"] li:hover {
    background-color: #1e1b4b !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Menu Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #6366f1; letter-spacing: 1px;'>🧪 MENU NAVIGASI</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Navigasi Halaman:", [
        "🏠 Beranda",
        "📖 Teori Dasar",
        "⚗️ Pereaksi Identifikasi",
        "🧪 Simulasi & Lab Kuantitatif",
        "🧬 Hemiasetal & Asetal",
        "📝 Kesimpulan"
    ])
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 0.85em; color: #64748b;'>Politeknik AKA Bogor<br><b style='color: #94a3b8;'>D3 Analisis Kimia 2026</b></p>", unsafe_allow_html=True)

# ==================== 1. BERANDA ====================
if menu == "🏠 Beranda":
    st.title("🧪 IDENTIFIKASI ALDEHID DAN KETON")
    st.subheader("Aplikasi Edukasi & Simulasi Laboratorium Kimia Organik")
    
    st.markdown("""
    <div class="card">
    <h3 style="color: #6366f1;">👋 Selamat Datang!</h3>
    Aplikasi ini dirancang sebagai media pembelajaran interaktif mengenai analisis kualitatif senyawa golongan 
    <b>Aldehid (Alkanal)</b> dan <b>Keton (Alkanon)</b>. Di sini, Anda dapat mempelajari teori dasar, 
    memahami prinsip kerja pereaksi spesifik, melihat persamaan reaksi kimia, hingga melakukan simulasi praktikum virtual.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👥 Identitas Pengembang")
    st.markdown("""
    <div class="identity-card">
    <h4 style="color: #818cf8; margin-bottom: 5px;"><b>Kelompok 6 - Kelas 1D</b></h4>
    <p style="margin: 2px 0;"><b>Program Studi:</b> D3 Analisis Kimia</p>
    <p style="margin: 2px 0;"><b>Institusi:</b> Politeknik AKA Bogor</p>
    <hr style='border-color: rgba(99, 102, 241, 0.2); margin: 15px 0;'>
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="border-bottom: 2px solid rgba(99,102,241,0.3); text-align: left;"><th>No.</th><th>Nama Anggota</th><th>NIM</th></tr>
        <tr><td>1.</td><td>Arrobbia Ainnur Kalam</td><td>2560582</td></tr>
        <tr style="background: rgba(255,255,255,0.02);"><td>2.</td><td>Rafi Nanda Satria</td><td>2560740</td></tr>
        <tr><td>3.</td><td>Syaila Annisa Putri</td><td>2560791</td></tr>
        <tr style="background: rgba(255,255,255,0.02);"><td>4.</td><td>Syifa Mawardini</td><td>2560793</td></tr>
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
        <div class="card" style="border-top: 4px solid #6366f1;">
        <h3 style="color: #6366f1;">🧪 Aldehid (Alkanal)</h3>
        <ul>
            <li><b>Rumus Struktur:</b> $R-CHO$ (Gugus karbonil selalu terikat di ujung rantai).</li>
            <li><b>Rumus Molekul:</b> $C_nH_{2n}O$</li>
            <li><b>Sifat Khas:</b> Bersifat reduktor kuat karena keberadaan atom hidrogen labil yang terikat langsung pada atom karbon karbonil.</li>
            <li><b>Kelarutan:</b> Suku rendah (metanal, etanal) larut sempurna dalam air berkat pembentukan ikatan hidrogen intermolekul.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card" style="border-top: 4px solid #db2777;">
        <h3 style="color: #db2777;">🧪 Keton (Alkanon)</h3>
        <ul>
            <li><b>Rumus Struktur:</b> $R-CO-R'$ (Gugus karbonil berada di tengah, diapit dua gugus alkil).</li>
            <li><b>Rumus Molekul:</b> $C_nH_{2n}O$ (Isomer fungsional dari senyawa aldehid).</li>
            <li><b>Sifat Khas:</b> Cenderung inert terhadap oksidasi ringan karena tidak memiliki hidrogen yang terikat langsung pada karbon karbonil.</li>
            <li><b>Kelarutan:</b> Menurun secara linear seiring bertambah beratnya massa molekul relatif (gugus nonpolar membesar).</li>
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
        st.markdown("<p style='font-size:1.1em;'>Silakan pilih sampel senyawa kimia di bawah ini (Pilihan teks sekarang kontras dan terlihat jelas):</p>", unsafe_allow_html=True)

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
                        <p style="font-size: 1.5em; margin: 0;">🌟 TOLLENS</p>
                        <p style="font-size: 1.1em; color: #cbd5e1 !important; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Lapisan cermin perak mengkilap di dinding tabung.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown("""
                    <div class="tube-card pos-fehling">
                        <p style="font-size: 1.5em; margin: 0;">🔴 FEHLING</p>
                        <p style="font-size: 1.1em; color: #f87171 !important; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Endapan merah bata Cu₂O terbentuk sempurna.</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown("""
                    <div class="tube-card pos-schiff">
                        <p style="font-size: 1.5em; margin: 0;">🔮 SCHIFF</p>
                        <p style="font-size: 1.1em; color: #f472b6 !important; margin: 5px 0;">POSITIF (+)</p>
                        <span style="font-size: 0.85em; font-weight: normal;">Larutan jernih berubah menjadi warna magenta/ungu pekat.</span>
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
            # --- PEMBAHASAN DETAIIL DAN TAJAM KHAS KIMIA ANALITIK ---
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<h3 style='color: #818cf8; margin-top:0;'>🧠 Pembahasan Mekanisme & Justifikasi Kimia Analitis</h3>", unsafe_allow_html=True)
            
            if is_aldehid:
                st.markdown(f"""
                Berdasarkan hasil pengujian simulasi pada sampel **{sampel}**, senyawa ini memberikan respon **Positif Terhadap Seluruh Uji Kualitatif Pembeda**. Berikut adalah penjelasan teoritis mendalam per reaksi:
                
                1. **Mekanisme Uji Tollens (Reduksi Perak):**
                   Aldehid memiliki atom hidrogen yang terikat langsung pada karbon karbonil ($R-CHO$). Hidrogen ini sangat mudah melepaskan elektron (teroksidasi). Ketika direaksikan dengan pereaksi Tollens, ion kompleks $[Ag(NH_3)_2]^+$ bertindak sebagai agen pengoksidasi lemah. Ion $Ag^+$ mengalami reduksi (penurunan bilangan oksidasi dari +1 menjadi 0) menerima elektron dari gugus aldehid, mengendap sebagai logam perak murni murni ($Ag^0$) yang menempel secara mekanis pada permukaan kaca membentuk **cermin perak**. Senyawa aldehid sendiri teroksidasi menjadi ion karboksilat ($R-COO^-$).
                
                2. **Mekanisme Uji Fehling (Reduksi Kupri ke Kupro):**
                   Ion aktif dalam pereaksi Fehling adalah kompleks Kupri-tartrat ($Cu^{2+}$) berwarna biru tua dalam medium basa kuat. Gugus fungsi aldehid mereduksi ion $Cu^{2+}$ (biloks +2) menjadi ion $Cu^+$ (biloks +1). Ion $Cu^+$ yang tidak stabil dalam air basa langsung bergabung dengan ion $OH^-$ membentuk endapan **Tembaga(I) Oksida ($Cu_2O$)** yang secara fisik kasat mata berwarna **merah bata**. Reaksi ini membutuhkan pemanasan ringan untuk mempercepat energi aktivasi transfer elektron.
                
                3. **Mekanisme Uji Schiff (Restorasi Kromofor):**
                   Pereaksi Schiff awalnya adalah larutan *p-rosaniline hydrochloride* (fuchsine) yang berwarna pink tua, namun kehilangan warnanya (menjadi dekolorisasi/bening) karena direduksikan oleh gas $SO_2$ membentuk senyawa asam leko-sulfonat yang tidak lagi memiliki sistem ikatan rangkap terkonjugasi (kromofor rusak). Ketika ditambahkan sampel aldehid, aldehid yang sangat elektrofilik akan mengikat gugus sulfonat tersebut, sehingga struktur ikatan rangkap terkonjugasi dari zat warna fuchsine pulih kembali, memunculkan senyawa kompleks baru berwarna **magenta/ungu pekat** yang khas.
                """)
            else:
                st.markdown(f"""
                Berdasarkan hasil pengujian simulasi pada sampel **{sampel}**, senyawa ini memberikan respon **Negatif Terhadap Seluruh Uji Kualitatif Pembeda**. Berikut adalah analisis teoritis mengapa reaksi tidak terjadi:
                
                1. **Ketiadaan Hidrogen Aktif (Resistensi Oksidasi):**
                   Senyawa keton memiliki rumus umum $R-CO-R'$, di mana atom karbon karbonil diapit langsung oleh dua atom karbon alkil/aril lainnya. Karena tidak ada atom hidrogen yang melekat pada karbon karbonil ($C=O$), keton tidak memiliki donor elektron yang labil, sehingga **tidak dapat dioksidasi oleh oksidator lemah** seperti pereaksi Tollens maupun Fehling pada kondisi laboratorium standar.
                
                2. **Kegagalan Uji Kualitatif:**
                   - **Pada Uji Tollens & Fehling:** Tidak terjadi transfer elektron. Bilangan oksidasi ion perak tetap +1 (larutan tetap bening) dan bilangan oksidasi ion tembaga tetap +2 (larutan tetap berwarna biru jernih tanpa adanya endapan merah bata).
                   - **Pada Uji Schiff:** Gugus karbonil keton kurang elektrofilik dibandingkan aldehid karena adanya efek induksi positif (+I) dari dua gugus alkil yang menyumbang elektron ke atom karbon karbonil. Akibatnya, keton tidak mampu memutuskan ikatan asam leko-sulfonat pada pereaksi Schiff, sehingga warna larutan **tetap bening/tidak berubah**.
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
    <h3 style="color: #818cf8;">💡 Mengapa Konsep ini Penting bagi Analis Kimia?</h3>
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
