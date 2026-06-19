import streamlit as st
import math  # Library bawaan Python

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Identifikasi Aldehid & Keton - Kelompok 6", 
    page_icon="🧪", 
    layout="wide"
)

# Custom CSS Premium: Latar Belakang Lab Hebat, Grid Pattern, & Solusi Selectbox Kontras
st.markdown("""
<style>
/* 1. LATAR BELAKANG LUAR BIASA BAGUS: Gradasi Kosmik & Tekstur Grid Lab */
.stApp {
    background-color: #020617;
    background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(168, 85, 247, 0.2) 0px, transparent 50%),
        linear-gradient(rgba(255, 255, 255, 0.005) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.005) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 35px 35px, 35px 35px;
}

/* Sidebar Estetik Gelap */
section[data-testid="stSidebar"] {
    background-color: #030712 !important;
    border-right: 1px solid rgba(99, 102, 241, 0.1);
}
h1, h2, h3, h4, label, .stMarkdown, p, li {
    color: #f8fafc !important;
}

/* 2. KARTU DENGAN EFEK GLOWING NEON (GLASSMORPHISM) */
.card {
    background: rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    border: 1px solid rgba(99, 102, 241, 0.2);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), 0 0 15px rgba(99, 102, 241, 0.05);
}

/* Kartu Identitas Pengembang */
.identity-card {
    background: rgba(3, 7, 18, 0.8);
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
    box-shadow: 0 12px 24px rgba(0,0,0,0.4);
}
.pos-tollens { background: linear-gradient(135deg, #64748b, #0f172a); color: #fff !important; border-top: 5px solid #cbd5e1; }
.pos-fehling { background: linear-gradient(135deg, #dc2626, #450a0a); color: #fff !important; border-top: 5px solid #f87171; }
.pos-schiff { background: linear-gradient(135deg, #db2777, #4c0519); color: #fff !important; border-top: 5px solid #f472b6; }
.neg-tube { background: linear-gradient(135deg, #1e40af, #030712); color: #93c5fd !important; border-top: 5px solid #3b82f6; }

th, td {
    color: #e2e8f0 !important;
    padding: 12px;
}

/* 3. PERBAIKAN TOTAL DROP-DOWN (SELECTBOX) SUPAYA JELAS TERBACA */
div[data-baseweb="select"] {
    background-color: #0f172a !important;
    border: 1px solid #6366f1 !important;
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
        st.markdown("<p style='font-size:1.15em; color: #e2e8f0;'>Silakan pilih sampel senyawa kimia di bawah ini untuk memulai pengujian kualitatif visual secara virtual:</p>", unsafe_allow_html=True)

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
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<h3 style='color: #818cf8; margin-top:0;'>🧠 Justifikasi & Pembahasan Kimia Analitis Terperinci</h3>", unsafe_allow_html=True)
            
            if is_aldehid:
                st.markdown(f"""
                Sampel yang Anda uji adalah **{sampel}**. Berdasarkan pengamatan virtual, senyawa ini memberikan hasil **POSITIF** pada ketiga uji pembeda karena termasuk dalam golongan **Aldehid (Alkanal)**. 
                
                Berikut adalah penjelasan detail mekanisme reaksinya agar mudah dipahami:
                
                * **Mengapa Uji Tollens Membentuk Cermin Perak?**
                    Aldehid memiliki atom hidrogen yang terikat langsung pada gugus fungsi karbonil ($R-CHO$). Atom hidrogen ini bersifat labil dan sangat mudah melepaskan elektronnya (mengalami oksidasi). Ketika ditambahkan pereaksi Tollens yang mengandung ion kompleks $[Ag(NH_3)_2]^+$, gugus aldehid bertindak sebagai **reduktor**. Gugus aldehid menyerahkan elektronnya untuk mereduksi ion $Ag^+$ (bilangan oksidasi +1) menjadi logam perak murni ($Ag^0$, bilangan oksidasi 0). Secara fisik, atom perak bebas ini akan mengendap dan menempel dengan rapat pada dinding dalam tabung reaksi yang bersih, membentuk lapisan mengkilap seperti **cermin perak**. Sementara itu, senyawa aldehidnya sendiri naik tingkat oksidasinya menjadi asam karboksilat.
                
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
