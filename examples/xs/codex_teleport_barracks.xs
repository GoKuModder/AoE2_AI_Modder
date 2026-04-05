// ============================================================
// Script Use Case: Teleport Object in Proximity using XS
// Maker / Owner Credit: GoKu
// Implementation Credit: Codex (GPT-5)
//
// Tools Used:
// - AoE2:DE XS scripting runtime
// - XS API functions: xsSetUnitPosition, xsGetUnitPosition, xsGetPlayerUnitIds,
//   xsDoesUnitExist, xsChatData, vector helpers
// - Validation tool: xs-check.exe
//
// Description:
// If a player's unit stands near a barracks from the left side (2 tiles away),
// it is teleported to the right side (2 tiles away), and a chat notification
// is sent when teleportation succeeds.
// ============================================================

const int cCodexBarracksObjectId = 12;
const int cCodexTeleportUnitObjectOrClassId = -1;
const float cCodexTeleportOffsetTiles = 2.0;
const float cCodexActivationRadiusTiles = 0.75;
const bool cCodexCheckCollision = true;

bool codexTeleportAcrossBarracksIfOnLeft(int unitId = -1, int barracksUnitId = -1) {
    if (unitId < 0 || barracksUnitId < 0) {
        return (false);
    }
    if (unitId == barracksUnitId) {
        return (false);
    }
    if (xsDoesUnitExist(unitId) == false || xsDoesUnitExist(barracksUnitId) == false) {
        return (false);
    }

    vector barracksPos = xsGetUnitPosition(barracksUnitId);
    vector unitPos = xsGetUnitPosition(unitId);

    vector leftPos = xsVectorSetX(barracksPos, xsVectorGetX(barracksPos) - cCodexTeleportOffsetTiles);
    vector rightPos = xsVectorSetX(barracksPos, xsVectorGetX(barracksPos) + cCodexTeleportOffsetTiles);

    float dx = xsVectorGetX(unitPos) - xsVectorGetX(leftPos);
    float dy = xsVectorGetY(unitPos) - xsVectorGetY(leftPos);
    float distSq = dx * dx + dy * dy;
    float activationSq = cCodexActivationRadiusTiles * cCodexActivationRadiusTiles;

    if (distSq <= activationSq) {
        bool teleported = xsSetUnitPosition(unitId, rightPos, cCodexCheckCollision);
        if (teleported) {
            xsChatData("Teleport object activated: moved from left side to right side of Barracks.");
        }
        return (teleported);
    }

    return (false);
}

rule codex_barracks_left_to_right_teleport
    minInterval 1
    maxInterval 1
    active
{
    int playerCount = xsGetNumPlayers();
    int playerId = 1;
    for (playerId = 1; < playerCount) {
        if (xsGetPlayerInGame(playerId) == false) {
            continue;
        }

        int barracksArrayId = xsGetPlayerUnitIds(playerId, cCodexBarracksObjectId);
        int barracksCount = xsArrayGetSize(barracksArrayId);
        if (barracksCount <= 0) {
            continue;
        }

        int unitArrayId = xsGetPlayerUnitIds(playerId, cCodexTeleportUnitObjectOrClassId);
        int unitCount = xsArrayGetSize(unitArrayId);
        if (unitCount <= 0) {
            continue;
        }

        int b = 0;
        for (b = 0; < barracksCount) {
            int barracksUnitId = xsArrayGetInt(barracksArrayId, b);
            if (xsDoesUnitExist(barracksUnitId) == false) {
                continue;
            }

            int u = 0;
            for (u = 0; < unitCount) {
                int unitId = xsArrayGetInt(unitArrayId, u);
                if (codexTeleportAcrossBarracksIfOnLeft(unitId, barracksUnitId)) {
                }
            }
        }
    }
}
