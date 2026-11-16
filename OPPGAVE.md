# Oppgave i utvikling, driftsstøtte og brukerstøtte

## Bakgrunn

Dere skal arbeide i grupper på to og bygge et lite digitalt community. Løsningen består av en Discord-server og minst én egenutviklet bot som kjører på en utdelt laptop med Ubuntu Server.

Målgruppen skal styre valgene dere tar i alle tre fagene.

## Velg tema

Dere kan for eksempel lage en server for et større LAN, med informasjon, arrangementer og hjelp til deltakere. Andre temaer avtales med lærer.

Beskriv målgruppen og minst ett konkret behov boten skal løse.

## Del 1: Driftsstøtte – DRS

Dere skal:

- Installere Ubuntu Server uten grafisk grensesnitt.
- Avklare nettverksoppsett med lærer eller IT-ansvarlig og konfigurere fast IP eller DHCP-reservasjon og hostname.
- Administrere serveren via SSH og terminal fra Mac.
- Bruke en egen Linux-bruker til boten; den skal ikke kjøre som root.
- Kjøre boten som en systemd-tjeneste som starter automatisk og restarter ved feil.
- Kunne finne tjenestestatus, lese logger og kontrollere ressursbruk.
- Undersøke strømforsyning, hvilemodus og hva som skjer når laptoplokket lukkes.
- Lage en plan for backup, gjenoppretting og oppdateringer.
- Dokumentere oppsettet slik at en annen gruppe kan gjenskape det.

## Del 2: Brukerstøtte – BRS

Dere skal:

- Lage en brukervennlig struktur med kanaler og kategorier.
- Definere roller og rettigheter etter behov, med minst mulig tilgang.
- Lage tydelig velkomstinformasjon, regler og hjelp.
- Skrive en brukerveiledning og FAQ tilpasset målgruppen.
- Lage en rutine for mottak, oppfølging og avslutning av supportsaker.
- Beskrive personvern, moderering og håndtering av regelbrudd.
- Gjennomføre brukertest med en annen gruppe og forbedre løsningen ut fra tilbakemeldinger.

## Del 3: Utvikling – UTV

Dere skal:

- Utvikle minst én nyttig botfunksjon i Python med discord.py. Andre teknologivalg avtales med lærer.
- Bygge videre på eventuell startkode, med egne funksjoner organisert i cogs/extensions.
- Håndtere relevant ugyldig input og feil uten at boten krasjer unødvendig.
- Bruke Git og GitHub med forståelige commits.
- Holde token og andre hemmeligheter utenfor koden og Git-historikken.
- Dokumentere hvilke kilder og KI-verktøy dere bruker, og hvordan resultatene kontrolleres.
- Demonstrere at boten fungerer på Ubuntu-serveren og i Discord.

Eksempler på funksjoner: velkomst, rolletildeling, quiz, avstemning, påminnelser, arrangementer eller moderering. En enkel `ping`-kommando fra startmalen oppfyller ikke alene kravet om egen nyttig funksjon.

## GitHub Actions og oppdatering

- GitHub Actions skal kontrollere syntaksen i Python-filene ved push og pull request.
- Bruk samme Python-versjon i CI som på serveren.
- Beskriv hvordan godkjent kode hentes og aktiveres på serveren.
- Manuelt utløst oppdatering kan skje via SSH eller en autorisert Discord-kommando. [Lærer avklarer om automatisert utrulling er obligatorisk.]

**Syntakskontroll garanterer ikke vellykket oppstart.** Avhengigheter, imports, konfigurasjon og Discord-tilkobling må kontrolleres separat.

En feilet CI-kontroll hindrer ikke automatisk push eller `git pull`. Bruk pull requests og en godkjenningsrutine før utrulling, gjerne med krav til bestått CI på `main` dersom GitHub-oppsettet støtter det.

## Samarbeid

Begge skal bidra i alle tre fagene og kunne forklare sentrale deler av løsningen. Bruk Issues til arbeidsoppgaver og la partneren gjennomgå viktige kodeendringer før fletting.

## Leveranser

- [ ] Privat repository med kode og de seks dokumentasjonsfilene.
- [ ] Fungerende Discord-server og egen botfunksjon.
- [ ] Bot som kjører som systemd-tjeneste på Ubuntu Server.
- [ ] Fungerende syntakskontroll i GitHub Actions.
- [ ] Dokumentert oppdaterings- og backuprutine.
- [ ] Tekniske tester og brukertest med minst én gjennomført forbedring.
- [ ] Kilder, KI-bruk og individuell refleksjon.
- [ ] Demonstrasjon av løsningen.

Innleveringsfrist: [Lærer fyller ut]

## Vurdering

| Område | Hva vurderes? |
|---|---|
| DRS | Fungerende og sikkert oppsett, feilsøking og gjenskapbar dokumentasjon |
| BRS | Tilpasning til målgruppen, veiledning, rettigheter og forbedring etter brukertest |
| UTV | Nyttig funksjon, forståelig struktur, feilhåndtering og versjonskontroll |
| Tverrfaglig | Begrunnede valg og sammenheng mellom behov, utvikling og drift |
| Individuelt | Eget bidrag og evne til å forklare og demonstrere løsningen |

Høy kvalitet vises gjennom begrunnede valg, relevante tester og dokumenterte forbedringer, ikke bare mange funksjoner eller lange tekster. Lærer avklarer vurderingen opp mot aktuelle kompetansemål før oppstart.
