# Discord-community – tverrfaglig prosjekt på Vg2

Vi skal utvikle og drifte et lite digitalt community med Discord-server og en egenutviklet bot. Prosjektet kombinerer driftsstøtte (DRS), brukerstøtte (BRS) og utvikling (UTV).

## Vårt prosjekt

| Felt | Innhold |
|---|---|
| Gruppenavn | [Fyll ut] |
| Gruppemedlemmer | [Fyll ut] |
| Tema | [Fyll ut] |
| Målgruppe | [Fyll ut] |
| Hva tjenesten hjelper brukerne med | [Fyll ut] |

## Kom i gang

1. Opprett et privat repository fra lærerens template med **Use this template**.
2. Gi partner og lærer tilgang.
3. Les [oppgaven](OPPGAVE.md) og fyll ut [prosjektplanen](docs/prosjektplan.md).
4. Avklar tema og omfang med lærer.
5. Opprett arbeidsoppgaver som GitHub Issues.
6. Utvikle, test og dokumenter underveis.

## Prosjektstruktur

- `bot.py`: Botens startfil.
- `utils.py`: Hjelpefunksjoner og eventuell registrering av administrative kommandoer.
- `cogs/`: Botens funksjoner, organisert som extensions.
- `requirements.txt`: Python-avhengigheter.
- `.env.example`: Eksempel på nødvendige miljøvariabler, uten hemmeligheter.
- `deploy/`: Mal for systemd-tjenesten.
- `.github/workflows/ci.yml`: Automatisk syntakskontroll.
- `docs/`: Gruppas dokumentasjon.

Tilpass oversikten til filene som faktisk finnes i repositoryet. En eventuell eksempelkommando i malen er bare en demonstrasjon og erstatter ikke gruppas egen nyttige botfunksjon.

## Installasjon og oppstart

Se [driftsdokumentasjonen](docs/drift.md) for fullstendig serveroppsett og startkommandoer.

| Innstilling | Verdi |
|---|---|
| Python-versjon | [Fyll ut] |
| Startfil | [For eksempel bot.py] |
| Kommando-prefiks | [For eksempel !] |
| Token-variabel | [For eksempel DISCORD_TOKEN] |
| systemd-tjeneste | [For eksempel discordbot.service] |

Token leses fra miljøvariabel. En `.env`-fil blir bare lest automatisk dersom startkoden er satt opp for det. På serveren kan systemd bruke `EnvironmentFile=`.

## Funksjoner

| Funksjon | Brukerbehov | Kommando eller hendelse | Status |
|---|---|---|---|
| [Fyll ut] | [Fyll ut] | [Fyll ut] | [Planlagt / under arbeid / ferdig] |

## Dokumentasjon

- [Oppgave og vurdering](OPPGAVE.md)
- [Prosjektplan](docs/prosjektplan.md)
- [Drift og sikkerhet](docs/drift.md)
- [Brukerstøtte og brukerveiledning](docs/brukerstotte.md)
- [Testing, kilder og refleksjon](docs/test-og-refleksjon.md)

## Kjente feil og begrensninger

[Beskriv konkrete begrensninger og eventuell midlertidig løsning.]

**Ikke legg token, passord, private nøkler eller unødvendige personopplysninger i repositoryet.**
