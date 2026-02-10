from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, ListFlowable, ListItem, PageBreak


@dataclass(frozen=True)
class CVConfig:
    output_pdf: Path
    updated_on: str

    name: str
    headline: str

    email: str
    website: str
    linkedin: str
    github: str
    location: str


def build_cv_es(cfg: CVConfig) -> None:
    cfg.output_pdf.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(cfg.output_pdf),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=18 * mm,
        title=f"CV - {cfg.name}",
        author=cfg.name,
        subject="Currículum",
    )

    styles = getSampleStyleSheet()
    base = styles["Normal"]

    s_title = ParagraphStyle(
        "Title",
        parent=base,
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        spaceAfter=2 * mm,
        textColor=colors.HexColor("#0B3D91"),
    )
    s_headline = ParagraphStyle(
        "Headline",
        parent=base,
        fontName="Helvetica-Bold",
        fontSize=11.25,
        leading=13.5,
        textColor=colors.black,
        spaceAfter=4 * mm,
    )
    s_contact = ParagraphStyle(
        "Contact",
        parent=base,
        fontName="Helvetica",
        fontSize=9.5,
        leading=12,
        textColor=colors.black,
    )
    s_section = ParagraphStyle(
        "Section",
        parent=base,
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        textColor=colors.HexColor("#0B3D91"),
        spaceBefore=4 * mm,
        spaceAfter=2 * mm,
    )
    s_body = ParagraphStyle(
        "Body",
        parent=base,
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        textColor=colors.black,
    )
    s_muted = ParagraphStyle(
        "Muted",
        parent=s_body,
        textColor=colors.HexColor("#4A4A4A"),
    )
    s_job = ParagraphStyle(
        "Job",
        parent=s_body,
        fontName="Helvetica-Bold",
        spaceAfter=1 * mm,
    )
    s_meta = ParagraphStyle(
        "Meta",
        parent=s_muted,
        fontSize=9.5,
        leading=12,
        spaceAfter=2 * mm,
    )

    def bullets(items: list[str]) -> ListFlowable:
        return ListFlowable(
            [ListItem(Paragraph(i, s_body), leftIndent=0) for i in items],
            bulletType="bullet",
            leftIndent=10,
            bulletFontName="Helvetica",
            bulletFontSize=9,
            bulletOffsetY=1,
        )

    story: list = []

    # ATS-friendly header: single column, no tables.
    story.append(Paragraph(cfg.name, s_title))
    story.append(Paragraph(cfg.headline, s_headline))
    story.append(
        Paragraph(
            f"{cfg.location} | {cfg.email} | {cfg.website} | {cfg.linkedin} | {cfg.github}",
            s_contact,
        )
    )
    story.append(Spacer(1, 3 * mm))

    # Summary
    story.append(Paragraph("RESUMEN PROFESIONAL", s_section))
    story.append(
        Paragraph(
            "Analytics Engineer especializado en convertir procesos manuales y datos dispersos en sistemas analíticos escalables. "
            "Diseño y opero pipelines (API/BD a BigQuery/MySQL a capa semántica a reporting), construyo modelos semánticos en Power BI "
            "y automatizo procesos críticos con Python, n8n y Make con foco en fiabilidad, calidad y rendimiento.",
            s_body,
        )
    )
    story.append(Spacer(1, 2 * mm))

    # Experience
    story.append(Paragraph("EXPERIENCIA", s_section))

    story.append(Paragraph("Becall | Analytics Engineer", s_job))
    story.append(Paragraph("España | 01/2025 - Presente", s_meta))
    story.append(
        Paragraph(
            "Diseño y opero data pipelines, construyo modelos semánticos en Power BI (DAX/M) e implemento automatizaciones operativas "
            "para convertir procesos manuales en sistemas escalables y confiables.",
            s_body,
        )
    )
    story.append(Spacer(1, 1.5 * mm))
    story.append(Paragraph("<b>Resultados (Becall, 2025-2026):</b>", s_body))
    story.append(
        bullets(
            [
                "<b>CRM:</b> de ejecuciones inestables (aprox. 30%) a aprox. 90-95% con SSO + OTP, validaciones, reintentos y alertas; aprox. 1000-2000 registros/día.",
                "<b>Power BI:</b> diseño y evolución de un modelo semántico complejo (múltiples fuentes + lógica de negocio), hasta <b>347 medidas</b> y <b>89 relaciones</b>.",
                "<b>BigQuery:</b> data products con capa de vistas para consolidar cientos de tablas heterogéneas y escalar consumo analítico.",
                "<b>Automatización:</b> workflows con Python + n8n/Make; integración por APIs, scheduling y reporting de ejecución.",
                "<b>Operación:</b> integraciones con plataformas de contact center y utilidades DNC (compliance) para reducir fricción operativa.",
            ]
        )
    )
    story.append(Spacer(1, 1.5 * mm))
    story.append(Paragraph("<b>Responsabilidades:</b>", s_body))
    story.append(
        bullets(
            [
                "Pipelines end-to-end (ingesta, transformación, carga) con observabilidad y operación estable.",
                "Automatización de procesos (APIs/portales/CRM) con idempotencia, logging y reconciliación.",
                "Colaboración con negocio para traducir reglas a modelos analíticos mantenibles.",
            ]
        )
    )
    story.append(Spacer(1, 2 * mm))

    story.append(Paragraph("Viscofan S.A. | Business Intelligence / Business Analytics", s_job))
    story.append(Paragraph("São Paulo, Brasil | 2024 - 2025", s_meta))
    story.append(
        bullets(
            [
                "Análisis y reporting para marketing: dashboards Power BI, KPIs y automatización de extracción con Python.",
                "Soporte a decisiones estratégicas mediante modelado de datos, ETL y análisis de mercado.",
                "Colaboración con equipos multifuncionales para mejorar adopción y uso de datos.",
            ]
        )
    )

    story.append(PageBreak())

    # Skills
    story.append(Paragraph("HABILIDADES (SKILLS)", s_section))
    story.append(
        bullets(
            [
                "<b>Lenguajes:</b> Python, SQL, DAX, Power Query (M).",
                "<b>Datos:</b> BigQuery, MySQL; diseño de vistas/capas analíticas; incrementalidad y upserts.",
                "<b>BI:</b> Power BI (modelado semántico, performance, gobernanza).",
                "<b>Automatización:</b> Python, n8n, Make; Playwright, Selenium; integración de APIs; scheduling.",
                "<b>Buenas prácticas:</b> idempotencia, retries/backoff, logging, alertas, data quality y reconciliación.",
            ]
        )
    )

    # Selected projects (anonymized)
    story.append(Paragraph("PROYECTOS DESTACADOS (ANONIMIZADOS)", s_section))
    story.append(
        bullets(
            [
                "Optimización de modelos Power BI complejos: reducción de cálculos costosos y mejora de mantenibilidad sin afectar producción.",
                "Consolidación de leads en BigQuery: vistas intermedias + vista final para escalar ante crecimiento de tablas y esquemas variables.",
                "ETLs de Marketing Analytics: Google Ads + Meta Ads hacia modelo analítico con control incremental y alerting.",
                "Automatizaciones CRM con SSO + OTP: workflows con Python + n8n/Make; extracción, deduplicación y carga incremental con reporte de ejecución.",
                "Integraciones operativas (contact center): sincronización de listas outbound y gestión DNC (bloquear/consultar/desbloquear).",
            ]
        )
    )

    # Certifications
    story.append(Paragraph("CERTIFICACIONES", s_section))
    story.append(
        Paragraph(
            "<b>PL-300:</b> Microsoft Power BI Data Analyst Associate "
            "(Emisión: 26/08/2024 · Renovación: 08/2025 · Vigente hasta: 08/2026)",
            s_body,
        )
    )

    # Education
    story.append(Paragraph("EDUCACIÓN", s_section))
    story.append(Paragraph("<b>Máster en Inteligencia de Negocios</b> | UNIR | 2023 - 2024", s_body))
    story.append(Paragraph("<b>Grado en Administración y Dirección de Empresas</b> | ULPGC | 2018 - 2022", s_body))

    # Languages
    story.append(Paragraph("IDIOMAS", s_section))
    story.append(Paragraph("Español (nativo) · Inglés (avanzado) · Portugués (avanzado)", s_body))

    # Avoid headers/footers for ATS parsing; keep content in the main body.
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(f"Actualizado: {cfg.updated_on}", s_meta))

    doc.build(story)


def main() -> None:
    cfg = CVConfig(
        output_pdf=Path("output/pdf/CV-Espanol.pdf"),
        updated_on="10 feb 2026",
        name="Jose David Batista Zerpa",
        headline="Analytics Engineer | Power BI (DAX/M) | BigQuery | Python",
        email="jbatistazerpa@gmail.com",
        website="www.davidzerpa.com",
        linkedin="linkedin.com/in/davidzerpago",
        github="github.com/DavidZerpa96",
        location="España",
    )
    build_cv_es(cfg)
    print(f"Wrote {cfg.output_pdf}")


if __name__ == "__main__":
    main()
