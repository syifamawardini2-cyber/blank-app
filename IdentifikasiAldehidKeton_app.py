import streamlit as st
import pandas as pd

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Identifikasi Aldehid & Keton - Kelompok 6", 
    page_icon="🧪", 
    layout="wide"
)

# Custom CSS untuk tampilan premium & profesional (Aksesibilitas Teks Terjaga)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #3b82f6);
}
section[data-testid="stSidebar"] {
    background-color: #0f172a !important;
}
h1, h2, h3, h4, label, .stMarkdown, p, li {
    color: #ffffff !important;
}
.card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}
.identity-card {
    background: rgba(15, 23, 42, 0.6);
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #3b82f6;
    margin-top: 15px;
}
th, td {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Menu Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🧪 Navigasi</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Pilih Halaman:", [
        "🏠 Beranda",
        "📖 Teori Dasar",
        "⚗️ Pereaksi Identifikasi",
        "🧪 Simulasi Praktikum",
        "🧬 Hemiasetal & Asetal",
        "📝 Kesimpulan"
    ])
    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 0.8em;'>Politeknik AKA Bogor<br>D3 Analisis Kimia 2026</p>", unsafe_allow_html=True)

# ==================== 1. BERANDA ====================
if menu == "🏠 Beranda":
    st.title("🧪 IDENTIFIKASI ALDEHID DAN KETON")
    st.subheader("Aplikasi Edukasi & Simulasi Laboratorium Kimia Organik")
    
    st.markdown("""
    <div class="card">
    <h3>👋 Selamat Datang!</h3>
    Aplikasi ini dirancang sebagai media pembelajaran interaktif mengenai analisis kualitatif senyawa golongan 
    <b>Aldehid (Alkanal)</b> dan <b>Keton (Alkanon)</b>. Di sini, Anda dapat mempelajari teori dasar, 
    memahami prinsip kerja pereaksi spesifik, melihat persamaan reaksi kimia, hingga melakukan simulasi praktikum virtual.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👥 Identitas Pengembang")
    st.markdown("""
    <div class="identity-card">
    <h4><b>Kelompok 6 - Kelas 1D</b></h4>
    <p><b>Program Studi:</b> D3 Analisis Kimia</p>
    <p><b>Institusi:</b> Politeknik AKA Bogor</p>
    <hr style='border-color: rgba(255,255,255,0.2);'>
    <table>
        <tr><th>No.</th><th>Nama Anggota</th><th>NIM</th></tr>
        <tr><td>1.</td><td>Arrobbia Ainnur Kalam</td><td>2560582</td></tr>
        <tr><td>2.</td><td>Rafi Nanda Satria</td><td>2560740</td></tr>
        <tr><td>3.</td><td>Syaila Annisa Putri</td><td>2560791</td></tr>
        <tr><td>4.</td><td>Syifa Mawardini</td><td>2560793</td></tr>
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
        ### 🧪 Aldehid (Alkanal)
        - **Rumus Struktur:** $R-CHO$ (Gugus karbonil selalu berada di **ujung** rantai karbon terikat pada minimal satu atom hidrogen).
        - **Rumus Molekul:** $C_nH_{2n}O$
        - **Sifat Khas:** Sangat mudah teroksidasi menjadi asam karboksilat karena adanya atom hidrogen yang terikat langsung pada karbon karbonil.
        - **Kelarutan:** Suku rendah (metanal, etanal) sangat larut dalam air karena mampu membentuk ikatan hidrogen dengan air.
        """)
        
    with col2:
        st.markdown("""
        ### 🧪 Keton (Alkanon)
        - **Rumus Struktur:** $R-CO-R'$ (Gugus karbonil berada di **tengah** rantai, diapit oleh dua gugus alkil/aril).
        - **Rumus Molekul:** $C_nH_{2n}O$ (Isomer fungsional dari aldehid).
        - **Sifat Khas:** Cenderung stabil dan sulit dioksidasi karena tidak memiliki atom hidrogen yang terikat langsung pada gugus karbonil. Oksidasi keton memerlukan kondisi ekstrem yang dapat memutus ikatan $C-C$.
        """)

# ==================== 3. PEREAKSI IDENTIFIKASI ====================
elif menu == "⚗️ Pereaksi Identifikasi":
    st.title("⚗️ Pereaksi Identifikasi Kualitatif")
    st.write("Berikut adalah prinsip kimia analitik di balik metode identifikasi pembeda aldehid dan keton:")
    
    # Tollens
    with st.expander("🌟 1. Pereaksi Tollens (Uji Cerminan Perak)"):
        st.markdown("""
        - **Prinsip:** Menggunakan larutan perak nitrat ($AgNO_3$) dalam amonia berlebih yang membentuk ion kompleks $[Ag(NH_3)_2]^+$. 
        - **Mekanisme:** Aldehid bertindak sebagai reduktor yang mereduksi ion $Ag^+$ menjadi logam perak ($Ag^0$) yang menempel pada dinding tabung, membentuk cermin perak. Keton tidak bereaksi.
        - **Persamaan Reaksi:**
        """)
        st.latex(r"R-CHO + 2[Ag(NH_3)_2]^+ + 3OH^- \rightarrow R-COO^- + 2Ag_{(s)} \downarrow + 4NH_3 + 2H_2O")

    # Fehling
    with st.expander("🔴 2. Pereaksi Fehling"):
        st.markdown("""
        - **Prinsip:** Terdiri atas campuran Fehling A ($CuSO_4$) dan Fehling B (Kalium Natrium Tartrat + $NaOH$). Ion aktifnya adalah kompleks $Cu^{2+}$-tartrat.
        - **Mekanisme:** Aldehid mereduksi ion $Cu^{2+}$ (berwarna biru tua) dalam suasana basa menjadi endapan tembaga(I) oksida ($Cu_2O$) yang berwarna **merah bata**. Keton tidak bereaksi.
        - **Persamaan Reaksi:**
        """)
        st.latex(r"R-CHO + 2Cu^{2+} + 5OH^- \rightarrow R-COO^- + Cu_2O_{(s)} \downarrow + 3H_2O")

    # Schiff
    with st.expander("🔮 3. Pereaksi Schiff"):
        st.markdown("""
        - **Prinsip:** Pereaksi Schiff dibuat dari pewarna *fushsin* yang didekolorisasi (dihilangkan warnanya) menggunakan gas $SO_2$ atau natrium bisulfit.
        - **Mekanisme:** Ketika bereaksi dengan aldehid, gugus bisulfit pada pereaksi lepas, sehingga struktur kromofor *fuchsian* kembali pulih dan memunculkan warna **magenta/merah keunguan** yang khas. Keton umumnya memberikan hasil negatif atau bereaksi sangat lambat.
        """)

# ==================== 4. SIMULASI PRAKTIKUM ====================
elif menu == "🧪 Simulasi Praktikum":
    st.title("🧪 Laboratorium Virtual: Identifikasi Karbonil")
    st.write("Silakan pilih sampel senyawa kimia di bawah ini untuk melihat hasil uji laboratorium secara teoritis.")

    sampel = st.selectbox("Pilih Sampel Senyawa:", [
        "Formaldehid (Metanal) - Aldehid",
        "Asetaldehid (Etanal) - Aldehid",
        "Aseton (Propanon) - Keton",
        "Butanon (Metil Etil Keton) - Keton"
    ])

    if st.button("🔬 Jalankan Pengujian Tabung Reaksi"):
        st.write("---")
        st.subheader(f"📊 Hasil Analisis untuk: {sampel}")
        
        if "Aldehid" in sampel:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.success("🌟 TOLLENS: POSITIF (+)")
                st.info("Terbentuk lapisan cermin perak mengkilap pada dinding tabung reaksi.")
            with col2:
                st.success("🔴 FEHLING: POSITIF (+)")
                st.info("Larutan biru berubah menjadi endapan merah bata (Cu₂O).")
            with col3:
                st.success("🔮 SCHIFF: POSITIF (+)")
                st.info("Larutan bening berubah warna menjadi ungu/magenta tajam.")
            
            st.markdown("""
            <div class="card" style="margin-top:20px;">
            <h4>🧠 Pembahasan Analitis:</h4>
            Sampel yang Anda uji terbukti memiliki gugus fungsi <b>Aldehid (-CHO)</b>. Karena hidrogen pada gugus karbonil aldehid sangat labil, ia dengan mudah memberikan elektronnya kepada agen pengoksidasi lemah seperti pereaksi Tollens dan Fehling, mengoksidasi dirinya sendiri menjadi asam karboksilat.
            </div>
            """, unsafe_allow_html=True)
            
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.error("❌ TOLLENS: NEGATIF (-)")
                st.warning("Larutan tetap jernih/tidak terbentuk cermin perak.")
            with col2:
                st.error("❌ FEHLING: NEGATIF (-)")
                st.warning("Larutan tetap berwarna biru tua, tidak ada endapan.")
            with col3:
                st.error("❌ SCHIFF: NEGATIF (-)")
                st.warning("Tidak terjadi perubahan warna menjadi magenta.")
                
            st.markdown("""
            <div class="card" style="margin-top:20px;">
            <h4>🧠 Pembahasan Analitis:</h4>
            Sampel yang Anda uji terbukti merupakan senyawa golongan <b>Keton (R-CO-R')</b>. Keton tidak mempunyai hidrogen aktif yang terikat pada karbon karbonilnya, sehingga bersifat resisten terhadap oksidasi ringan. Oleh karena itu, keton memberikan hasil negatif terhadap uji Tollens, Fehling, maupun Schiff.
            </div>
            """, unsafe_allow_html=True)

# ==================== 5. HEMIASETAL & ASETAL ====================
elif menu == "🧬 Hemiasetal & Asetal":
    st.title("🧬 Konsep Lanjut: Hemiasetal dan Asetal")
    
    st.markdown("""
    <div class="card">
    <h3>💡 Mengapa Konsep ini Penting bagi Analis Kimia?</h3>
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

# ==================== 6. KESIMALAN ====================
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
