import streamlit as st

# 1. Atur konfigurasi halaman Streamlit agar memenuhi layar (Wide Mode)
st.set_page_config(
    page_title="PCPM BI: Analisis Profil & Karir",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Masukkan seluruh kode HTML + Tailwind + Chart.js Anda ke dalam variabel teks
html_code = """
<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCPM BI: Analisis Profil & Karir</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 400px;
        }
        @media (min-width: 768px) { .chart-container { height: 400px; } }
        @media (max-width: 640px) { .chart-container { height: 280px; } }
        
        .tab-content {
            display: none;
            animation: fadeIn 0.4s ease-in-out;
        }
        .tab-content.active { display: block; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .timeline-node, .skill-card { transition: all 0.3s ease; }
        .timeline-node:hover, .skill-card:hover {
            transform: scale(1.03);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
    </style>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        bi: {
                            blue: '#004A8D',
                            light: '#E6F0F9',
                            gold: '#D4AF37'
                        }
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">

    <!-- Navigation -->
    <nav class="fixed w-full bg-white/90 backdrop-blur-md shadow-sm z-50 top-0 border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center space-x-2">
                    <span class="text-2xl">🏦</span>
                    <span class="font-bold text-xl text-bi-blue tracking-tight">PCPM<span class="text-slate-500 font-light">Insight</span></span>
                </div>
                <div class="hidden md:flex space-x-8 text-sm font-semibold text-slate-600">
                    <a href="#overview" class="hover:text-bi-blue transition-colors">Overview</a>
                    <a href="#seleksi" class="hover:text-bi-blue transition-colors">Jalur Seleksi</a>
                    <a href="#skills" class="hover:text-bi-blue transition-colors text-bi-blue border-b-2 border-bi-blue pb-1">Skill Set & Prep</a>
                    <a href="#pekerjaan" class="hover:text-bi-blue transition-colors">Apa yang Dikerjakan</a>
                    <a href="#demografi" class="hover:text-bi-blue transition-colors">Profil Alumni</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="pt-20">
        
        <!-- Section 1: Overview -->
        <section id="overview" class="py-16 px-4 md:px-8 max-w-6xl mx-auto">
            <div class="bg-bi-blue text-white rounded-3xl p-8 md:p-12 shadow-xl flex flex-col md:flex-row items-center gap-8 relative overflow-hidden">
                <div class="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 rounded-full bg-white opacity-10"></div>
                <div class="absolute bottom-0 left-0 -ml-16 -mb-16 w-48 h-48 rounded-full bg-bi-gold opacity-20"></div>
                
                <div class="w-full md:w-2/3 z-10">
                    <div class="inline-block px-3 py-1 bg-white/20 rounded-full text-xs font-bold tracking-wider mb-4 border border-white/30 uppercase">Laporan Riset Profesional</div>
                    <h1 class="text-3xl md:text-5xl font-extrabold mb-4 leading-tight">Membongkar Rahasia Karir<br><span class="text-bi-gold">PCPM Bank Indonesia</span></h1>
                    <p class="text-lg md:text-xl text-blue-100 mb-6 leading-relaxed">
                        Pendidikan Calon Pegawai Muda (PCPM) adalah jalur kepemimpinan elit Bank Indonesia. Berdasarkan penelusuran profil LinkedIn dan rekam jejak alumni, kami menganalisis apa yang membuat mereka terpilih, keahlian apa yang wajib dipersiapkan, dan apa yang mereka kerjakan.
                    </p>
                    <div class="flex gap-4">
                        <a href="#skills" class="bg-bi-gold hover:bg-yellow-500 text-slate-900 font-bold py-3 px-6 rounded-lg transition-colors shadow-lg">Lihat Panduan Skill Set 🎯</a>
                    </div>
                </div>
                <div class="w-full md:w-1/3 z-10 flex justify-center text-8xl md:text-9xl opacity-90 drop-shadow-2xl">
                    📈
                </div>
            </div>
        </section>

        <!-- Section 2: Jalur Seleksi -->
        <section id="seleksi" class="py-16 px-4 md:px-8 max-w-6xl mx-auto border-t border-slate-200">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-slate-800 mb-4">Bagaimana Cara Mereka Lolos?</h2>
                <p class="text-slate-600 max-w-2xl mx-auto">PCPM dikenal dengan tingkat kompetisi yang sangat brutal. Dari ratusan ribu pendaftar, hanya kurang dari 0.1% yang akhirnya diterima. Berikut adalah tahapan seleksinya.</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div class="space-y-6">
                    <div class="timeline-node flex items-start gap-4 p-4 bg-white rounded-xl shadow-sm border border-slate-100 border-l-4 border-l-slate-300">
                        <div class="text-2xl bg-slate-100 p-2 rounded-lg">📝</div>
                        <div>
                            <h3 class="font-bold text-lg text-slate-800">1. Seleksi Administrasi</h3>
                            <p class="text-sm text-slate-600">Screening IPK, jurusan, dan usia. Profil LinkedIn sukses biasanya menunjukkan IPK > 3.5 dan pengalaman organisasi/magang yang solid sejak kuliah.</p>
                        </div>
                    </div>
                    <div class="timeline-node flex items-start gap-4 p-4 bg-white rounded-xl shadow-sm border border-slate-100 border-l-4 border-l-blue-400">
                        <div class="text-2xl bg-blue-50 p-2 rounded-lg">🧠</div>
                        <div>
                            <h3 class="font-bold text-lg text-slate-800">2. Tes Potensi Dasar (TPD) & Kebanksentralan</h3>
                            <p class="text-sm text-slate-600">Menguji logika, numerik, dan pemahaman ekonomi makro. Persiapan mandiri berbulan-bulan mempelajari fungsi BI adalah kunci.</p>
                        </div>
                    </div>
                    <div class="timeline-node flex items-start gap-4 p-4 bg-white rounded-xl shadow-sm border border-slate-100 border-l-4 border-l-blue-600">
                        <div class="text-2xl bg-blue-100 p-2 rounded-lg">🗣️</div>
                        <div>
                            <h3 class="font-bold text-lg text-slate-800">3. LGD & Psikotes</h3>
                            <p class="text-sm text-slate-600">Focus Group Discussion. Disini soft-skill dinilai. Analisis LinkedIn menunjukkan mereka aktif di himpunan mahasiswa, debat, atau kompetisi bisnis.</p>
                        </div>
                    </div>
                    <div class="timeline-node flex items-start gap-4 p-4 bg-white rounded-xl shadow-sm border border-slate-100 border-l-4 border-l-bi-gold">
                        <div class="text-2xl bg-yellow-50 p-2 rounded-lg">👔</div>
                        <div>
                            <h3 class="font-bold text-lg text-slate-800">4. Wawancara Akhir & Medcheck</h3>
                            <p class="text-sm text-slate-600">Wawancara dengan jajaran direktur. Mereka dituntut memiliki visi, ketahanan mental, dan fisik yang prima.</p>
                        </div>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-2xl shadow-lg border border-slate-100">
                    <h3 class="text-center font-bold text-slate-700 mb-2">Tingkat Keberhasilan (Estimasi)</h3>
                    <p class="text-center text-xs text-slate-500 mb-6">Visualisasi rasio penyusutan kandidat di setiap tahapan.</p>
                    <div class="chart-container">
                        <canvas id="funnelChart"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 3: Skill Set & Prep -->
        <section id="skills" class="py-16 px-4 md:px-8 max-w-6xl mx-auto border-t border-slate-200">
            <div class="text-center mb-12">
                <span class="text-xs font-bold text-bi-blue tracking-widest uppercase bg-blue-50 px-3 py-1 rounded-full">Preparation Blueprint</span>
                <h2 class="text-3xl font-bold text-slate-800 mt-2 mb-4">Skill Set & Portofolio yang Perlu Dipersiapkan</h2>
                <p class="text-slate-600 max-w-2xl mx-auto">Berdasarkan penelusuran portofolio profesional alumni PCPM di LinkedIn, Anda tidak bisa hanya mengandalkan nilai akademik. Bank Indonesia mencari kandidat dengan profil multi-dimensi.</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-12">
                <div class="bg-white p-6 rounded-2xl shadow-lg border border-slate-100">
                    <h3 class="text-center font-bold text-slate-700 mb-2">Radar Keseimbangan Kompetensi PCPM</h3>
                    <p class="text-center text-xs text-slate-500 mb-6">Peta kompetensi ideal yang dievaluasi selama proses rekrutmen.</p>
                    <div class="chart-container">
                        <canvas id="skillsChart"></canvas>
                    </div>
                </div>

                <div class="space-y-6">
                    <div class="skill-card bg-white p-5 rounded-2xl shadow-sm border border-slate-100 border-t-4 border-t-bi-blue">
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-2xl">💻</span>
                            <h3 class="font-bold text-lg text-slate-800">1. Hard Skills & Literasi Kuantitatif</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-3">Kemampuan analitis teknis sangat dihargai untuk menyusun kebijakan moneter yang presisi.</p>
                        <div class="flex flex-wrap gap-2 text-xs">
                            <span class="bg-slate-100 text-slate-700 px-2 py-1 rounded">Ekonomi Makro & Mikro</span>
                            <span class="bg-slate-100 text-slate-700 px-2 py-1 rounded">Python / R / SQL</span>
                            <span class="bg-slate-100 text-slate-700 px-2 py-1 rounded">Analisis Laporan Keuangan</span>
                            <span class="bg-slate-100 text-slate-700 px-2 py-1 rounded">IELTS (Skor Min. 6.5)</span>
                        </div>
                    </div>

                    <div class="skill-card bg-white p-5 rounded-2xl shadow-sm border border-slate-100 border-t-4 border-t-bi-gold">
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-2xl">🤝</span>
                            <h3 class="font-bold text-lg text-slate-800">2. Soft Skills & Karakter Kepemimpinan</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-3">Diuji secara ketat dalam LGD (Leaderless Group Discussion) dan wawancara akhir guna melihat potensi kepemimpinan masa depan.</p>
                        <div class="flex flex-wrap gap-2 text-xs">
                            <span class="bg-yellow-50 text-yellow-800 px-2 py-1 rounded">Structured Problem Solving</span>
                            <span class="bg-yellow-50 text-yellow-800 px-2 py-1 rounded">Diplomasi & Negosiasi</span>
                            <span class="bg-yellow-50 text-yellow-800 px-2 py-1 rounded">Strategic Thinking</span>
                            <span class="bg-yellow-50 text-yellow-800 px-2 py-1 rounded">Emotional Resilience</span>
                        </div>
                    </div>

                    <div class="skill-card bg-white p-5 rounded-2xl shadow-sm border border-slate-100 border-t-4 border-t-emerald-500">
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-2xl">🚀</span>
                            <h3 class="font-bold text-lg text-slate-800">3. Portofolio & LinkedIn Boosters</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-3">Rekam jejak eksternal yang membuat profil Anda "menyala" saat kurasi administrasi dan CV.</p>
                        <div class="flex flex-wrap gap-2 text-xs">
                            <span class="bg-emerald-50 text-emerald-800 px-2 py-1 rounded">Magang di Kemenkeu/OJK/Multinasional</span>
                            <span class="bg-emerald-50 text-emerald-800 px-2 py-1 rounded">Sertifikasi FRM / CFA Level 1</span>
                            <span class="bg-emerald-50 text-emerald-800 px-2 py-1 rounded">Pemenang Business Case / Paper Kebijakan</span>
                            <span class="bg-emerald-50 text-emerald-800 px-2 py-1 rounded">Ketua Organisasi Kampus</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-bi-light/50 border border-bi-blue/20 rounded-2xl p-6 md:p-8">
                <h3 class="font-bold text-slate-800 mb-4 flex items-center gap-2">
                    <span>📅</span> Garis Waktu & Langkah Persiapan Mandiri Anda:
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
                    <div class="bg-white p-4 rounded-xl border border-slate-100">
                        <div class="font-bold text-bi-blue mb-1">Fase 1: Fondasi Finansial & Data</div>
                        <p class="text-xs text-slate-600 leading-relaxed">Fokus mengasah kemampuan kuantitatif. Ambil sertifikasi data analytics, perdalam materi APBN dan instrumen moneter BI, serta raih sertifikasi bahasa Inggris formal.</p>
                    </div>
                    <div class="bg-white p-4 rounded-xl border border-slate-100">
                        <div class="font-bold text-bi-blue mb-1">Fase 2: Portofolio Aktual & Opini</div>
                        <p class="text-xs text-slate-600 leading-relaxed">Mulai menulis opini ekonomi/kebijakan di LinkedIn. Ikuti kompetisi riset ekonomi makro. Latih pemecahan masalah dengan metode MECE.</p>
                    </div>
                    <div class="bg-white p-4 rounded-xl border border-slate-100">
                        <div class="font-bold text-bi-blue mb-1">Fase 3: Simulasi LGD & Interview</div>
                        <p class="text-xs text-slate-600 leading-relaxed">Berlatih memimpin diskusi tanpa bersikap mendominasi. Simulasikan wawancara menggunakan metode STAR untuk menceritakan pengalaman organisasi Anda.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 4: Apa yang Dikerjakan -->
        <section id="pekerjaan" class="py-16 px-4 md:px-8 bg-slate-100 border-y border-slate-200">
            <div class="max-w-6xl mx-auto">
                <div class="text-center mb-10">
                    <h2 class="text-3xl font-bold text-slate-800 mb-4">Apa yang Mereka Kerjakan?</h2>
                    <p class="text-slate-600 max-w-2xl mx-auto">Setelah lulus masa pendidikan, peserta PCPM diangkat menjadi Asisten Manajer. Berdasarkan data LinkedIn, peran mereka tersebar di berbagai departemen strategis. Klik pilar di bawah untuk mengeksplorasi peran mereka.</p>
                </div>

                <div class="flex flex-wrap justify-center gap-2 mb-8">
                    <button class="tab-btn px-6 py-3 rounded-full font-bold text-sm transition-colors bg-bi-blue text-white shadow-md" data-target="tab-moneter">📊 Moneter & Ekonomi</button>
                    <button class="tab-btn px-6 py-3 rounded-full font-bold text-sm transition-colors bg-white text-slate-600 hover:bg-slate-200 shadow-sm" data-target="tab-pembayaran">💳 Sistem Pembayaran</button>
                    <button class="tab-btn px-6 py-3 rounded-full font-bold text-sm transition-colors bg-white text-slate-600 hover:bg-slate-200 shadow-sm" data-target="tab-stabilitas">🛡️ Stabilitas Keuangan</button>
                    <button class="tab-btn px-6 py-3 rounded-full font-bold text-sm transition-colors bg-white text-slate-600 hover:bg-slate-200 shadow-sm" data-target="tab-pendukung">⚙️ Pendukung Strategis</button>
                </div>

                <div class="bg-white rounded-2xl shadow-xl p-6 md:p-10 min-h-[300px]">
                    <div id="tab-moneter" class="tab-content active">
                        <div class="flex flex-col md:flex-row gap-8 items-center">
                            <div class="w-full md:w-1/3 text-6xl text-center">📈</div>
                            <div class="w-full md:w-2/3">
                                <h3 class="text-2xl font-bold text-bi-blue mb-3">Penetapan Kebijakan Moneter & Riset Ekonomi</h3>
                                <p class="text-slate-600 mb-4">Ini adalah pekerjaan klasik bank sentral. Lulusan PCPM di sektor ini bertugas memantau inflasi, nilai tukar rupiah, dan pertumbuhan ekonomi.</p>
                                <ul class="space-y-2">
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Analis Ekonomi:</strong> Menyusun asesmen ekonomi makro untuk RDG.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Riset Kebijakan:</strong> Membangun model ekonometrika untuk memproyeksi dampak suku bunga.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Pengelolaan Devisa:</strong> Melakukan analisis pasar global dan intervensi valas.</span></li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div id="tab-pembayaran" class="tab-content">
                        <div class="flex flex-col md:flex-row gap-8 items-center">
                            <div class="w-full md:w-1/3 text-6xl text-center">📱</div>
                            <div class="w-full md:w-2/3">
                                <h3 class="text-2xl font-bold text-bi-blue mb-3">Pengembangan & Pengawasan Sistem Pembayaran</h3>
                                <p class="text-slate-600 mb-4">Pekerjaan ini melibatkan pengembangan ekosistem pembayaran digital (seperti QRIS, BI-FAST, dan wacana Rupiah Digital).</p>
                                <ul class="space-y-2">
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Inovasi Digital:</strong> Merancang blueprint kebijakan pembayaran nasional masa depan.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Pengawasan PJP:</strong> Mengaudit fintech, e-wallet, dan bank agar mematuhi standar keamanan BI.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Pengelolaan Uang Rupiah:</strong> Merencanakan pencetakan dan distribusi uang fisik.</span></li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div id="tab-stabilitas" class="tab-content">
                        <div class="flex flex-col md:flex-row gap-8 items-center">
                            <div class="w-full md:w-1/3 text-6xl text-center">🏦</div>
                            <div class="w-full md:w-2/3">
                                <h3 class="text-2xl font-bold text-bi-blue mb-3">Makroprudensial & Stabilitas Sistem Keuangan</h3>
                                <p class="text-slate-600 mb-4">Menjaga agar sistem keuangan tidak runtuh (mencegah krisis). Mereka mengawasi keterkaitan antar institusi keuangan.</p>
                                <ul class="space-y-2">
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Surveilans Sistem Keuangan:</strong> Menganalisis risiko sistemik dari perbankan dan korporasi besar.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Kebijakan Makroprudensial:</strong> Mengatur regulasi rasio LTV untuk KPR.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Kerjasama Internasional:</strong> Mewakili BI dalam forum internasional seperti G20 atau IMF.</span></li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div id="tab-pendukung" class="tab-content">
                        <div class="flex flex-col md:flex-row gap-8 items-center">
                            <div class="w-full md:w-1/3 text-6xl text-center">👨‍💻</div>
                            <div class="w-full md:w-2/3">
                                <h3 class="text-2xl font-bold text-bi-blue mb-3">Manajemen Internal & Pendukung Strategis</h3>
                                <p class="text-slate-600 mb-4">Lulusan jurusan non-ekonomi (IT, Hukum, Psikologi) sering ditempatkan di sini untuk memastikan operasional BI berjalan modern.</p>
                                <ul class="space-y-2">
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Sistem Informasi / IT:</strong> Mengelola cyber-security, data analytics, dan infrastruktur IT kritikal nasional.</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>Departemen Hukum:</strong> Merancang rancangan Peraturan Bank Indonesia (PBI).</span></li>
                                    <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <span class="text-sm text-slate-700"><strong>SDM:</strong> Mengembangkan talenta bank sentral dan mengelola transformasi kelembagaan.</span></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 5: Profil Alumni -->
        <section id="demografi" class="py-16 px-4 md:px-8 max-w-6xl mx-auto">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-slate-800 mb-4">Profil Demografi PCPM (Berdasarkan Sampel)</h2>
                <p class="text-slate-600 max-w-2xl mx-auto">Meski terbuka untuk banyak jurusan, penelusuran karir menunjukkan pola tertentu mengenai latar belakang pendidikan para penerima PCPM.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-6 rounded-2xl shadow-lg border border-slate-100 flex flex-col">
                    <h3 class="font-bold text-slate-800 mb-2 text-center">Distribusi Latar Belakang Jurusan</h3>
                    <p class="text-xs text-slate-500 mb-4 text-center">Dominasi ekonomi tetap ada, namun STEM mulai mengambil porsi besar.</p>
                    <div class="chart-container flex-grow">
                        <canvas id="jurusanChart"></canvas>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-2xl shadow-lg border border-slate-100 flex flex-col">
                    <h3 class="font-bold text-slate-800 mb-2 text-center">Asal Perguruan Tinggi Teratas</h3>
                    <p class="text-xs text-slate-500 mb-4 text-center">Menunjukkan Universitas yang kerap menyumbang talenta ke PCPM.</p>
                    <div class="chart-container flex-grow">
                        <canvas id="univChart"></canvas>
                    </div>
                </div>
            </div>
            
            <div class="mt-8 bg-blue-50 border-l-4 border-bi-blue p-4 rounded-r-lg">
                <p class="text-sm text-slate-700">
                    <strong>Kesimpulan Riset:</strong> Menerima PCPM bukan hanya soal nilai akademis. Analisis profil LinkedIn mereka rata-rata menunjukkan portofolio yang sangat seimbang antara <em>hard-skill</em> dan <em>soft-skill</em>. Di dalam BI, mereka menjadi "arsitek" kebijakan ekonomi dan teknologi keuangan negara.
                </p>
            </div>
        </section>

    </main>

    <footer class="bg-slate-900 text-slate-400 py-8 text-center mt-12">
        <p class="text-sm">© 2026 PCPM Insight Dashboard. Data disimulasikan berdasarkan tren profil profesional publik untuk tujuan edukasi.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Tab Navigation Logic
            const tabBtns = document.querySelectorAll('.tab-btn');
            const tabContents = document.querySelectorAll('.tab-content');

            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    tabBtns.forEach(b => {
                        b.classList.remove('bg-bi-blue', 'text-white', 'shadow-md');
                        b.classList.add('bg-white', 'text-slate-600');
                    });
                    btn.classList.remove('bg-white', 'text-slate-600');
                    btn.classList.add('bg-bi-blue', 'text-white', 'shadow-md');

                    tabContents.forEach(content => content.classList.remove('active'));
                    const targetId = btn.getAttribute('data-target');
                    document.getElementById(targetId).classList.add('active');
                });
            });

            // Chart.js Configuration
            Chart.defaults.font.family = 'ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            Chart.defaults.color = '#64748b';
            
            const formatLabel = (str, maxwidth = 16) => {
                const sections = [];
                const words = str.split(" ");
                let temp = "";
                words.forEach((item, index) => {
                    if (temp.length > 0) {
                        let concat = temp + ' ' + item;
                        if (concat.length > maxwidth) {
                            sections.push(temp);
                            temp = "";
                        } else {
                            if (index == (words.length - 1)) {
                                sections.push(concat);
                                return;
                            } else {
                                temp = concat;
                                return;
                            }
                        }
                    }
                    if (index == (words.length - 1)) {
                        sections.push(item);
                        return;
                    }
                    if (item.length < maxwidth) { temp = item; } else { sections.push(item); }
                });
                return sections;
            };

            // Funnel Chart
            const ctxFunnel = document.getElementById('funnelChart').getContext('2d');
            new Chart(ctxFunnel, {
                type: 'bar',
                data: {
                    labels: ['Pendaftar', 'Lolos Adm', 'Lolos Tes Dasar', 'Lolos Psikotes/LGD', 'Diterima (PCPM)'],
                    datasets: [{
                        data: [100, 30, 10, 2, 0.15],
                        backgroundColor: ['rgba(148, 163, 184, 0.5)', 'rgba(96, 165, 250, 0.6)', 'rgba(59, 130, 246, 0.7)', 'rgba(29, 78, 216, 0.8)', 'rgba(212, 175, 55, 1)'],
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        y: {
                            beginAtZero: true,
                            type: 'logarithmic',
                            ticks: {
                                callback: function(value) {
                                    if (value === 100 || value === 10 || value === 1 || value === 0.1) return value + '%';
                                    return null;
                                }
                            }
                        },
                        x: { ticks: { callback: function(value) { return formatLabel(this.getLabelForValue(value), 12); } } }
                    }
                }
            });

            # Radar Chart
            const ctxSkills = document.getElementById('skillsChart').getContext('2d');
            new Chart(ctxSkills, {
                type: 'radar',
                data: {
                    labels: ['Ekonomi Makro & Finansial', 'Analisis Data & Kuantitatif', 'Kepemimpinan & Kerja Sama', 'Komunikasi & Diplomasi', 'Ketahanan Mental & Adaptabilitas', 'Bahasa Asing & Global Mindset'],
                    datasets: [{
                        data: [90, 80, 85, 90, 95, 85],
                        backgroundColor: 'rgba(0, 74, 141, 0.2)',
                        borderColor: '#004A8D',
                        borderWidth: 2,
                        pointBackgroundColor: '#D4AF37',
                        pointBorderColor: '#fff'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            suggestedMin: 50,
                            suggestedMax: 100,
                            ticks: { display: false },
                            pointLabels: { font: { size: 10, weight: 'bold' }, color: '#475569' }
                        }
                    },
                    plugins: { legend: { display: false } }
                }
            });

            # Doughnut Chart
            const ctxJurusan = document.getElementById('jurusanChart').getContext('2d');
            new Chart(ctxJurusan, {
                type: 'doughnut',
                data: {
                    labels: ['Ilmu Ekonomi/Manajemen', 'Akuntansi/Keuangan', 'Teknik/IT/Sistem Informasi', 'Hukum', 'Matematika/Statistika', 'Lainnya'],
                    datasets: [{
                        data: [35, 20, 25, 10, 5, 5],
                        backgroundColor: ['#004A8D', '#3B82F6', '#D4AF37', '#94A3B8', '#64748B', '#E2E8F0']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '60%',
                    plugins: { legend: { position: 'right', labels: { font: { size: 11 }, boxWidth: 12 } } }
                }
            });

            # Horizontal Bar Chart
            const ctxUniv = document.getElementById('univChart').getContext('2d');
            new Chart(ctxUniv, {
                type: 'bar',
                data: {
                    labels: ['UI', 'ITB', 'UGM', 'Unpad', 'Undip', 'Univ Luar Negeri', 'Lainnya'],
                    datasets: [{
                        data: [85, 75, 70, 50, 45, 40, 60],
                        backgroundColor: '#004A8D',
                        borderRadius: 4
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { x: { display: false }, y: { grid: { display: false } } }
                }
            });
        });
    </script>
</body>
</html>
"""

# 3. Eksekusi komponen HTML ke dalam halaman Streamlit dengan tinggi statis (misal 1500px agar scroller-nya pas)
st.components.v1.html(html_code, height=1800, scrolling=True)
