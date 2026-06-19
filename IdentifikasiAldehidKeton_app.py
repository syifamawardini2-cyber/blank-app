import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Identifikasi Aldehid & Keton - Kelompok 6", 
    page_icon="🧪", 
    layout="wide"
)

# Custom CSS Premium: Tema Gradasi Biru-Merah Futuristik & Partikel Ikon Organik Glow
st.markdown("""
<style>
/* Background Gradasi Biru - Merah Futuristik */
.stApp {
    background: #0d0b18;
    background-image: 
        radial-gradient(circle at 10% 15%, rgba(37, 99, 235, 0.25) 0%, transparent 55%),
        radial-gradient(circle at 90% 85%, rgba(225, 29, 72, 0.22) 0%, transparent 60%),
        linear-gradient(135deg, #09070f 0%, #11132e 50%, #1c0d18 100%);
    background-attachment: fixed;
    overflow-x: hidden;
}

/* Penambahan Micro-Icons Unsur Organik dengan Efek Transparan */
.stApp::before {
    content: "⬡ 🧪 ⚛ ⬢ 🧪 ⬡ ⚛ ⬢";
    position: fixed;
    top: 5%;
    left: 3%;
    font-size: 28px;
    color: rgba(37, 99, 235, 0.08);
    font-family: monospace;
    pointer-events: none;
    letter-spacing: 40px;
    line-height: 200px;
    word-break: break-all;
    width: 95vw;
}

.stApp::after {
    content: "🧪 ⚛ ⬢ ⬡ 🧪 ⬢ ⚛ ⬡";
    position: fixed;
    bottom: 8%;
    right: 5%;
    font-size: 24px;
    color: rgba(225, 29, 72, 0.07);
    font-family: monospace;
    pointer-events: none;
    letter-spacing: 50px;
    line-height: 180px;
    word-break: break-all;
    direction: rtl;
    width: 95vw;
}

/* Sidebar Styling Khusus dengan Batas Gradasi Lembut */
section[data-testid="stSidebar"] {
    background-color: #06050b !important;
    border-right: 2px solid rgba(139, 92, 246, 0.25);
}

/* Warna Teks Utama */
h1, h2, h3, h4, label, .stMarkdown, p, li {
    color: #f8fafc !important;
}

/* Efek Glassmorphism Premium dengan Pendaran Neon Halus (Cyber-Lab Card) */
.card {
    background: rgba(20, 18, 33, 0.7);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5), 0 0 15px rgba(139, 92, 246, 0.05);
}

/* Kartu Identitas dengan Garis Samping Gradasi */
.identity-card {
    background: rgba(10, 8, 18, 0.9);
    padding: 25px;
    border-radius: 16px;
    border-left: 6px solid #e11d48;
    margin-top: 15px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

/* Indikator Tabung Reaksi Virtual */
.tube-card {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}
.pos-tollens { background: linear-gradient(135deg, #868e96, #212529); color: #fff !important; border-top: 5px solid #dee2e6; }
.pos-fehling { background: linear-gradient(135deg, #e11d48, #4c0519); color: #fff !important; border-top: 5px solid #fda4af; }
.pos-schiff { background: linear-gradient(135deg, #be185d, #4c0519); color: #fff !important; border-top: 5px solid #f472b6; }
.neg-tube { background: linear-gradient(135deg, #1d4ed8, #0f172a); color: #93c5fd !important; border-top: 5px solid #60a5fa; }

/* Menjaga warna teks tombol lab kualitatif agar tetap terbaca */
.tube-card p, .tube-card span {
    color: #ffffff !important;
}

th, td {
    color: #e2e8f0 !important;
    padding: 10px;
}

/* Mengubah warna teks list item drop-down menjadi hitam agar kontras saat melayang */
div[role="listbox"] li {
    color: #000000 !important;
    background-color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Menu Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #db2777;'>⬡ MENU UTAMA</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Navigasi Halaman:", [
        "🏠 Beranda",
        "📖 Teori Dasar",
        "⚗️ Pereaksi Identifikasi",
        "🧪 Simulasi & Lab Kualitatif",
        "🧬 Hemiasetal & Asetal",
        "📝 Kesimpulan"
    ])
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 0.85em; color: #a1a1aa;'>Politeknik AKA Bogor<br><b>D3 Analisis Kimia 2026</b></p>", unsafe_allow_html=True)

# ==================== 1. BERANDA ====================
if menu == "🏠 Beranda":
    st.title("🧪 IDENTIFIKASI ALDEHID DAN KETON")
    st.subheader("Aplikasi Edukasi & Simulasi Laboratorium Kimia Organik")
    
    st.markdown("""
    <div class="card">
    <h3 style="color: #2563eb;">👋 Selamat Datang!</h3>
    Aplikasi ini dirancang sebagai media pembelajaran interaktif mengenai analisis kualitatif senyawa golongan 
    <b>Aldehid (Alkanal)</b> dan <b>Keton (Alkanon)</b>. Di sini, Anda dapat mempelajari teori dasar, 
    memahami prinsip kerja pereaksi spesifik, melihat persamaan reaksi kimia, hingga melakukan simulasi praktikum virtual.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👥 Identitas Pengembang")
    st.markdown("""
    <div class="identity-card">
    <h4 style="color: #f43f5e; margin-bottom: 5px;"><b>Kelompok 6 - Kelas 1D</b></h4>
    <p style="margin: 2px 0;"><b>Program Studi:</b> D3 Analisis Kimia</p>
    <p style="margin: 2px 0;"><b>Institusi:</b> Politeknik AKA Bogor</p>
    <hr style='border-color: rgba(255,255,255,0.1); margin: 15px 0;'>
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="border-bottom: 2px solid rgba(255,255,255,0.15);"><th>No.</th><th>Nama Anggota</th><th>NIM</th></tr>
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
        <div class="card" style="border-top: 4px solid #2563eb;">
        <h3 style="color: #2563eb;">🧪 Aldehid (Alkanal)</h3>
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
        <div class="card" style="border-top: 4px solid #e11d48;">
        <h3 style="color: #e11d48;">🧪 Keton (Alkanon)</h3>
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

# ==================== 4. SIMULASI & LAB KUALITATIF ====================
elif menu == "🧪 Simulasi & Lab Kualitatif":
    st.title("🧪 Laboratorium Virtual & Analisis Gugus Fungsi")
    
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
        col1, col2, col3 = st.columns(3)
        
        if is_aldehid:
            with col1:
                st.markdown("""
                <div class="tube-card pos-tollens">
                    <p style="font-size: 1.5em; margin: 0;">🌟 TOLLENS</p>
                    <p style="font-size: 1.1em; margin: 5px 0;">POSITIF (+)</p>
                    <span style="font-size: 0.85em; font-weight: normal;">Terbentuk lapisan cermin perak mengkilap mendinding.</span>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="tube-card pos-fehling">
                    <p style="font-size: 1.5em; margin: 0;">🔴 FEHLING</p>
                    <p style="font-size: 1.1em; margin: 5px 0;">POSITIF (+)</p>
                    <span style="font-size: 0.85em; font-weight: normal;">Larutan biru berubah total menjadi endapan merah bata Cu₂O.</span>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown("""
                <div class="tube-card pos-schiff">
                    <p style="font-size: 1.5em; margin: 0;">🔮 SCHIFF</p>
                    <p style="font-size: 1.1em; margin: 5px 0;">POSITIF (+)</p>
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
        
        # JALUR PEMBAHASAN DETAIL
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: #f43f5e; margin-top: 0;'>🧠 Pembahasan Kimia Analitis Eksklusif</h3>", unsafe_allow_html=True)
        
        if is_aldehid:
            st.markdown(f"""
            Senyawa **{sampel}** sukses memberikan hasil **POSITIF** pada semua uji karena ia memiliki gugus fungsi **Aldehid ($R-CHO$)**. 
            Kunci utama reaktivitas aldehid terletak pada **atom hidrogen ($H$)** yang terikat langsung pada karbon karbonil ($C=O$). Hidrogen ini sangat rapuh (labil) sehingga aldehid berperan sebagai **reduktor kuat** (penyumbang elektron).

            #### 1. Uji Tollens (Mengapa Muncul Cermin Perak?)
            * **Alasan Positif:** Pereaksi Tollens mengandung ion kompleks perak diamina $[Ag(NH_3)_2]^+$. Karena aldehid suka mendonasikan elektronnya, ia mereduksi ion perak tersebut menjadi logam perak murni bermuatan netral.
            * **Mengapa Warnanya Begitu?** Logam perak yang baru terbentuk berwujud partikel padat mikroskopis. Partikel-partikel ini akan menempel dan melapisi permukaan kaca bagian dalam tabung reaksi yang bersih secara merata, menghasilkan visual reflektif kilap seperti **cermin kaca perak**.
            * **Persamaan Reaksi:**
            """)
            st.latex(r"R-CHO + 2[Ag(NH_3)_2]^+ + 3OH^- \rightarrow R-COO^- + 2Ag_{(s)} \downarrow + 4NH_3 + 2H_2O")
            
            st.markdown("""
            #### 2. Uji Fehling (Mengapa Terbentuk Endapan Merah Bata?)
            * **Alasan Positif:** Pereaksi Fehling kaya akan ion tembaga(II) atau Kupri ($Cu^{2+}$) berwarna biru tua yang diikat oleh garam tartrat dalam suasana basa. Aldehid yang mereduksi lingkungan sekitarnya memaksa ion Kupri menangkap elektron dan berubah menjadi ion Kupro ($Cu^+$).
            * **Mengapa Warnanya Begitu?** Ion Kupro langsung berikatan dengan ion hidroksida dari basa kuat, membentuk senyawa padat baru bernama **Tembaga(I) Oksida ($Cu_2O$)**. Karakteristik alami dari molekul kristal ini tidak larut di dalam air dan memantulkan spektrum cahaya berwarna **merah bata**.
            * **Persamaan Reaksi:**
            """)
            st.latex(r"R-CHO + 2Cu^{2+} + 5OH^- \rightarrow R-COO^- + Cu_2O_{(s)} \downarrow + 3H_2O")
            
            st.markdown("""
            #### 3. Uji Schiff (Mengapa Berubah Menjadi Magenta/Ungu Tua?)
            * **Alasan Positif & Perubahan Warna:** Pereaksi Schiff awalnya dibuat dari zat warna merah bernama *fuchsine*. Zat warna tersebut dialiri gas belerang dioksida sehingga strukturnya rusak dan warnanya hilang total (menjadi bening). Ketika senyawa aldehid ditambahkan, sifat aldehid yang sangat suka elektron (*elektrofilik*) akan menyerang dan menarik molekul belerang menjauh dari zat warna tersebut. Karena belerang terlepas, struktur pembawa warna asli (*kromofor*) dari *fuchsine* kembali pulih dan memancarkan warna **magenta atau ungu pekat**.
            """)
        else:
            st.markdown(f"""
            Senyawa **{sampel}** memberikan hasil **NEGATIF** pada seluruh uji karena merupakan golongan **Keton ($R-CO-R'$)**. 
            Keton memiliki struktur di mana karbon karbonil ($C=O$) dijepit erat di tengah-tengah oleh dua rantai karbon (gugus alkil) dan **tidak mempunyai atom hidrogen** yang menempel langsung pada pusat karbonilnya.

            #### 1. Gagal Pada Uji Oksidasi (Tollens & Fehling)
            * **Alasan Negatif:** Karena tidak memiliki hidrogen labil, keton adalah senyawa yang stabil dan bersifat **inert (tidak reaktif)** terhadap zat pengoksidasi lemah. Keton tidak mampu menyumbangkan elektron kepada ion perak pada pereaksi Tollens maupun ion tembaga pada pereaksi Fehling.
            * **Mengapa Warnanya Begitu?** Akibat tidak terjadinya perpindahan elektron ataupun pembentukan senyawa baru:
              - Pada **Tollens**, larutan akan **tetap jernih transparan** tanpa kilapan perak sedikit pun.
              - Pada **Fehling**, larutan akan **tetap berwarna biru tua bening** bawaan dari ion kompleks tembaga, bahkan setelah tabung dipanaskan dalam penangas air.

            #### 2. Gagal Pada Uji Schiff
            * **Alasan Negatif & Warna:** Dua gugus alkil yang mengapit karbonil pada keton selalu mendorong elektron ke arah pusat. Hal ini membuat pusat karbonil keton menjadi tidak begitu haus elektron dibandingkan dengan aldehid. Akibatnya, keton **tidak punya kekuatan yang cukup** untuk menarik atau merebut molekul belerang dari pereaksi Schiff. Struktur penentu warna *fuchsine* tetap rusak, sehingga larutan pengujian akan **tetap konstan bening atau tidak berwarna**.
            """)
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== 5. HEMIASETAL & ASETAL ====================
elif menu == "🧬 Hemiasetal & Asetal":
    st.title("🧬 Konsep Lanjut: Hemiasetal dan Asetal")
    
    st.markdown("""
    <div class="card">
    <h3 style="color: #2563eb;">💡 Mengapa Konsep ini Penting bagi Analis Kimia?</h3>
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
