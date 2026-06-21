import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO


def create_pdf(planet, row):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    pdf.setTitle("Galactic Report")

    pdf.drawString(100, 800, f"Planet Report: {planet}")

    pdf.drawString(100, 760, f"Population: {row['population']}")
    pdf.drawString(100, 740, f"Economy: {row['economy']}")
    pdf.drawString(100, 720, f"Military: {row['military']}")
    pdf.drawString(100, 700, f"Technology: {row['technology']}")
    pdf.drawString(100, 680, f"Happiness: {row['happiness']}")

    pdf.save()

    buffer.seek(0)

    return buffer