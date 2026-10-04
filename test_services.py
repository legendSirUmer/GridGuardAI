import sys
from services import generate_nepra_petition, get_feeder_gis_data, analyze_12_month_history, generate_dispatch_alerts

p = generate_nepra_petition('GG-2026-0142', 'Engr. Umer Hussain', '14-88412-0498112-U', 'IESCO', 'Islamabad', '410 kWh', 'Rs. 25,750', 'Transformer trips')
print('TEST 1 (NEPRA):', p['petition_title'], '| Refund claim:', p['refund_claim'])
assert 'SECTION 38' in p['petition_title']
assert 'Rs.' in p['refund_claim']

g = get_feeder_gis_data('Islamabad')
print('TEST 2 (GIS):', g['substation']['name'], '| Feeders:', len(g['feeders']), '| Transformers:', len(g['transformers']))
assert len(g['feeders']) >= 2
assert len(g['transformers']) >= 3

t = analyze_12_month_history('410 kWh', 'Rs. 25,750', 'IESCO')
print('TEST 3 (Tariff): Months:', len(t['months']), '| Has breach:', t['has_slab_breach'], '| Penalty:', t['slab_breach_penalty'])
assert len(t['months']) == 12
assert t['has_slab_breach'] is True

d = generate_dispatch_alerts('GG-2026-0142', 'Islamabad', 'Trips', '410 kWh', 'Rs. 25,750', 'IESCO', 'Engr. Umer Hussain')
print('TEST 4 (Dispatch): Work Order:', d['work_order_id'], '| Lineman SMS chars:', len(d['lineman_sms']))
assert 'WO-IESCO' in d['work_order_id']
assert len(d['whatsapp_notice']) > 50

print('\nALL 4 ENTERPRISE BACKEND SERVICES OPERATING PERFECTLY!')
