# OMSP Automation Notes

## GitHub Project Automation

Önerilen otomasyonlar:

- Yeni issue açılınca Project'e ekle
- Yeni PR açılınca Project'e ekle
- PR review aşamasına gelince status `In Review`
- PR merge edilince bağlı issue `Done`

## Branch Protection

İleride önerilen ayarlar:

- `main` branch'e doğrudan push kapalı
- PR review zorunlu
- Status check zorunlu

## CI

İlk aşamada minimum CI hedefi:

- Lint/check
- Test varsa test
- Markdown link/check opsiyonel
