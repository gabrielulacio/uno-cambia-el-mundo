import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from api.models.payment import PaymentReport

logger = logging.getLogger(__name__)

def send_email_notification(report: PaymentReport):
    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    receiver = sender 

    if not sender or not password:
        logger.warning("No hay credenciales de correo configuradas en el entorno.")
        return

    message = MIMEMultipart("alternative")
    message["Subject"] = f"💰 Nuevo Aporte: {report.amount} {report.currency} - {report.project}"
    message["From"] = sender
    message["To"] = receiver

    text = f"""
    Nuevo reporte de donación recibido:
    
    Donante: {report.name} ({'Anónimo' if report.anonymous else 'Público'})
    Email: {report.email}
    Monto: {report.amount} {report.currency}
    Método de Pago: {report.method}
    Referencia: {report.reference}
    Proyecto: {report.project}
    
    Verifica la transacción en el banco y en el Google Sheet.
    """
    
    message.attach(MIMEText(text, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(message)
        logger.info(f"✅ Correo de notificación enviado para donación de {report.email}")
    except Exception as e:
        logger.error(f"❌ Error enviando correo: {e}")
