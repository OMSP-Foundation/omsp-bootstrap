# GitHub Project Workflow Setup

Bu dosya, OMSP Roadmap GitHub Project panosunun repoyla bağlanması için kontrol listesidir.

## Auto-add Workflow

GitHub Project içinde:

1. Project → Workflows
2. Auto-add to project
3. Repository seçimi: `OMSP-Foundation/omsp-bootstrap`
4. Filter:

```txt
is:issue OR is:pr
```

## Önerilen Project Fields

- Status
- Priority
- Sprint / Iteration
- Area
- Estimate
- Target Date

## Önerilen Views

- Backlog
- Current Sprint
- Roadmap
- Bugs / Triage
- Done

## Issue → Project Yönetimi

Yeni issue açıldığında:

1. Project'e otomatik düşmeli
2. Status başlangıçta `Backlog` olmalı
3. Triage sonrası Priority, Area ve Sprint atanmalı
4. Sprint'e alınan issue `Ready` olmalı
5. Çalışma başlayınca `In Progress`
6. PR açılınca `In Review`
7. Merge sonrası `Done`
