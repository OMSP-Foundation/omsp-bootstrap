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
- project-management

### Sprint / Iteration

Sprint bazlı iteration field kullanılmalıdır.

Başlangıç sprintleri:

- Sprint 0 - Foundation Setup
- Sprint 1 - Bootstrap MVP
- Sprint 2 - Core Workflow

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

Sprint 0 işleri için daha dar filtre istenirse:

```txt
is:issue label:sprint-0
```

## 4. Sprint 0 Project Intake

Aşağıdaki issue'lar Sprint 0 kapsamındadır ve Project panosunda görünmelidir:

| Issue | Başlık | Önerilen Status | Priority | Area |
| --- | --- | --- | --- | --- |
| #5 | Project management setup: issues, sprints, milestones | Backlog | P1 | project-management |
| #6 | Connect OMSP Roadmap project to omsp-bootstrap repo | Ready | P0 | project-management |
| #7 | Create OMSP Sprint 0 and Sprint 1 milestones | Ready | P1 | project-management |
| #8 | Create and apply OMSP label set | Ready | P1 | project-management |

## 5. İlk Kontrol

Yeni açılan issue'lar otomatik project panosuna düşüyorsa bağlantı tamamdır.

Doğrulama için:

1. Test issue açılır veya mevcut #6 kontrol edilir.
2. Project panosunda item olarak görünüp görünmediği kontrol edilir.
3. Status alanı `Backlog` veya `Ready` yapılır.
4. Sprint / Iteration alanı `Sprint 0` yapılır.
5. Project panosunda görünüyorsa #6 tamamlanabilir.

## 6. Araç Sınırı Notu

Bu repodaki issue, label, branch, PR ve merge işlemleri ChatGPT üzerinden yapılabilir. GitHub Project item ekleme veya Project field güncelleme aracı mevcut değilse Project UI içinde auto-add workflow ve field ayarları manuel yapılmalıdır.
