# CLAUDE.md — OMSP Working Agreement

Bu dosya, Claude'un `OMSP-Foundation/omsp-bootstrap` deposunda çalışırken uyması
gereken bağlamı, kuralları ve iş akışını tanımlar. Depoya katkı yapan her Claude
oturumu, iş yapmadan önce bu dosyayı okumuş kabul edilir.

## 1. Proje Özeti

**OMSP (Open Maritime Systems Platform)** — bilgi-öncelikli (knowledge-first),
model-güdümlü bir denizcilik sistem mühendisliği platformu. Referans gemi:
**Hanse 460** yelkenlisi (dijital ikiz hedefi).

- **Depo:** `OMSP-Foundation/omsp-bootstrap`
- **Tek katkıcı:** Cengiz (GitHub: `toss-cengiz`) — iletişim Türkçe
- **Kavramsal mimari — dört motor** (henüz kavramsal gruplamalar, yazılım bileşeni değil):
  Engineering Kernel, Knowledge Engine, Traceability Engine, Publication Engine.
- **Sürüm:** v0.5.0 civarı (Sprint 2–5 sonrası, `develop`).

Yönlendirici ilke: **"Yönetişimi büyütmeyi bırak, alan içeriğini büyüt."**
(Stop growing governance, grow domain content.)

## 2. Dal Stratejisi (Branching)

İki ana dal:

- `main` — bootstrap iskele (scaffolding). Doğrudan çalışılmaz.
- `develop` — asıl çalışma dalı. Tüm yeni işler buradan dallanır ve buraya döner.

Çalışma dalı isimlendirmesi:

- `feature/wp-XXXX-kisa-aciklama` — numaralı Work Package işi (örn. `feature/wp-0004-schemas-templates`)
- `feature/NN-kisa-aciklama` — issue numarasına bağlı özellik
- `task/NN-kisa-aciklama` — daha küçük görev/bakım işi

**Kural:** Claude asla doğrudan `main` veya `develop` üzerine commit atmaz.
Her değişiklik bir çalışma dalında yapılır ve PR ile `develop`'a önerilir.

## 3. Work Package (WP-XXXX) Konvansiyonu

- İş, sprint'ler içinde **WP-XXXX** numaralı work package'lar hâlinde organize edilir.
- Her WP bir çalışma dalına, bir issue'ya ve artefakt düzeyinde izlenebilirliğe (traceability) bağlanır.
- Yeni WP numarası verirken mevcut en yüksek numarayı kontrol et (issue/branch/planning listesinden) ve bir sonrakini kullan.

## 4. PR ve Onay Sınırları

Tüm PR'lar `.github/PULL_REQUEST_TEMPLATE.md` şablonunu doldurur. Şablonun
zorunlu bölümleri: Summary, Related Issue (`Closes #NN`), Changed Artifacts,
Acceptance Criteria, Quality Gates, Review Notes ve **AI Assistance Boundary**.

**AI Assistance Boundary (mutlak sınır):**

- AI yardımı yalnızca **danışmandır (advisory)**.
- AI; **governance, architecture, baseline, release veya validation** yetkisini onaylamaz.
- AI **kanıt uydurmaz** (evidence invention yasak).
- İnsan onayı gereken kararlarda son söz Cengiz'dedir; Claude öneri sunar, karar vermez.

## 5. CI Kalite Gate'leri

`.github/workflows/` altında ~24 workflow çalışır. PR açılmadan önce ilgili
kontrollerin geçeceğinden emin ol; geçmeyecekse PR'da gerekçesini açıkla.

Öne çıkan gate'ler:

- `omsp-validator.yml` → `tooling/omsp_validate.py` (governed artifact metadata, örn. `Title`)
- `quality-gate.yml` → `tooling/omsp_quality_gate.py`
- `markdown.yml` / `lint.yml` → markdownlint-cli2 (`.markdownlint.json`, `.markdownlint-cli2.jsonc`)
- `link-check.yml` / `links.yml` → lychee (`.lychee.toml`)
- `ontology.yml`, `platform-context.yml`, `platform-engines.yml`,
  `traceability-design.yml`, `publication-design.yml`, `checklist-lint-design.yml`
- `canonical-authority.yml`, `security-supply-chain.yml`,
  `production-release-readiness.yml`, `operations-recovery-drill.yml`,
  `observability-audit.yml`, `repository-generator.yml`, `release.yml`

**Yerel doğrulama (push öncesi):**

```bash
# CI ile AYNI kapsam (.github/workflows/omsp-validator.yml) — governed path'ler
python3 tooling/omsp_validate.py governance planning roadmap architecture \
  knowledge reference release schemas validation
python3 tooling/omsp_quality_gate.py      # kalite gate
```

`omsp_validate.py` JSON çıktısı verir; ihlaller `findings` altında listelenir.

> Not: `omsp_validate.py .` tüm ağacı tarar ve governed olmayan config dosyalarını
> (`.claude/`, kök dokümanlar) da içine alır — bunların YAML front-matter'ı
> yanlış `OMSP-META-001` pozitifleri üretir. Rutin kontrolde `.` yerine yukarıdaki
> governed path listesini kullan.

