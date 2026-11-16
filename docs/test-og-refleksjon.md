# Testing, forbedring, kilder og refleksjon

Fyll ut etter hvert som dere tester. Ikke marker en test som godkjent før den er gjennomført. Dokumenter resultater uten token, private nøkler eller unødvendige personopplysninger.

## 1. Tekniske tester

Syntakskontroll er minstekravet til automatisert kontroll. Oppstart og funksjonalitet testes separat.

| Test | Forventet resultat | Faktisk resultat | Status og dokumentasjon |
|---|---|---|---|
| Push med gyldig Python | CI består | [Fyll ut] | [Lenke/status] |
| Syntaksfeil i egen testbranch | CI feiler | [Fyll ut] | [Lenke/status] |
| Omstart av Ubuntu-server | Boten starter automatisk | [Fyll ut] | [Bevis] |
| Uventet avslutning av botprosess | systemd starter boten igjen | [Fyll ut] | [Bevis] |
| Vanlig brukerkommando | Riktig svar | [Fyll ut] | [Bevis] |
| Ugyldig input | Forståelig feil uten krasj | [Fyll ut] | [Bevis] |
| Bruker uten administrativ tilgang | Administrativ kommando avvises | [Fyll ut] | [Bevis] |
| Oppdatering av botkode | Ny versjon hentes og fungerer etter aktivering | [Fyll ut] | [Commit-ID/resultat] |
| Gjenoppretting fra backup | Avtalte data eller konfigurasjon gjenopprettes | [Fyll ut] | [Bevis] |

Hvis dere har `!update` og cog-reload, test også:

| Test | Forventet resultat | Faktisk resultat |
|---|---|---|
| Ingen nye commits | Ingen oppdateringer rapporteres | [Fyll ut] |
| Endret cog-fil | Endringen vises og reload fungerer | [Fyll ut] |
| Feil ved Git-henting | Feilmelding, ikke falsk suksess | [Fyll ut] |
| To samtidige oppdateringer | Bare én oppdatering kjører | [Fyll ut] |
| Endring i utils.py | Ny kode fungerer etter restart | [Fyll ut] |

Feiltester gjennomføres kontrollert og avtales med lærer når de påvirker andre. Ikke legg bevisste feil på driftsgrenen bare for å teste CI.

## 2. Brukertest med en annen gruppe

- Testgruppe: [Gruppenavn]
- Dato: [Dato]

Be testgruppen løse disse oppgavene uten muntlig veiledning først:

1. Finn serverens formål og regler.
2. Finn hvordan du får hjelp.
3. Bruk gruppas viktigste botfunksjon.
4. Meld en avtalt, ufarlig supportsak.

| Oppgave | Observasjon | Tilbakemelding | Foreslått tiltak |
|---|---|---|---|
| [Oppgave] | [Hva skjedde?] | [Fyll ut] | [Fyll ut] |

## 3. Forbedringer

Gjennomfør minst én forbedring basert på brukertesten.

| Funn | Endring vi gjorde | Hvorfor prioriterte vi dette? | Resultat etter ny test |
|---|---|---|---|
| [Fyll ut] | [Fyll ut] | [Fyll ut] | [Fyll ut] |

Gjenstående feil og begrensninger: [Fyll ut]

## 4. Kilder

Registrer kilder dere faktisk brukte. Oppgi konkrete dokumentasjonssider og aktuell versjon når det er relevant.

| Kilde/URL | Hva brukte vi den til? | Hva lærte vi? | Hvordan kontrollerte vi resultatet? |
|---|---|---|---|
| [Kilde] | [Fyll ut] | [Fyll ut] | [Fyll ut] |

Aktuelle kildetyper er dokumentasjonen til discord.py, Discord API, Python, Ubuntu Server, GitHub Actions og lokale manualsider som `man systemd.service` og `man journalctl`.

## 5. KI-bruk

KI kan brukes som hjelp, men dere skal forstå og kunne forklare løsningen. Ikke del token, passord, private nøkler eller personopplysninger med KI-verktøy.

| Verktøy | Hva ba vi om hjelp til? | Hva tok vi i bruk? | Hvordan verifiserte vi det? |
|---|---|---|---|
| [Verktøy] | [Kort beskrivelse] | [Fyll ut] | [Test eller dokumentasjon] |

Hvis KI ikke er brukt, skriv det.

## 6. Gruppas oppsummering

- Hva leverer vi, og hvilket behov løser det? [Fyll ut]
- Hvordan henger DRS, BRS og UTV sammen i løsningen? [Gi et konkret eksempel]
- Hvilket teknisk valg var viktigst, og hvorfor? [Fyll ut]
- Hva ville vi gjort annerledes neste gang? [Fyll ut]

## 7. Individuell refleksjon

### Gruppemedlem 1: [Navn]

- Mine viktigste bidrag: [Fyll ut]
- Dette lærte jeg i DRS: [Fyll ut]
- Dette lærte jeg i BRS: [Fyll ut]
- Dette lærte jeg i UTV: [Fyll ut]
- En feil jeg undersøkte og hvordan jeg løste den: [Fyll ut]
- Dette kan jeg forklare og demonstrere selv: [Fyll ut]

### Gruppemedlem 2: [Navn]

- Mine viktigste bidrag: [Fyll ut]
- Dette lærte jeg i DRS: [Fyll ut]
- Dette lærte jeg i BRS: [Fyll ut]
- Dette lærte jeg i UTV: [Fyll ut]
- En feil jeg undersøkte og hvordan jeg løste den: [Fyll ut]
- Dette kan jeg forklare og demonstrere selv: [Fyll ut]
