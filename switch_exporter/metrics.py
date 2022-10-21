COUNTERS = {
    'packets', 'multicast packets', 'unicast packets', 'broadcast packets',
    'bytes', 'error packets', 'discard packets', 'packets of 64 bytes', 
    'packets of 128-255 bytes', 'packets of 256-511 bytes', 'packets of 512-1023 bytes', 
    'packets of 1024-1518 bytes', 'packets Jumbo', 'fcs errors', 'undersize packets', 
    'oversize packets', 'pause packets', 'unknown control opcode', 'symbol errors',
    'discard packets by storm control'
}

def name_to_metric(name: str) -> str:
    name = 'switch_port_' + name.replace(' ', '_') + '_total'
    # prometheus does not like dashses in metric names
    return name.replace('-','_')
