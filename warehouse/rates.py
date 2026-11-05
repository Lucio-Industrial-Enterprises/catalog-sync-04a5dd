"""Shipping rate calculations."""

_ZONE_BASE = {"local": 5.0, "regional": 8.0}
_SERVICE_SURCHARGE = {"standard": 0.0, "express": 7.0}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars for the given service level."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in _ZONE_BASE:
        raise ValueError("unknown zone")
    if service not in _SERVICE_SURCHARGE:
        raise ValueError("unknown service")
    return round(_ZONE_BASE[zone] + 1.5 * weight_kg + _SERVICE_SURCHARGE[service], 2)