## 6. Depo Yapısı (üst düzey)

`main`/`develop` kökündeki başlıca dizinler ve amaçları:

- `canon/` — OMSP dili/kimliği: vizyon, misyon, ilkeler, terminoloji, ontoloji özeti
- `foundation/` — mühendislik standartları (artefakt, metadata, izlenebilirlik, adlandırma, AI governance)
- `governance/` — planlama, inceleme, onay, release ve baseline yönetişimi
- `platform/` — dört motorun kavramsal tanımları
- `ontology/`, `schemas/` — meta-model ve makine-okunur şemalar
- `templates/` — ADR, requirement, risk, validation, Work Package şablonları
- `tooling/` — validator/generator scriptleri (`omsp_validate.py` ve `validate_*.py` ailesi)
- `validation/`, `tests/` — kalite gate'leri, doğrulama çerçevesi, kontrol listeleri
- `reference/`, `examples/`, `demonstrator/`, `pilot/` — alan örnekleri ve gösterim
- `roadmap/`, `planning/` — sprint planları ve program yol haritası
- `release/`, `provenance/`, `recovery/`, `security/`, `observability/`, `performance/` — işletim/yönetişim alanları

**Yapı kuralı:** Her üst düzey dizinin net bir mühendislik amacı olmalıdır. Yeni
dizin, ancak sorumluluğu mevcut bir alanla temsil edilemiyorsa eklenir.

## 7. Bilinen Durum ve Öncelikler (v0.5.0)

**Açık teknik borç:**

- `foundation/` içindeki üç standart belgede eksik `Title` metadata (validator ihlali).
- Kök `README.md`, `CHANGELOG.md`, `RELEASE_NOTES.md` bayat (hâlâ Sprint 1 / v0.1.0-alpha referanslı).
- `foundation/` ↔ `governance/` arasında çözülmemiş örtüşme/tekrar.
- Hanse 460 dijital ikiz katmanı yalnızca README placeholder — gerçek ekipman envanteri / operasyonel YAML modeli yok.
- Residual riskler RR-001…RR-005 yeniden değerlendirme planı olmadan ertelenmiş.
- Markdown dosyalarının ~%57'si <15 satır stub; `AI_GOVERNANCE.md` üç satırlık placeholder.
- Ontoloji jenerik meta-model — henüz denizciliğe özgü kavram yok.

**Üç ufuklu geliştirme vizyonu:**

- **Horizon 1 (yakın):** Öz-tutarlılık — 3 metadata ihlalini düzelt, `foundation/`–`governance/` tekrarını çöz, kök dokümanları v0.5.0'a güncelle.
- **Horizon 2 (orta):** İlk gerçek alan değeri — Hanse 460'ı doküman stub'larından doğrulanmış YAML modellerine ve operasyonel senaryolara çevir.
- **Horizon 3 (uzun):** Platformlaşma — Hanse 460 şablonundan ikinci bir gemi tipi türet (yeniden kullanılabilirliği kanıtla), sonra topluluk erişimi.

## 8. Claude Çalışma Kalıpları (bu depoda işe yarayanlar)

- Verimli inceleme: `git clone --depth N --branch develop` + zincirli git komutları.
- Checkout'suz dosya okuma: `git show FETCH_HEAD:<path>`.
- Toplu stub analizi: `for f in $(git ls-tree -r --name-only FETCH_HEAD | grep '\.md$'); do ...; done`.
- Validator çıktısını programatik ayrıştır: `python3 tooling/omsp_validate.py . | python3 -c "import json,sys; ..."`.
- Issue/metadata için GitHub `search_*` araçlarını tercih et (rate limit'ten kaçın).
- Analiz katman katman ilerler: yapı → mimari → şemalar → yönetişim → aksiyon alınabilir issue önerileri.

## 9. İş Akışı Özeti (adım adım)

1. `develop`'tan güncel durumu al.
2. İş için WP numarası / issue belirle, `feature/wp-XXXX-...` veya `task/NN-...` dalı aç.
3. Değişiklikleri yap; **governed artefaktlarda metadata'yı (Title vb.) ekle**.
4. Yerelde `omsp_validate.py` ve ilgili `validate_*.py` / quality gate'i çalıştır.
5. PR şablonunu doldur (özellikle Quality Gates ve AI Assistance Boundary kutuları).
6. PR'ı `develop`'a aç, `Closes #NN` ile issue'ya bağla.
7. CI yeşil olana kadar düzelt. Onay ve merge kararı **insana (Cengiz)** aittir.

---

*Not: Bu depo tek katkıcılıdır ve yönetişim/CI olgunluğu, alan içeriği olgunluğunun
önündedir. Claude'un katkıları alan derinliğini (gerçek denizcilik modelleri, veri)
artırmaya yönelmeli; yeni yönetişim katmanı üretmekten kaçınmalıdır.*
