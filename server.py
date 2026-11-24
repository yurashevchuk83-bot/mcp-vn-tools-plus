# server.py
import logging
import datetime

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
    return datetime.datetime.now().isoformat()

@mcp.tool()
def play_radio(station_name: str) -> str:
    """Вмикає радіостанцію за назвою. Наразі підтримується лише Хіт FM."""
    stations = {
        "хіт фм": "http://online.hitfm.ua/HitFM",
        "hit fm": "http://online.hitfm.ua/HitFM"
    }
    
    name_lower = station_name.strip().lower()
    
    if name_lower in stations:
        url = stations[name_lower]
        return f"Відтворюю радіостанцію Хіт FM за посиланням: {url}"
    else:
        return f"Вибачте, я не знаю станцію '{station_name}'. Спробуйте 'Хіт FM'."

if __name__ == "__main__":
    mcp.run(transport="stdio")
