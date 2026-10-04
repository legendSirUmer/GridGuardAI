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
