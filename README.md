# Online Reservierung – API

**Kurz für Scanner*innen**

Backend-API für eine serviceorientierte Online-Reservierungsanwendung.  
Teil eines Microservice-Portfolios mit Fokus auf saubere Architektur, klare Schnittstellen und praxisnahe Backend-Entwicklung.

---

## Überblick

Dieses Repository enthält die **API-Komponente** des Portfolio-Projekts **Online Reservierung**.

Die API bildet das backendseitige Fundament der Anwendung und stellt klar definierte Schnittstellen für reservierungsbezogene Geschäftslogik bereit.  
Der Schwerpunkt liegt auf **Struktur**, **Nachvollziehbarkeit** und **Erweiterbarkeit**, nicht auf schneller Feature-Vollständigkeit.

Das Projekt ist bewusst als **Work in Progress** angelegt und entwickelt sich schrittweise weiter.

---

## Zielsetzung

Ziel dieses Projekts ist es, eine Backend-API zu entwickeln, die:

- realistische Anforderungen abbildet  
- wartbar und verständlich strukturiert ist  
- klare Verantwortlichkeiten besitzt  
- sich in eine serviceorientierte Architektur einfügt  
- als Grundlage für spätere Microservices dient  

Der Fokus liegt auf **sauberem API-Design** und **klarer Businesslogik**, nicht auf UI- oder Framework-Showcases.

---

## Architekturidee

Die API folgt einem **API-first-Ansatz** und ist so aufgebaut, dass:

- Routing, Businesslogik und Persistenz klar getrennt sind  
- Datenmodelle und Schnittstellen explizit definiert werden  
- Erweiterungen (z. B. Auth-Service, User-Service) über separate Services möglich sind  

Weitere fachliche oder technische Services werden in **eigenständigen Repositories** umgesetzt und über definierte Schnittstellen angebunden.

---

## Technischer Stack

- Python 3.11  
- FastAPI  
- Pydantic (Request-/Response-Validierung)  
- SQLAlchemy (Persistenzschicht)  
- Docker (lokale Entwicklungsumgebung)  
- Git & GitHub  

---

## Projektstatus

🚧 **Work in Progress**

**Stand: 07.01.2025**

Der aktuelle Stand bildet den Entwicklungsfortschritt zum oben genannten Datum ab.  
Änderungen an Architektur, Struktur und Implementierung sind während des laufenden Entwicklungsprozesses ausdrücklich vorbehalten.

Aktueller Fokus:

- stabile Projekt- und Ordnerstruktur  
- saubere Trennung der Schichten  
- verständliche, nachvollziehbare API-Endpunkte  
- bewusste Dokumentation von Architekturentscheidungen  

Funktionale Erweiterungen erfolgen schrittweise.

---

## Einordnung im Portfolio

Dieses Projekt ist Teil meines Developer-Portfolios und zeigt meinen Übergang von klassischer Web-Applikationsentwicklung hin zu **API- und serviceorientierter Backend-Architektur**.

Der Anspruch ist nicht Perfektion, sondern **Realismus**:  
Entscheidungen, Abwägungen und technische Kompromisse sollen sichtbar und nachvollziehbar bleiben.
