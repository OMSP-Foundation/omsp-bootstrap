# OMSP Branching Standard

## Ana Branch'ler

- `main`: Stabil ana branch
- `develop`: Aktif geliştirme branch'i

## İş Branch Formatı

Issue bazlı branch açılır:

```txt
feature/<issue-number>-short-name
bugfix/<issue-number>-short-name
task/<issue-number>-short-name
```

Örnek:

```txt
feature/12-bootstrap-mvp
bugfix/18-fix-ci
```

## PR Kuralı

- Her PR en az bir issue'ya bağlanır.
- PR açıklamasında `Closes #issue` veya `Refs #issue` kullanılır.
- Review sonrası merge edilir.
