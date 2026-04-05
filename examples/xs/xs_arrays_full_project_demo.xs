// xs_arrays_full_project_demo.xs
// Full project-style example for XS arrays + vector arrays.
//
// Input trigger variables expected from scenario setup:
// - 300..307 : hero unitId per slot (8 heroes max)
// - 320..327 : hero max HP per slot (optional; <=0 means fallback to current HP)
// - 340      : self unitId (the AI hero used for distance tie-break)
//
// Output trigger variables:
// - 50 : target player id chosen by weakest-hero logic
// - 51 : target mode (1 = hero focus)
// - 52 : switch pulse incremented when target changes

int cHeroSlots = 8;

int cVarHeroUnitBase = 300;
int cVarHeroMaxHpBase = 320;
int cVarSelfUnitId = 340;

int cVarTargetPlayer = 50;
int cVarTargetMode = 51;
int cVarSwitchPulse = 52;

int aHeroUnitId = -1;
int aHeroOwner = -1;
int aHeroCurrentHp = -1;
int aHeroMaxHp = -1;
int aHeroHpPct = -1;
int aHeroAlive = -1;
int aHeroPos = -1;

int gLastTargetPlayer = -1;
int gSwitchPulse = 0;

rule xs_arrays_init
active
minInterval 1
maxInterval 1
{
    aHeroUnitId = xsArrayCreateInt(cHeroSlots, -1, "hero_unit_ids");
    aHeroOwner = xsArrayCreateInt(cHeroSlots, -1, "hero_owner_ids");
    aHeroCurrentHp = xsArrayCreateFloat(cHeroSlots, 0.0, "hero_current_hp");
    aHeroMaxHp = xsArrayCreateFloat(cHeroSlots, 1.0, "hero_max_hp");
    aHeroHpPct = xsArrayCreateFloat(cHeroSlots, 1.0, "hero_hp_pct");
    aHeroAlive = xsArrayCreateBool(cHeroSlots, false, "hero_alive");
    aHeroPos = xsArrayCreateVector(cHeroSlots, cInvalidVector, "hero_pos");

    xsDisableSelf();
}

rule xs_arrays_sync_heroes
active
minInterval 1
maxInterval 1
{
    int i = 0;
    int unitId = -1;
    int owner = -1;
    int rc = 0;
    float hp = 0.0;
    float maxHp = 0.0;
    float hpPct = 0.0;
    bool alive = false;
    vector pos = cInvalidVector;

    i = 0;
    while (i < cHeroSlots)
    {
        unitId = xsTriggerVariable(cVarHeroUnitBase + i);
        owner = -1;
        hp = 0.0;
        maxHp = 0.0;
        hpPct = 0.0;
        alive = false;
        pos = cInvalidVector;

        if (unitId >= 0)
        {
            if (xsDoesUnitExist(unitId))
            {
                alive = true;
                owner = xsGetUnitOwner(unitId);
                hp = xsGetUnitHitpoints(unitId);
                maxHp = xsTriggerVariable(cVarHeroMaxHpBase + i);
                if (maxHp <= 0.0)
                {
                    maxHp = hp;
                }
                if (maxHp > 0.0)
                {
                    hpPct = hp / maxHp;
                }
                else
                {
                    hpPct = 0.0;
                }
                pos = xsGetUnitPosition(unitId);
            }
        }

        rc = xsArraySetInt(aHeroUnitId, i, unitId);
        rc = xsArraySetInt(aHeroOwner, i, owner);
        rc = xsArraySetFloat(aHeroCurrentHp, i, hp);
        rc = xsArraySetFloat(aHeroMaxHp, i, maxHp);
        rc = xsArraySetFloat(aHeroHpPct, i, hpPct);
        rc = xsArraySetBool(aHeroAlive, i, alive);
        rc = xsArraySetVector(aHeroPos, i, pos);

        i = i + 1;
    }
}

rule xs_arrays_pick_target
active
minInterval 1
maxInterval 1
{
    int i = 0;
    int bestIndex = -1;
    int bestOwner = 0;
    int selfPlayer = 0;
    int selfUnitId = -1;

    float bestHpPct = 9999.0;
    float bestDistSq = 999999999.0;
    float hpPct = 0.0;
    float dx = 0.0;
    float dy = 0.0;
    float distSq = 0.0;

    bool alive = false;
    vector selfPos = cInvalidVector;
    vector heroPos = cInvalidVector;

    selfPlayer = xsGetContextPlayer();
    selfUnitId = xsTriggerVariable(cVarSelfUnitId);
    if (selfUnitId >= 0)
    {
        if (xsDoesUnitExist(selfUnitId))
        {
            selfPos = xsGetUnitPosition(selfUnitId);
        }
    }

    i = 0;
    while (i < cHeroSlots)
    {
        alive = xsArrayGetBool(aHeroAlive, i);
        if (alive)
        {
            if (xsArrayGetInt(aHeroOwner, i) != selfPlayer)
            {
                hpPct = xsArrayGetFloat(aHeroHpPct, i);
                heroPos = xsArrayGetVector(aHeroPos, i);

                dx = xsVectorGetX(heroPos) - xsVectorGetX(selfPos);
                dy = xsVectorGetY(heroPos) - xsVectorGetY(selfPos);
                distSq = (dx * dx) + (dy * dy);

                if (hpPct < bestHpPct)
                {
                    bestHpPct = hpPct;
                    bestDistSq = distSq;
                    bestIndex = i;
                }
                else
                {
                    if (hpPct == bestHpPct)
                    {
                        if (distSq < bestDistSq)
                        {
                            bestDistSq = distSq;
                            bestIndex = i;
                        }
                    }
                }
            }
        }

        i = i + 1;
    }

    if (bestIndex >= 0)
    {
        bestOwner = xsArrayGetInt(aHeroOwner, bestIndex);
    }
    else
    {
        bestOwner = 0;
    }

    if (bestOwner != gLastTargetPlayer)
    {
        gSwitchPulse = gSwitchPulse + 1;
        xsSetTriggerVariable(cVarTargetPlayer, bestOwner);
        xsSetTriggerVariable(cVarTargetMode, 1);
        xsSetTriggerVariable(cVarSwitchPulse, gSwitchPulse);
        gLastTargetPlayer = bestOwner;
    }
}
