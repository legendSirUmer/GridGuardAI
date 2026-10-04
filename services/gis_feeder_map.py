"""
GridGuard AI - Geospatial SCADA & Feeder Topology Engine
Provides high-precision GIS network topology for Pakistan electricity distribution circles.
"""

def get_feeder_gis_data(city_area: str = "", case_id: str = "GG-2026-0142") -> dict:
    """
    Returns GIS topology, SCADA breaker states, and transformer telemetry for the selected area.
    """
    ca = city_area.lower()
    
    if "lahore" in ca:
        city_key = "lahore"
        center = [31.5204, 74.3587]
        substation_name = "132kV Gulberg Grid Substation (LESCO)"
        disco_code = "LESCO"
        feeder_name = "Jail Road 11kV Feeder (Circuit 4)"
        feeders = [
            {
                "id": "F-LHR-04",
                "name": "Jail Road 11kV Feeder",
                "path": [[31.5204, 74.3587], [31.5260, 74.3510], [31.5340, 74.3430], [31.5390, 74.3360]],
                "voltage_kv": 11.2,
                "current_amps": 342,
                "loading_pct": 88.5,
                "status": "warning"
            },
            {
                "id": "F-LHR-09",
                "name": "Main Boulevard Feeder",
                "path": [[31.5204, 74.3587], [31.5150, 74.3640], [31.5080, 74.3710]],
                "voltage_kv": 11.4,
                "current_amps": 210,
                "loading_pct": 58.0,
                "status": "normal"
            }
        ]
        transformers = [
            {"id": "TR-LHR-88", "name": "Gulberg III Transformer (630 kVA)", "coords": [31.5260, 74.3510], "voltage": 228, "load": 64, "status": "normal"},
            {"id": "TR-LHR-91", "name": "Jail Road Commercial Transformer (400 kVA)", "coords": [31.5340, 74.3430], "voltage": 216, "load": 91, "status": "warning"},
            {"id": "TR-LHR-99", "name": "Consumer Zone Transformer (250 kVA)", "coords": [31.5375, 74.3395], "voltage": 194, "load": 98, "status": "tripped", "breaker": "OPEN - Relay 51 Trip"}
        ]
        consumer_pin = {"coords": [31.5372, 74.3390], "label": f"Consumer Meter #{case_id}", "discrepancy": "+18.4 kWh phantom surge on breaker reclose"}
        outage_zone = [[31.5320, 74.3460], [31.5410, 74.3330], [31.5440, 74.3380], [31.5360, 74.3500]]

    elif "karachi" in ca:
        city_key = "karachi"
        center = [24.8138, 67.0299]
        substation_name = "132kV Clifton Substation (K-Electric Grid)"
        disco_code = "K-Electric"
        feeder_name = "Clifton Block 4 11kV Feeder (Circuit K-2)"
        feeders = [
            {
                "id": "F-KE-02",
                "name": "Clifton Block 4 Feeder",
                "path": [[24.8138, 67.0299], [24.8180, 67.0340], [24.8230, 67.0410], [24.8270, 67.0490]],
                "voltage_kv": 10.9,
                "current_amps": 412,
                "loading_pct": 94.2,
                "status": "warning"
            },
            {
                "id": "F-KE-07",
                "name": "Defence Phase 5 Ring",
                "path": [[24.8138, 67.0299], [24.8070, 67.0360], [24.7990, 67.0430]],
                "voltage_kv": 11.3,
                "current_amps": 240,
                "loading_pct": 62.0,
                "status": "normal"
            }
        ]
        transformers = [
            {"id": "TR-KE-40", "name": "Clifton Marine Drive (630 kVA)", "coords": [24.8180, 67.0340], "voltage": 230, "load": 70, "status": "normal"},
            {"id": "TR-KE-44", "name": "Sea View Commercial (400 kVA)", "coords": [24.8230, 67.0410], "voltage": 219, "load": 88, "status": "warning"},
            {"id": "TR-KE-49", "name": "Consumer Feeder Tap (250 kVA)", "coords": [24.8255, 67.0460], "voltage": 188, "load": 99, "status": "tripped", "breaker": "OPEN - High Temperature Trip"}
        ]
        consumer_pin = {"coords": [24.8252, 67.0458], "label": f"Consumer Meter #{case_id}", "discrepancy": "+22.1 kWh surge recorded during restoration"}
        outage_zone = [[24.8200, 67.0380], [24.8300, 67.0520], [24.8330, 67.0480], [24.8220, 67.0350]]

    elif "rawalpindi" in ca:
        city_key = "rawalpindi"
        center = [33.5989, 73.0450]
        substation_name = "132kV Rawalpindi Cantt Grid Substation (IESCO)"
        disco_code = "IESCO (Rawalpindi Circle)"
        feeder_name = "Saddar Express 11kV Feeder (Circuit R-3)"
        feeders = [
            {
                "id": "F-RWP-03",
                "name": "Saddar Express 11kV Feeder",
                "path": [[33.5989, 73.0450], [33.6040, 73.0510], [33.6120, 73.0580], [33.6180, 73.0640]],
                "voltage_kv": 11.0,
                "current_amps": 365,
                "loading_pct": 91.2,
                "status": "warning"
            },
            {
                "id": "F-RWP-07",
                "name": "Westridge Residential Feeder",
                "path": [[33.5989, 73.0450], [33.5920, 73.0380], [33.5850, 73.0310]],
                "voltage_kv": 11.3,
                "current_amps": 205,
                "loading_pct": 54.0,
                "status": "normal"
            }
        ]
        transformers = [
            {"id": "TR-RWP-21", "name": "Haider Road Commercial PMT (630 kVA)", "coords": [33.6040, 73.0510], "voltage": 226, "load": 68, "status": "normal"},
            {"id": "TR-RWP-26", "name": "Bank Road PMT (400 kVA)", "coords": [33.6120, 73.0580], "voltage": 214, "load": 94, "status": "warning"},
            {"id": "TR-RWP-33", "name": "Consumer Tap Station (250 kVA)", "coords": [33.6160, 73.0620], "voltage": 190, "load": 98, "status": "tripped", "breaker": "OPEN - Overcurrent Relay Trip"}
        ]
        consumer_pin = {"coords": [33.6158, 73.0618], "label": f"Consumer Meter #{case_id}", "discrepancy": "+19.2 kWh surge recorded on feeder reclose"}
        outage_zone = [[33.6080, 73.0540], [33.6200, 73.0660], [33.6220, 73.0610], [33.6110, 73.0500]]

    elif "peshawar" in ca:
        city_key = "peshawar"
        center = [33.9965, 71.4851]
        substation_name = "132kV Hayatabad Grid Substation (PESCO)"
        disco_code = "PESCO (KPK Grid)"
        feeder_name = "Hayatabad Phase 3 Feeder (Circuit P-1)"
        feeders = [
            {
                "id": "F-PES-01",
                "name": "Hayatabad Phase 3 Feeder",
                "path": [[33.9965, 71.4851], [34.0020, 71.4780], [34.0090, 71.4690], [34.0150, 71.4610]],
                "voltage_kv": 10.8,
                "current_amps": 420,
                "loading_pct": 95.0,
                "status": "warning"
            },
            {
                "id": "F-PES-05",
                "name": "University Road Feeder",
                "path": [[33.9965, 71.4851], [33.9910, 71.4920], [33.9840, 71.5010]],
                "voltage_kv": 11.2,
                "current_amps": 235,
                "loading_pct": 59.0,
                "status": "normal"
            }
        ]
        transformers = [
            {"id": "TR-PES-12", "name": "Hayatabad Sector F-2 PMT (630 kVA)", "coords": [34.0020, 71.4780], "voltage": 224, "load": 72, "status": "normal"},
            {"id": "TR-PES-18", "name": "Industrial Estate Spur (400 kVA)", "coords": [34.0090, 71.4690], "voltage": 210, "load": 93, "status": "warning"},
            {"id": "TR-PES-24", "name": "Consumer Tap PMT (250 kVA)", "coords": [34.0135, 71.4635], "voltage": 186, "load": 99, "status": "tripped", "breaker": "OPEN - Thermal Relay Lockout"}
        ]
        consumer_pin = {"coords": [34.0132, 71.4632], "label": f"Consumer Meter #{case_id}", "discrepancy": "+21.5 kWh surge recorded on breaker trip"}
        outage_zone = [[34.0060, 71.4720], [34.0180, 71.4580], [34.0210, 71.4640], [34.0080, 71.4770]]

    else:
        # Default: Islamabad (Sector F-7 / Blue Area - IESCO)
        city_key = "islamabad"
        center = [33.7182, 73.0605]
        substation_name = "132kV Blue Area Grid Substation (IESCO)"
        disco_code = "IESCO"
        feeder_name = "Feeder F-12 (Blue Area / Sector F-7 Express)"
        feeders = [
            {
                "id": "F-IESCO-12",
                "name": "Feeder F-12 (Blue Area / Sector F-7)",
                "path": [[33.7182, 73.0605], [33.7225, 73.0645], [33.7280, 73.0700], [33.7340, 73.0760]],
                "voltage_kv": 11.1,
                "current_amps": 385,
                "loading_pct": 89.2,
                "status": "warning"
            },
            {
                "id": "F-IESCO-04",
                "name": "Feeder F-7/2 Residential",
                "path": [[33.7182, 73.0605], [33.7230, 73.0530], [33.7275, 73.0470]],
                "voltage_kv": 11.4,
                "current_amps": 195,
                "loading_pct": 52.0,
                "status": "normal"
            },
            {
                "id": "F-IESCO-08",
                "name": "Margalla Spur Feeder",
                "path": [[33.7182, 73.0605], [33.7300, 73.0580], [33.7370, 73.0530]],
                "voltage_kv": 11.3,
                "current_amps": 220,
                "loading_pct": 57.5,
                "status": "normal"
            }
        ]
        transformers = [
            {"id": "TR-ISB-101", "name": "F-7 Markaz Commercial PMT (630 kVA)", "coords": [33.7225, 73.0645], "voltage": 230, "load": 65, "status": "normal"},
            {"id": "TR-ISB-104", "name": "Sector F-7/2 PMT (400 kVA)", "coords": [33.7280, 73.0700], "voltage": 218, "load": 92, "status": "warning"},
            {"id": "TR-ISB-109", "name": "Consumer Feeder Tap Substation (250 kVA)", "coords": [33.7320, 73.0740], "voltage": 192, "load": 97, "status": "tripped", "breaker": "OPEN - Transient Tap Surge"}
        ]
        consumer_pin = {"coords": [33.7315, 73.0735], "label": f"Consumer Meter #{case_id}", "discrepancy": "+18.4 kWh phantom surge recorded post-trip"}
        outage_zone = [[33.7260, 73.0680], [33.7360, 73.0780], [33.7380, 73.0720], [33.7280, 73.0620]]

    return {
        "city_key": city_key,
        "center": center,
        "zoom": 14,
        "substation": {
            "name": substation_name,
            "coords": center,
            "rating": "132/11 kV Dual Transformer Bus",
            "active_power_mva": 28.4,
            "power_factor": 0.92,
            "status": "OPERATIONAL"
        },
        "disco": disco_code,
        "feeder_name": feeder_name,
        "feeders": feeders,
        "transformers": transformers,
        "consumer_pin": consumer_pin,
        "outage_zone": outage_zone,
        "scada_metrics": {
            "grid_frequency_hz": 50.02,
            "bus_voltage_kv": 11.2,
            "feeder_trips_24h": 3,
            "unresolved_anomalies": 1,
            "scada_sync_status": "LOCKED (IEC 61850 Protocol)"
        }
    }
