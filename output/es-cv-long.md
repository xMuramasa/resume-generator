# MARTÍN SALINAS SCUSSOLIN

**Software & Cloud Engineer** — Santiago, Chile
[martin.salinas.scussolin@gmail.com](mailto:martin.salinas.scussolin@gmail.com) · [x-muramasa.dev](https://x-muramasa.dev) · [LinkedIn](https://www.linkedin.com/in/xmuramasa) · [GitHub](https://github.com/xMuramasa)

---

## HABILIDADES TÉCNICAS

* **Arquitectura de Sistemas:** Diseño de Microservicios, Arquitectura Orientada a Eventos, Planificación de Escalabilidad, Sistemas Distribuidos.
* **Infraestructura Cloud:** AWS (ECS, Fargate, Lambda, VPC, SQS, Secrets Manager), Azure (Arquitectura de Red, VPN), Proxmox VE.
* **Gestión de Identidad y Accesos (IAM):** AWS Cognito, Clerk, OAuth, JWT, Google Cloud Service Accounts, Apple Developer.
* **Infraestructura como Código (IaC):** Terraform, CloudFormation.
* **Backend y Automatización:** Go, Python, TypeScript/Node.js, Bun, FastAPI, Docker, GitHub Actions CI/CD.
* **Apps y Autoalojamiento:** React Native (Expo), SwiftUI, Jetpack Compose, Docker Compose, Caddy, Tailscale.
* **Bases de Datos:** PostgreSQL, AWS Aurora, AWS DynamoDB, MongoDB, SQLite, Optimización de Consultas.
* **Observabilidad y Redes:** Wireshark, CloudWatch, Cacti, Grupos de Seguridad (Security Groups).

## EXPERIENCIA PROFESIONAL

### Full Stack Software Engineer · Mynu.ai
*(Mar 2024 – Presente) | Santiago, Chile*

* **Full-Stack & Mobile Development:** Diseñé e implementé la arquitectura mobile-first y web app desde cero hasta producción para **Mynu App** (iOS/Android) utilizando **React Native (Expo)** y plataformas web como **app.mynubaby.cl** y **mi.mynu.ai** con **React**, asegurando una integración fluida con los microservicios backend.
* **Client-Side Optimization & State Management:** Optimicé el rendimiento client-side e implementé estrategias eficientes de manejo de estado y caching con **TanStack Query**, reduciendo la latencia percibida por el usuario y garantizando estabilidad en entornos de producción mobile y web.
* **Cloud Infrastructure & Migration:** Lideré la migración cloud desde Azure hacia **AWS ECS/Fargate**, reestructurando el despliegue de contenedores para mejorar el throughput, la escalabilidad y la eficiencia de costos.
* **Infrastructure as Code (IaC):** Diseñé e implementé un microservicio de notificaciones event-driven utilizando **Terraform** (SQS & Lambda), desacoplando tareas asíncronas y eliminando cuellos de botella en el procesamiento del backend.
* **IAM & Authentication Architecture:** Diseñé un sistema de autenticación personalizado utilizando **AWS Cognito** en una arquitectura híbrida; posteriormente ejecuté una migración de usuarios a **Clerk** con cero downtime y cero pérdida de datos, integrando flujos personalizados de OAuth con Google y Apple.
* **CI/CD & Security Automation:** Construí pipelines de despliegue automatizados utilizando **GitHub Actions**, Environments y **AWS Secrets Manager** para la inyección dinámica de credenciales, eliminando el uso de credenciales hardcodeadas.
* **Performance Engineering:** Reduje la latencia de respuesta en 2 segundos en integraciones con APIs de terceros (Edamam API) mediante la implementación de mecanismos de in-memory caching y ALB Sticky Sessions.
* **Network & Security Design:** Configuré topologías de VPC seguras con VPC Peering e Interface Endpoints para garantizar una comunicación privada bajo el principio de menor privilegio entre servicios distribuidos.

### Software Engineer · Zippedi Inc.
*(Jun 2022 – Oct 2023) | Santiago, Chile*

* **Full-Stack & Mobile Engineering:** Desarrollé funcionalidades clave e implementé mejoras continuas para aplicaciones móviles y plataformas web orientadas a clientes, trabajando tanto en ciclos de desarrollo de largo plazo (Shape-Up) como en sprints ágiles para despliegue rápido de features y bug fixes.
* **Internal QA Tooling & Platforms:** Implementé features y mantuve herramientas en la plataforma web para el equipo de QA, optimizando los ciclos de validación de software interno.

### Junior Cybersecurity Engineer (Intern) · NTT DATA Europe & LATAM
*(Ene 2022 – Feb 2022) | Santiago, Chile*

* **Cloud Security & Policy:** Evalué topologías de red en Azure para clientes corporativos, identificando vulnerabilidades e implementando marcos de hardening cloud-native.
* **Threat Modeling & Governance Research:** Investigué y documenté metodologías de Cyber Kill Chain para fortalecer el análisis de vulnerabilidades y el modelado de amenazas; realicé investigaciones de seguridad alineadas con el estándar ISO 27001 para respaldar estrategias de cumplimiento y gestión de riesgos.

### Operations Engineer (Intern) · ITD Telecom
*(Ene 2021 – Ago 2021) | Santiago, Chile*

* **Hosting Infrastructure Support & Internal Tooling:** Proporcioné soporte técnico a la plataforma de hosting y desarrollé herramientas internas para mejorar la eficiencia operacional.
* **Service Management & GLPI Implementation:** Trabajé en la implementación de GLPI para optimizar las operaciones de TI internas y el seguimiento de tickets.
* **Infrastructure Monitoring:** Monitoreé la salud y las métricas de rendimiento de la infraestructura de hosting utilizando **Cacti**.
* **SLA & Process Governance:** Contribuí en el desarrollo de políticas internas de SLA para optimizar los flujos de trabajo generales de la empresa.

### Ayudante Docente y de Laboratorio · Universidad Técnica Federico Santa María
*(Ago 2019 – Dic 2022) | Santiago, Chile*

* **Ayudante de Cátedra:** Gestión de Proyectos de Informática *(Abr 2022 – Dic 2022)*, Estructuras de Datos *(Mar 2020 – Jul 2022)*, Introducción a la Ingeniería *(Ago 2020 – Ene 2021)* y Programación en Python *(Mar 2020 – Jul 2020)*: apoyo en cátedras, material de estudio, ayudantías y corrección de tareas de código y teoría.
* **Ayudante de Laboratorio** *(Ago 2019 – Oct 2019)*: Mantenimiento preventivo y correctivo de los equipos de laboratorio.

## PROYECTOS DESTACADOS

* **Cloud Infrastructure Blueprint (Terraform):** Diseñé e implementé una plataforma AWS de nivel de producción utilizando Terraform, la cual incluye VPCs aisladas, VPC Peering, servicios ECS, mensajería SQS, políticas de mínimo privilegio de IAM y comunicación orientada a eventos para demostrar patrones de arquitectura cloud escalable.
* **Trismegistus (Go, Swift, Kotlin):** Relay WebSocket en Go con SQLite y reenvío de eventos para un agente de IA autoalojado, y apps nativas SwiftUI (macOS) y Jetpack Compose (Android) sobre un protocolo común con contract tests.
* **Homelab Autoalojado:** 25 contenedores Docker Compose tras Caddy (TLS wildcard vía Cloudflare DNS-01), DNS con AdGuard, acceso solo por Tailscale, monitoreo con Beszel/Uptime Kuma y respaldos nocturnos con restic.
* **Open Source:** [news-reader](https://github.com/xMuramasa/news-reader) (noticias generadas con IA como JSON validado; Bun, MongoDB, React), [img-transformer](https://github.com/xMuramasa/img-transformer) (conversión de imágenes con FastAPI) y [on-site-meeting-logger](https://github.com/xMuramasa/on-site-meeting-logger) (de grabaciones de reuniones a actas y PDFs).
* **Desarrollo con IA:** Construí estos proyectos dirigiendo agentes de IA (Claude Code) con specs y revisión estricta.
* **Tesis - Machine Learning para Clasificación de Autómatas:** Construí un modelo de alta precisión para autómatas celulares 1D, demostrando sólidas habilidades de diseño analítico y algorítmico.

## EDUCACIÓN

### Universidad Técnica Federico Santa María
*(2017 – 2023) | Santiago, Chile*

* Licenciatura en Ciencias (B.Sc.) en Ingeniería Civil Informática (Grado Profesional de 5 años)

## CERTIFICACIONES

* **Docker Mastery:** Kubernetes & Swarm (Udemy) · **Go - The Complete Guide** (Udemy)

## SOBRE MÍ

Software and Cloud Engineer con una sólida base en ingeniería backend y gestión de identidades y accesos. Enfocado en el diseño de sistemas distribuidos escalables, modulares y seguros. Sobresalgo en la traducción de requisitos de negocio complejos hacia arquitecturas cloud de alto rendimiento, aprovechando la infraestructura como código (IaC) para garantizar consistencia y confiabilidad desde sus cimientos.
