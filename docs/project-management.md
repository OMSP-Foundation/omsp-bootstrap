# OMSP Project Management

Bu repo, OMSP işlerini GitHub Issues, Milestones ve GitHub Projects üzerinden yönetmek için yapılandırılmıştır.

## Ana Project

Önerilen proje panosu: **OMSP Roadmap**

Repo: `OMSP-Foundation/omsp-bootstrap`

## İş Akışı

### Status

- **Backlog**: Henüz sprint'e alınmamış iş
- **Ready**: Tanımı net, yapılmaya hazır iş
- **In Progress**: Aktif geliştirme
- **In Review**: PR/review aşaması
- **Blocked**: Dış bağımlılık veya karar bekliyor
- **Done**: Tamamlandı

### Priority

- **P0**: Kritik / bloklayıcı
- **P1**: Sprint hedefi için yüksek öncelik
- **P2**: Normal öncelik
- **P3**: İyileştirme / düşük öncelik

### Area

- `area:bootstrap`
- `area:backend`
- `area:frontend`
- `area:infra`
- `area:docs`
- `area:product`

### Type

- `type:feature`
- `type:bug`
- `type:task`
- `type:docs`
- `type:decision`

## Sprint Yapısı

Önerilen milestone yapısı:

1. **Sprint 0 - Foundation Setup**
   - Project board bağlantısı
   - Issue template kurulumu
   - Repo çalışma standardı
   - İlk backlog çıkarımı

2. **Sprint 1 - Bootstrap MVP**
   - Bootstrap repo temel kullanım akışı
   - Development branch düzeni
   - CI / kalite kontrol başlangıcı

3. **Sprint 2 - Core Workflow**
   - Issue → branch → PR → review → merge akışı
   - Release notları
   - Dokümantasyon güncelleme standardı

## Issue Yazım Standardı

Her issue mümkünse şu bölümleri içermeli:

```md
## Amaç

## Kapsam

## Kabul Kriterleri

## Notlar
```

## ChatGPT ile Yönetim Komutları

Bu repo ChatGPT üzerinden şu komutlarla yönetilebilir:

- `Yeni issue aç: ...`
- `#12 issue'yu güncelle: ...`
- `#12 issue'ya label ekle: type:bug, P1`
- `açık issue'ları listele`
- `Sprint 1 için işleri çıkar`
- `Son PR'ları incele`

## Project Board Kullanım Notu

Bu bağlantıda issue/PR işlemleri yönetilebilir. GitHub Project panosuna otomatik item ekleme aracı mevcut değilse, Project tarafında repo için otomatik ekleme workflow'u açılmalıdır:

- Project → Workflows
- Auto-add to project
- Repository: `OMSP-Foundation/omsp-bootstrap`
- Filter: `is:issue OR is:pr`

Böylece bu repoda açılan yeni issue ve PR'lar otomatik olarak project panosuna düşer.
