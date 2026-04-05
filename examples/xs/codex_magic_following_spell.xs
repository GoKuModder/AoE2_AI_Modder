// ============================================================
// Script Use Case: Magic following spell
// Maker / Owner Credit: GoKu
// Implementation Credit: Codex (GPT-5)
//
// Description:
// Creates Archer units in a fixed 3-tile ring around each Militia.
// Spawned units are set to 3 HP and -180 regeneration.
// Map size is only used for boundary checks.
// ============================================================

// ---- Config ----
const int cCodexMagicMilitiaObjectId = 74;           // Militia
const int cCodexMagicFireObjectId = 4;               // Archer
const float cCodexMagicSpawnDistance = 3.0;          // Fixed 3 tiles around militia
const float cCodexMagicBorderMargin = 1.0;           // Keep spawns inside map border
const float cCodexMagicFireHitpoints = 3.0;          // Required by design
const float cCodexMagicFireRegenPerMinute = -180.0;  // Required by design
const int cCodexMagicDebug = 1;

// ---- State ----
int gCodexMapWidth = -1;
int gCodexMapHeight = -1;
int gCodexDbgMain = 0;
int gCodexDbgRule = 0;
int gCodexDbgMilitiaFound = 0;
int gCodexDbgSpawnSuccess = 0;
int gCodexDbgSpawnFail = 0;
int gCodexDbgMapInvalid = 0;

void codexMagicInitMapSize() {
    if (gCodexMapWidth < 0) {
        gCodexMapWidth = xsGetMapWidth();
    }
    if (gCodexMapHeight < 0) {
        gCodexMapHeight = xsGetMapHeight();
    }
}

bool codexMagicPositionInsideBorder(float x = -1.0, float y = -1.0) {
    codexMagicInitMapSize();

    if (gCodexMapWidth <= 2) {
        if (cCodexMagicDebug == 1) {
            if (gCodexDbgMapInvalid == 0) {
                xsChatData("Magic debug: invalid map size; spawn blocked.");
                gCodexDbgMapInvalid = 1;
            }
        }
        return (false);
    }
    if (gCodexMapHeight <= 2) {
        if (cCodexMagicDebug == 1) {
            if (gCodexDbgMapInvalid == 0) {
                xsChatData("Magic debug: invalid map size; spawn blocked.");
                gCodexDbgMapInvalid = 1;
            }
        }
        return (false);
    }

    float minX = cCodexMagicBorderMargin;
    float minY = cCodexMagicBorderMargin;
    float maxX = (0.0 + gCodexMapWidth) - cCodexMagicBorderMargin;
    float maxY = (0.0 + gCodexMapHeight) - cCodexMagicBorderMargin;

    if (x < minX) {
        return (false);
    }
    if (y < minY) {
        return (false);
    }
    if (x > maxX) {
        return (false);
    }
    if (y > maxY) {
        return (false);
    }
    return (true);
}

void Magic_following_spell(int militiaUnitId = -1) {
    if (militiaUnitId < 0) {
        return;
    }
    if (xsDoesUnitExist(militiaUnitId) == false) {
        return;
    }

    int owner = xsGetUnitOwner(militiaUnitId);
    if (owner < 1) {
        return;
    }
    if (owner > 8) {
        return;
    }

    // Configure spawned unit template for this player.
    xsEffectAmount(cSetAttribute, cCodexMagicFireObjectId, cHitpoints, cCodexMagicFireHitpoints, owner);
    xsEffectAmount(cSetAttribute, cCodexMagicFireObjectId, cRegenerationRate, cCodexMagicFireRegenPerMinute, owner);

    vector center = xsGetUnitPosition(militiaUnitId);
    float centerX = xsVectorGetX(center);
    float centerY = xsVectorGetY(center);
    float centerZ = xsVectorGetZ(center);

    int ox = -1;
    for (ox = -1; < 2) {
        int oy = -1;
        for (oy = -1; < 2) {
            if (ox == 0) {
                if (oy == 0) {
                    continue;
                }
            }

            float spawnX = centerX + (0.0 + ox) * cCodexMagicSpawnDistance;
            float spawnY = centerY + (0.0 + oy) * cCodexMagicSpawnDistance;
            if (codexMagicPositionInsideBorder(spawnX, spawnY) == false) {
                continue;
            }

            vector spawnPos = xsVectorSet(spawnX, spawnY, centerZ);
            int createdUnitId = xsCreateUnit(cCodexMagicFireObjectId, owner, spawnPos, false, false, false);
            if (createdUnitId >= 0) {
                bool setHpOk = xsSetUnitHitpoints(createdUnitId, cCodexMagicFireHitpoints);
                if (setHpOk) {
                }
                if (cCodexMagicDebug == 1) {
                    if (gCodexDbgSpawnSuccess == 0) {
                        xsChatData("Magic debug: spawn success unit id", createdUnitId);
                        gCodexDbgSpawnSuccess = 1;
                    }
                }
            } else {
                if (cCodexMagicDebug == 1) {
                    if (gCodexDbgSpawnFail == 0) {
                        xsChatData("Magic debug: xsCreateUnit failed.");
                        gCodexDbgSpawnFail = 1;
                    }
                }
            }
        }
    }
}

void main() {
    codexMagicInitMapSize();
    if (cCodexMagicDebug == 1) {
        if (gCodexDbgMain == 0) {
            xsChatData("Magic debug: main reached.");
            xsChatData("Magic debug: map width", gCodexMapWidth);
            xsChatData("Magic debug: map height", gCodexMapHeight);
            gCodexDbgMain = 1;
        }
    }
    xsEnableRule("codex_magic_following_spell_rule");
}

rule codex_magic_following_spell_rule
    minInterval 1
    maxInterval 1
    active
{
    if (cCodexMagicDebug == 1) {
        if (gCodexDbgRule == 0) {
            xsChatData("Magic debug: rule running.");
            gCodexDbgRule = 1;
        }
    }

    int playerId = 1;
    for (playerId = 1; < 9) {
        if (xsGetPlayerInGame(playerId) == false) {
            continue;
        }

        int militiaArrayId = xsGetPlayerUnitIds(playerId, cCodexMagicMilitiaObjectId);
        int militiaCount = xsArrayGetSize(militiaArrayId);
        if (militiaCount <= 0) {
            continue;
        }

        if (cCodexMagicDebug == 1) {
            if (gCodexDbgMilitiaFound == 0) {
                xsChatData("Magic debug: militia count", militiaCount);
                gCodexDbgMilitiaFound = 1;
            }
        }

        int i = 0;
        for (i = 0; < militiaCount) {
            int militiaUnitId = xsArrayGetInt(militiaArrayId, i);
            if (xsDoesUnitExist(militiaUnitId) == false) {
                continue;
            }
            Magic_following_spell(militiaUnitId);
        }
    }
}
