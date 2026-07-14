# Maritime Instance Schema Fixtures (WP-0078)

Bu dizin, `schemas/*.schema.json` maritime instance şemalarının kalıcı
test fixture'larını içerir. Doğrulama komutu:
`python3 tooling/validate_instance_schemas.py` (self-test: `positive/`
altındaki her fixture GEÇMELİ, `negative/` altındaki her fixture
REDDEDİLMELİDİR).

## Kurgusallık beyanı (D6 — Cengiz onayı, 2026-07-14, issue #199)

- Bu dizindeki **tüm veriler kurgusaldır**. `vessel-design:fixture:*`,
  `equipment:configuration:vessel-design:fixture:*`, `source:fixture:*`,
  `document:fixture:*` kimlikleri yalnızca şema self-testleri için
  üretilmiş yapay kimliklerdir.
- `source:fixture:...` kaynak kimlikleri **hiçbir kaynak kayıt defterinde
  (`reference/HANSE_460_SOURCE_REGISTER.md` dahil) mevcut değildir** ve
  kanıt değeri taşımaz; register-çözünürlük doğrulaması WP-0083 kapsamıdır.
- Hiçbir fixture gerçek bir tekneyi, ekipmanı, üreticiyi veya teknik değeri
  temsil etmez. Sayısal değerler ve birimler (`fixture-unit` vb.) uydurma
  yer tutuculardır; Hanse 460 dahil hiçbir gerçek gemi verisi içermez
  (gerçek veri WP-0082 kapsamıdır).
- Fixture içerikleri operasyonel talimat değildir ve hiçbir emniyet,
  sertifikasyon veya denize elverişlilik anlamı taşımaz.

## Düzen

- `positive/` — her instance tipi için en az bir geçerli örnek; ayrıca
  açık `unknown` temsili ve elektrik-dışı (tatlı su) nötrlük örneği.
- `negative/` — her biri tek bir ihlali izole eden, ayrı dosyalar hâlinde
  kalıcı ret örnekleri (N1–N11; test checklist TS-3, TS-4, TS-5, TS-6).
  N1–N10 şema sözleşmesi ihlalleridir; N11
  (`n11-system-concept-unresolvable.yaml`, WP-0080) ontoloji-uygunluk
  ihlalidir: kavram kimliği `ontology/omsp-ontology.json` registry'sine
  çözünmez ve şema `concept` const kontrolünden bağımsız olarak
  `OMSP-ISCHEMA-005` kuralıyla reddedilir.
