import qrcode
import json
from pathlib import Path

QR_DIR = Path("app/static/qrcodes")
QR_DIR.mkdir(parents=True, exist_ok=True)


def generate_qr(registration_id: str, event_id: int):
    payload = {
        "registration_id": registration_id,
        "event_id": event_id
    }

    img = qrcode.make(json.dumps(payload))
    file_path = QR_DIR / f"{registration_id}.png"
    img.save(file_path)

    return str(file_path)
