# OMSP Roadmap Project Board Setup

Bu dosya, açılan GitHub Project panosunun `OMSP-Foundation/omsp-bootstrap` reposuyla bağlanması için uygulanacak ayarları içerir.

## 1. Project Fields

Aşağıdaki field'lar önerilir:

### Status

- Backlog
- Ready
- In Progress
- In Review
- Blocked
- Done

### Priority

- P0
- P1
- P2
- P3

### Area

- bootstrap
- backend
- frontend
- infra
- docs
- product

### Sprint / Iteration

Sprint bazlı iteration field kullanılmalıdır.

## 2. Views

- Backlog
- Current Sprint
- Roadmap
- Bugs / Triage
- Done

## 3. Auto-add Workflow

Project içinde:

1. Workflows sekmesine git
2. Auto-add to project seç
3. Repository olarak `OMSP-Foundation/omsp-bootstrap` seç
4. Filter olarak şunu kullan:

```txt
is:issue OR is:pr
```

## 4. İlk Kontrol

Yeni açılan issue'lar otomatik project panosuna düşüyorsa bağlantı tamamdır.
