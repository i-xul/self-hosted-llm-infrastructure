# Benchmark Result

## Configuration

| Item | Value |
|---|---|
| Timestamp | `2026-08-14T11:16:29.553341+03:00` |
| Batch timestamp | `20260814-111325` |
| Run | `1/1` |
| Model | `phi4:14b` |
| Prompt | `summarization.md` |
| Run type | `warm` |
| Thinking | `off` |
| Context size | `4096` |
| Temperature | `0` |
| Seed | `42` |

## Environment

| Item | Value |
|---|---|
| Operating system | `Windows-11-10.0.26200-SP0` |
| Machine architecture | `AMD64` |
| Python version | `3.13.15` |
| Python implementation | `CPython` |
| Ollama version | `0.32.9` |
| Model format | `gguf` |
| Model family | `phi3` |
| Model families | `phi3` |
| Parameter size | `14.7B` |
| Quantization | `Q4_K_M` |
| Model context length | `16384` |

## Metrics

| Metric | Value |
|---|---:|
| Total duration | 11.58 s |
| Model load duration | 0.084 s |
| Prompt tokens | 267 |
| Prompt evaluation duration | 0.327 s |
| Generated tokens | 510 |
| Generation duration | 11.137 s |
| Generation speed | 45.79 tokens/s |

## Prompt

```text
Summarize the following text in Finnish.

Requirements:

- Use no more than five sentences.
- Preserve the main arguments and conclusions.
- Do not introduce information that is not present in the source text.
- Use neutral and natural Finnish.

SOURCE TEXT:

A small organization is planning to replace several separate servers with a consolidated virtualization platform. The current environment contains independent systems for file storage, internal web applications, monitoring and backups. Maintaining the servers separately has increased electricity consumption, hardware costs and administrative work.

The proposed virtualization platform would allow multiple isolated virtual machines to run on fewer physical computers. Supporters of the change argue that centralized management would simplify updates, backups and monitoring. Hardware resources could also be allocated dynamically according to the needs of each service.

However, the change introduces new risks. A failure in a virtualization host could affect several services simultaneously. The organization would therefore need reliable backups, tested recovery procedures and sufficient hardware redundancy. Administrators would also require training before the existing production services could be migrated safely.

The organization has decided to begin with a limited pilot deployment. Non-critical services will be migrated first, and performance, reliability and administrative workload will be evaluated for three months. A wider migration will be considered only if the pilot meets the agreed technical and operational requirements.
```

## Response

Pieni organisaatio suunnittelee korvata useat erilliset palvelimet yhdistetyllä virtualisointialustalla. Nykyinen ympäristö sisältää itsenäisiä järjestelmiä tiedostojen tallennukseen, sisäisiin verkkosovelluksiin, valvontaan ja varmuuskopioihin. Erillisten palvelinten ylläpito on lisännyt sähkönkulutusta, laitteistokustannuksia ja hallinnollista työtä.

Ehdotettu virtualisointialusta mahdollistaisi useiden eristyksissä olevien virtuaalikoneiden toiminnan vähemmän fyysisillä tietokoneilla. Muutoksen kannattajat väittävät, että keskitetty hallinta yksinkertaistaisi päivityksiä, varmuuskopioita ja valvontaa. Laitevarat voidaan myös jakaa dynaamisesti jokaisen palvelun tarpeiden mukaan.

Muutos tuo kuitenkin uusia riskejä: virhe virtualisointi-isäntässä voisi vaikuttaa useita palveluita samanaikaisesti. Organisaatio tarvitsisi luotettavia varmuuskopioita, testattuja palautusprosesseja ja riittävästi laitteistojen redundanssia. Hallintohenkilöstöllä olisi myös tarpeen saada koulutusta ennen kuin olemassa olevat tuotantopalvelut voidaan siirtää turvallisesti.

Organisaatio on päättänyt aloittaa rajattuun pilotointiin. Ensiksi siirretään ei-kriittisiä palveluita, ja niiden suorituskykyä, luotettavuutta ja hallinnollista työmäärää arvioidaan kolmen kuukauden ajan. Laajempi siirtymä harkitaan vain, jos pilotointi täyttää sovittujen teknisten ja toiminnallisten vaatimusten.

