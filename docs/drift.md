# Drift og sikkerhet

Beskriv det faktiske oppsettet. En annen gruppe skal kunne følge dokumentasjonen uten å måtte få alle stegene forklart muntlig. Bruk kommandoer, konfigurasjon og begrunnelser; skjermbilder alene er ikke nok.

## 1. Server og kjøremiljø

| Felt | Verdi |
|---|---|
| Ubuntu-versjon | [Fyll ut] |
| Hostname | [Fyll ut] |
| Python-versjon | [Fyll ut] |
| Linux-bruker for boten | [For eksempel discordbot] |
| Repositorymappe | [For eksempel /opt/discordbot] |
| Virtuelt Python-miljø | [For eksempel /opt/discordbot/.venv] |
| Startfil | [For eksempel bot.py] |
| Tjenestenavn | [For eksempel discordbot.service] |

Nettverksinformasjon skal håndteres etter skolens regler. Ikke publiser intern informasjon eller tilgangsdetaljer åpent.

## 2. Installasjon og konfigurasjon

Dokumenter kommandoene i riktig rekkefølge og hva dere kontrollerte etterpå.

| Steg | Kommando eller endring | Hvorfor? | Kontroll av resultat |
|---|---|---|---|
| Ubuntu-installasjon | [Fyll ut] | [Fyll ut] | [Fyll ut] |
| SSH fra Mac | [Fyll ut] | Fjernadministrasjon | [Fyll ut] |
| Egen botbruker | [Fyll ut] | Unngå kjøring som root | [Fyll ut] |
| Tilgang til privat GitHub-repository | [Fyll ut uten privat nøkkel] | [Fyll ut] | [Fyll ut] |
| Kloning og virtuelt miljø | [Fyll ut] | [Fyll ut] | [Fyll ut] |
| Avhengigheter | [Fyll ut] | Pakker fra requirements.txt | [Fyll ut] |
| systemd-tjeneste | [Henvis til tjenestefilen] | Automatisk oppstart og restart | [Fyll ut] |

## 3. Token og tilgang

- Token-variabel: [For eksempel DISCORD_TOKEN]
- Hvor token konfigureres: [Filsti eller mekanisme, ikke tokenet]
- Filens eierskap og rettigheter: [Fyll ut]
- GitHub-tilgang: [For eksempel read-only deploy key]
- Administrative Discord-kommandoer: [Hvordan autoriseres brukere?]

Tilgang til oppdatering skal gis eksplisitt, for eksempel via kontrollerte bruker-ID-er eller rolle-ID-er. Ikke bruk visningsnavn som autorisasjon. Dersom `commands.is_owner()` brukes, er botens eier ikke nødvendigvis Discord-serverens administrator.

### Sikkerhetssjekk

- [ ] Token, `.env` og private nøkler er utelatt fra Git.
- [ ] Boten kjører som egen Linux-bruker, ikke root.
- [ ] GitHub deploy key har bare lesetilgang, hvis denne modellen brukes.
- [ ] Administrative kommandoer har eksplisitt tilgangskontroll.
- [ ] Ingen vilkårlige shellkommandoer kan sendes fra Discord.
- [ ] Logger og skjermbilder er kontrollert for hemmeligheter.

Ved lekkasje: varsle lærer, tilbakekall eller erstatt hemmeligheten og oppdater serveren. Det er ikke nok å slette filen fra GitHub.

## 4. Daglig drift og feilsøking

Tilpass tjenestenavnet i eksemplene:

```bash
sudo systemctl status discordbot.service
sudo systemctl restart discordbot.service
sudo journalctl -u discordbot.service -n 100 --no-pager
sudo journalctl -u discordbot.service -f
free -h
df -h
top
```

| Symptom | Hva undersøker vi først? | Mulig tiltak |
|---|---|---|
| Boten er offline | Tjenestestatus og journal | [Fyll ut] |
| Kommando svarer ikke | Registrering, prefiks, intents og rettigheter | [Fyll ut] |
| Cog lastes ikke | Import- og oppstartsfeil i journalen | [Fyll ut] |
| Git-oppdatering feiler | SSH-tilgang, gren og lokale endringer | [Fyll ut] |

`active (running)` er ikke alene bevis på fungerende Discord-tilkobling. Test også en kommando.

## 5. CI og oppdatering

- Workflow-fil: [For eksempel .github/workflows/ci.yml]
- Driftsgren: [For eksempel main]
- Hvordan sikrer vi at CI er godkjent før utrulling? [Fyll ut]
- Hvordan startes oppdateringen? [SSH / autorisert Discord-kommando / separat tjeneste]

Rutine:

1. Kontroller godkjent endring og bestått syntakskontroll.
2. Registrer gammel commit-ID og kontroller lokale kodeendringer.
3. Hent ny kode og kontroller resultatet.
4. Se hvilke filer som ble endret.
5. Installer avhengigheter ved behov.
6. Reload cogs eller restart tjenesten.
7. Test Discord-tilkobling og relevant funksjon.
8. Registrer ny commit-ID og resultat.

| Endring | Typisk handling etter henting |
|---|---|
| Eksisterende cog | Reload aktuell extension og test |
| Ny eller slettet cog | Load/unload eksplisitt eller restart, og kontroller |
| bot.py eller utils.py | Restart tjenesten |
| Felles importerte hjelpemoduler | Restart er tryggest med mindre avhengigheter håndteres eksplisitt |
| requirements.txt | Installer avhengigheter og restart |

`git pull` oppdaterer filer, men laster dem ikke automatisk inn i boten og kontrollerer ikke CI-status. Reload av `cogs.*` reloader ikke automatisk `utils.py` eller alle importerte moduler.

## 6. Backup og tilbakeføring

| Hva sikkerhetskopieres? | Hvor ofte? | Hvor lagres kopien? | Hvem har tilgang? |
|---|---|---|---|
| Lokal konfigurasjon | [Fyll ut] | [Fyll ut] | [Fyll ut] |
| Eventuelle botdata | [Fyll ut] | [Fyll ut] | [Fyll ut] |
| Tjenestefil | [Fyll ut] | [Fyll ut] | [Fyll ut] |

GitHub versjonskontrollerer koden, men tar ikke automatisk backup av lokale data og hemmeligheter. Kopier med sensitive opplysninger må beskyttes.

- Hvordan gjenoppretter vi backup? [Beskriv stegene]
- Hvordan går vi tilbake til en kjent fungerende versjon? [Beskriv stegene og avhengighetene]
- Hvordan kontrollerer vi resultatet? [Fyll ut]
- Gjennomført gjenopprettingstest: [Dato og resultat, eller ikke gjennomført]

## 7. Laptop og vedlikehold

- Strøm og lokk-lukking: [Oppsett og test]
- Hvilemodus: [Oppsett og test]
- Sikkerhetsoppdateringer: [Rutine og ansvar]
- Ved avslutning av prosjektet: [Overlevering, sletting av lokale data og tilbakekalling av tilgang]
