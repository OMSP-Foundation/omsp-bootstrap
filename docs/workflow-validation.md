# Workflow Validation

Bu doküman OMSP issue → branch → PR → merge → issue close akışının doğrulama kaydıdır.

## Doğrulanan Akış

1. Issue seçildi.
2. Issue numarasını içeren branch oluşturuldu.
3. Değişiklik branch üzerinde commit edildi.
4. PR açıldı.
5. PR açıklamasında closing keyword kullanıldı.
6. PR merge edildi.
7. GitHub issue kapanma davranışı doğrulandı veya doğrulanacak olarak takip edildi.

## İlk Doğrulama Kaydı

### Issue

- #9 — Define Bootstrap MVP scope

### Branch

```txt
feature/9-bootstrap-mvp-scope
```

### Pull Request

- #11 — Define Bootstrap MVP scope

### Closing Keyword

```md
Closes #9
```

### Merge Sonucu

PR #11 squash merge edildi.

### Beklenen Sonuç

PR #11 default branch olan `main` üzerine merge edildiği için #9 issue'su GitHub tarafından otomatik kapanmalıdır.

## Standart Kural

Bundan sonra her PR açıklamasında ilgili issue için aşağıdaki format kullanılacaktır:

```md
Closes #<issue-number>
```

Bir PR birden fazla issue kapatıyorsa her issue ayrı satırda yazılabilir:

```md
Closes #12
Closes #13
```

## Başarılı Sayılma Kriteri

- PR merge edilebiliyor
- PR body içinde `Closes #...` var
- İlgili issue PR merge sonrası kapanıyor
- Project panosunda item status'u manuel veya otomasyonla `Done` yapılabiliyor
