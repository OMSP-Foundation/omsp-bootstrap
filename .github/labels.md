# OMSP Labels

Bu dosya OMSP issue ve PR yönetimi için kullanılacak standart label setini tanımlar.

## Type

İşin türünü belirtir.

- `type:feature`
- `type:bug`
- `type:task`
- `type:docs`
- `type:decision`

## Priority

İşin önceliğini belirtir.

- `P0` — Kritik / bloklayıcı
- `P1` — Sprint hedefi için yüksek öncelik
- `P2` — Normal öncelik
- `P3` — Düşük öncelik / iyileştirme

## Area

İşin hangi alanı etkilediğini belirtir.

- `area:bootstrap`
- `area:backend`
- `area:frontend`
- `area:infra`
- `area:docs`
- `area:product`
- `area:project-management`

## Sprint

Sprint bazlı takip için kullanılır.

- `sprint-0`

İleride ihtiyaç oldukça eklenebilir:

- `sprint-1`
- `sprint-2`

## Status Helpers

Project status alanını destekleyen yardımcı etiketlerdir.

- `blocked`
- `needs-triage`
- `ready`

## Sprint 0 Uygulama Durumu

Sprint 0 açık issue'larında uygulanan minimum label seti:

| Issue | Type | Priority | Area | Sprint | Status helper |
| --- | --- | --- | --- | --- | --- |
| #5 | `type:task` | `P1` | `area:project-management` | `sprint-0` | - |
| #6 | `type:task` | `P0` | `area:project-management` | `sprint-0` | `ready` |
| #8 | `type:task` | `P1` | `area:project-management` | `sprint-0` | `ready` |

## Kullanım Kuralı

Her issue mümkünse şu label kombinasyonuna sahip olmalıdır:

```txt
type:* + P* + area:* + sprint-* veya project field
```

Örnek:

```txt
type:task + P1 + area:project-management + sprint-0 + ready
```

## Not

GitHub label oluşturma aracı mevcut değilse, label'lar GitHub UI üzerinden oluşturulmalıdır. Bu bağlantı üzerinden mevcut label'lar issue ve PR'lara uygulanabilir.
