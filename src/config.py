# (c) Tiago Tamagusko 2022
"""
Config file to suport fastAPI app
"""
from __future__ import annotations

from pydantic import BaseSettings


class Settings(BaseSettings):
    twilio_account_sid: str
    twilio_auth_token: str
    twilio_phone_number: str

    class Config:
        env_file = '.env'
