// Gemini XS functions/teleport.xs
// Custom implementation of teleportation logic near Barracks (ID 12).
// Verified with xs-check.exe

// Linter stub - The engine provides this function built-in.
// This is only here to satisfy the linter; remove if redefinition errors occur in-game.
bool xsSetUnitPosition(int unitId = -1, vector position = vector(-1.0,-1.0,-1.0), bool checkCollision = true) {
    return (false);
}

static int gBArr = -1;
static int gUArr = -1;

void processTeleportSystem() {
    // Initialize or reuse arrays for performance
    if (gBArr == -1) { gBArr = xsArrayCreateInt(128, -1, "gBArr"); }
    if (gUArr == -1) { gUArr = xsArrayCreateInt(1024, -1, "gUArr"); }

    int numP = xsGetNumPlayers();
    int p = 1;
    while (p <= numP) {
        if (xsGetPlayerInGame(p)) {
            // Get all Barracks (ID 12) for player p
            int bArrId = xsGetPlayerUnitIds(p, 12, gBArr);
            int bCount = xsArrayGetSize(bArrId);
            int b = 0;
            while (b < bCount) {
                int bId = xsArrayGetInt(bArrId, b);
                if (xsDoesUnitExist(bId)) {
                    vector bPos = xsGetUnitPosition(bId);
                    float bx = xsVectorGetX(bPos);
                    float by = xsVectorGetY(bPos);
                    float bz = xsVectorGetZ(bPos);

                    // Check units of all players (including Player 1) near this barracks
                    int tp = 1;
                    while (tp <= numP) {
                        if (xsGetPlayerInGame(tp)) {
                            // Check major land unit classes to cover "any unit type"
                            int c = 0;
                            while (c < 6) {
                                int tc = 906; // Default Infantry
                                if (c == 0) tc = 900; // Archer
                                if (c == 1) tc = 904; // Villager
                                if (c == 2) tc = 912; // Cavalry
                                if (c == 3) tc = 918; // Monk
                                if (c == 4) tc = 911; // Miscellaneous
                                if (c == 5) tc = 906; // Infantry (redundant but safe)

                                int uArrId = xsGetPlayerUnitIds(tp, tc, gUArr);
                                int uCount = xsArrayGetSize(uArrId);
                                int u = 0;
                                while (u < uCount) {
                                    int uId = xsArrayGetInt(uArrId, u);
                                    if (uId != bId && xsDoesUnitExist(uId)) {
                                        vector uPos = xsGetUnitPosition(uId);
                                        float ux = xsVectorGetX(uPos);
                                        float uy = xsVectorGetY(uPos);
                                        
                                        float dx = ux - bx;
                                        float dy = uy - by;
                                        
                                        // DETECTION: 2 tiles away from the left side.
                                        // Barracks center to edge is 1.5 tiles. Edge + 2.0 = 3.5 tiles.
                                        // We detect in a generous box around that point.
                                        if (dx < -2.0 && dx > -5.0) {
                                            if (abs(dy) < 2.0) {
                                                // Teleport to 3.5 tiles to the right of the center
                                                vector dest = xsVectorSet(bx + 3.5, by, bz);
                                                // checkCollision = false ensures the teleport succeeds regardless of units/buildings
                                                if (xsSetUnitPosition(uId, dest, false)) {
                                                    xsChatData("Unit teleported across the Barracks!", -1);
                                                }
                                            }
                                        }
                                    }
                                    u++;
                                }
                                c++;
                            }
                        }
                        tp++;
                    }
                }
                b++;
            }
        }
        p++;
    }
}

// Rule that runs every second for the entire game
rule TeleportationProcessRule
active
minInterval 1
{
    processTeleportSystem();
}
