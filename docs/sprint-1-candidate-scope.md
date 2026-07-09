# Sprint 1 - Bootstrap MVP Scope

## Hedef

`omsp-bootstrap` reposunu OMSP için minimum kullanılabilir geliştirme zemini yapmak.

Sprint 1 sonunda repo, yeni işler için issue tabanlı planlama, branch/PR akışı ve temel kalite kontrol yaklaşımıyla kullanılabilir durumda olmalıdır.

## MVP Kullanım Senaryosu

Bir OMSP geliştiricisi veya maintainer şu akışı eksiksiz uygulayabilmelidir:

1. GitHub issue seçer veya açar.
2. Issue numarasını içeren branch oluşturur.
3. Değişikliği ilgili dokümantasyon/kod dosyalarına işler.
4. PR açar.
5. PR açıklamasına ilgili issue için `Closes #<issue-number>` ekler.
6. Review/merge sonrası issue otomatik kapanır.

## Sprint 1 Kapsamı

### 1. Repo amacı ve kullanım dokümantasyonu

- README içinde `omsp-bootstrap` reposunun amacı net anlatılmalı.
- Repo hangi problem için başlangıç zemini sağlıyor belirtilmeli.
- Yeni katılımcı için ilk okuma yönlendirmeleri yer almalı.

### 2. Development branch akışı

- Ana branch stratejisi uygulanabilir olmalı.
- Issue bazlı branch isimlendirme standardı kullanılmalı.
- PR hedef branch kuralı net olmalı.

### 3. PR ile otomatik issue kapatma

- Her PR açıklamasında ilgili issue için `Closes #<issue-number>` kullanılmalı.
- Merge sonrası issue kapanışı doğrulanmalı.
- Bu akış #10 ile ayrıca test edilmeli.

### 4. Minimum kalite kontrol yaklaşımı

- İlk aşamada dokümantasyon ve repo standardı kontrol edilmeli.
- CI/check ihtiyacı Sprint 1 sonunda netleştirilmeli.
- Daha ağır otomasyon Sprint 2'ye bırakılabilir.

### 5. Project board takibi

- Sprint 1 işleri OMSP Roadmap project panosunda görünmeli.
- Status alanı Backlog → Ready → In Progress → In Review → Done akışını izlemeli.

## Sprint 1 Dışı

Aşağıdakiler Sprint 1 kapsamı dışında tutulur:

- Çok repo otomasyonları
- Tam release pipeline
- Gelişmiş CI/CD
- Production deployment
- Ayrıntılı permission/branch protection matrisi

## Sprint 1 Aday Issue Listesi

- #9 — Define Bootstrap MVP scope
- #10 — Validate issue to PR workflow

## Definition of Done

- Sprint 1 kapsamı bu dokümanda netleşti.
- Sprint 1 issue listesi belirlendi.
- PR açıklamalarında `Closes #...` standardı kullanılıyor.
- En az bir PR issue ile bağlı şekilde merge edilmeye hazır.
- Sprint 1 kapsam dışı işler açıkça ayrıldı.
