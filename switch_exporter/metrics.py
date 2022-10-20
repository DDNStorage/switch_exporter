COUNTERS = {
    'packets', 'multicast packets', 'unicast packets', 'broadcast packets',
    'bytes', 'error packets', 'discard packets', 'packets of 64 bytes', 'packets Jumbo'
}


def name_to_metric(name: str) -> str:
    return 'switch_port_' + name.replace(' ', '_') + '_total'
