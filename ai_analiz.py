from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from pathlib import Path
import json

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)



def fiyat_farki_analizi(en_ucuz_urun,en_pahali_urun,ucuz_yorumlar="",pahali_yorumlar=""):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return json.dumps({"hata": "GEMINI_API_KEY bulunamadı."})

    prompt=f"""
    Aşağıdaki verileri inceleyerek analiz et:

    EN UCUZ ÜRÜN: {en_ucuz_urun}
    EN UCUZ YORUMLAR: {ucuz_yorumlar}

    EN PAHALI ÜRÜN: {en_pahali_urun}
    EN PAHALI YORUMLAR: {pahali_yorumlar}"""

    try:
        client=genai.Client(api_key=api_key)

        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "OBJECT",
                "properties": {
                    "genel_memnuniyet": {"type": "STRING"},
                    "fiyat_performans_farki": {"type": "STRING"},
                    "tavsiye_edilen_urun": {"type": "STRING"},
                    "tercih_nedeni": {"type": "STRING"},
                },
                "required": [
                    "genel_memnuniyet",
                    "fiyat_performans_farki",
                    "tavsiye_edilen_urun",
                    "tercih_nedeni",
                ],
            },
        )

        response = client.models.generate_content(
            model="gemini-3.6-flash", contents=prompt, config=config
        )

        return response.text

    except Exception as e:
       return json.dumps({"hata":str(e)})
