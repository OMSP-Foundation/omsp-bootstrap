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
- **Tek delegasyon istisnası — test-gated merge (#212):** `develop`'a giden
  PR'larda `omsp-tester` (`gate:tester-approved`/`gate:test-failed`) ve
  ardından `omsp-cto` (`gate:cto-approved`) gate'leri Cengiz'in açık
  delegasyonuyla işler; iki gate + yeşil CI sonrası `approval-gate-merge.yml`
  otomatik merge eder (playbook §5.8–5.9). Cengiz label kaldırarak veya
  workflow'u kapatarak her an override eder. Diğer tüm onay yolları insana aittir.

**Test-gated akış (özet):** Sprint öncesi `omsp-tester` her sprint issue'suna
test-senaryo checklist'i yorumlar (`<!-- omsp-test-checklist -->`). PR açılınca
bağlı issue proje panosunda **Testing** statüsüne geçer
(`pr-testing-status.yml`; `PROJECT_TOKEN` secret'ı gerekir). Tester checklist'i
PR dalında koşar: FAIL → test raporu + `gate:test-failed` + issue In
Progress'e; PASS → test raporu + `gate:tester-approved` + issue In Review'a.
`omsp-cto` TDD uygunluğunu inceleyip `gate:cto-approved` ekler; CI yeşilse PR
otomatik merge olur ve issue kapanır.

## 5. CI Kalite Gate'leri

`.github/workflows/` altında ~24 workflow çalışır. PR açılmadan önce ilgili
kontrollerin geçeceğinden emin ol; geçmeyecekse PR'da gerekçesini açıkla.

Öne çıkan gate'ler:

- `omsp-validator.yml` → `tooling/omsp_validate.py` (governed artifact metadata, örn. `Title`)
- `quality-gate.yml` → `tooling/omsp_quality_gate.py`
- `markdown.yml` / `lint.yml` → markdownlint-cli2 (`.markdownlint.json`, `.markdownlint-cli2.jsonc`)
- `link-check.yml` → lychee (`.lychee.toml`)
- `ontology.yml`, `platform-context.yml`, `platform-engines.yml`,
  `traceability-design.yml`, `publication-design.yml`, `checklist-lint-design.yml`
- `canonical-authority.yml`, `security-supply-chain.yml`,
  `production-release-readiness.yml`, `operations-recovery-drill.yml`,
  `observability-audit.yml`, `repository-generator.yml`,
  `release-automation.yml`, `release-drafter.yml`

**Yerel doğrulama (push öncesi):**

```bash
# CI ile AYNI kapsam (.github/workflows/omsp-validator.yml) — governed path'ler
python3 tooling/omsp_validate.py governance planning roadmap architecture \
  knowledge reference schemas validation
python3 tooling/omsp_quality_gate.py      # kalite gate
```

`omsp_validate.py` JSON çıktısı verir; ihlaller `findings` altında listelenir.

> Not: `omsp_validate.py .` tüm ağacı tarar ve governed olmayan config dosyalarını
> (`.claude/`, kök dokümanlar) da içine alır — bunların YAML front-matter'ı
> yanlış `OMSP-META-001` pozitifleri üretir. Rutin kontrolde `.` yerine yukarıdaki
> governed path listesini kullan.

## 6. Depo Yapısı (üst düzey)

`main`/`develop` kökündeki başlıca dizinler ve amaçları:

- `canon/` — OMSP dili/kimliği: vizyon, misyon, ilkeler, terminoloji, metodoloji envanteri, ontoloji özeti
- `governance/` — mühendislik standartları + planlama/inceleme/onay/release yönetişimi
  (yaşam döngüsü politikalarının tek kaynağı `ENGINEERING_PLAYBOOK.md`;
  otorite kaydı `CANONICAL_AUTHORITY_MAP.md`. `foundation/` ve `platform/`
  dizinleri WP-0072'de emekliye ayrıldı — motor tanımları `architecture/` altında)
- `ontology/`, `schemas/` — meta-model ve makine-okunur şemalar
- `templates/` — ADR, requirement, risk, validation, Work Package şablonları
- `tooling/` — validator/generator scriptleri (`omsp_validate.py` ve `validate_*.py` ailesi)
- `validation/`, `tests/` — kalite gate'leri, doğrulama çerçevesi, kontrol listeleri
- `reference/`, `examples/`, `demonstrator/`, `pilot/` — alan örnekleri ve gösterim
- `roadmap/`, `planning/` — sprint planları ve program yol haritası
- `provenance/`, `recovery/`, `security/`, `observability/`, `performance/` — işletim/yönetişim alanları

**Release ve proje takibi:** Depoda `release/` klasörü yoktur (kaldırıldı).
Release kayıtları GitHub Releases'ta; issue, milestone ve sprint/WP takibi
GitHub Projects üzerinde yürütülür. Proje yönetimi işleri için `omsp-pm`
agent'ı kullanılır (`.claude/agents/omsp-pm.md`).

**Agent hiyerarşisi (hepsi advisory):** En üst katman `omsp-cto`
(`.claude/agents/omsp-cto.md`) — teknik vizyon, program isterleri,
metodoloji gözetimi, TDD bekçiliği ve onay paketi hazırlığı; isterleri
`omsp-pm` ile birlikte belirler, `omsp-pm` bunları sprint/WP planına çevirir,
`omsp-domain-engineer` (`.claude/agents/omsp-domain-engineer.md`) CTO'nun
spesifikasyonlarına uygun alan içeriğini (denizcilik ontolojisi, MODS/VDM
içeriği, diyagram kaynakları, senaryolar) üretir,
`omsp-tester` (`.claude/agents/omsp-tester.md`) sprint issue'larının test
checklist'lerini ve test verdiklerini sahiplenir, `omsp-auditor` uygunluğu
denetler (tipik kadans: sprint kapanışı ve release-readiness öncesi).
§4'teki test-gated merge delegasyonu (#212) dışında hiçbir agent
onay yetkisi taşımaz; karar Cengiz'indir. Orkestrasyon ve genel
implementasyon **tasarım gereği** ana Claude oturumundadır — ayrı bir
implementer/orchestrator agent'ı bilinçli olarak yoktur; agent'lar devir
paketlerini ana oturuma teslim eder. Kanonik agent listesi ve yetki
sınırları: `governance/AI_GOVERNANCE.md` §1/§5.

**Yapı kuralı:** Her üst düzey dizinin net bir mühendislik amacı olmalıdır. Yeni
dizin, ancak sorumluluğu mevcut bir alanla temsil edilemiyorsa eklenir.

## 7. Bilinen Durum ve Öncelikler (Sprint-6 kapandı, sırada Sprint-7 / v0.6.0)

**Güncel durum (2026-07-13):**

- **Sprint-6 kapandı (#222):** WP-0070…WP-0076 (#165, #191, #166, #167, #168,
  #169, #170) tamamlandı, `v0.5.1 — Clean Baseline & Product Reorientation`
  yayınlandı, v0.5.1 milestone'u kapalı. Sprint-7 (epic #171, milestone
  v0.6.0) planlı; WP-0077…WP-0089 (#198–#210) backlog'da hazır.
- Resmî roadmap: issue #145 "Post-Audit Product Reorientation" (Cengiz onaylı).
  `planning/SPRINT_6_EXECUTION_PLAN.md` (pilot-readiness) Superseded;
  WP-0060–0068 numaraları emekli, yeniden kullanılamaz.
- Metodoloji envanteri canon'da: `canon/ENGINEERING_METHODOLOGY.md` (WP-0069).
- Depo topolojisi: monorepo — `governance/ADR-0001-REPOSITORY-TOPOLOGY.md`
  (tetikleyicili yeniden değerlendirme: dış katkıcı / bağımsız VDM kadansı /
  dış MODS tüketicisi).
- Eski borçlardan kapananlar: Title metadata ihlalleri (validator 0 bulgu),
  kök dokümanlar v0.5.0 hizalı (#143 kapalı). Stub oranı ~%30'a düştü.

**Açık teknik borç:**

- Hanse 460: hiçbir alan doğrulanmış değil; ontolojide denizcilik kavramı yok (Sprint-7+ işi).
- Residual riskler RR-001…RR-005 açık.
- (Kapananlar: şablon doldurma WP-0071/#191, stub disposisyonu ve
  `platform/`/`foundation/` emekliliği WP-0072/#166 ile çözüldü.)

**Ürün mimarisi (spec-first MODS yığını, `omsp-cto` sahipliğinde):**
MODS Specification (ODS-100…600) → Marine Diagram System → Core Operations
Manual → Vessel Definition Module (ilk: Hanse 460) → Scenario Library → QRH.
YAML modeli tek kaynak; MODS insan-okur yayın standardıdır. Katman N içeriği,
N−1 en az Draft olmadan üretilmez.

**Üç ufuklu geliştirme vizyonu (Sprint bloklarıyla):**

- **Horizon 1 (Sprint-6):** Temiz taban — WP-0070…0076, v0.5.1 baseline. **Tamamlandı.**
- **Horizon 2 (Sprint-7…10):** İlk gerçek alan değeri — denizcilik ontolojisi,
  MODS Spec v0.1, Hanse 460 elektrik golden path, senaryolar + 5 dk demo
  (v0.6.0), ikinci alan dilimi (v0.6.1).
- **Horizon 3 (Sprint-11+):** Platformlaşma — VDM + ikinci tekne profili
  (v0.7.0), QRH + tasarım-ortağı pilotu (v0.8.0), topluluk (v0.9.0),
  v1.0 stabilizasyon. Ayrıntı: `roadmap/OMSP_ROADMAP.md`.

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
