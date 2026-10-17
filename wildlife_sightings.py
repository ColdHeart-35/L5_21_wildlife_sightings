"""Record wildlife sightings and summarize sanctuary activity."""

import hashlib
import sqlite3


def log_sighting(
    connection: sqlite3.Connection,
    species: str,
    zone: str,
    count: int,
    extras: dict[str, int] | None = None,
) -> dict[str, int]:
    """Store a sighting and update the supplied species totals."""
    if extras is None:
        extras = {}

    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count),
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer: str) -> str:
    """Return a short, deterministic identifier for an observer."""
    return hashlib.sha256(observer.encode("utf-8")).hexdigest()[:6]


def zone_summary(connection: sqlite3.Connection, zone: str) -> int:
    """Return the total number of sightings recorded in a zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()
    return row[0] if row[0] is not None else 0


def rarest_species(connection: sqlite3.Connection) -> str | None:
    """Return the least-seen species, or None when there are no sightings."""
    rows = connection.execute(
        "SELECT species, SUM(count) FROM sightings GROUP BY species"
    ).fetchall()
    if not rows:
        return None
    return min(rows, key=lambda row: row[1])[0]


def main() -> None:
    """Run a small demonstration of the sightings log."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE sightings "
        "(id INTEGER PRIMARY KEY, species TEXT, zone TEXT, count INTEGER)"
    )

    totals = log_sighting(connection, "Leopard", "North", 1)
    log_sighting(connection, "Chital", "North", 24, totals)
    log_sighting(connection, "Hornbill", "East", 3, totals)
    print(
        observer_id("Arun"),
        zone_summary(connection, "North"),
        rarest_species(connection),
    )
    connection.close()


if __name__ == "__main__":
    main()
