import ipaddress

from ipware.ip import get_ip


def get_client_ip_from_request(request) -> str:
    return get_ip(request)


def is_internal_ip(ip: str) -> bool:
    return ipaddress.ip_address(ip).is_private


def is_internal_ip_from_request(request) -> bool:
    return is_internal_ip(get_client_ip_from_request(request))
