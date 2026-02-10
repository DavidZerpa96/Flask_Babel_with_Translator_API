from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
    PageBreak,
)


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


def _footer(canvas, doc, cfg: CVConfig) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.grey)
    canvas.drawString(doc.leftMargin, 12 * mm, f"Actualizado: {cfg.updated_on}")
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 12 * mm, f"Página {doc.page}")
    canvas.restoreState()


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
        fontSize=11.5,
        leading=14,
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

    # Header (2 columns): name/headline + contact
    left = [
        Paragraph(cfg.name, s_title),
        Paragraph(cfg.headline, s_headline),
    ]
    right_lines = [
        f"<b>Ubicación:</b> {cfg.location}",
        f"<b>Email:</b> {cfg.email}",
        f"<b>Web:</b> {cfg.website}",
        f"<b>LinkedIn:</b> {cfg.linkedin}",
        f"<b>GitHub:</b> {cfg.github}",
    ]
    right = [Paragraph(x, s_contact) for x in right_lines]

    header = Table(
        [[left, right]],
        colWidths=[115 * mm, None],
        style=TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        ),
    )
    story.append(header)
    story.append(Spacer(1, 2 * mm))

    # Summary
    story.append(Paragraph("PERFIL", s_section))
    story.append(
        Paragraph(
            "Analytics Engineer especializado en convertir procesos manuales y datos dispersos en sistemas analíticos escalables. "
            "Diseño y opero pipelines (API/DB -&gt; BigQuery/MySQL -&gt; capa semántica -&gt; reporting), optimizo modelos de Power BI "
            "y automatizo procesos críticos con foco en fiabilidad, calidad y rendimiento.",
            s_body,
        )
    )
    story.append(Spacer(1, 2 * mm))

    # Highlights (numbers first)
    story.append(Paragraph("IMPACTO (2025-2026)", s_section))
    story.append(
        bullets(
            [
                "<b>Power BI:</b> optimización de modelos de alta complejidad (hasta <b>347 medidas</b> y <b>89 relaciones</b>).",
                "<b>Automatización CRM:</b> fiabilidad mejorada de ~30% a ~90-95% con SSO + OTP; ~1000-2000 registros/día.",
                "<b>BigQuery:</b> data products para consolidar cientos de tablas heterogéneas y escalar consumo analítico.",
                "<b>ETL Marketing:</b> pipelines incrementales (Google Ads + Meta Ads) con upserts, retries/backoff y alertas.",
                "<b>Operación:</b> integraciones con plataformas de contact center, sincronización de listas y utilidades DNC (compliance).",
            ]
        )
    )

    # Experience
    story.append(Paragraph("EXPERIENCIA", s_section))

    story.append(Paragraph("Becall | Analytics Engineer", s_job))
    story.append(Paragraph("España | 2025 - Presente", s_meta))
    story.append(
        bullets(
            [
                "Diseño y operación de pipelines end-to-end (ingesta, transformación, carga, observabilidad).",
                "Modelado semántico y performance en Power BI (DAX/M), gobernanza de medidas y mantenibilidad.",
                "Automatización de procesos operativos (APIs/portales/CRM) con reintentos por etapa, validaciones y alertas.",
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
    story.append(Paragraph("STACK TÉCNICO", s_section))
    story.append(
        bullets(
            [
                "<b>Lenguajes:</b> Python, SQL, DAX, Power Query (M).",
                "<b>Datos:</b> BigQuery, MySQL; diseño de vistas/capas analíticas; incrementalidad y upserts.",
                "<b>BI:</b> Power BI (modelado semántico, performance, gobernanza).",
                "<b>Automatización:</b> Playwright, Selenium; integración de APIs; scheduling.",
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
                "Automatizaciones CRM con SSO + OTP: extracción, limpieza, deduplicación y carga incremental con reporte de ejecución.",
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

    doc.build(story, onFirstPage=lambda c, d: _footer(c, d, cfg), onLaterPages=lambda c, d: _footer(c, d, cfg))


def main() -> None:
    cfg = CVConfig(
        output_pdf=Path("output/pdf/CV-Espanol.pdf"),
        updated_on="10 feb 2026",
        name="Jose David Batista Zerpa",
        headline="Analytics Engineer | Power BI (DAX/M) | BigQuery | Python | Data Pipelines & Automation",
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

