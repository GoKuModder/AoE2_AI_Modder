// xs_array_injection_demo_generated.xs
int aInjectedIds = -1;

rule xs_injection_demo
active
minInterval 1
maxInterval 1
{
    int injectedValue = -1;
    // INJECT_HERE
    aInjectedIds = xsArrayCreateInt(4, -1, "injected_ids");
    injectedValue = xsArrayGetInt(aInjectedIds, 0);
    xsDisableSelf();
}
