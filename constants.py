from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId

building_abilities: dict[AbilityId, UnitTypeId] = {
    # Protoss
    AbilityId.BUILD_SHIELDBATTERY: UnitTypeId.SHIELDBATTERY,
    AbilityId.PROTOSSBUILD_ASSIMILATOR: UnitTypeId.ASSIMILATOR,
    AbilityId.PROTOSSBUILD_CYBERNETICSCORE: UnitTypeId.CYBERNETICSCORE,
    AbilityId.PROTOSSBUILD_DARKSHRINE: UnitTypeId.DARKSHRINE,
    AbilityId.PROTOSSBUILD_FLEETBEACON: UnitTypeId.FLEETBEACON,
    AbilityId.PROTOSSBUILD_FORGE: UnitTypeId.FORGE,
    AbilityId.PROTOSSBUILD_GATEWAY: UnitTypeId.GATEWAY,
    AbilityId.PROTOSSBUILD_NEXUS: UnitTypeId.NEXUS,
    AbilityId.PROTOSSBUILD_PHOTONCANNON: UnitTypeId.PHOTONCANNON,
    AbilityId.PROTOSSBUILD_PYLON: UnitTypeId.PYLON,
    AbilityId.PROTOSSBUILD_ROBOTICSBAY: UnitTypeId.ROBOTICSBAY,
    AbilityId.PROTOSSBUILD_ROBOTICSFACILITY: UnitTypeId.ROBOTICSFACILITY,
    AbilityId.PROTOSSBUILD_STARGATE: UnitTypeId.STARGATE,
    AbilityId.PROTOSSBUILD_TEMPLARARCHIVE: UnitTypeId.TEMPLARARCHIVE,
    AbilityId.PROTOSSBUILD_TWILIGHTCOUNCIL: UnitTypeId.TWILIGHTCOUNCIL
}

train_abilities: dict[AbilityId, UnitTypeId] = {
    # Protoss
    AbilityId.NEXUSTRAIN_PROBE: UnitTypeId.PROBE,
    AbilityId.GATEWAYTRAIN_ZEALOT: UnitTypeId.ZEALOT,
    AbilityId.WARPGATETRAIN_ZEALOT: UnitTypeId.ZEALOT,
    AbilityId.GATEWAYTRAIN_STALKER: UnitTypeId.STALKER,
    AbilityId.WARPGATETRAIN_STALKER: UnitTypeId.STALKER,
    AbilityId.GATEWAYTRAIN_SENTRY: UnitTypeId.SENTRY,
    AbilityId.WARPGATETRAIN_SENTRY: UnitTypeId.SENTRY,
    AbilityId.TRAIN_ADEPT: UnitTypeId.ADEPT,
    AbilityId.TRAINWARP_ADEPT: UnitTypeId.ADEPT,
    AbilityId.GATEWAYTRAIN_HIGHTEMPLAR: UnitTypeId.HIGHTEMPLAR,
    AbilityId.WARPGATETRAIN_HIGHTEMPLAR: UnitTypeId.HIGHTEMPLAR,
    AbilityId.GATEWAYTRAIN_DARKTEMPLAR: UnitTypeId.DARKTEMPLAR,
    AbilityId.WARPGATETRAIN_DARKTEMPLAR: UnitTypeId.DARKTEMPLAR,
    AbilityId.ROBOTICSFACILITYTRAIN_IMMORTAL: UnitTypeId.IMMORTAL,
    AbilityId.ROBOTICSFACILITYTRAIN_COLOSSUS: UnitTypeId.COLOSSUS,
    AbilityId.TRAIN_DISRUPTOR: UnitTypeId.DISRUPTOR,
    AbilityId.MORPH_ARCHON: UnitTypeId.ARCHON,
    AbilityId.ROBOTICSFACILITYTRAIN_OBSERVER: UnitTypeId.OBSERVER,
    AbilityId.ROBOTICSFACILITYTRAIN_WARPPRISM: UnitTypeId.WARPPRISM,
    AbilityId.STARGATETRAIN_PHOENIX: UnitTypeId.PHOENIX,
    AbilityId.STARGATETRAIN_VOIDRAY: UnitTypeId.VOIDRAY,
    AbilityId.STARGATETRAIN_ORACLE: UnitTypeId.ORACLE,
    AbilityId.STARGATETRAIN_CARRIER: UnitTypeId.CARRIER,
    AbilityId.STARGATETRAIN_TEMPEST: UnitTypeId.TEMPEST,
    AbilityId.NEXUSTRAINMOTHERSHIP_MOTHERSHIP: UnitTypeId.MOTHERSHIP
}

abilities_set = set(train_abilities.keys()) | set(building_abilities.keys())
