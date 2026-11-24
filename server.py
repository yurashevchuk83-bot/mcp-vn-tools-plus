# server.py
import logging
try:
    from mcp.server.fastmcp import FastMCP
    logging.warning("Using FastMCP from mcp.server.fastmcp")
except Exception:
    from fastmcp import FastMCP
    logging.warning("Using FastMCP from fastmcp")

mcp = FastMCP("VN Tools Minimal")

@mcp.tool()
def ping(text: str) -> str:
    """Echo input to verify tool pipeline."""
    return f"pong: {text}"

@mcp.tool()
def time_now() -> str:
    """Return current server time ISO."""
    import datetime
    return datetime.datetime.now().isoformat()

if __name__ == "__main__":
    mcp.run(transport="stdio")
@mcp.tool()
def play_radio(station_name: str) -> str:
    """Вмикає радіостанцію за назвою. Наразі підтримується лише Хіт FM."""
    # Словник зі станціями (поки що одна)
    stations = {
        "хіт фм": "http://online.hitfm.ua/HitFM",
        "hit fm": "http://online.hitfm.ua/HitFM"
    }
    
    # Переводимо назву в нижній регістр для пошуку
    name_lower = station_name.lower()
    
    if name_lower in stations:
        url = stations[name_lower]
        # Повертаємо текст, який агент спробує інтерпретувати як команду
        return f"Відтворюю радіостанцію Хіт FM за посиланням: {url}"
    else:
        return f"Вибачте, я не знаю станцію '{station_name}'. Спробуйте 'Хіт FM'."
