# Model Integrity Fixtures (WP-0083 / #204)

Bu dizin, `tooling/validate_model_integrity.py` bütünlük doğrulayıcısının
(WP-0083 / ISSUE-204) kalıcı test fixture'larını içerir. Doğrulama komutu:

```bash
python3 tooling/validate_model_integrity.py tests/integrity/positive/package \
  --register tests/integrity/register.md
```

Unit testler: `tests/test_model_integrity.py` (quality gate `unit-tests`
keşfi, `python3 tooling/omsp_quality_gate.py`).

## Kurgusallık beyanı

`tests/schemas/README.md` D6 beyanı burada da geçerlidir: bu dizindeki
**tüm veriler kurgusaldır**. `vessel-design:fixture:itest:*`,
`source:fixture:itest:*`, `document:fixture:itest:*` kimlikleri ve
`register.md` girişleri yalnızca bütünlük-doğrulayıcı testleri için
üretilmiş yapay kimliklerdir; hiçbir gerçek tekneyi, ekipmanı, üreticiyi,
dokümanı veya teknik değeri temsil etmez ve kanıt değeri taşımaz. Hiçbir
fixture operasyonel talimat değildir.

## Düzen

- `register.md` — kurgusal mini kaynak register'ı; gerçek register'ın
  (`reference/HANSE_460_SOURCE_REGISTER.md`) makine-okur tablo yapısını
  (§2.2 kaynak girişleri, §4.3 erişilemeyen kaynaklar, §7 doküman-referans
  eşlemesi) birebir kullanır — doğrulayıcı ID kümelerini bu tablolardan
  MEKANİK okur, sabit-kod yoktur (TS-4).
- `positive/package/` — dört bütünlük sınıfının DÖRDÜNÜN de tek koşuda
  kontrol edilip 0 bulgu ürettiği geçerli mini paket (TS-1). Çoklu-claim
  POZİTİF örneği paketin içindedir
  (`equipment-distribution-panel.yaml`: iki claim'li `claims[]`, her
  claim beş alanlı provenance ile geçer).
- `negative/` — her biri TEK ihlali izole eden kalıcı ret paketleri (TS-2):
  - `n1-interface-endpoint-unknown-port/` — var olmayan port'a bağlanan
    interface endpoint'i (`OMSP-INTEGRITY-001`);
  - `n2-scenario-unknown-equipment/` — var olmayan equipment role'üne
    referans veren scenario (`OMSP-INTEGRITY-002`);
  - `n3-document-not-in-register/` — register eşleme tablosunda olmayan
    doküman referansı (`OMSP-INTEGRITY-003`);
  - `n4-provenance-field-missing/` — provenance alt-alanı
    (`retrieval_date`) eksik non-`unknown` değer (`OMSP-INTEGRITY-004`);
  - `n5-claim-missing-provenance/` — `claims[]` içinde provenance'sız
    claim (`OMSP-INTEGRITY-004`, çoklu-claim negatifi);
  - `n6-source-id-not-in-register/` — beş alanı tam ama `source_id`'si
    register'a çözünmeyen provenance (`OMSP-INTEGRITY-004`; ret mesajı
    register yolunu gösterir — TS-4 kanıtı);
  - `n7-document-maps-to-inaccessible/` — register'da erişilemeyen (§4.3)
    kaynağa eşlenmiş dokümanı citing eden instance
    (`OMSP-INTEGRITY-003`, eşleme kuralı 3).

Her negatif fixture ayrı koşuda tam olarak bir bulgu ve exit 1 üretir;
pozitif paket 0 bulgu ve exit 0 üretir.
