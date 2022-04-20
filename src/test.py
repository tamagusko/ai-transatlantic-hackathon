# (c) Tiago Tamagusko 2022
"""
Test fastapi env

Example:
    https://mvptransatlanticai.herokuapp.com/test?text1='abc'&text2='bca'
    return: data
"""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get('/test')
async def test(text1: str, text2: str):
    return {'data1': '{}'.format(text1), 'data2': '{}'.format(text2)}
